import streamlit as st
import joblib

model = joblib.load("placement.pkl")

def main():
    st.set_page_config(page_title="Placement Predictor", page_icon=":guardsman:", layout="centered")
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f8ff;
        }
        .main {
            background-color: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Welcome to Placement Predictor 🎓💼")

    st.sidebar.header("Enter Your Details")
    
    cgpa = st.slider("Choose your CGPA from slider", min_value=0.0, max_value=10.0, step=0.1)
    st.write(f"### Your CGPA: {cgpa:.2f}")

    department = st.selectbox("Select Your Department", ["Computer Science", "Electrical", "Mechanical", "Civil", "Other"])

    st.write(f"### Department: {department}")

    if st.button("Predict"):
        result = model.predict([[cgpa]])

        predicted_package = result[0]
        st.success(f"🔮 **Your Predicted Salary Package**: {predicted_package} LPA")
        
        if cgpa >= 8.5:
            st.write("💡 Excellent CGPA! You’re on track for top companies.")
        elif cgpa >= 7.0:
            st.write("🟠 Solid performance. Consider improving for better offers.")
        else:
            st.write("⚠️ You might need to focus on building skills and projects.")

    st.markdown("""
        <div style='text-align:center; margin-top:30px;'>
        <p style='font-size: 12px;'>Created with ❤️ by Ranjeet Kumar</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
