# appointment_scheduler
For UCSD cogs18. Basic chatbox that allows you to schedule and view appointments. 
This project is a clinic scheduling chatbox. The user, or client, has 3 choices.

Option 1: Pressing '1' allows client to see the clinic's operation hours. The Triton Clinic chatbox should respond to this input with 'We operate Monday to Friday, from 8:00 to 17:00. Our last time slot is at 16:00'.

Option 2: Pressing '2' allows client to schedule an appointment. The client will be prompted to input their full name, desired day, then time. The chatbot will check that the day and time are available, and check that the patient has not already scheduled. If all three conditions are satisfied, then the client will receive a message confirming their appointment.

Option 3: Pressing '3' allows client to check if they've already scheduled. They will be prompted to enter their full name. If they haven't scheduled yet, they will receive a message saying their appointment does not exist. Otherwise, they will receive a message saying their appointment has already been made.

Tests do not have docustrings as I felt that was repetitive with docustrings that are already in 'classes.py' and 'functions.py'
