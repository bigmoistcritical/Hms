import streamlit as st
import os

# Initialize file paths
patients_file = "patients.txt"
doctors_file = "doctors.txt"
appointments_file = "appointments.txt"

# Helper function to check and create files if they don't exist
def initialize_files():
    for file in [patients_file, doctors_file, appointments_file]:
        if not os.path.exists(file):
            open(file, "w").close()

# Patient Management Functions
def add_patient():
    st.subheader("Add a New Patient")
    patient_id = st.text_input("Enter Patient ID:")
    name = st.text_input("Enter Patient Name:")
    age = st.text_input("Enter Patient Age:")
    gender = st.selectbox("Select Gender:", ["Male", "Female", "Other"])
    contact_number = st.text_input("Enter Patient Contact Number:")
    medical_condition = st.text_input("Enter Patient Medical Condition:")

    if st.button("Add Patient"):
        with open(patients_file, "a") as f:
            f.write(f"{patient_id},{name},{age},{gender},{contact_number},{medical_condition}\n")
        st.success("Patient added successfully!")

def view_all_patients():
    st.subheader("View All Patients")
    if os.path.exists(patients_file):
        with open(patients_file, "r") as f:
            patients = f.readlines()
            for patient in patients:
                patient_id, name, age, gender, contact_number, medical_condition = patient.strip().split(",")
                st.write(f"**Patient ID:** {patient_id}, **Name:** {name}, **Age:** {age}, **Gender:** {gender}, **Contact Number:** {contact_number}, **Medical Condition:** {medical_condition}")
    else:
        st.warning("No patient records found!")

def search_patient():
    st.subheader("Search for a Patient")
    patient_id_or_name = st.text_input("Enter Patient ID or Name:")
    
    if st.button("Search Patient"):
        if os.path.exists(patients_file):
            with open(patients_file, "r") as f:
                patients = f.readlines()
                for patient in patients:
                    patient_id, name, age, gender, contact_number, medical_condition = patient.strip().split(",")
                    if patient_id_or_name in [patient_id, name]:
                        st.write(f"**Patient ID:** {patient_id}, **Name:** {name}, **Age:** {age}, **Gender:** {gender}, **Contact Number:** {contact_number}, **Medical Condition:** {medical_condition}")
                        return
                st.error("Patient not found!")
        else:
            st.warning("No patient records found!")

# Doctor Management Functions
def add_doctor():
    st.subheader("Add a New Doctor")
    doctor_id = st.text_input("Enter Doctor ID:")
    name = st.text_input("Enter Doctor Name:")
    specialization = st.text_input("Enter Specialization:")
    contact_number = st.text_input("Enter Contact Number:")

    if st.button("Add Doctor"):
        with open(doctors_file, "a") as f:
            f.write(f"{doctor_id},{name},{specialization},{contact_number}\n")
        st.success("Doctor added successfully!")

def view_all_doctors():
    st.subheader("View All Doctors")
    if os.path.exists(doctors_file):
        with open(doctors_file, "r") as f:
            doctors = f.readlines()
            for doctor in doctors:
                doctor_id, name, specialization, contact_number = doctor.strip().split(",")
                st.write(f"**Doctor ID:** {doctor_id}, **Name:** {name}, **Specialization:** {specialization}, **Contact Number:** {contact_number}")
    else:
        st.warning("No doctor records found!")

def search_doctor():
    st.subheader("Search for a Doctor")
    specialization = st.text_input("Enter Doctor Specialization to Search:")
    
    if st.button("Search Doctor"):
        if os.path.exists(doctors_file):
            with open(doctors_file, "r") as f:
                doctors = f.readlines()
                for doctor in doctors:
                    doctor_id, name, spec, contact_number = doctor.strip().split(",")
                    if specialization.lower() == spec.lower():
                        st.write(f"**Doctor ID:** {doctor_id}, **Name:** {name}, **Specialization:** {spec}, **Contact Number:** {contact_number}")
                        return
                st.error("Doctor not found!")
        else:
            st.warning("No doctor records found!")

# Appointment Management Functions
def book_appointment():
    st.subheader("Book an Appointment")
    patient_id = st.text_input("Enter Patient ID:")
    doctor_id = st.text_input("Enter Doctor ID:")
    date = st.date_input("Select Appointment Date:")
    time = st.time_input("Select Appointment Time:")

    if st.button("Book Appointment"):
        with open(appointments_file, "a") as f:
            f.write(f"{patient_id},{doctor_id},{date},{time}\n")
        st.success("Appointment booked successfully!")

def view_all_appointments():
    st.subheader("View All Appointments")
    if os.path.exists(appointments_file):
        with open(appointments_file, "r") as 

