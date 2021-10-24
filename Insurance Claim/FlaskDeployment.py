import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import re
import math

app = Flask("__name__")

q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")



@app.route("/", methods=['POST'])
def InsuranceClaimPrediction():
    data = pd.read_csv("Insurance Dataset.csv")
    data1=data.copy()


# In[6]:


data1.head(10)


# # Fill nan values with mode value

# In[7]:


data1["Area_Service"].fillna('Hudson Valley',inplace=True) # data['Area_Service'].mode() = Hudson Valley
data1["Hospital Id"].fillna(413.0,inplace=True) # data['Hospital Id'].mode() = 413.0
data1["Hospital County"].fillna('Erie',inplace=True) # data['Hospital County'].mode() = Erie
data1["Mortality risk"].fillna(1.0,inplace=True) # data['Mortality risk'].mode() = 1.0


# In[8]:


data1.isna().sum() # it is clear that the data is cleaned


# # Checking for duplicte rows

# In[9]:


#Print the duplicated rows
data1[data1.duplicated()]


# In[10]:


#Count of duplicated rows
data[data.duplicated()].shape


# In[11]:


data_cleaned=data1.drop_duplicates()


# In[12]:


data_cleaned.shape


# In[13]:


len(data_cleaned['Days_spend_hsptl'].unique())


# In[14]:


data_cleaned['Days_spend_hsptl'].unique()


# In[15]:


data_cleaned['Days_spend_hsptl'].replace(to_replace='120 +',value='121',inplace=True)


# In[16]:


data_cleaned['Days_spend_hsptl']=data_cleaned['Days_spend_hsptl'].astype('int64')


# In[17]:


data_cleaned['Days_spend_hsptl'].unique()


# In[18]:


Q1 = data_cleaned.quantile(0.25)
Q3 = data_cleaned.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[19]:


data_cleaned = data_cleaned[~((data_cleaned < (Q1 - 1.5 * IQR)) |(data_cleaned > (Q3 + 1.5 * IQR))).any(axis=1)]


# In[ ]:





# # converting coloumns with string datatypes into categorical data using label encoder

# In[20]:


labelencoder = LabelEncoder()
data_cleaned.iloc[:,0] = labelencoder.fit_transform(data_cleaned.iloc[:,0])
data_cleaned.iloc[:,1] = labelencoder.fit_transform(data_cleaned.iloc[:,1])
data_cleaned.iloc[:,3] = labelencoder.fit_transform(data_cleaned.iloc[:,3])
data_cleaned.iloc[:,4] = labelencoder.fit_transform(data_cleaned.iloc[:,4])
data_cleaned.iloc[:,5] = labelencoder.fit_transform(data_cleaned.iloc[:,5])
data_cleaned.iloc[:,6] = labelencoder.fit_transform(data_cleaned.iloc[:,6])
data_cleaned.iloc[:,8] = labelencoder.fit_transform(data_cleaned.iloc[:,8])
data_cleaned.iloc[:,9] = labelencoder.fit_transform(data_cleaned.iloc[:,9])
data_cleaned.iloc[:,12] = labelencoder.fit_transform(data_cleaned.iloc[:,12])
data_cleaned.iloc[:,15] = labelencoder.fit_transform(data_cleaned.iloc[:,15])
data_cleaned.iloc[:,17] = labelencoder.fit_transform(data_cleaned.iloc[:,17])
data_cleaned.iloc[:,18] = labelencoder.fit_transform(data_cleaned.iloc[:,18])


# 

# In[21]:


data_cleaned.drop(['Abortion','Surg_Description','Emergency dept_yes/No','ethnicity','Admission_type','Area_Service','Weight_baby','Hospital County','Gender','Cultural_group','Payment_Typology','Mortality risk'],inplace=True,axis=1)


# In[22]:


X=data_cleaned.drop(['Result'],axis=1)


# In[23]:


Y=data_cleaned.Result
Y


# In[24]:


# Redefining values as the coloumns are deleted


# # ## Check whether Data is Balanced or Imbalanced

# In[28]:


from imblearn.combine import SMOTETomek
smot = SMOTETomek(ratio="auto",random_state=42)
x_smot, y_smot = smot.fit_sample(X,Y)


# From the data we came to know that data is containing 75% of Genuine data (1) and 25% of Fraudulent (0) data.
# This imbalance may create biasness in the model towards Genuine data, So Over Sampling is done to balance the data.


# In[27]:
inputQuery1 = request.form['query1']
inputQuery2 = request.form['query2']
inputQuery3 = request.form['query3']
inputQuery4 = request.form['query4']
inputQuery5 = request.form['query5']
inputQuery6 = request.form['query6']
inputQuery7 = request.form['query7']
inputQuery8 = request.form['query8']
inputQuery9 = request.form['query9']
inputQuery10 = request.form['query10']
inputQuery11 = request.form['query11']
# splitting the data into training and testing dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_smot, y_smot,test_size=0.3)


# In[28]:


# applying decision tree classification
from sklearn.tree import DecisionTreeClassifier
Model = DecisionTreeClassifier(criterion='gini',max_depth=14,max_features=9)
Model.fit(x_train,y_train)
y_pred = Model.predict(x_test)

# Create the pandas DataFrame 
    new_df = pd.DataFrame(data, columns = ['Hospital ID','Age','Days_spend_hsptl','Home or self care','ccs_diagnosis_code','ccs_procedure_code','drug description','Code_illness','Surg_Description','Tot_charg','Tot_cost'])
    single = model.predict(new_df)
    probability = model.predict_proba(new_df)[:,1]
    print(probability)
    if single==1:
        output = "insurance claim is genuine"
        output1 = "Confidence: {}".format(probability*100)
    else:
        output = "Insurance Claim is Fraud"
        output1 = ""
    
    return render_template('home.html', output1=output, output2=output1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'],query9 = request.form['query9'],query10 = request.form['query10'],query5 = request.form['query11']])
    
app.run()


