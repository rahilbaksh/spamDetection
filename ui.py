import streamlit as st
import joblib

# Load the saved model
@st.cache_resource
def load_model():
    model = joblib.load(r"C:\Users\HP\Desktop\spam_detection\spam_classifier.pkl")

    return model

model = load_model()

# Streamlit UI Layout
st.title("📩 SMS Spam Detector")
st.markdown("### Enter an SMS message to check if it's spam or not.")

# Input text box
sms_text = st.text_area("Enter SMS message:")

if st.button("Check Spam"):
    if sms_text.strip():  # Ensure the input text is not empty
        # Predict if the message is spam or not
        prediction = model.predict([sms_text])[0]
        
        if prediction == 1:
            result = "🚨 Spam"
        else:
            result = "✅ Not Spam"
        
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a message to check.")
