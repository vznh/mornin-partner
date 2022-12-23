import os
class Person:

    def __init__(self, name, pn, city, time = 8):
        self.name = name
        self.pn = pn
        self.city = city
        self.time = time
        self.reminders = []
        
    def loadReminders(self):
        if os.path.exists(f"{self.name}rm.txt"):
            with open(f"{self.name}rm.txt", "r") as f:
                file = f.readlines()
                for line in file:
                    self.reminders.append(line) # self.reminders = []
        else:
            with open(f"{self.name}rm.txt", "x") as f:
                f.close()
            
    def checkReminders(self):
        return (len(self.reminders) > 0)

    def returnPhoneNumber(self):
        return self.pn

    def addReminder(self, reminder):
        self.reminders.append(reminder)
        with open(f"{self.name}rm.txt", "a") as f:
            f.write(f"{reminder}\n")
    
    def removeReminder(self, index):
        self.reminders.pop(index-1)
    
    def clearReminder(self):
        os.remove(f"{self.name}rm.txt")

    def msg(self):
        message = ""
        with open(f"{self.name}rm.txt", "r") as file:
            rm = file.readlines()
        rm = [x.strip("\n") for x in rm]
        for _ in range(len(rm)):
            message += f"{_+1}: {rm[_]}\n" # Convert to message when uploading
        return message

