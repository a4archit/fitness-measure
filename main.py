import pickle
import pandas 
import streamlit as st

from typing import Dict, Literal


st.set_page_config(page_title="Fitness measure", page_icon="🏋️")

## header
st.header("Fitness Measure", divider=True)
st.write("Are you physically fit or not? Let's check it!")

## importing model
model = pickle.load(open('./model_fitness_measure_7999.pkl', 'rb'))


## ------------------- getting user details ------------------ ##
tab1, tab2 = st.columns([1,1])

with tab1:
    bmi: float = st.number_input(
        label = "Enter your BMI score",
        min_value = 5.0,
        max_value = 80.0,
        step = 1.0,
        value = 21.0
    )

with tab2:
    body_fat: float = st.number_input(
        label = "Your body fat rate (in percentage %)",
        min_value = 0.0,
        max_value = 100.0,
        value = 7.0,
        step = 1.0
    )

with tab1:
    sit_and_bend_forward: float = st.number_input(
        label = "Enter the score of sit and bend forward test (in cm)",
        min_value = -50.0,
        max_value = 50.0,
        value = 0.0,
        step = 1.0
    )


with tab2:
    broad_jump: float = st.number_input(
        label = "Enter the score you achieve in broad jump (in cm)",
        min_value = 0.0,
        max_value = 700.0,
        value = 0.0,
        step = 1.0
    )

with tab1:
    sit_ups_counts: float = st.number_input(
        label = "Enter the total number of sit ups you done within a second",
        min_value = 0.0,
        max_value = 200.0,
        value = 0.0,
        step = 1.0
    )

# with tab2:

if st.button("Is I'm Fit?", type='primary', use_container_width=True):
    with st.spinner("Measuring your fitness...."):

        user_data: Dict[str,float] = {
            'bmi': bmi,
            'body fat_%': body_fat,
            'sit and bend forward_cm': sit_and_bend_forward,
            'broad jump_cm': broad_jump,
            'sit-ups counts': sit_ups_counts
        }

        user_data_df = pandas.DataFrame(user_data, index=[0])

        prediction: Literal[0,1] = model.predict(user_data_df)[0]

        msg = "Your are not a fit person" if prediction else "You are a fit person"

        st.info(msg)

