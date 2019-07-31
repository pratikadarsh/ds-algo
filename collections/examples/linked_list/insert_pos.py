import sys_setup

from element import *
from linked_list import *

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

la = Linked_List(e1)
la.append(e3)
la.append(e4)
print("Before insertion")
la.display()
la.insert_pos(2, e2)
print("After inserting 2 in the 2nd position")
la.display()
