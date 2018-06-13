#To create a list with user defined inputs.
l1 = [0,0,0,0,0,0]
l1[0] = int(input("Enter a number: "))
l1[1] = int(input("Enter another number: "))
l1[2] = int(input("Enter another number: "))
l1[3] = int(input("Enter another number: "))
l1[4] = int(input("Enter another number: "))
l1[5] = int(input("Enter another number: "))


l2 =["google,facebook,apple,microsoft,tesla"]
print(l1.extend(l2))
print(l1)


#count the number of time an object occur in alist.

l = (1,2,'a', 3,1,4,5,1)
print(l.count(1))
print(l)


#To create a list of number and sort them in ascending order..

l1 = [4,2,6,5,8,1]
l2 = [7,9,8,2,1,0]
l1.sort()
l2.sort()
l = [l1,l2]
print(l)
print("\n")

l1 = [4,2,6,5,8,1]
l2 = [7,9,8,2,1,0]
l1.sort()
l2.sort()
l = l1+l2
print(l)
 

l1 = [4,2,6,5,8,1]
l2 = [7,9,8,2,1,0]
l1.sort()
l2.sort()
l= l1+l2
l.sort()
print(l)


# Implementing using stack 

stack = ["Amit", "Ashish", "Avilash"]
stack.append("Raut")
stack.append("mohan")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)	
print("\n")	 


# Implementing using Queue
queue =["Amit", "Ashish", "Avilash", "Ayush"]
print(queue)
queue.append("deepak")
print(queue)
queue.append("Chandu")
print(queue)
print(queue.pop())                 
print(queue.pop())                 
print(queue)


#To count even amd odd number in that list.

number = (2,4,6,7,5,9,10,11,12,13,14)
count_odd = 0
count_even = 0
for x in number:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

 
