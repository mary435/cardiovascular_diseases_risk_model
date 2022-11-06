# Cardiovascular disease risk model

## About the project:
The availability of health monitoring equipment is increasing every day and the objective of this project 
is to use this information to warn of the risk of cardiovascular diseases.

This model allows predicting the probability of suffering from cardiovascular disease,
with an accuracy of 80%, trained from a database of more than 68,000 data, with the aim of alerting people to this risk.

# Running the model:

The project is available on AWS and can be used from http://177.71.199.40:3000/

<img src="images/1.png">
 
On the Service APIs section, click the option: Post/classify:

<img src="images/2.png">

Next click the Try it out button and complete the Request body:

<img src="images/3.png">

### Acceptable values:
* age: years of age
* gender: 1 - women, 2 - men
* height: cm
* weight: kg
* ap_high: systolic blood pressure
* ap_low: diastolic blood pressure
* cholesterol: 1: normal, 2: above normal, 3: well above normal
* glucose: 1: normal, 2: above normal, 3: well above normal
* smoke: 0: no, 1: yes
* alcohol: 0: no, 1: yes
* physical_activity: 0: no, 1: yes

### Here is a sample for you to try:

```json
{
  "age": 38,
  "gender": 1,
  "height": 165,
  "weight": 54,
  "ap_high": 120,
  "ap_low": 60,
  "cholesterol": 1,
  "glucose": 1,
  "smoke": 0,
  "alcohol": 0,
  "physical_activity": 1
}
```

When you complete the data click on execute and you can see the probability below in the box
Response body, like:
<img src="images/5.png">


## For running localy download the docker image from:

```docker
docker pull maryorihuela/cardiovascular_diseases_risk
```

## Run localy:
```docker
docker run -it --rm -p 3000:3000 clamytoe/covid_risk_classifier serve --production
```

## Try the service:
Just opening a browser to <http://localhost:3000>
And follow the same instructions as above for AWS.


## Data: 
* You can download the dataset from this link on kaggle: <https://www.kaggle.com/datasets/aiaiaidavid/cardio-data-dv13032020?select=cardiovascular_diseases_dv3.csv>

* Another option from github:   <https://github.com/mary435/cardiovascular_diseases_risk_model/blob/28c9346a431fdfe8543174c9ea6af4dfd89074c9/cardiovascular_diseases_dv3.csv>

* Third option download it from the notebook. I leave the lines with wget ready.

## Notebook
The notebook was created with this anaconda environment: [cardio_project_env.yaml](cardio_project_env.yaml)
You can download it and import it to your anaconda, option environments, import.

Next, open the jupyter Notebook file and run it to view the EDA analyzes and training of differents models.
In the xgboost model, for the parameter adjustment, you will find a line with the comment ####### that indicates 
the different parameters that you need to change, to then execute this cell again and see the graph with the comparison with them.

## Train.py
This script reads the dataset that should be saved in the same folder with the name: 'cardiovascular_diseases_dv3.csv'. 
Then prepares the data, trains the final model and saves it with BentoML.
For running it you need the same environment from the notebook file. You can download it from this link: [cardio_project_env.yaml](cardio_project_env.yaml)  
And import it to your anaconda, option environments, import.
From anaconda's "open terminal" option, you can run the "train.py" script with the >>python train.py command this read the dataset,
prepare the data, train the final model, and save it with BentoML.

Alternatively with pipenv you need to download this 2 files: 
[Pipfile](Pipfile)
[Pipfile.lock](Pipfile.lock)

And next run >>pipenv install. When finished run >>pipenv run python train.py

## Docker 
If you have docker and bentoml installed, you can run >>bentoml build 'tag' 
Where you replace the 'tag' with the real tag that results from the notebook or train.py. 

Likewise  

  
  
