#lists are mutable, tuples are immutable - can be used with square brackets and round brackets

#Create a tuple with different data types

tuplex = ("tuple", False, 3, 2, 1)
print(tuplex)

#create a tuple
tuplex = (4,6,2,8,3,1)
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#counts the number of occurences of item 50 from a tuple
tuple1 = (50,10,60,70,50)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isnt defined, is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)

#Flip Flop
#function to check whether palindrome or not
def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s] != r[e]):
            return False
        
        s+=1 #s=s+1
        e-=1 #e=e-1
    return True

r = (1,2,3,3,2,1)

if(palind(r)):
    print("The Tuple is Flip-Flop")
else:
    print("The tuple is not Flip-Flop")
    
 
#Weather Prediction   
weather = (1,0,0,0,1,1,0) #0 means rainy, 1 means sunny
sunny = 0
rainy = 0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
        
if(sunny>rainy):
    print("Good weather")

else:
    print("Bad Weather")