# import streamlit as st
# import requests

# def main():
#     st.title('Heart Disease Prediction')

#     age = st.number_input('Age', min_value=0, max_value=120, value=50)
#     sex = st.selectbox('Sex', ['Male', 'Female'])
#     cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
#     trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
#     chol = st.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200)
#     fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
#     restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
#     thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
#     exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
#     oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=0.0)
#     slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
#     ca = st.number_input('Number of Major Vessels (0-3) Colored by Flourosopy', min_value=0, max_value=3, value=0)
#     thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

#     if st.button('Predict'):
#         data = {
#             'age': age,
#             'sex': sex,
#             'cp': cp,
#             'trestbps': trestbps,
#             'chol': chol,
#             'fbs': fbs,
#             'restecg': restecg,
#             'thalach': thalach,
#             'exang': exang,
#             'oldpeak': oldpeak,
#             'slope': slope,
#             'ca': ca,
#             'thal': thal
#         }

#         response = requests.get('/predict_heart', params=data)
#         result = response.json()

#         st.success(result['Result'])

# if __name__ == '__main__':
#     main()


import streamlit as st
import requests

def main():
    st.title('Heart Disease Prediction')

    age = st.number_input('Age', min_value=0, max_value=120, value=50)
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
    chol = st.number_input('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200)
    # fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
    # restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
    # thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
    # exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    # oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=0.0)
    # slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    # ca = st.number_input('Number of Major Vessels (0-3) Colored by Flourosopy', min_value=0, max_value=3, value=0)
    # thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    if st.button('Predict'):
        data = {
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            # 'fbs': fbs,
            # 'restecg': restecg,
            # 'thalach': thalach,
            # 'exang': exang,
            # 'oldpeak': oldpeak,
            # 'slope': slope,
            # 'ca': ca,
            # 'thal': thal
        }

        # Replace 'localhost' with your server's hostname or IP address if needed
        response = requests.get('/predict_heart', params=data)
        result = response.json()

        st.success(result['Result'])

if __name__ == '__main__':
    main()
    

