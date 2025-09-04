from socket import *
import random
 
# ===== Função Cifra de César =====
def caesar(texto, k):
    resultado = ""
    for c in texto:
        codigo = ord(c)
        if 32 <= codigo <= 126: 
            novo_codigo = 32 + ((codigo - 32 + k) % 95)
            resultado += chr(novo_codigo)
        else:
            resultado += c  
    return resultado
# ===== primo fast =====
def verificaPrimo(numero):
    i = 2
    while i < numero:
        R = numero % i
        if R == 0:
            return False
        i += 1
    else:
        return True
# ===== Configuração Diffie-Hellman =====
N = 9  # primo
G = 154858  # base
y = random.randint(100000, 999999)  # expoente do servidor
primo = verificaPrimo(N)
if primo: 
    serverPort = 1300
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("0.0.0.0", serverPort))  # escuta em todas interfaces
    serverSocket.listen(5)
    print("Servidor TCP aguardando conexão...\n")
    
    connectionSocket, addr = serverSocket.accept()
    print("Conectado com:", addr)
    
    # ===== 1. Recebe R1 do cliente =====
    R1 = int(connectionSocket.recv(65000).decode("utf-8"))
    print("R1 recebido:", R1)
    
    # ===== 2. Calcula R2 e envia =====
    R2 = pow(G, y, N) 
    connectionSocket.send(str(R2).encode("utf-8"))
    print("R2 enviado:", R2)
    
    # ===== 3. Calcula chave compartilhada =====
    K = pow(R1, y, N)
    print("Chave K:", K)
    
    # ===== 4. Recebe mensagem cifrada =====
    sentence = connectionSocket.recv(65000).decode("utf-8")
    print("Recebido do cliente (cifrado):", sentence)
    
    # ===== 5. Decifra =====
    decifrado = caesar(sentence, -K)
    print("Decifrado no servidor:", decifrado)
    
    # ===== 6. Converte para UPPER e reenvia cifrado =====
    upper_text = decifrado.upper()
    cifrado = caesar(upper_text, K)
    connectionSocket.send(cifrado.encode("utf-8"))
    print("Enviado ao cliente (cifrado):", cifrado)
    
    connectionSocket.close()
    serverSocket.close()
else:
     print ("Numero não é primo ", N)