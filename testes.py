senha = "marcondys"

chanches = 0
while chanches < 5:
    nome = input("Nome: ")
    if nome == senha:
        print("Bem-vindo!")
        break
    else:
        print("Login ou senha errado.")
    chanches += 1
