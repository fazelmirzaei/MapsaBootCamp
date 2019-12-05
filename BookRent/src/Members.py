import datetime
import random
class Members(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.date = datetime.datetime.now().date()
        self.iD = None  ## because its value is None, there is no need to define in def section as argument
        self.rent = None

   # def idGenerator(self):
   #     if self.iD is None:
   #         self.iD = self.date.year + self.date.month + self.date.day + self.date.minute
   #         print('your ID is {}'.format(self.iD))
   #     else:
   #         print('This member hasbeen found in our database')
   #
   #      self.iD += 1

    def idGenerator(self):
        if self.iD==None:
            self.iD= ''.join(random.sample('0123456789', 5))
            print('Id is: '+ self.iD)
        else:
            for i,j in Members():
                if self.iD[i]==self.iD[j]:
                    print('its a douplicated Id, please try again ')
                else:
                    return
            return


#### Ques: How can I make my class's object iterable???

    def expireCheck(self):
        regdt=datetime.datetime.now().date()
        duedt=datetime.datetime.today().date()
        a=10000*duedt.year+100*duedt.month+duedt.day
        b=10000*regdt.year+100*regdt.month+regdt.day

        if a-b>= 10000:
            print('Please register as soon as possible')
        else:
            print('your registeration is validate')



p1 = Members('hassan', 25)
p2=Members('ali',88)
p3=Members('fazel',77)

p3.idGenerator()
p1.expireCheck()






