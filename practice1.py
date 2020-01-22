import math

#Function that displays all numbers that are divisible by 7
#but not divisible by 5 all on one line, separated by commas
##Divisible by 7, Not by 5
if __name__ == '__main__':
    db7nb5()

def db7nb5():
    fin = []
    for i in range(2000,3201):
        if i%7 == 0 and i%5 != 0:
            fin.append(str(i))
    return ','.join(fin)

def dictBuild(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i**2
    return d

def SR(csv):
    l = csv.split(',')
    print(l)
    fin = []
    for i in l:
        fin.append(int(math.sqrt((2*50*int(i))/30)))
    return fin

def twoD(csv):
    inp = csv.split(',')
    print(inp)
    fin = []
    for i in range(int(inp[0])):
        new = []
        for j in range(int(inp[1])):
            new.append(i*j)
        fin.append(new)
    return fin

def Alphabet():
    csv = input()
    fin = [i for i in csv.split(',')]
    fin.sort()
    return fin
