import numpy as np

class MathTree:
    def __init__(self,L_number,operator,R_number):
        self.key=operator
        self.right=None
        self.left=None
        
        if R_number:
            if R_number[1]==True:
                self.right=R_number
            elif R_number[1]==False:
                self.right=MathTree(self.cos(R_number[0])) 
        if L_number:
            if L_number[1]==True:
                self.left=L_number
            elif R_number[1]==False:
                self.left=MathTree(self.cos(L_number[0])) 
        
    def cos(txt):
        
        order=np.array([
            ["+","-"],
            ["*","/","\\",":"], # nie ma różnicy między `/`, oraz `\` są dzieleniem prawostronnym
            ["^","**"]])
        
        function=np.array([
            ["sqrt","log_","log","ln","pow","exp","log2"],
            ["sin","cos","tan","cot","sec","cosec"]
            ["arcsin","arccos","asin","acos","arctan","atan","acot","arccot"],
            ["sinh","cosh","tanh","coth","sech","cosech"],
            ["'"]
        ])
        
        i=0
        l=len(txt)
        
        first=""
        secound=""
        
        while i < l:
            if txt[i]=="(":
                j=1
                while True: # założyłem, że nawiasy są poprawnie wstawione
                    if txt[j]==")"
        
        
        while i<l:
            if txt[i].isnumeric():
                j=1
                while i+j<l and txt[i:i+j+1].isnumeric():
                    j+=1
                
                numbers.append(float(txt[i:i+j]))
            elif txt[i] in order[0]:
                operators.append(txt[i])
                action=True
                
            elif txt[i] in order[1]:
                operators.append(txt[i])
                action=True
            
            elif txt[i] in order[2] or txt[i:i+2] in order[2]:
                operators.append("^")
                action=True
            

def derivate(txt):
    tree=MathTree([txt.replace(" ", ""),False],"=",[None,None])


"""        numbers=[]
        operators=[]
        action=False
        last=None
        while i<l:
            if txt[i].isnumeric():
                j=1
                while i+j<l and txt[i:i+j+1].isnumeric():
                    j+=1
                
                numbers.append(float(txt[i:i+j]))
            elif txt[i] in order[0]:
                operators.append(txt[i])
                action=True
                
            elif txt[i] in order[1]:
                operators.append(txt[i])
                action=True
            
            elif txt[i] in order[2] or txt[i:i+2] in order[2]:
                operators.append("^")
                action=True
                    
                    
            i+=1
        return numbers"""