import pandas as pd
import random

# General Education Scholars
general_education_scholars = {
    "Name": [f"Scholar {i}" for i in range(1, 11)],
    "Institution": [f"Institution {i}" for i in range(1, 11)],
    "Course": [f"Course {i}" for i in range(1, 11)],
    "Date of Birth": [pd.to_datetime(f"2000-{random.randint(1, 12):02}-{random.randint(1, 28):02}") for _ in range(10)],
    "Date Awarded Scholarship": [pd.to_datetime(f"2020-{random.randint(1, 12):02}-{random.randint(1, 28):02}") for _ in range(10)]
}
general_education_scholars_df = pd.DataFrame(general_education_scholars)
general_education_scholars_df.to_csv("data/general_education_scholars.csv", index=False)

# Tertiary Education Scholars
tertiary_education_scholars = {
    "Name": [f"Scholar {i}" for i in range(11, 21)],
    "Institution": [f"Institution {i}" for i in range(11, 21)],
    "Course": [f"Course {i}" for i in range(11, 21)],
    "Date of Birth": [pd.to_datetime(f"1995-{random.randint(1, 12):02}-{random.randint(1, 28):02}") for _ in range(10)],
    "Date Awarded Scholarship": [pd.to_datetime(f"2015-{random.randint(1, 12):02}-{random.randint(1, 28):02}") for _ in range(10)]
}
tertiary_education_scholars_df = pd.DataFrame(tertiary_education_scholars)
tertiary_education_scholars_df.to_csv("data/tertiary_education_scholars.csv", index=False)

# Scholar Tracker
scholar_tracker = {
    "Scholar Name": [f"Scholar {i}" for i in range(1, 11)],
    "Academic Year": [f"2020-2021" for _ in range(10)],
    "Progress": [random.choice(["Good", "Fair", "Excellent"]) for _ in range(10)]
}
scholar_tracker_df = pd.DataFrame(scholar_tracker)
scholar_tracker_df.to_csv("data/scholar_tracker.csv", index=False)

# Response Network Alumni
response_network_alumni = {
    "Name": [f"Alumnus {i}" for i in range(1, 11)],
    "Graduation Year": [f"20{random.randint(10, 20)}-{random.randint(10, 20)+1}" for _ in range(10)],
    "Current Occupation": [f"Occupation {i}" for i in range(1, 11)],
    "Contact Info": [f"contact{i}@email.com" for i in range(1, 11)]
}
response_network_alumni_df = pd.DataFrame(response_network_alumni)
response_network_alumni_df.to_csv("data/response_network_alumni.csv", index=False)