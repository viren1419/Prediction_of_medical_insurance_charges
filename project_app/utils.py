import pickle
import json
import numpy as np
import config

class MedicalInsurance():
    def __init__(self, age, sex, bmi, children, smoker, region):       ###parameters
        self.age = age
        self.sex = sex                                                 ### user inputs we created instance variables
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_'+ region
    
    def load_model(self):                                              ### for test we can load pickle file
        with open (config.MODEL_FILE_PATH,'rb')as f:                   ## self >> instance 
            self.model = pickle.load(f)
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)                              ## self>>using for creating variables
    
    def get_predicted_charges(self):                   
        self.load_model()                                              ###previous function we are using as self self.load_model


        region_index = self.json_data['columns'].index(self.region)    ##index of region from list of columns using .index function


        test_array = np.zeros(len(self.json_data['columns']))          ##columns from json files and length 9 items 
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]
        test_array[region_index] = 1
        
        # print("test_array :", test_array)

        predicted_charges = self.model.predict([test_array])
        return predicted_charges

if __name__ ==  "__main__":
        age = 54
        sex = 'male'
        bmi = 28.3
        children =3
        smoker = 'yes'
        region= 'southeast'

        med_insurance = MedicalInsurance(age, sex, bmi, children, smoker, region)  ## MedicalInsurance<< this is instance
        med_insurance.get_predicted_charges()








