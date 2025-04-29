import random  # Importa o módulo random para gerar caracteres aleatórios

def gerar_caracteres():
    """
    Retorna uma string com todos os caracteres permitidos para as senhas.
    """
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@!#$%^&*(),.?'

def gerar_senha(tamanho, caracteres):
    """
    Gera uma senha aleatória com o tamanho especificado, escolhendo caracteres da lista fornecida.
    """
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def main():
    """
    Função principal que executa a lógica de entrada de dados, geração e exibição das senhas.
    """
    print('Gerador de senhas')

    try:
        # Solicita ao usuário a quantidade de senhas a serem geradas
        qtd_senhas = int(input('Quantidade de senhas: '))

        # Solicita ao usuário o tamanho de cada senha
        qtd_caracteres = int(input('Quantidade de caracteres por senha: '))
    except ValueError:
        # Caso o usuário digite algo que não seja número, exibe um aviso e encerra
        print("Erro: por favor, insira apenas números.")
        return

    # Obtém a lista de caracteres permitidos
    caracteres = gerar_caracteres()

    # Gera e exibe cada senha
    for _ in range(qtd_senhas):
        senha = gerar_senha(qtd_caracteres, caracteres)
        print(senha)

# Garante que o código só será executado se o script for chamado diretamente
if __name__ == "__main__":
    main()


