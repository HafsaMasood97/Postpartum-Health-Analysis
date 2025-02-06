import streamlit as st
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Streamlit App Title with custom styling
st.set_page_config(page_title="Postpartum Depression Risk Predictor", page_icon="🍼")
st.title("Postpartum Depression Risk Predictor")
st.markdown(
    """
    <style>
        .main {background-color: #f8e1e8; padding: 2rem; border-radius: 15px;}
        .header {color: #9b1b30;}
        .subheader {color: #4a9bb5;}
        .prediction {font-weight: bold; font-size: 1.5rem;}
        .result-text {color: #9b1b30;}
        .probability-text {color: #4a9bb5;}
    </style>
    """, unsafe_allow_html=True
)

# Introduction section
st.markdown("""
    <div class="main">
        <h2 class="header">Understand Your Postpartum Mental Health</h2>
        <p class="subheader">Please fill in the details below to predict the likelihood of postpartum depression.</p>
    </div>
""", unsafe_allow_html=True)

# Input Section
st.markdown("<h3 class='subheader'>Fill in the information below:</h3>", unsafe_allow_html=True)

# User input fields
age = st.selectbox("Age Range", ["25-30", "30-35", "35-40", "40-45", "45-50"])
feeling_sad = st.radio("Feeling sad or tearful?", ["Yes", "No", "Sometimes"])
irritable = st.radio("Irritable towards baby & partner?", ["Yes", "No", "Sometimes"])
trouble_sleeping = st.radio("Trouble sleeping at night?", ["Yes", "No", "Often"])
concentration = st.radio("Problems concentrating or making decisions?", ["Yes", "No", "Often"])
appetite = st.radio("Overeating or loss of appetite?", ["Yes", "No", "Not at all"])
guilt = st.radio("Feeling of guilt?", ["Yes", "No", "Maybe"])
bonding = st.radio("Problems bonding with baby?", ["Yes", "No", "Sometimes"])
suicide_attempt = st.radio("Have you attempted suicide?", ["Yes", "No", "Not interested to say"])

# Mapping categorical inputs to numeric values
age_mapping = {"25-30": 27.5, "30-35": 32.5, "35-40": 37.5, "40-45": 42.5, "45-50": 47.5}
mappings = {"Yes": 1, "No": 0, "Sometimes": 0.5, "Often": 2, "Not at all": 0, "Maybe": 0.5, "Not interested to say": 0.5}

# Convert user input to numeric format
input_data = pd.DataFrame({
    "Age": [age_mapping[age]],
    "Feeling sad or Tearful": [mappings[feeling_sad]],
    "Irritable towards baby & partner": [mappings[irritable]],
    "Trouble sleeping at night": [mappings[trouble_sleeping]],
    "Problems concentrating or making decision": [mappings[concentration]],
    "Overeating or loss of appetite": [mappings[appetite]],
    "Feeling of guilt": [mappings[guilt]],
    "Problems of bonding with baby": [mappings[bonding]],
    "Suicide attempt": [mappings[suicide_attempt]]
})

# Prediction button
if st.button("Analyze Risk"):
    try:
        prediction = model.predict(input_data)
        probabilities = model.predict_proba(input_data)[0]
        
        # Display results
        st.markdown("---")
        st.markdown("<h2 class='prediction'>Analysis Results</h2>", unsafe_allow_html=True)
        
        if prediction[0] == 1:
            risk_level = "High Risk 🚨"
            color = "#9b1b30"
            probability = probabilities[1] * 100
            prob_text = f"High Risk Probability: {probability:.1f}%"
        else:
            risk_level = "Low Risk ✅"
            color = "#4a9bb5"
            probability = probabilities[0] * 100
            prob_text = f"Low Risk Probability: {probability:.1f}%"
        
        st.markdown(f"""
            <div style='background-color: {color + "20"}; padding: 1rem; border-radius: 10px;'>
                <h3 style='color: {color};'>Risk Level: {risk_level}</h3>
                <p class='probability-text'>{prob_text}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Add recommendations
        st.markdown("---")
        st.markdown("<h3 class='subheader'>Recommendations</h3>", unsafe_allow_html=True)
        if prediction[0] == 1:
            st.markdown("""
                - Seek immediate professional help
                - Contact a mental health specialist
                - Reach out to support groups
                - Emergency hotline: 1-800-273-TALK (8255)
            """)
        else:
            st.markdown("""
                - Maintain regular check-ins with your healthcare provider
                - Practice self-care routines
                - Stay connected with support networks
                - Monitor your mental health regularly
            """)
            
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        st.error("Please check your inputs and try again.")