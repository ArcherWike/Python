a = 'sing'
b = a
print('b is',b)
a = 'none'
print('b is',b)
print('a is',a)

L1 = [1, 2, 3]
L2 = L1
L1.append(4)
print('\nTest 1:\nL1 is ', L1, 'L2 is ', L2)
print(L1 == L2)
print(L1 is L2)
L1 = [0, 0, 0]
L2 = [0, 0, 0]
print('\nTest2:\nL1 is ', L1, 'L2 is ', L2)
print(L1 == L2)
print(L1 is L2)

L1 = ['Lista',3,3]
L2 = L1[:]
import copy
L3 = copy.copy(L1)


#what happened?


# In python i variables are actually pointers to the memory space occupied by the object.
#
#           a = 3
#   ________                         _______
#   |       |                       /       \
#   |   a   |--------------------->|    3    |
#   |_______|                       \_______/

a = 3
b = a

#   ________                         _______
#   |       |                       /       \
#   |   a   |--------------------->|    3    |
#   |_______|              .------> \_______/
#   ________              /
#   |       |            /
#   |   b   |-----------/
#   |_______|


print(a is b, a == b)  #<--- True, True

a = "I'm not b"
#what is b?
print("1) a is:",a, "|, b is:",b)
#   ________                         _______
#   |       |                       /       \
#   |   a   |----------            |    3    |
#   |_______|          _\____.----> \_______/
#   ________          /   \          ________
#   |       |        /    '-------->/         \
#   |   b   |-------'              |"I'm not b"|
#   |_______|                       \_________/
print(a is b, a == b)  #<--- False, False


a = 3
b = a
a += 2
print("2) a is:",a, "|, b is:",b)