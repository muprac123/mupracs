from tabulate import tabulate

##FOR AND GATE
##x1 = [0,0,1,1]
##x2 = [0,1,0,1]
##w1 = [1,1,1,1]
##w2 = [1,1,1,1]
##
##t=2
##
##print("x1  x2  w1  w2  t   O")
##for i in range(len(x1)):
##    if(x1[i]*w1[i] + x2[i]*w2[i] ) >= t:
##        print(x1[i],' ',x2[i],' ',w1[i],' ',w2[i],' ',t,' ',1)
##    else:
##        print(x1[i],' ',x2[i],' ',w1[i],' ',w2[i],' ',t,' ',0)


##FOR OR GATE
##x1 = [0,0,1,1]
##x2 = [0,1,0,1]
##w1 = [1,1,1,1]
##w2 = [1,1,1,1]
##
##t=1
##
##print("x1  x2  w1  w2  t   O")
##for i in range(len(x1)):
##    if(x1[i]*w1[i] + x2[i]*w2[i] ) >= t:
##        print(x1[i],' ',x2[i],' ',w1[i],' ',w2[i],' ',t,' ',1)
##    else:
##        print(x1[i],' ',x2[i],' ',w1[i],' ',w2[i],' ',t,' ',0)


##FOR NOT GATE
x = [0,1]
w = [-1,-1]
t=0

print("x    w   t   O")
for i in range(len(x)):
    if(x[i]*w[i]) >= t:
        print(x[i],' ',w[i],' ',t,' ',1)
    else:
        print(x[i],' ',w[i],' ',t,' ',0)

        
