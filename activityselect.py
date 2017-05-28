s=[]
f=[]
n=input("Enter the number of activities")
for i in range(n):
    s.append(input("Enter the start time of activity"))
    f.append(input("Enter the finish time of activity"))

print "The activities selected are at indices :"


def activityselect(s,f):
    i=0
    print i

    for j in xrange(1,n):
        if(s[j]>=f[i]):
            print j
            i=j

        

activityselect(s,f)



