from socket import *

#Função de validação da resposta
def verificar_resposta(questao, resposta):
    return questao['resposta_correta'] == resposta

def iniciar_servidor():
    serverPort = 3000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")

    while True:
        connectionSocket, addr = serverSocket.accept()
        
        questoes = [
            {
                'questao': "Qual é a capital do Brasil?",
                'opcoes': ['1. Brasília', '2. Rio de Janeiro', '3. São Paulo'],
                'resposta_correta': '1'
            },
            {
                'questao': "Qual é o maior país do mundo?",
                'opcoes': ['1. Rússia', '2. China', '3. Brasil'],
                'resposta_correta': '1'
            }
        ]
        
        acertos = 0
        resultados = []

        #Envio das questões
        for questao in questoes:
            connectionSocket.send(f"{questao['questao']}\n".encode())
            for opcao in questao['opcoes']:
                connectionSocket.send(f"{opcao}\n".encode())

            resposta_cliente = connectionSocket.recv(1024).decode().strip()

            #Validando respostas do cliente
            if verificar_resposta(questao, resposta_cliente):
                acertos += 1
                resultados.append(f"Questão: {questao['questao']} - Resposta correta")
            else:
                resultados.append(f"Questão: {questao['questao']} - Resposta incorreta")

        #Resultados sendo enviados
        connectionSocket.send(f"\nVocê acertou {acertos} de 2 questões.\n".encode())
        for resultado in resultados:
            connectionSocket.send(f"{resultado}\n".encode())

        connectionSocket.close()

if __name__ == "__main__":
    iniciar_servidor()
