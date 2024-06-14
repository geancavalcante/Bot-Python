import pywhatkit 
from datetime import datetime

list_people = {
    'Kaio':['17.03','+55 99 ****-****'],
    'Ana': ['09.09','+55 99 ****-****'],
    'Luiz':['14/06','+55 99 ****-****'],
    'Isa':['09/10', '+55 99 ****-****'],
}

class Mensager():

    def __init__(self):
        time = datetime.today().strftime('%d/%m')
        self.time = time

    def bot(self):
        for people in list_people:
          if list_people[people][0] == self.time:
              pywhatkit.sendwhatmsg(list_people[people][1], 'Oi, Feliz aniversário!', 7,30)
              break   
          else:
              print(False)

people = Mensager()
people.bot()

    
        



