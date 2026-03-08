class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def pegar_emprestado(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print("Livro emprestado com sucesso!")
        else:
            print("Livro indisponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print("Livro devolvido com sucesso!")
        else:
            print("Este livro não está com o usuário.")

    def listar_livros(self):
        if not self.livros_emprestados:
            print("Nenhum livro emprestado.")
            return
        print("Livros emprestados pelo usuário:")
        for livro in self.livros_emprestados:
            print(livro)

    def __str__(self):
        return f"Usuário: {self.nome} | Matrícula: {self.matricula}"