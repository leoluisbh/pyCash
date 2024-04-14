import getpass

print("***************************************")
print("*** Learn Python - Caixa Eletrônico ***")
print("***************************************")

account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')

accounts_list = {
    '0001-01':{
        'password': '123456',
        'name': 'Fulano da Silva',
        'value': 100
    },
    '0002-02':{
        'password': '12345',
        'name': 'Ciclano dos Santos',
        'value': 0
    }
}

if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
    print("***************************************")
    print("*** Learn Python - Caixa Eletrônico ***")
    print("***************************************")
    print('1 - Saldo')
    option_typed = input('Escolhe uma das opções acima: ')
    if option_typed == '1':
        print('Seu saldo é: R$ %s' %accounts_list[account_typed]['value'])

else:
    print('Conta inválida')

