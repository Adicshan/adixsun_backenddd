import os
import sys

import pandas as pd
from sklearn.linear_model import LogisticRegression


script_path=os.path.dirname(os.path.abspath(__file__))
csv_path=os.path.join(script_path,'Play_tennis.csv')
df=pd.read_csv(csv_path)


outlook_mapping={'Sunny':0,"Rainy":1,"Overcast":2}
temperature_mapping={'Hot':0,'Mild':1,'Cool':2}
humidity_mapping={'High':0,'Normal':1}
windy_mapping={False:0,True:1}


df['Outlook']=df['Outlook'].map(outlook_mapping)
df['Temperature']=df['Temperature'].map(temperature_mapping)
df['Humidity']=df['Humidity'].map(humidity_mapping)
df['Windy']=df['Windy'].map(windy_mapping)


X= df.drop('PlayTennis',axis=1)
y=df['PlayTennis']

model=LogisticRegression()
model.fit(X,y)


input_outlook=''
input_temperature=''
input_humidity=''
input_windy=''


if __name__ == '__main__':
    if len(sys.argv)<5:
        print('no input provided')
    else:
       input_outlook = sys.argv[1]
       input_temperature= sys.argv[2]
       input_humidity=sys.argv[3]
       input_windy=sys.argv[4]  
       input_windy = input_windy.lower() == 'true'
       


outlook_encode=outlook_mapping.get(input_outlook)
temperature_encode=temperature_mapping.get(input_temperature)
humidity_encode=humidity_mapping.get(input_humidity)
windy_encode= windy_mapping.get(input_windy)


user_input=[[outlook_encode,temperature_encode,humidity_encode,windy_encode]]


prediction_proba= model.predict_proba(user_input)
predicted_result= model.classes_[prediction_proba.argmax()]
print(predicted_result)
probability_yes= prediction_proba[0,1]
print(probability_yes)



