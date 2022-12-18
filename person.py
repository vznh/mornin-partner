class Person:

    def __init__(self, name, pn, city, time = 8):
        self.name = name
        self.pn = pn
        self.city = city
        self.time = time
        self.reminders = []

    def getUserData(self):
        return [self.name, self.pn, self.city, self.time]

    def createReminder(self, content):
        self.reminders.append(content)
        return f"{len(self.reminders)}. {content}"
    
    def checkReminders(self):
        if self.reminders == 0:
            return False
        else:
            return True

    def removeReminder(self, number):
        self.reminders.pop(number-1)

    def returnPhoneNumber(self):
        return self.pn
