import streamlit as st
import pandas as pd
from utils.data_utils import load_csv, save_csv

def render():
    st.title("Scholar Tracker")
    st.write("This page displays information about scholars' progress.")

    try:
        # Load the data
        data = load_csv("data/scholar_tracker.csv")
        st.dataframe(data)
    except FileNotFoundError:
        st.write("No data file found. Please enter data manually.")

    # Create a form to add new scholar progress
    st.write("Add a new scholar progress:")
    form = st.form(key="add_progress")
    scholar_name = form.text_input("Scholar Name")
    academic_year = form.text_input("Academic Year")
    progress = form.text_input("Progress")
    submit = form.form_submit_button("Add Progress")

    # Add the new scholar progress to the data
    if submit:
        new_progress = pd.DataFrame({
            "Scholar Name": [scholar_name],
            "Academic Year": [academic_year],
            "Progress": [progress]
        })

        try:
            # Load existing data and append new progress
            data = load_csv("data/scholar_tracker.csv")
            data = pd.concat([data, new_progress])
        except FileNotFoundError:
            # If no data file exists, create a new one
            data = new_progress

        save_csv(data, "data/scholar_tracker.csv")
        st.success("Progress added successfully!")

render()