from socket import *
import random
 
def main():
    N = 1000003 #primo
    G = 154858 #nao necessariamente primo, mas menor que N
 
    x = random.randint(100000, 999999) #x aleatorio
    primo = verificaPrimo(N)
    if primo: 
        serverName = "10.1.70.2"
        serverPort = 1300
    
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
    
        R1 = (G**x) % N
    
        print ("R1: ", R1)
    
        clientSocket.send(bytes(str(R1), "utf-8"))
    
        R2 = int(clientSocket.recv(65000).decode("utf-8"))
        print("R2 recebido:", R2)

        K = (R2**x) % N  
    
        print ("K usado no cesar: ", K)
    
        sentence = input("Digite a sentença: ")
    
        sentenceCriptograda = caesar(sentence, K)
    
        clientSocket.send(bytes(sentenceCriptograda, "utf-8"))
    
        modifiedSentence = clientSocket.recv(65000)
    
        modifiedSentence = str(modifiedSentence,"utf-8")
    
        print ("Sentença criptograda recebida do servidor: ", modifiedSentence)
    
        sentenceDescriptograda = caesar(modifiedSentence, -K)
    
        print ("Sentença descriptograda recebida do servidor: ", sentenceDescriptograda)
    
        clientSocket.close()
    else:
         print ("Numero não é primo ", N)
 
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

 #primo fast
def verificaPrimo(numero):
    i = 2
    while i < numero:
        R = numero % i
        if R == 0:
            return False
        i += 1
    else:
        return True
    
main()

