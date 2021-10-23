import pandas as pd

from flask import Flask, request, render_template
import pickle
app=Flask(__name__)



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")



@app.route("/predict", methods=['POST'])
def predict():
    
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



    model = pickle.load(open('Decision_Tree.sav', 'rb'))



# Create the pandas DataFrame 
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5,inputQuery6, inputQuery7, inputQuery8, inputQuery9, inputQuery10,inputQuery11]]
    new_df = pd.DataFrame(data, columns = ['Hospital ID','Age','Days_spend_hsptl','Home_or_self care','ccs_diagnosis_code','ccs_procedure_code','drug description','Code_illness','Surg_Description','Tot_charg','Tot_cost'])
    single = model.predict(new_df)
    probability = model.predict_proba(new_df)[:,1]
    print(probability)
    if single==1:
        output = "The claim is genuine"
        output1 = "Confidence: {}".format(probability*100)
    else:
        output = "The claim is fraud"
        output1 = ""
    
    
    return render_template('home.html', output1=output, output2=output1, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'],query6 = request.form['query6'],query7 = request.form['query7'],query8 = request.form['query8'],query9 = request.form['query9'],query10 = request.form['query10'],query11 = request.form['query11'])

if __name__ == '__main__':
	app.run(debug=True)    



