import sys_setup

from element import *
from linked_list import *

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

ll = Linked_List(e1)
ll.append(e2)
print("Before inserting at start.")
ll.display()
ll.insert_first(e3)
print("After inserting 3 at start.")
ll.display()
