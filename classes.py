class ClinicScheduling():
    """Class that can schedule and check appointments.
    """
    
    def __init__(self):
        self.appointment_list = []
        """Initalizes an empyty list to hold appointments in.
        """

    def verify_within_days(self, day):
        """Verifies if appointment is on a weekday (Monday-Friday).

        Parameters
        ----------
        day : str
        Name of day

        Returns
        -------
        answer : bool
        True if chosen date is on a weekday, otherwise False
        """
        # checks if input for day is from Mon-Fri (weekday)
        return day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
    def verify_within_hours(self, time):
        """Verifies if appointment is between the time 8:00 to 16:00.

        Parameters
        ----------
        time : str
        Hours from 8 to 16

        Returns
        -------
        answer : bool
        True if chosen time is from 8 to 16, otherwise False
        """
        # checks if input for time is from 8-16
        return time in ['8', '9', '10', '11', '12', '13', '14', '15', '16']

    def is_appointment_available(self, patient_name, day, time):
        """Checks if patient has booked yet and if slot is available.

        Parameters
        ----------
        patient_name : str
        Name of patient booking appointment
        day : str
        Day requested for appointment
        time : str
        Time requested for appointment

        Returns
        -------
        answer : bool
        False if patient has not already booked or slot not taken, True otherwise
        """
        # Iterates appointment list to see if patient has booked or if appointment is already booked
        for appointment in self.appointment_list:
            if appointment['name'] == patient_name or (appointment['day'] == day and appointment['time'] == time):
                return False
        return True
        
    def schedule_appointment(self, patient_name, day, time):
        """Schedules patient's appointment if they haven't booked yet and if time and day are valid.

        Parameters
        ----------
        patient_name : str
        Name of patient to schedule for
        day : str
        Day of appointment
        time : str
        Time of appointment

        Returns
        -------
        answer : str
        A message that will either confirm the scheduling or deny it with a reason (e.g. patient picked weekend)
        """
        valid_days = self.verify_within_days(day)
        valid_hours = self.verify_within_hours(time)
        
        # Combines previous verification tests and runs them together to ensure no double-booking and valid appointment date
        if not valid_days and not valid_hours:
            return 'Sorry, but please pick another day and time. Press 2 to schedule.'
        if not valid_days:
            return 'Sorry, but please pick a weekday. Press 2 to schedule.'
        if not valid_hours:
            return 'Sorry, but please pick within 8:00 to 16:00. Press 2 to schedule.'
        if not self.is_appointment_available(patient_name, day, time):
            return "Sorry, but that's already been booked. Please press 2 to pick another time or enter another name."

        # Appointment added to list if it passes all checks
        self.appointment_list.append({'name' : patient_name, 'day' : day, 'time' : time})

        # Returns confirmation message with name, day, and time
        return f"{patient_name}, your appointment on {day} at {time} has been successfully confirmed!"

    def check_appointment(self, patient_name):
        """Checks if patient has successfully scheduled an appointment yet.

        Parameters
        ----------
        patient_name : str
        Name of patient to check scheduling for
        
        Returns
        -------
        answer : str
        A message that will either confirm or deny whether or not patient's appointment exists
        """
        # Iterate through appointment list to check for patient's existing appointment, then confirm or deny its existence
        for appointment in self.appointment_list:
            if appointment['name'] == patient_name:
                return f"{patient_name}, your appointment has already been made."
        return 'Your appointment does not exist.'
