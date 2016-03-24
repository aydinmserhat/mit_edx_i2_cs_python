class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def __init__(self, name):
        Person.__init__(self, name)
        Lecturer.__init__(self, name)
    def say(self, stuff):
        return "Prof. " + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def __init__(self, name):
        Professor.__init__(self, name)
        Lecturer.__init__(self, name)
        Person.__init__(self, name)

    def say(self, stuff):
        return 'Prof. ' + Person.say(self, '')+ 'It is obvious that ' + Lecturer.lecture(self,stuff)

    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self,stuff)

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

stuff = "the sky is blue"

print e.say(stuff)
print le.say(stuff)
print le.lecture(stuff)
print pe.say(stuff)
print pe.lecture(stuff)
print ae.say(stuff)
print ae.lecture(stuff)
