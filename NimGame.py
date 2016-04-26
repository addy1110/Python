from random import randrange, randint
def nim_status(a): # to check the current status of nim game
    #print ' '.join(map(str,a))
    for i in range(len(a)):
	print a[i],

def nim_suma(c): # used to check current nim sum.Nim sum zero means game is balanced and if not zero then game is unbalanced. 
    suma=0
    for i in range(len(c)):
        suma=suma^c[i] # X-OR Logic is to find the nim sum
    #print "nim sum =",suma
    if suma == 0:
	return True 
    else:
	return False

'''  # comp_take plays on behalf of computer and tries to balance the game by subracting a magic number from one of the created heaps'''
def comp_take(d):
    b=d
    m=0
    n=0
    for i in range(len(b)):
        if nim_suma(b):
	    break
        for j in range(b[i]+1):
            b[i] = b[i] - j
            #print i,j,b[i]
            if nim_suma(b):
                n=j
                m=i
                #a[i]= a[i]-j
                break 
            b[i] = b[i]+j
            #print i,j,b[i]  

    return n,m


''' this rnd_take function is called when if human plays smart and balance the game before computer does, then with comp_take logic computer will pick zero objects as game is already balanced. So, rnd_take just plays a random chance in hope that human will do a mistake'''
def rnd_take(a,n):
    while True:
        r=int(randrange(1,14))
        p=int(randrange(0,n))    
	if a[p]!=0 and a[p]>0: 
	    while True:
                r=int(randrange(1,14))
	        if r>0 and r<=a[p]:
		    break
            break
    return r,p


a=[]
g=h=x=y=0
n = randrange(3,9,2) #calculating n for  no. of heaps 
for i in range(n):
    a.append(int(randrange(9,15,2))) #generating length for each heaps
print "Created",n,"heaps of sizes",
nim_status(a)
print ' '
first = randint(0,1) # randomly choosing [computer,human]
if first == 0:
    print "Player computer goes first"
else:
    print "Player human goes first"

chance = first
while True: 
    if a == [0,0,0] or a == [0,0,0,0,0] or a == [0,0,0,0,0,0,0]:
	break
    if chance == 0:
	if nim_suma(a):
	    g,h = rnd_take(a,n)
	    a[h] = a[h]-g
	#print nim_suma(a)
        else:
	    g,h =comp_take(a)
	print "Player computer took",g,"objects from heap",h+1
	#a[h] = a[h]-g
        chance = chance+1
	nim_status(a)
	print ' '
  
	if a == [0,0,0] or a == [0,0,0,0,0] or a == [0,0,0,0,0,0,0]:
            break
     
    if chance == 1:
	while True:
	    inp=raw_input("Player human enter the number of objects (Y) to take from what heap (X)- in order: Y X ")
            y,x =[int(i) for i in inp.split() if i.isdigit()]
	    if y>0 and y<=a[x-1]:
                break
            print "Player human that is an invalid move, try again"
      
        a[x-1]=a[x-1]-y
	nim_status(a)
	print ' '

        chance = chance-1

if chance == 0:
    print "Player human wins"
if chance == 1:
    print "Player computer wins"  
