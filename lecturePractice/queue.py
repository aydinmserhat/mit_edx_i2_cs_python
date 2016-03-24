class Queue(object):

    def __init__(self):
        self.elementList = []

    def insert(self, elm):
        self.elementList.append(elm)

    def remove(self):
        if self.elementList == []:
            raise ValueError()
        else:
            element = self.elementList[0]
            self.elementList.remove(element)
            return element

q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()





