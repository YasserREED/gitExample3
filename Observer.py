class Observer():
    def update(self, subject):
        print("Observer : My Subject just  updated and tols me avout it")
        print("Observer: It's status is now - " + str(subject._state))

class Subject():
    _state = 0
    _observer = []

    def attach(self, observer):
        self._observer.append(observer)

    def dettach(self, observer):
        self._observer.remove(observer)

    def notify(self):
        print("Observer: Im Notify my observer ...")
        for observer in self._observer:
            observer.update(self)

    def updatestate(self,n):
        print("Subject: I've received state update")
        self._observer =  n
        self.notify()

s = Subject()

ob1=  Observer()
ob2 = Observer()
ob3 = Observer() 

s.attach(ob1)
s.attach(ob2)
s.attach(ob3)

s.updatestate(5)