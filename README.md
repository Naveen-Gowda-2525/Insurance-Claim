
# Insurance-Claim
It is an Hospital Insurance project dealing with insurance claim. The business objective was to check if an health insurance claim was genuine or fraudulent.

For  EDA refer  = Insurance Claim Project.pdf.

For Data Preprocessing, Feature Engineering, Model Building refer 
= Final_DT.ipynb.

For Deployment refer = Deployment.py

## API Reference

 https://insurance-claim-api.herokuapp.com/
 
## Data Preprocessing
1-All the null values were replaced by Null values.   
2-All the duplicate values were removed.                        
3-Outliers were removed by applying IQR technique.


## EDA and Feature Engineering Summary
1-Different visualizations were plotted with the help of seaborn and matplotlib libraries to get a deep insight into the data. 

2-Label Encoder was used on the categorical columns to convert them into numeric.

3-Extra trees classifier was used to get the feature scores and the features which had little impact on the model building were eliminated.

![Images](https://github.com/Naveen-Gowda-2525/Insurance-Claim/blob/main/Images/Feature%20Engineering.png?raw=true)
Features Abortion, Surg_Description, Emergencydept_yes/No, ethnicity, Admission_type, Area_Service, Weight_baby, Hospital County, Gender, Cultural_group, Payment_Typology, Mortality risk were dropped as they did not have great impact.

4-Smote oversampling technique was used to create the balance in the result column.

![Images](https://github.com/Naveen-Gowda-2525/Insurance-Claim/blob/main/Images/smote.png?raw=true)

## Model Building
![Images](https://github.com/Naveen-Gowda-2525/Insurance-Claim/blob/main/Images/Model%20Building.png?raw=true)
![Images](https://github.com/Naveen-Gowda-2525/Insurance-Claim/blob/main/Images/Model%20Building1.png?raw=true)

## Model Deployment Screenshot
![Images](https://github.com/Naveen-Gowda-2525/Insurance-Claim/blob/main/Images/Model%20Deployment.png?raw=true)