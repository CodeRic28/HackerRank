#example array
ar = [3,2,1,3]

#Finding the greatest number
mval = 0
for i in ar:
    if i>mval:
        mval=i
print(mval)
#Counting how many times the greatest number repeats
count = 0
for j in ar:
    if j == mval:
        count = count + 1
print(count)
