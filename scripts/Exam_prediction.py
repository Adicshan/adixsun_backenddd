import os
import sys
import math
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
pandas_path = '/opt/render/.local/lib/python3.7/site-packages'
sklearn_path = '/opt/render/.local/lib/python3.7/site-packages'
sys.path.append(pandas_path)
sys.path.append(sklearn_path)

file_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(file_path, 'Exam_data.csv')
df = pd.read_csv(csv_path)

toughness_mapping = {
    'UPSC_IIT_AIIMS_CAT': 0,
    'NDA_NEET_CLAT_SSC': 1,
    'CBSE_ICSE_StateBoard': 2,
    'Class_6-10': 3,
    'UPSC IIT AIIMS CAT': 0,
    'NDA NEET CLAT SSC': 1,
    'CBSE ICSE StateBoard': 2,
    'Class 6-10': 3
}

hour_mapping = {
    'greater_than_10': 0,
    'more than 10': 0,
    'ten': 1,
    'six': 2,
    'three': 3,
    '10': 1,
    '6': 2,
    '3': 3
    
}

consistency_mapping = {
    'seven': 0,
    'six': 1,
    'five': 2,
    'four': 3,
    'three': 4,
    '7':0,
    '6': 1,
    '5': 2,
    '4': 3,
    '3': 4
}

syllabus_mapping = {
    'hundred': 0,
    'eighty': 1,
    'sixty': 2,
    'forty': 3,
    '100':0,
    '80': 1,
    '60': 2,
    '40': 3
}

time_mapping = {
    'eighty': 0,
    'sixty': 1,
    'forty': 2,
    'twenty': 3,
    '80':0,
    '60': 1,
    '40': 2,
    '20': 3,
}

df['Toughness'] = df['Toughness'].map(toughness_mapping)
df['Hours'] = df['Hours'].map(hour_mapping)
df['Consistency'] = df['Consistency'].map(consistency_mapping)
df['Syllabus'] = df['Syllabus'].map(syllabus_mapping)
df['Time'] = df['Time'].map(time_mapping)



# Check for NaN values in the DataFrame


df_cleaned = df.dropna()

# Display the cleaned DataFrame


X = df_cleaned.drop('Pass', axis=1)
y = df_cleaned['Pass']

model = LogisticRegression()


model.fit(X,y)


input_toughness=''
input_hour=''
input_consist=''
input_syllabus=''
input_time=''
if __name__ =="__main__":
    if len(sys.argv)<6:
        print('no input data')
    else:
        input_toughness=sys.argv[1]
        input_hour=sys.argv[2]
        input_consist=sys.argv[3]
        input_syllabus=sys.argv[4]
        input_time=sys.argv[5]

toughness_encode=toughness_mapping.get(input_toughness)
hour_encode=hour_mapping.get(input_hour)
consistency_encode=consistency_mapping.get(input_consist)
syllabus_encode= syllabus_mapping.get(input_syllabus)
time_encode=time_mapping.get(input_time)


user_input=[[toughness_encode,hour_encode,consistency_encode,syllabus_encode,time_encode]]
prediction_proba=model.predict_proba(user_input)
prediction_result=model.classes_[prediction_proba.argmax()]
print(prediction_result)
prediction_yes = prediction_proba[0, 1]
rounded_prediction_yes = round(prediction_yes, 3)
print(rounded_prediction_yes)
