# Insurance-Claim
Project Overview
    
The business objective was to check if an health insurance claim was genuine or fraudulent .The dataset had 1046119 rows and 24 coloumns.
Pre processing techniques such as EDA , feature selection, outlier detection were carried out to clean the dat and various insights  were drawn from EDA .
The less important features were dropped upon by carrying out feature selection technique called decision tree classifier where the feature importance was plotted. From the plot it was very clear that total charges and total cost played a major role in deciding whether the claim is genuine or fraud.
The dataset was also checked if it was balanced or not and it was found to be imbalanced so in order to fix this over sampling by smote was implemented to fix it. A classification model was built by splitting the dataset into test and train dataset and finding the right hyper parameters to Random forest classifier, Decision tree, Ada boost and XG boost were found using grid search cv and then the accuracy of the models were found.
Decision Tree Algorithm was selected as the best fit for the model which had a very good accuraccy andmodel was deployed using streamlit framework and API was created with the help of heroku


For  EDA refer  = Insurance Claim Project.pdf
For feature selection, outlier detection , Model Building refer = Final_DT.ipynb
For Deployment refer = Deployment.py
Heroku Deployment link = https://insurance-claim-api.herokuapp.com/
