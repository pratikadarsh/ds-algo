''' Class Definition of the building block unit.'''

class Element():

   def  __init__(self,value=None):
        self.next = None
        self.previous = None
        self.value = value
