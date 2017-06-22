print "Hello.. Welcome to SPYCHAT..!! :D"
from datetime import datetime

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy=Spy
friends=[]


#ask spy name
Spy.name = raw_input("What is your Spy name: ")
if len(spy.name)>0:
    print "Welcome " + Spy.name +  " to the spychat:)"

    #spy salutation
    Spy.salutation = raw_input("what should i call you before yur name Mr. or Ms. ? ")
    Spy.name = Spy.salutation + " " + Spy.name
    print "Alright " + Spy.name + " we need some information about you. Please help us know more about you with giving us few of your details.."

    Spy.age=0
    Spy.rating=0.0
    Spy.is_online=False
    Spy.age = raw_input("What is your Age?  ")

    Spy.age= int(Spy.age)

    #Age cannot be less than 15 and no spies greater than 50 are allowed to exist
    #For condition check we are using Nested If

    if Spy.age>15 and Spy.age<50:

        Spy.rating = raw_input("What rating would yu like to give us ")
        Spy.rating = float(Spy.rating)

        if Spy.rating > 4.5:
            print "Good experience."
        elif Spy.rating > 3.5 and Spy.rating <=4.5 :
            print "not bad experience"
        elif Spy.rating >= 2.5 and Spy.rating<=3.5 :
            print "bad experience"
        else:
            print"yu can do better"

        #online
        Spy.is_online= True



        #one final message with all the details
        print "information complete.. Welcome "+ Spy.name +" age: "+ str(Spy.age) + " and rating of: " + str(Spy.rating) + "... nice to have you on this"


    else:
        print "Sorry you are not eligible to use :("

else:
    print "name not valid. Try again please"