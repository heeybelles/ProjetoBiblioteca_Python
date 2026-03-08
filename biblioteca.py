from livro import Livro, LivroDigital
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, matricula):
        for usuario in self.usuarios:
            if usuario.matricula == matricula:
                return usuario
        return None

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def listar_livros_disponiveis(self):
        print("=== Livros Disponíveis ===")
        encontrados = False
        for livro in self.livros:
            if livro.disponivel:
                print(livro)
                encontrados = True
        if not encontrados:
            print("Nenhum livro disponível no momento.")

    def listar_livros_emprestados(self):
        print("=== Livros Emprestados ===")
        encontrados = False
        for livro in self.livros:
            if not livro.disponivel:
                print(livro)
                encontrados = True
        if not encontrados:
            print("Nenhum livro emprestado no momento.")