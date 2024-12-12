def say_bye():
    """Shows a message that signifies the end of chat.

    Returns
    -------
    bool : 
        Always returns True
    """
    print('Have a great day, and thank you for using our services!')
    return True

def chatbox():
    """An interactive chatbox that allows patients to see operation hours, schedule, and view appointments at Triton Clinic.
    """
    
    # Opening message that directs patient to choose an option and get started with chatbox interaction
    print("Welcome to Triton clinic! I'm happy to assist! Press 1 to view our hours. Press 2 to create an appointment. Press 3 to view your appointment.")

    # An instance of ClinicScheduling created to allow patient to schedule appointments
    from my_modules.classes import ClinicScheduling
    patient_schedule = ClinicScheduling()

    # Infinite loop so patient can keep sending input as much as they want
    while True:
        
        # Collects patient's input
        user_input = input('Client: ').strip()
        
        # Patient typing 'bye' will call say_goodbye to show a bye message and exit the chat
        if user_input.lower() == 'bye':
            if say_bye():
                break

        # if patient chooses option 1, message will show clinic's operation hours
        elif user_input == '1':
            print('We operate Monday to Friday, from 8:00 to 17:00. Our last time slot is at 16:00')

        # if patient chooses option 2, chatbox will possibly schedule an appointment
        elif user_input == '2':

            # Chatbox requests patient's full name
            patient_name = input('Please provide your full name: ').strip()

            # Will exit chat if patient types 'bye'
            if patient_name.lower() == 'bye' and say_bye():
                break

            # Chatbox will request desired day of appointment
            day = input('Please provide your desired day: ').strip()

             # Will exit chat if patient types 'bye'
            if day.lower() == 'bye' and say_bye():
                break

            # Chatbox will request desired time of appointment
            time = input('Please provide your desired time: ').strip()

            # Will exit chat if patient types 'bye'
            if time.lower() == 'bye' and say_bye():
                break

            # Check if appointment meets all requirements to be scheduled
            output = patient_schedule.schedule_appointment(patient_name, day, time)
            print(f"Triton Clinic: {output}")

        # If patient chooses option 3, chatbox will check their appointment status
        elif user_input == '3':
            patient_name = input("Please enter your name to view your appointment: ").strip()

            # Will exit chat if patient types 'bye'
            if patient_name.lower() == 'bye' and say_bye():
                break

            # Check and display patient's appointment status
            output = patient_schedule.check_appointment(patient_name)
            print(f"Triton Clinic: {output}")

        # If patient does not input any of the options, display error message
        else:
            print('Please choose one of the three options')
