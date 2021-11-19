def ordinary_polynomial_value_calc(coeff, arg):
    # w ciele tej funkcji zawrzyj kod wyliczający wartość wielomianu w tradycyjny sposób;
    # argument 'coeff' niech będzie listą współczynników wielomianu w kolejności od stopnia zerowego (wyrazu wolego) wzwyż;
    # argument 'arg' niech będzie punktem, w którym chcemy policzyć wartość wielomianu;
    # w zmiennej 'count_mult' zwróć liczbę mnożeń, jakie zostału wykonane do uzyskania tego wyniku;
    # w zmiennej 'count_add' zwróć liczbę dodawań, jakie zostału wykonane do uzyskania tego wyniku;
    
    value=0
    count_add=0
    count_mult=0
    
    for i in range(len(coeff)):
        value+=arg**i*coeff[i]
        count_mult+=i+1 # uznałem, że x**0 to nie jest mnożenie
        count_add+=1
        
    return value, count_mult, count_add
  
def smart_polynomial_value_calc(coeff, arg):
    # w ciele tej funkcji zawrzyj kod wyliczający wartość wielomianu w sposób maksymalnie ograniczający liczbę wykonywanych mnożeń;
    # argument 'coeff' niech będzie listą współczynników wielomianu w kolejności od stopnia zerowego (wyrazu wolego) wzwyż;
    # argument 'arg' niech będzie punktem, w którym chcemy policzyć wartość wielomianu;
    # w zmiennej 'count_mult' zwróć liczbę mnożeń, jakie zostału wykonane do uzyskania tego wyniku;
    # w zmiennej 'count_add' zwróć liczbę dodawań, jakie zostału wykonane do uzyskania tego wyniku;
    
    value=0
    count_add=0
    count_mult=0
    value=coeff[-1]
    
    for i in coeff[-2::-1]:
        value=i+value*arg
        count_add+=1
        count_mult+=1
    
    
    return value, count_mult, count_add
  
  
# jeśli potrzebujesz, możesz dopisać również inne funkcje (pomocnicze), 
# jednak główne cele zadania muszą być realizowane w powyższych dwóch funkcjach;