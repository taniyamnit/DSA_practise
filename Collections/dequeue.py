from collections import deque

de = deque([1,2,3,4,5])
print(de)

#append inserts elements on the right
de.append(4)

#printing after appending - normal
print(de)

de.appendleft(0)

#printing after appending on the left
print(de)

#deleting element from right - normal
de.pop()

#printing after deleting the element on right - normal
print(de)

#deleting the element on the left
de.popleft()

#printing after deleting the element on left using popleft
print(de)