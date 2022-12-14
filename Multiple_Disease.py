import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
import sklearn

# Loading the saved models
diabetes = pickle.load(open("diabetes_model.sav", "rb"))

heart = pickle.load(open("heart_model.sav", "rb"))

alzheimer = pickle.load(open("alzheimer_model.sav","rb"))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu("Health Assistant",
                            ["Alzheimer",
                            "Diabetes",
                            "Heart Disease",],
                            default_index=0)

if (selected == "Alzheimer"):
    st.title("Alzheimer predictions using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sex = st.text_input('Sex')
        
    with col2:
        age = st.text_input('Age')
    
    with col3:
        educ = st.text_input('Years of education')
    
    with col1:
        ses = st.text_input('Socioeconomic status')
    
    with col2:
        cdr = st.text_input('Clinical dimentia rating')
    
    with col3:
        mmse = st.text_input('Mini mental state examination')

    with col1:
        etiv = st.text_input('Estimated total intracranial volume')
    
    with col2:
        nwbv = st.text_input('Normalized whole brain volume')
    
    with col3:
        asf = st.text_input("Atlas scaling factor")
    
    # code for Prediction
    alz_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Alzheimer Test Result'):
        alz_prediction = alzheimer.predict([[sex,age,educ,ses,mmse,cdr,etiv,nwbv,asf]])
        
        if (alz_prediction[0] == 1):
          alz_diagnosis = 'The person is prone to Alzheimer'
        else:
          alz_diagnosis = 'The person is not prone to Alzheimer'
        
    st.success(alz_diagnosis)
    
    
    

if (selected == "Diabetes"):
    st.title("Diabetes Prediction using ML")
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

if (selected == "Heart Disease"):
    st.title("Heart Disease Predictions using ML")

    introduction = """
    Features for Heart Disease:
1.	Age
2.	Sex
3.	cp: Chest pain
4.	trestbps: resting blood pressure
5.	chol: cholestrol
6.	fbs: fasting blood sugar mg/dl
7.	restecg: resting electrocardiographic results
8.	thalach: maximum heart rate achieved
9.	exang: exercise induced angina
10.	oldpeak: ST depression induced segment
11.	slope: the slope of the peak exercise ST segment
12.	ca: number of major vessles(0-3) colored by flouorsopy
13.	thal: \n
\ta.	0 Normal\n
\tb.	1 Fixed\n
\tc.	2 reversible

    """
    st.write(introduction)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        List = [age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]
        List = [eval(i) for i in List]
        heart_prediction = heart.predict([List])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)



        