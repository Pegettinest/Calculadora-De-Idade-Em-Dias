def calcular_anos_em_dias():
    print('Olá, para começarmos, me diga quantos anos você gostaria de converter em dias:')
    anos = input('Digite a quantidade de anos: ')
    print(f'Em {anos} anos, temos {int(anos) * 365} dias.')
    again = input('Gostaria de fazer outra conversão? (s/n): ')
    if again.lower() == 's':
        calcular_anos_em_dias()
    else:
        print('Obrigado por usar o conversor!')
calcular_anos_em_dias()