# Cardiovascular disease risk model:

This model allows predicting the probability that a patient has of suffering from cardiovascular disease, 
trained from a database of more than 68,000 data, with the aim of alerting people to this risk.

The project is available on AWS and can be used from http://177.71.199.40:3000/

Inside the option: Post/classify: button Try it out and complete the Request body:

age: years of age

gender: 1 - women, 2 - men

height: cm

weight: kg

ap_high: systolic blood pressure

ap_low: diastolic blood pressure

cholesterol: 1: normal, 2: above normal, 3: well above normal

glucose: 1: normal, 2: above normal, 3: well above normal

smoke: 0: no, 1: yes

alcohol: 0: no, 1: yes

physical_activity: 0: no, 1: yes


When you complete the data click on execute and you can see the probability below in the box
Response body, like:

{
  "result": 0.050249941647052765
}

