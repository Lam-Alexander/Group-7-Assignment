from doctor import Doctor
# Create Doctor-Manager class
class Doctor_Manager:

    # Doctor Manager Constructor
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    # Format dr info method to format the doctor objects information to match the txt file
    def format_dr_info(self,doctor):
        return doctor.__str__()
    
    # Read from the doctor txt file, strip and split the data in the file to create a doctor object for each line in the file. Then append that object to the doctors list created in the constructor.
    def read_doctors_file(self):
        with open("Project-Classes-Group-7/doctors.txt", 'r') as file:
            for line in file:
                doctor_id, name ,specialization,working_time,qualification,room_number = line.strip().split('_')
                if name == 'name':
                    name = 'Name'
                if specialization == 'specilist':
                    specialization = 'Speciality'
                if qualification == 'qualification':
                    qualification = 'Qualification'

                try:
                    doctor_id = int(doctor_id)
                    room_number = int(room_number)
                except ValueError:
                    doctor_id= "Id"
                    room_number ="Room Number"
                doctor = Doctor(doctor_id,name,specialization,working_time, qualification,room_number)
                self.doctors.append(doctor)    

    # Prompts user to enter doctor infomotion than returns the inputs in one line.
    def enter_dr_info(self):
        print()
        doctor_id = input("Enter the doctor’s ID: ")
        name = input("Enter the doctor’s name: ")
        specility = input("Enter the doctor’s specility: ")
        work_time = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        doctor = Doctor(doctor_id,name,specility,work_time,qualification,room_number,)
        return doctor
        
    # Prompt user to input ID, Iterates over the for loop to check for that ID, returns that ID if found with .format spacing, if not prints can't find that id.
    def search_doctor_by_id(self):
        print()
        doctor_id = int(input("Enter the doctor ID: "))
        print()
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<15}".format('Id','Name','Speciality','Timing','Qualification','Room Number\n'))
                return self.display_doctor_info(doctor)
        else:

            return print("Can't find the doctor with the same ID on the system\n")

    # Prompt User to input a Doctor name, Iterates over the for loop to check for that name, returns that name along with the information if found with .format spacing if not prints can't find name.        
    def search_doctor_by_name(self):
        print()
        doctor_name = input("Enter the doctor Name: ")
        print()
        for doctor in self.doctors:
            if doctor.get_name() == doctor_name:
                print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<15}".format('Id','Name','Speciality','Timing','Qualification','Room Number \n'))
                return self.display_doctor_info(doctor)
        else:
            return print("Can't find the doctor with the same name on the system\n")
        
    # Displays the doctor object in a table like format with .format to space out the data.    
    def display_doctor_info(self,doctor): 
        print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<15}".format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time().capitalize(), doctor.get_qualification(), doctor.get_room_number()))
        print()

    # Prompt user to enter the doctor ID they would like to edit, set a variable to none, then checks list to find that ID to store to variable set to noneD if variable doesn't == to none prompt user to edit otherwise print can't find ID. 
    def edit_doctor_info(self):
        found_doctor = None
        print()
        doctor_id = int(input("Please enter the id of the doctor that you want to edit their information: "))
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                found_doctor = doctor
                break   
               
        if found_doctor != None:
            new_name = input("Enter new Name: ")
            new_specialization = input("Enter new Specilist in: ")
            new_working_time = input("Enter new Timing: ")
            new_qualification = input("Enter new Qualification: ")
            new_room_number = input("Enter new Room number: ")
            found_doctor.set_name(new_name)
            found_doctor.set_specialization(new_specialization )
            found_doctor.set_working_time(new_working_time)
            found_doctor.set_qualification(new_qualification)
            found_doctor.set_room_number(new_room_number )
            self.write_list_of_doctors_to_file()
            print()
            print(f"Doctor whose ID is {doctor_id} has been edited \n")
        else:
            print(f"Cannot find the doctor with an ID of {doctor_id}")
            
    # Creates a for loop to iterate over each doctor object in the doctors list and uses the display doctor info function to diplay the object
    def display_doctor_list(self):
        for doctor in self.doctors: 
             self.display_doctor_info(doctor)

    # Write a doctor object to the doctors txt file in the correct formating using format_dr_info.
    def write_list_of_doctors_to_file(self):
        with open("Project-Classes-Group-7/doctors.txt", 'w') as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")

    # Calls the enter dr info which stores it in a variable as a new doctor, check to see if the id exists and print the id is already in use if the id already exists, else if it does not exist append the new doctor object to the doctors list and write the new doctor object to the file of doctors,print a message that the doctor has been added.
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        for doctor in self.doctors:
            if int(new_doctor.get_doctor_id()) == doctor.get_doctor_id():
                print("That Doctor ID is already in use please select another ID\n")   
                break
        else:
            self.doctors.append(new_doctor)
            self.write_list_of_doctors_to_file()
            print()
            print(f'Doctor whose ID is {new_doctor.get_doctor_id()} has been added \n')