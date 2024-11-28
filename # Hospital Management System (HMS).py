import os

# Initialize file paths
patients_file = "patients.txt"
doctors_file = "doctors.txt"
appointments_file = "appointments.txt"

# Patient Management Functions
def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    gender = input("Enter Patient Gender: ")
    contact_number = input("Enter Patient Contact Number: ")
    medical_condition = input("Enter Patient Medical Condition: ")

    with open(patients_file, "a") as f:
        f.write(f"{patient_id},{name},{age},{gender},{contact_number},{medical_condition}\n")
    print("Patient added successfully!")

def view_all_patients():
    if os.path.exists(patients_file):
        with open(patients_file, "r") as f:
            patients = f.readlines()
            for patient in patients:
                patient_id, name, age, gender, contact_number, medical_condition = patient.strip().split(",")
                print(f"Patient ID: {patient_id}, Name: {name}, Age: {age}, Gender: {gender}, Contact Number: {contact_number}, Medical Condition: {medical_condition}")
    else:
        print("No patient records found!")

def search_patient():
    patient_id_or_name = input("Enter Patient ID or Name: ")
    if os.path.exists(patients_file):
        with open(patients_file, "r") as f:
            patients = f.readlines()
            for patient in patients:
                patient_id, name, age, gender, contact_number, medical_condition = patient.strip().split(",")
                if patient_id_or_name in [patient_id, name]:
                    print(f"Patient ID: {patient_id}, Name: {name}, Age: {age}, Gender: {gender}, Contact Number: {contact_number}, Medical Condition: {medical_condition}")
                    return
        print("Patient not found!")
    else:
        print("No patient records found!")

# Doctor Management Functions
def add_doctor():
    doctor_id = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    contact_number = input("Enter Contact Number: ")

    with open(doctors_file, "a") as f:
        f.write(f"{doctor_id},{name},{specialization},{contact_number}\n")
    print("Doctor added successfully!")

def view_all_doctors():
    if os.path.exists(doctors_file):
        with open(doctors_file, "r") as f:
            doctors = f.readlines()
            for doctor in doctors:
                doctor_id, name, specialization, contact_number = doctor.strip().split(",")
                print(f"Doctor ID: {doctor_id}, Name: {name}, Specialization: {specialization}, Contact Number: {contact_number}")
    else:
        print("No doctor records found!")

def search_doctor():
    specialization = input("Enter Doctor Specialization to Search: ")
    if os.path.exists(doctors_file):
        with open(doctors_file, "r") as f:
            doctors = f.readlines()
            for doctor in doctors:
                doctor_id, name, spec, contact_number = doctor.strip().split(",")
                if specialization.lower() == spec.lower():
                    print(f"Doctor ID: {doctor_id}, Name: {name}, Specialization: {spec}, Contact Number: {contact_number}")
                    return
        print("Doctor not found!")
    else:
        print("No doctor records found!")

# Appointment Management Functions
def book_appointment():
    patient_id = input("Enter Patient ID: ")
    doctor_id = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date (YYYY-MM-DD): ")
    time = input("Enter Appointment Time (HH:MM): ")

    with open(appointments_file, "a") as f:
        f.write(f"{patient_id},{doctor_id},{date},{time}\n")
    print("Appointment booked successfully!")

def view_all_appointments():
    if os.path.exists(appointments_file):
        with open(appointments_file, "r") as f:
            appointments = f.readlines()
            for appointment in appointments:
                patient_id, doctor_id, date, time = appointment.strip().split(",")
                print(f"Patient ID: {patient_id}, Doctor ID: {doctor_id}, Date: {date}, Time: {time}")
    else:
        print("No appointments found!")

# Main Menu
while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search for Patient")
    print("4. Add Doctor")
    print("5. View All Doctors")
    print("6. Search for Doctor")
    print("7. Book Appointment")
    print("8. View All Appointments")
    print("9. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 9.")
        continue

    if choice == 1:
        add_patient()
    elif choice == 2:
        view_all_patients()
    elif choice == 3:
        search_patient()
    elif choice == 4:
        add_doctor()
    elif choice == 5:
        view_all_doctors()
    elif choice == 6:
        search_doctor()
    elif choice == 7:
        book_appointment()
    elif choice == 8:
        view_all_appointments()
    elif choice == 9:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")