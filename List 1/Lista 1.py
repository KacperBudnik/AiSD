def NWD(a,b):
    if a>b:
        return NWD(a-b,b)
    elif b>a:
        return NWD(a,b-a)
    else:
        return a


class Fraction:
    def __init__(self, Num, Dem):
        print(type(Num), type(Dem))
        if type(Num)!=int or type(Dem)!= int:
            raise ValueError("Muszą być liczby całkowite")
        
        if Dem==0:
            raise ValueError("Mianownik musi być różny od zera")
        
        nwd=NWD(abs(Num),abs(Dem))
        self.sign = 1 if Num*Dem>0 else -1 if Num*Dem<0 else 0
        print(self.sign)
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
    
    mixed=False
    
    def __init__(self, Num, Dem=1):

        if Dem==0:
            raise ValueError("Mianownik musi być różny od zera")
        
        self.sign = 1 if Num*Dem>0 else -1 if Num*Dem<0 else 0
        
        num=Num.as_integer_ratio()
        dem=Dem.as_integer_ratio()
                
        Num=abs(num[0]*dem[1])
        Dem=abs(num[1]*dem[0])
        
        nwd=NWD(Num,Dem)
        self.num=Num//nwd
        self.dem=Dem//nwd
        
    def __add__(self, other):
        return frac(self.sign*self.num*other.dem + other.sign*other.num*self.dem, self.dem*other.dem)
    
    def __sub__(self, other):
        return frac(self.sign*self.num*other.dem - other.sign*other.num*self.dem, self.dem*other.dem)   
    
    def __pow__(self, power):
        return frac((self.sign*self.num)**power, self.dem**power) if power > 0 else frac((self.sign*self.dem)**(-power), self.num**(-power))
    
    def __mul__(self, other):
        return frac(self.sign*other.sign*self.num*other.num, self.dem*other.dem)
    
    def __truediv__(self, other):
        return self * frac(other.sign*other.dem, other.num)
        
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
        if not self.mixed or self.num//self.dem == 0:
            return str(self.sign*self.num)+" // "+ str(self.dem) if self.dem != 1 else str(self.sign*self.num)
        else:
            a = self.num//self.dem
            b = self.num - a*self.dem
            return str(self.sign*a) + " i " + str(b) + " // " + str(self.dem) if b !=0 else str(self.sign*a)

    def show_mixed():
        frac.mixed=not frac.mixed