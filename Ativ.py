usuarios = {
    "admin" : "12345"
}

print("="*31)
print("============ LOGIN ============")
print("="*31)
usuario = input("Usuário: ").lower()
senha = input("Senha: ")
print("="*31)

if usuario == "admin" and senha == "12345":
    while True:
        print("\n=========== OPÇÕES ===========")
        print("="*30)
        print("1 - CADASTRAR USUÁRIO")
        print("2 - LISTAR USUÁRIOS")
        print("3 - REMOVER USUÁRIO")
        print("4 - SAIR")
        print("="*30)

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome do usuário: ").lower()
            senha_usu = input("Digite a senha do usuário: ")
            usuarios[nome] = senha_usu 
            print("Usuário cadastrado!")

        elif opcao == 2:
            print("\n========== USUÁRIOS ==========")
            print("="*30)
            for nome, senha in usuarios.items():
                print (f"Usuário: {nome} | Senha: {senha}")

        elif opcao == 3:
            nome = input("Nome do usário para remover: ").lower()

            if nome in usuarios:
                del usuarios[nome]
                print("Usuário removido!")
            else:
                print("Usuário não encontrado")

        elif opcao == 4:
            print("Programa encerrado!")
            break

        else: 
            print("Opção inválida")
else:
    print("Usuário ou senha incorreto!")