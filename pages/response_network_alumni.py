import streamlit as st
import pandas as pd
from utils.data_utils import load_csv, save_csv

def render():
    st.title("Alumni Database")
    st.write("This page displays information about our alumni.")

    try:
        # Load the data
        data = load_csv("data/alumni_database.csv")
        st.dataframe(data)
    except FileNotFoundError:
        st.write("No data file found. Please enter data manually.")

    # Create a form to add new alumni
    st.write("Add a new alumnus:")
    form = st.form(key="add_alumnus")
    name = form.text_input("Name")
    graduation_year = form.text_input("Graduation Year")
    current_occupation = form.text_input("Current Occupation")
    contact_info = form.text_input("Contact Info")
    submit = form.form_submit_button("Add Alumnus")

    # Add the new alumnus to the data
    if submit:
        new_alumnus = pd.DataFrame({
            "Name": [name],
            "Graduation Year": [graduation_year],
            "Current Occupation": [current_occupation],
            "Contact Info": [contact_info]
        })

        try:
            # Load existing data and append new alumnus
            data = load_csv("data/alumni_database.csv")
            data = pd.concat([data, new_alumnus])
        except FileNotFoundError:
            # If no data file exists, create a new one
            data = new_alumnus

        save_csv(data, "data/alumni_database.csv")
        st.success("Alumnus added successfully!")

render()