import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv(r"D:\pythtest\updated.csv")

l=LabelEncoder()
df['Potability_encoded']=l.fit_transform(df['Potability'])



x=df.drop(columns=['Potability','Potability_encoded'])
y=df['Potability_encoded']

x_train, x_, y_train, y_= train_test_split(x, y, test_size=0.40, random_state=1)
x_cv, x_test, y_cv, y_test = train_test_split(x_, y_, test_size=0.50, random_state=1)

#scaling
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
x_train_scaled = scaler.fit_transform(x_train)
x_cv_scaled = scaler.transform(x_cv)
x_test_scaled = scaler.transform(x_test)



oversample = SMOTE(sampling_strategy={1: 1998}, random_state=42)
X_resampled2, y_resampled2 = oversample.fit_resample(x_scaled, y)

x_train_s2, x_s2, y_train_s2, y_s2= train_test_split(X_resampled2, y_resampled2, test_size=0.4,random_state=1)
x_cv_s2, x_test_s2, y_cv_s2, y_test_s2 = train_test_split(x_s2, y_s2, test_size=0.50, random_state=1)


st.set_page_config(
    page_title='Water Quality Predictor',
    page_icon=r"D:\pythtest\water-drop-icon-isolated-on-white-background-vector-34177727.jpg",
    initial_sidebar_state='collapsed',

)
def load_model(selected_model):
    if selected_model == "knn":
        return joblib.load(open(r"D:\pythtest\models\knn_modelf.pkl", 'rb'))
    elif selected_model == "Logistic Regression":
        return joblib.load(open(r"D:\pythtest\models\logistic_modelf.pkl", 'rb'))
    elif selected_model == "Decision Trees":
        return joblib.load(open(r"D:\pythtest\models\decisiontree_modelf.pkl", 'rb'))
    elif selected_model == "SVM":
        return joblib.load(open(r"D:\pythtest\models\svm_modelf.pkl", 'rb'))
  

models = ["knn", "Logistic Regression", "Decision Trees", "SVM"]
selected_model = st.sidebar.selectbox("Select a Model:", models)
model = load_model(selected_model)
#if selected_model == "knn" or selected_model == "Logistic Regression":
#    model.fit(X_train, y_train)

if selected_model == "knn":
    y_pred=model.predict(x_test_s2)
    acc=accuracy_score(y_test_s2,y_pred)

else:
    y_pred = model.predict(x_test_scaled)
    acc=accuracy_score(y_test,y_pred)







def predict(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    features = np.array([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return prediction[0]

# Main
st.write('# Water Quality Prediction')
st.write('-----------------')


st.subheader('Please , enter the inputs')
ph = st.number_input("Enter PH:", max_value=14.0, min_value=0.0)
Hardness = st.number_input("Enter Hardness:")
Solids = st.number_input("Enter Solids:")
Chloramines = st.number_input("Enter Chloramines:")
Sulfate = st.number_input("Enter Sulfate:")
Conductivity = st.number_input("Enter Conductivity:")
Organic_carbon = st.number_input("Enter Organic_carbon:")
Trihalomethanes = st.number_input("Enter Trihalomethanes:")
Turbidity = st.number_input("Enter Turbidity:")


sample = predict(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)

if st.button("Get the Result"):
        if sample == 0:
            st.write("This sample is not Suitable for Drinking")
            st.image(r"D:\pythtest\do-not-use-tap-water-prohibition-sign-drink-symbol-template-vector-illustration-red-crossed-circle-drop-icon-inside-no-266230605 (1).webp",width=400)
            st.write("Accuracy:")
            st.write(acc)

            
            

        elif sample == 1:
            st.write("This sample is Suitable for Drinking")
            st.image(r"D:\pythtest\isolated-pictogram-safe-drink-water-260nw-2415432797 (1).webp", width=400)
            st.write("Accuracy:")
            st.write(acc)


