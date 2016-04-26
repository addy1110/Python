n= input("Enter the length of list: ")
m= input("Enter the deleting position: ")
k= input("Enter length of reaining list: ")
def delfromcircle(n,m,k):

	a =[]
	for i in range(0, n):
    		a.append(i)
	print "the list is :",a
	pointer = 1
	l = n-k
	for i in range(0,l):
	    move = pointer+m
	    if move > n:
	        newindex = move-n
	        del(a[newindex-1])
	        n= len(a)
	        pointer = newindex
	    else:
	        del(a[move-1])
	        pointer = move
	        n= len(a)
	print "The remaining numbers in the list is: ",a

delfromcircle(n,m,k)
	

	
	

