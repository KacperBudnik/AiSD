def NWD(a,b):
    while a!=b:
        if a>b:
            if b==1:
                a=1
            else:   
                if a>b*10**3:
                    p=4
                    while a>b*10**p:
                        p+=1
                    p-=1
                    a-=b*10**p
                else:
                    a-=b
        else:
            if a==1:
                b=1
            else:
                if b>a*10**3:
                    p=4
                    while b>a*10**p:
                        p+=1
                    p-=1
                    b-=a*10**p
                else:
                    b-=a
    return a


class Fraction:
    def __init__(self, Num, Dem):
        if type(Num)!=int or type(Dem)!= int:
            raise TypeError("Muszą być liczby całkowite")
        
        if Dem==0:
            raise ValueError("Mianownik musi być różny od zera")
        
        nwd=NWD(abs(Num),abs(Dem))
        self.sign = 1 if Num*Dem>0 else -1 if Num*Dem<0 else 0
        self.num=abs(Num)//nwd
        self.dem=abs(Dem)//nwd
        
    def __add__(self, other):
        return Fraction(self.sign*self.num*other.dem + other.sign*other.num*self.dem, self.dem*other.dem)
    
    def __sub__(self, other):
        return Fraction(self.sign*self.num*other.dem - other.sign*other.num*self.dem, self.dem*other.dem)   
    
    def __mul__(self, other):
        return Fraction(self.sign*other.sign*self.num*other.num, self.dem*other.dem)
    
    def __truediv__(self, other):
        return self * Fraction(other.sign*other.dem, other.num)
        
    def __gt__(self,other):
        if self.sign*self.num*other.dem > other.sign*other.num*self.dem:
            return True
        return False
    
    def __ge__(self,other):
        if self.sign*self.num*other.dem >= other.sign*other.num*self.dem:
            return True
        return False
    
    def __eq__(self, other):
        if self.sign*self.num*other.dem == other.sign*other.num*self.dem:
            return True
        return False
                
    def getNum(self):
        return self.num
    
    def getDem(self):
        return self.dem
    
    def __str__(self):
        return str(self.sign*self.num)+" // "+ str(self.dem)
    
    





















class frac:
    
    mixed=False # Normalny czy mieszany
    precision=0 # Do którego miejsca po przecinku cyfry mają znaczenie. 0-maksynalne
    decimal=False # Czy wyświetlać w postaci ułamka dziesiętnego (ważniejsze niż mixed)
    
    def __init__(self, Num, Dem=1):
        
        if type(Num) not in (float,int, frac) or type(Dem) not in (float,int,frac):
            raise TypeError("Musisz podać liczbę")

        if Dem==0:
            raise ValueError("Mianownik musi być różny od zera")
        
        self.sign = 1 if Num*Dem>0 else -1 if Num*Dem<0 else 0
        
        
        if frac.precision==0:
            num=Num.as_integer_ratio()
            dem=Dem.as_integer_ratio()
            Num=abs(num[0]*dem[1])
            Dem=abs(num[1]*dem[0])
        else:
            Num=int(abs(Num*10**frac.precision))
            Dem=int(abs(Dem*10**frac.precision))

        if Num!=0:
            nwd=NWD(Num,Dem)
        else:
            nwd=1
            Dem=1
        self.num=Num//nwd
        self.dem=Dem//nwd
        
    def __add__(self, other):
        if type(other)!=frac:
            other=frac(other)
        return frac(self.sign*self.num*other.dem + other.sign*other.num*self.dem, self.dem*other.dem)
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        #return frac(self.sign*self.num*other.dem - other.sign*other.num*self.dem, self.dem*other.dem)
        return self+(-1)*other
    
    def __rsub__(self, other):
        return -1*self+other
    
    def __pow__(self, power):
        if type(power)==frac:
            power=power.num/power.dem
        return frac((self.sign*self.num)**power, self.dem**power) if power > 0 else frac((self.sign*self.dem)**(-power), self.num**(-power))
    
    def __rmul__(self, other):
        return self*other
    
    def __mul__(self, other):
        if type(other)!=frac:
            other=frac(other)
        return frac(self.sign*other.sign*self.num*other.num, self.dem*other.dem)
    
    def __truediv__(self, other):
        return self * other**(-1)
        
    def __gt__(self,other):
        if type(other)!=frac:
            other=frac(other)
        if self.sign*self.num*other.dem > other.sign*other.num*self.dem:
            return True
        return False
    
    def __ge__(self,other):
        if type(other)!=frac:
            other=frac(other)
        if self.sign*self.num*other.dem >= other.sign*other.num*self.dem:
            return True
        return False
    
    def __eq__(self, other):
        if type(other)!=frac:
            other=frac(other)
        if self.sign*self.num*other.dem == other.sign*other.num*self.dem:
            return True
        return False
    
    def __lt__(self,other):
        if type(other)!=frac:
            other=frac(other)
        if self.sign*self.num*other.dem < other.sign*other.num*self.dem:
            return True
        return False
    
    def __le__(self,other):
        if type(other)!=frac:
            other=frac(other)
        if self.sign*self.num*other.dem <= other.sign*other.num*self.dem:
            return True
        return False
            
    def getNum(self):
        return self.num
    
    def getDem(self):
        return self.dem
    
    def __str__(self):
        if frac.decimal:
            return str(self.sign*self.num/self.dem)
        elif not self.mixed or self.num//self.dem == 0:
            return str(self.sign*self.num)+" // "+ str(self.dem) if self.dem != 1 else str(self.sign*self.num)
        else:
            a = self.num//self.dem
            b = self.num - a*self.dem
            return str(self.sign*a) + " i " + str(b) + " // " + str(self.dem) if b !=0 else str(self.sign*a)
        
    def __repr__(self):
        return self.__str__()
        
    def __abs__(self):
        return frac(self*self.sign)
    
    def as_integer_ratio(self):
        return (self.sign*self.num, self.dem)
    
    def __neg__(self):
        return frac((-1)*self)
    
    def __pos__(self):
        return frac(self)
    
    def __float__(self):
        return self.sign*self.num/self.dem
    
    def __int__(self):
        return self.sign*(self.num//self.dem)
        
#frac.precision=2
#a=frac(2,3)
#b=frac(1,2)
#b*2

"""
import math
a=frac(1,2)
b=frac(1,3)
c=frac(-1/2)
f=frac(math.pi)

a+b
a-b
a*b
a+c
a-c
a*5
frac.mixed=True
a*5
f
frac.decimal=True
f
h=a**b
h
h=h**3
h
h-a
a-1/2
frac(1/4)**a
frac.decimal=False
frac.mixed=False
a=frac(1,1)
a
a/2
a>1/2
a/2>1/2
a/2>=1/2
1/2>=a/2
a/2>=frac(1/3)
1==a
(a/2).as_integer_ratio()

frac.decimal=True
k=-f
k
k+f

frac.decimal=False


float(f)
int(f)
f
math.sin(f)
math.sin(math.pi)-math.sin(f)
math.exp(frac(1,2))-math.e**(1/2)
"""