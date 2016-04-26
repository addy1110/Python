a=[0,2,3,5,6,8]
b=[1,4,7,9]

class Solution:
    def findMedian(self,a,b):
        i=j=0
        med1=med2=0
        n= len(a) + len(b)
        while( i+j < (n/2)+1):
            if (i< len(a) and j< len(b)):
                if a[i]<b[j]:
                    med2=med1
                    med1 = a[i]
           
                    i +=1
                else:
                    med2 = med1
                    med1 = b[j]
                    
                    j +=1
            elif i< len(a):
                med2=med1
                med1 = a[i]
              
                i +=1
            elif j< len(b):
                med2 = med1
                med1 = b[j]
                
                j +=1
        if (n%2 == 0):
            return [med2, med1]
        else:
            return med1
        
s= Solution()
print "The Median is: ",s.findMedian(a,b)
