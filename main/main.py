import random

cls = lambda: print('\n'*100)



def  fill_array(s,x,y):
    array=[]
    for i in range(x):
      array.append([s]*y)

    array[0][0]='@'
    return array


def print_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end=' ')
        print()


def read():
    s=input()
    if s=='s':
        return 0
    elif s=='w':
        return 1
    elif s=='d':
        return 2
    elif s=='a':
        return 3






#-------------------------------------------------------------
array = (fill_array('*',5,5))


print()
i=100
course=0
x=0
y=0

c=random.randint(0,4)
d=random.randint(0,4)
array[c][d]='o'
rez=0

a=random.randint(1,4)
b=random.randint(1,4)
array[a][b]='+'
k=round(random.random())+1

print_array(array)


while i >0:
    course=read()
    if (course==0)and(x<len(array)-1):
        x=x+1
        array[x][y]='@'
        array[x-1][y]='*'
        if (x==a)and(y==b)and(k==1):
            i=i+20
            k=-1
        elif(x==a)and(y==b)and(k==2):
            i=i-20
            k = -1
        if (x==c)and(y==d):
            rez=rez+1
            c = random.randint(0, 4)
            d = random.randint(0, 4)
            array[c][d] = 'o'
        i=i-5
        cls()
        print_array(array)
        print(i,'xp')
        print(rez)


    elif (course==1)and(x>0):
        x= x - 1
        array[x][y] = '@'
        array[x + 1][y] = '*'
        if (x==a)and(y==b)and(k==1):
            i=i+20
            k = -1
        elif(x==a)and(y==b)and(k==2):
            i=i-20
            k = -1
        if (x==c)and(y==d):
            rez=rez+1
            while (c==x)and(d==b):
                c = random.randint(0, 4)
                d = random.randint(0, 4)
            array[c][d] = 'o'
        i = i - 5
        cls()

        print_array(array)
        print(i,'xp')
        print(rez)

    elif (course==2)and(y<len(array)-1):
        y=y+1
        array[x][y]='@'
        array[x][y-1]='*'
        if (x==a)and(y==b)and(k==1):
            i=i+20
            k = -1
        elif(x==a)and(y==b)and(k==2):
            i=i-20
            k = -1
        if (x==c)and(y==d):
            rez=rez+1
            c = random.randint(0, 4)
            d = random.randint(0, 4)
            array[c][d] = 'o'
        i=i-5
        cls()
        print_array(array)
        print(i,'xp')
        print(rez)


    elif (course==3)and(y>0):
        y= y - 1
        array[x][y] = '@'
        array[x][y + 1] = '*'
        if (x==a)and(y==b)and(k==1):
            i=i+20
            k = -1
        elif(x==a)and(y==b)and(k==2):
            i=i-20
            k = -1
        if (x==c)and(y==d):
            rez=rez+1
            c = random.randint(0, 4)
            d = random.randint(0, 4)
            array[c][d] = 'o'
        i = i - 5
        cls()

        print_array(array)
        print(i,'xp')
        print(rez)
print('Game Over')