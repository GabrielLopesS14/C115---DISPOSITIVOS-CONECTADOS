from socket import *

def iniciar_cliente():
    # Definindo o nome do servidor e a porta
    serverName = 'localhost'
    serverPort = 3000

    # Criando o socket do cliente
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Conectando ao servidor
    clientSocket.connect((serverName, serverPort))

    while True:
        # Receber a questão do servidor
        questao = clientSocket.recv(1024).decode()
        if not questao:
            break
        print(questao)

        # Receber as opções da questão
        while True:
            opcao = clientSocket.recv(1024).decode()
            if not opcao:
                break
            print(opcao)
        
        # Aguardar a entrada do usuário
        resposta = input("Escolha a opção correta (1, 2, 3): ")  # Espera o usuário digitar a resposta
        clientSocket.send(resposta.encode())  # Envia a resposta para o servidor

    # Receber os resultados do servidor
    resultado_final = clientSocket.recv(1024).decode()
    print(resultado_final)

    # Receber o feedback das questões
    while True:
        resultado_questao = clientSocket.recv(1024).decode()
        if not resultado_questao:
            break
        print(resultado_questao)

    # Fecha a conexão
    clientSocket.close()

if __name__ == "__main__":
    iniciar_cliente()
