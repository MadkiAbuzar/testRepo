from pywebio.input import *
from pywebio.output import *

def voting():
    name = input("Enter Your Name", type=TEXT)
    age = input("Enter Your Age", type=NUMBER)

    if  age < 10:
        put_text("Too Old to vote")
    elif(age > 60):
        put_text("Too Young to vote")
    else:
        put_text("Verify Details")
        put_table([["Name","Age"],[name, age]])

        check = checkbox(options=["I hereby confirm my details"])

        if(check):
            selection = radio("Which is the best fantasy universe", ["Marvel", "DC", "None of these"])
            if selection == "DC":
                put_text("Sorry your answer could not be recorded. You were found Naive during the assessment by our invigilators")
            elif selection == "None of these":
                put_text("Sorry your answer could not be recorded. Suggestions by our Invigilators: Mumma ko bolo complan pilaye!")
            else:
                put_text("Your response has been recorded")



voting()

