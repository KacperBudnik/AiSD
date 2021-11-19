def probability(n, k, p):
    # w ciele funkcji umieść swój kod realizujący cel zadania;
    # argument 'n' niech będzie liczbą prób;
    # argument 'k' niech będzie maksymalną liczbą sukcesów;
    # argument 'p' niech będzie prawdpodobieństwem sukcesu w pojedynczej próbie;
    # w zmiennej 'prob' zwróć oczekiwane prawdopodobieństwo;
    # w zmiennej 'count_mult' zwróć liczbę mnożeń, jaką wykonał Twój program;
    # jeśli potrzebujesz, możesz dopisać również inne funkcje (pomocnicze), 
    # jednak główny cel zadania musi być realizowany w tej funkcji;
    
    prob=1 #(1-p)^n
    count_mult=0 # liczba mnożeń
    rev=1-p # zdażenie przeciwne
    
    for i in bin(n)[:1:-1]:
        if i=="1":
            prob*=rev
            count_mult+=1
        rev**=2
        count_mult+=1
        
    prob_i=1 # prawdopodobieństwo w i-tym kroku (1 dla i==0)
    prob_frac=p/(1-p)
    count_mult+=1
    prob_sum=0 # wynik sumy
    newton=1 # n po 0
    for i in range(k+1):
        prob_sum += prob_i
        prob_i = prob_i*prob_frac*((n-i)/(i+1))
        count_mult+=3
    
    prob*=prob_sum
        
        
    return (prob, count_mult)