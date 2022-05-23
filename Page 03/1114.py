correctPassword = 2002

while True:
    password = int(input())

    if password == correctPassword: 
        print('Acesso Permitido')
        break
    if password != correctPassword: 
        print('Senha Invalida')    