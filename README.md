# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
- To build a supervised learning model that will predict whether or not a loan would be approved.
- Deploy the model to cloud and test it by using different tools

Overall, the completed project workflow is shown in the figures below.
![](/images/workflow.png)

## Hypothesis
Hypotheses examined included:
-Applicants that have a good credit history are likely to get approved 
-Applicants with higher applicant and coapplicant income 
-Applicants with a higher level of education may earn more, and therefore more likely to be approved 
-Number of dependents may affect eligibility due to less disposable income with more dependents 

## Process
#### Step 1
Hypothesis generation

#### Step 2
Data exploration -EDA
![](/images/eda.png)
![](/images/eda-2.png)

#### Step 3
Data cleaning

#### Step 4
Building a predictive model using pipeline
![](/images/model.png)
![](/images/model-2.png)

### Step 5
Model deployment
- I were testing the API in my local host to make sure it works and then tested it on cloud- AWS 
![](/images/api-local-test.png)
![](/images/aws-test.png)

## Results/Demo
- Tried different models, the best one is the logistic regression model 

## Challanges 
- I got some difficulty about how to correctly using pipeline with multiple different classifiers 
- Second, I got some difficulty with deploying to AWS.
But finaly, i made it for the whole part. 
