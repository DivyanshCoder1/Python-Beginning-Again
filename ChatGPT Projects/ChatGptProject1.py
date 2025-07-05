#This project is some ayanokoji style manipulation type project with creating a class of student with
#different students as object and setting their props to different levels

class Student:
    def __init__(self, name, iq):
        self.name = name
        self.iq = iq
        self.trust = {}
        self.secrets = []
    
    def reveal_secret(self,secret):
        self.secrets.append(secret)
        print("-----------")
        print(f"{self.name} reveals a secret: {secret}")
        print("-----------")

    def betray(self, betrayer_student, trust_decrease):
        #Considering here self will be the victim student
        if betrayer_student in self.trust.keys():
            self.trust[betrayer_student] -= trust_decrease
            if self.trust[betrayer_student] < 0:
                self.trust[betrayer_student] = 0
        else:
            #Considering people trust each other easily but there will be some exception in people here
            self.trust[betrayer_student] = 100
            self.trust[betrayer_student] -= trust_decrease
            #done this way to make program undestandable at the place of explicitly setting it to 100 - trsut_decrease


    def gain_trust(self, trust_increase, student):
        if student in self.trust.keys():
            self.trust[student] += trust_increase
            if self.trust[student] > 100:
                self.trust[student] = 100
        else:
            self.trust[student] = 100 # same logic, people trust each other too well in here, can change to 50 is you want to keep everyone a bit sharp
    
    def add_trusted_people(self, trusted_person, trust_value):
        if trusted_person not in self.trust.keys():
            self.trust[trusted_person] = trust_value
            print(f"{trusted_person} is added to trust list of {self.name} with trust value of {trust_value}")
        else:
            print(f"This student is already in the trusted person list for {self.name}, the new trust value will get updated as per input")
    
    def show_profile(self):
        print("------------------------------------------")
        print(f"Profile for {self.name}")
        print(f"IQ: {self.iq}")
        print(f"Trust Level(student wise out of 100): {self.trust}")
        print("Secrets: ")
        print(*self.secrets)
        print("------------------------------------------")
            

Std1 = Student("Std1", 200)
Std2 = Student("Std2", 100)
Std3 = Student("Std3", 150)

# Std1.show_profile()
# Std2.show_profile()

# Std1.reveal_secret("Secret 1")
# Std1.betray("Std2", 50)
# Std1.gain_trust(20, "Std2") 
# Std1.add_trusted_people("Std3", 70) 

# Std1.show_profile()

while True:
    print("Function names are as follows:- "
    "reveal_secret(secret)"
    "betray(betrayer_student, trust_decrease)"
    "gain_trust(trust_increase, student name)"
    "add_trusted_people(student to be trusted, trust score initilaizer)"
    "show_profile()")

    command = input("$ ")

    if command.lower() in ["quit", "exit"]:
        print("Exiting the simulation")
        break

    else:
        try:

            eval(command)
        except Exception as e:
            try:
                exec(command)
            except Exception as ee:
                print(f"Exception occured {ee}")