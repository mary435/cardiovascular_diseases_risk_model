#!/usr/bin/env python
# coding: utf-8
# Marilina Orihuela: mary.orihuela@gmail.com

#%%
import pandas as pd
import xgboost as xgb
import bentoml
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score

#%%
file_name = f'model_xgb.bin'
__author__ = "Marilina Orihuela"
#%% Data Preparation

print('Data Preparation')

data = 'cardiovascular_diseases_dv3.csv'

df = pd.read_csv(data ,delimiter=';')
df.columns = df.columns.str.lower()

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1, )
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1, )

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)

y_train = df_train.cardio_disease.values
y_val = df_val.cardio_disease.values
y_test = df_test.cardio_disease.values

del df_train['cardio_disease']
del df_val['cardio_disease']
del df_test['cardio_disease']

dv = DictVectorizer(sparse=False)

train_dicts = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)

val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)

#%% xgboost best parameters

xgb_params = {
            'eta': 0.05, 
            'max_depth': 5,
            'min_child_weight': 5,

            'objective': 'binary:logistic',
            'eval_metric': 'auc',

            'nthread': 8,
            'seed': 1,
            'verbosity': 1,
        }

#%% training
print('Doing validation')

#features = dv.get_feature_names_out()
dtrain = xgb.DMatrix(X_train, label=y_train)#, feature_names=features)
dval = xgb.DMatrix(X_val, label=y_val) #, feature_names=features)
model = xgb.train(xgb_params, dtrain, num_boost_round=115)

#%% Train the final model
print('Training the final model')

y_full_train = df_full_train.cardio_disease
del df_full_train['cardio_disease']

dicts_full_train = df_full_train.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)

d_full_train = xgb.DMatrix(X_full_train, label = y_full_train)

d_test = xgb.DMatrix(X_test)

model = xgb.train(xgb_params, d_full_train, num_boost_round=115)

y_pred = model.predict(d_test)

auc_final = roc_auc_score(y_test, y_pred)

print('Final results:')
print(f'AUC={auc_final}')
#%% Save the model

with open(file_name, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'The model is saved to {file_name}')

with open(file_name, 'rb') as f_in: 
    dv, model = pickle.load(f_in)


#%% save the model with BentoML

f_out = bentoml.xgboost.save_model("cardiovascular_diseases_risk_model", 
                                    model, 
                                    labels ={
                                            "owner": __author__
                                    },
                                    custom_objects={
                                                    "dictVectorizer": dv
                                    },
                                    signatures= {
                                                "predict":{
                                                        "batchable": True,
                                                        "batch_dim": 0
                                                } 
                                    }
                                )

print(f'The Bento model is saved to {f_out}')