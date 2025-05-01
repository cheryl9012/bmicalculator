import streamlit as st
import time

st.set_page_config(page_title=" BMI Calculator" , page_icon="😊", layout="centered" )

st.title("BMI Calculator")
st.markdown(""" 
## calculate your bmi and know your health status** weight and height** """)

col1, col2 = st.columns(2)

with col1:
    weight =st.number_input("Enter your weight in kg : " , min_value=1.0 , format ="%.2f" )
with col2:
    height =st.number_input("Enter your height in m : " , min_value=1.0 , format ="%.2f" )

    if height > 0 and weight >0:
        bmi = weight / (height * height)
        st.subheader(f"Your BMI is : ") 
        st.markdown(f"{bmi:.2f}" , unsafe_allow_html = True)

        if bmi < 18.5:
            st.error("You are Underweight")
        elif bmi >= 18.5 and bmi < 25:
            st.success("You are Normal")
        elif bmi >= 25 and bmi < 30:
            st.warning("You are Overweight")
        else:
            st.error("You are Obese")

    else: 
        st.info("please enter a valid weight and height")

  