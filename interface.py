from distutils.debug import DEBUG
import re
from sre_constants import SUCCESS
from flask import Flask, jsonify, render_template, request
import config
from project_app.utils import  MedicalInsurance  ###importing utils means we are runing utils.py


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_charges',methods=['POST'])
def get_insurance_charges():
    if request.method=='POST':
        data = request.form
        print("DATA", data)
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children =eval(data['children'])
        smoker   = data['smoker']
        region   = data['region']

        print("age, sex, bmi, children, smoker, region",age, sex, bmi, children, smoker, region)
        

        med_insurance = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_insurance.get_predicted_charges()
        
        return render_template('home.html', data=charges)



if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER,debug=False)


