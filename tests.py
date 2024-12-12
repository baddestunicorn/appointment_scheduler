import pytest
from unittest.mock import patch
from my_modules.classes import ClinicScheduling
from my_modules.functions import say_bye, chatbox

# Test verify_within_days (method)
def test_verify_within_days():
    clinic = ClinicScheduling()
    # verify weekdays will return True
    assert clinic.verify_within_days('Monday') == True
    assert clinic.verify_within_days('Wednesday') == True
    # verify weekends will return False
    assert clinic.verify_within_days('Saturday') == False
    assert clinic.verify_within_days('Sunday') == False

# Test verify_within_hours (method)
def test_verify_within_hours():
    clinic = ClinicScheduling()
    # verify 8:00-16:00 will return True
    assert clinic.verify_within_hours('8') == True
    assert clinic.verify_within_hours('16') == True
    # verify hours outside 8-16 will return False
    assert clinic.verify_within_hours('19') == False
    assert clinic.verify_within_hours('21') == False

# Test is_appointment_available (method)
def test_is_appointment_available():
    clinic = ClinicScheduling()
    # example of preexisting appointment list
    clinic.appointment_list = [{'name': 'Amy Pongpun', 'day': 'Friday', 'time': '12'}]
    # verify same appointment cannot be double-booked
    assert clinic.is_appointment_available('Amy Pongpun', 'Friday', '12') == False
    # verify new name, day, and time is available for booking
    assert clinic.is_appointment_available('Sara Lee', 'Tuesday', '12') == True
    # verify new patient cannot book pre-existing appointment
    assert clinic.is_appointment_available('Sara lee', 'Friday', '12') == False

# Test schedule_appointment (method)
def test_schedule_appointment():
    clinic = ClinicScheduling()
    # return confirmation message if appointment is available
    assert clinic.schedule_appointment('Amy Pongpun', 'Friday', '12') == 'Amy Pongpun, your appointment on Friday at 12 has been successfully confirmed!'
    # return rejection message if appointment already booked
    assert clinic.schedule_appointment('Sara Lee', 'Friday', '12') == "Sorry, but that's already been booked. Please press 2 to pick another time or enter another name."
    # return rejection message if weekend selected
    assert clinic.schedule_appointment('Sara Lee', 'Sunday', '13') == 'Sorry, but please pick a weekday. Press 2 to schedule.'
    # return rejection message if time out of range selected
    assert clinic.schedule_appointment('Sara Lee', 'Thursday', '20') == 'Sorry, but please pick within 8:00 to 16:00. Press 2 to schedule.'

# Test check_appointment (method)
def test_check_appointment():
    clinic = ClinicScheduling()
    # example of pre-existing appointment
    clinic.appointment_list = [{'name': 'Eric Morgan', 'day': 'Wednesday', 'time': '16'}]
    # confirm appointment exists
    assert clinic.check_appointment('Eric Morgan') == 'Eric Morgan, your appointment has already been made.'
    # deny that appointment exists
    assert clinic.check_appointment('Stanley Morgan') == 'Your appointment does not exist.'

# https://stackoverflow.com/questions/20507601/writing-a-pytest-function-for-checking-the-output-on-console-stdout (what I used to write test functions)
# Test say_bye function
def test_say_bye(capsys):
    # Verify say_bye will always return True and print goodbye message
    assert say_bye() == True
    out, err = capsys.readouterr()
    assert out.strip() == 'Have a great day, and thank you for using our services!'

# Test option_1 function
def test_option_1(capfd):
    # verify that by entering '1', clinic's hours are presented and entering "bye" will exit chat
    inputs = iter(['1', 'bye'])
    with patch('builtins.input', lambda _: next(inputs)):
        chatbox()
    out, err = capfd.readouterr()
    assert 'Welcome to Triton clinic!' in out
    assert 'We operate Monday to Friday, from 8:00 to 17:00. Our last time slot is at 16:00' in out
    assert 'Have a great day, and thank you for using our services!' in out

# Test option_2 function
def test_option_2(capfd):
    # 1: Verify appointment can be scheduled and confirmed and 'bye' exits chat
    inputs = iter(['2', 'Choi Beomgyu', 'Thursday', '10', 'bye'])
    with patch('builtins.input', lambda _: next(inputs)):
        chatbox()
    out, err = capfd.readouterr()
    assert 'Welcome to Triton clinic!' in out
    assert 'Choi Beomgyu, your appointment on Thursday at 10 has been successfully confirmed!' in out
    assert 'Have a great day, and thank you for using our services!' in out

    # 2: Deny appointment due to day and time selected and inputting 'bye' will exit chat
    inputs = iter(['2', 'Choi Soobin', 'Sunday', '20', 'bye'])
    with patch('builtins.input', lambda _: next(inputs)):
        chatbox()
    out, err = capfd.readouterr()
    assert 'Welcome to Triton clinic!' in out
    assert 'Sorry, but please pick another day and time. Press 2 to schedule.' in out
    assert 'Have a great day, and thank you for using our services!' in out

# Test option 3 function
def test_option_3(capfd):
    # Since appointment not yet made, patient will receive a denial message and inputting 'bye' will exit chat
    inputs = iter(['3', 'Huening Kai', 'bye'])
    with patch('builtins.input', lambda _: next(inputs)):
        chatbox()
    out, err = capfd.readouterr()
    assert 'Welcome to Triton clinic!' in out
    assert 'Your appointment does not exist.' in out
    assert 'Have a great day, and thank you for using our services!' in out

# Test invalid function
def test_invalid(capfd):
    # If not inputting either '1', '2', '3', or 'bye', a message prompting patient to do so will pop up
    inputs = iter(['10', 'bye'])
    with patch('builtins.input', lambda _: next(inputs)):
        chatbox()
    out, err = capfd.readouterr()
    assert "Welcome to Triton clinic!" in out
    assert "Please choose one of the three options" in out
    assert "Have a great day, and thank you for using our services!" in out





