from biblioteca import Biblioteca
from livro import Livro, LivroDigital
from usuario import Usuario

biblioteca = Biblioteca()

while True:
    print("\n===== SISTEMA DA BIBLIOTECA =====")
    print("1 - Cadastrar livro físico")
    print("2 - Cadastrar livro digital")
    print("3 - Cadastrar usuário")
    print("4 - Realizar empréstimo")
    print("5 - Devolver livro")
    print("6 - Listar livros disponíveis")
    print("7 - Listar livros emprestados")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)
        print("Livro físico cadastrado com sucesso!")

    elif opcao == "2":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        tamanho = float(input("Tamanho do arquivo (MB): "))
        livro = LivroDigital(titulo, autor, ano, tamanho)
        biblioteca.adicionar_livro(livro)
        print("Livro digital cadastrado com sucesso!")

    elif opcao == "3":
        nome = input("Nome do usuário: ")
        matricula = input("Matrícula: ")
        usuario = Usuario(nome, matricula)
        biblioteca.cadastrar_usuario(usuario)
        print("Usuário cadastrado!")

    elif opcao == "4":
        matricula = input("Matrícula do usuário: ")
        titulo = input("Título do livro: ")
        usuario = biblioteca.buscar_usuario(matricula)
        livro = biblioteca.buscar_livro(titulo)
        if not usuario:
            print("Usuário não encontrado.")
            continue
        if not livro:
            print("Livro não encontrado.")
            continue
        usuario.pegar_emprestado(livro)

    elif opcao == "5":
        matricula = input("Matrícula do usuário: ")
        titulo = input("Título do livro: ")
        usuario = biblioteca.buscar_usuario(matricula)
        livro = biblioteca.buscar_livro(titulo)
        if not usuario:
            print("Usuário não encontrado.")
            continue
        if not livro:
            print("Livro não encontrado.")
            continue
        usuario.devolver_livro(livro)

    elif opcao == "6":
        biblioteca.listar_livros_disponiveis()

    elif opcao == "7":
        biblioteca.listar_livros_emprestados()

    elif opcao == "8":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")