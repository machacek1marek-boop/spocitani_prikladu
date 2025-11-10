print('cau')

print('spočítam ti přiklad')
cislo_1 = int(input('napiš číslo 1:'))
znamenko = input('napiš znaménko:')
cislo_2 = int(input('napiš číslo 2:'))

#spocitaní
if znamenko == '/':
    vysledek = cislo_1/cislo_2    
elif znamenko == '*':
    vysledek = cislo_1*cislo_2    
elif znamenko == '+':
    vysledek = cislo_1+cislo_2   
elif znamenko == '-':
    vysledek = cislo_1-cislo_2
else:
    print('něco se pokazilo skontrolujte zadání')



print(f'{cislo_1}{znamenko}{cislo_2} se rovna: {vysledek}')



