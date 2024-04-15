import getpass
import os

accounts_list = {
    '0001-01':{
        'password': '123456',
        'name': 'Fulano da Silva',
        'value': 100,
        'is_admin': False
    },
    '0002-02':{
        'password': '12345',
        'name': 'Ciclano dos Santos',
        'value': 50,
        'is_admin': False
    },
    '0003-03':{
        'password': '12345',
        'name': 'Admin Gomes',
        'value': 1000,
        'is_admin': True
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5
}

while True:
    print("***************************************")
    print("*** Learn Python - Caixa Eletrônico ***")
    print("***************************************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("***************************************")
        print("*** Learn Python - Caixa Eletrônico ***")
        print("***************************************")
        print('1 - Saldo')
        print('2 - Saque')
        if accounts_list[account_typed]['is_admin']:
            print('10 - Incluir cédulas')

        option_typed = input('Escolhe uma das opções acima: ')

        if option_typed == '1':
            print('Seu saldo é: R$ %s' %accounts_list[account_typed]['value'])
        elif option_typed =='10' and accounts_list[account_typed]['is_admin']:
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = int(input('Digite o valor a ser sacado: '))
            money_slips_user = {}

            if value_typed // 100 > 0 and value_typed // 100 <= money_slips['100']:
                money_slips_user['100'] = value_typed // 100
                value_typed -= value_typed // 100 * 100
            
            if value_typed // 50 > 0 and value_typed // 50 <= money_slips['50']:
                money_slips_user['50'] = value_typed // 50
                value_typed -= value_typed // 50 * 50

            if value_typed // 20 > 0 and value_typed // 20 <= money_slips['20']:
                money_slips_user['20'] = value_typed // 20
                value_typed -= value_typed // 20 * 20
            
            if value_typed != 0:
                print('O caixa não tem cédulas disponíveis para este valor')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                print('Pegue as notas:')
                print(money_slips_user)
            
    else:
        print('Conta inválida')

    input('Pressione <ENTER> para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')