import string
N=26
N2 = N*N

def to676(bigramm, count):
    res = string.ascii_lowercase.index(bigramm[count][0])*N+string.ascii_lowercase.index(bigramm[count][1])
    return res

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

print ('Введите строку')
s = input()
print('Введенная строка: '+s)
print('Введите первую известную биграмму')
know1= input().split(" ")
#print(know1)
print('Введите вторую известную биграмму')
know2= input().split(" ")

T1 = to676(know1,0)
T2 = to676(know2,0)
C1 = to676(know1,1)
C2 = to676(know2,1)

gcd, x, y= extended_gcd(abs(C1-C2),N2)
#print('The GCD is', gcd)
#print(f'x = {x}, y = {y}')
rev_rasnC=x
if rev_rasnC<0:
    rev_rasnC+=N2
ah=(abs(T1-T2))*rev_rasnC%N2
bh=(T1-ah*C1)%N2
print(rev_rasnC, ' ', ah," ", bh)
res=''
for i in range(0,len(s), 2):
    Ci=string.ascii_lowercase.index(s[i])*N+string.ascii_lowercase.index(s[i+1])
    Ti=(ah*Ci+bh)%N2
    print(Ti)
    res+=chr(ord('`')+Ti//N+1)
    res+=chr(ord('`')+Ti%N+1)
print(res)    
#print(str(T1)+" "+str(T2))
#print(str(C1)+" "+str(C2))