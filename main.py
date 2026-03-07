#Nomes: Eduarda e Ellen

from Biblioteca import Biblioteca
from Livro import Livro
from Usuario import Usuario

biblioteca = Biblioteca()

while True:
    print("\n===== SISTEMA DA BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Realizar empréstimo")
    print("4 - Devolver livro")
    print("5 - Listar livros disponíveis")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do usuário: ")
        matricula = input("Matrícula: ")

        usuario = Usuario(nome, matricula)
        biblioteca.cadastrar_usuario(usuario)

        print("Usuário cadastrado!")

    elif opcao == "3":
        matricula = input("Matrícula do usuário: ")
        titulo = input("Título do livro: ")

        usuario_encontrado = None
        livro_encontrado = None

        for usuario in biblioteca.usuarios:
            if usuario.matricula == matricula:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("Usuário não encontrado.")
            continue

        for livro in biblioteca.livros:
            if livro.titulo == titulo:
                livro_encontrado = livro
                break

        if livro_encontrado is None:
            print("Livro não encontrado.")
            continue

        usuario_encontrado.pegar_emprestado(livro_encontrado)

    elif opcao == "4":

        while True:
            matricula = input("Matrícula do usuário: ")

            usuario_encontrado = None
            for usuario in biblioteca.usuarios:
                if usuario.matricula == matricula:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                break
            else:
                print("Usuário não encontrado. Digite novamente.")

        while True:
            titulo = input("Título do livro: ")

            livro_encontrado = None
            for livro in usuario_encontrado.livros_emprestados:
                if livro.titulo == titulo:
                    livro_encontrado = livro
                    break

            if livro_encontrado:
                break
            else:
                print("Este usuário não possui esse livro. Digite novamente.")

        usuario_encontrado.devolver_livro(livro_encontrado)

    elif opcao == "5":
        biblioteca.listar_livros_disponiveis()

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")