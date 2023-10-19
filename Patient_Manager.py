# Define patient manager class   
from Patient import Patient
class Patient_Manager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # formatts getters into one sentence with under scores as space
    def format_patient_info_for_file(self,patient):
        return patient.__str__()

    # Enter patient info method that allows the user to create a patient object
    def enter_patient_info(self):
        print()
        pid = input("Enter the patient ID: ")
        name = input("Enter the patient name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the gender of the patient: ")
        age = input("Enter the patient's age: ")
        patient_info = Patient(pid,name,disease,gender,age)
        return patient_info

    # Read patients txt file and create a patient object with specific properties for each line in the file.
    def read_patients_file(self):
        with open("Project-Classes-Group-7/patients.txt", 'r') as file:
            for line in file:
                pid, name, disease, gender, age = line.strip().split('_')
                try:
                    age = int(age)
                    pid = int(pid)
                except ValueError:
                    age = "Age"
                    pid = "ID"
                patient = Patient(pid,name,disease,gender,age)
                self.patients.append(patient)
    
    # Searchs for a patient object based on the id entered in the user input and displays
    def search_patient_by_id(self):
        print()
        patient_id = input("Enter a patient ID: ")
        print()
        for patient in self.patients:
            if int(patient_id) == patient.get_pid():
                print("{:<5}{:<20}{:<15}{:<15}{:<15}".format('ID','Name','Disease','Gender','Age\n'))
                return self.display_patient_info(patient)
        else:
            print("Can't find the Patient with the same id on the system \n")

    # Display patient info method to display and format a patient object in the correct format of the output file.
    def display_patient_info(self,patient):
        print("{:<5}{:<20}{:<15}{:<15}{:<15}".format(patient.get_pid(), patient.get_name(), patient.get_disease(), patient.get_gender(),patient.get_age()))
        print()

    # Edit patient info method to edit a specific patient object from the patiens list and then update and write that objects properties to the patients txt file.
    def edit_patient_info_by_id(self):
        found_patient = None
        print()
        patient_id = input("Please enter the id of the patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == int(patient_id):
                found_patient= patient
                break      
        if found_patient != None:
            new_name = input("Enter new Name: ")
            new_disease = input("Enter new disease: ")
            new_gender = input("Enter new gender: ")
            new_age = input("Enter new age: ")
            found_patient.set_name(new_name)
            found_patient.set_disease(new_disease)
            found_patient.set_gender(new_gender)
            found_patient.set_age(new_age)
            self.write_list_of_patients_to_file()
            print()
            print(f"Patient whose ID is {patient_id} has been edited \n")
        else:
            print(f"Cannot find the patient with an ID of {patient_id}")
            
    # Display patient list method that iterates over the patient list and correctly displays each patient objct using the display patient info function       
    def display_patient_list(self):
        for patient in self.patients: 
            self.display_patient_info(patient)
            
    # Write list of patients method which writes and formats a patient object to the patients.txt file 
    def write_list_of_patients_to_file(self):
        with open('Project-Classes-Group-7/patients.txt', 'w') as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")
    
    # Calls the enter patient info which stores it in a variable as a new patient, check to see if the id exists and print the id is already in use if the id of that patient already exists. Else if it does not exist append the new patient object to the patients list and write the new patient object to the patients.txt file and print a message that the patient has been added 
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        for patient in self.patients:
            if int(new_patient.get_pid()) == patient.get_pid():
                print("That Patient ID is already in use please select another ID")   
                break 
        else:
            self.patients.append(new_patient)
            self.write_list_of_patients_to_file()
            print()
            print(f'Patient whose ID is {new_patient.get_pid()} has been added \n')