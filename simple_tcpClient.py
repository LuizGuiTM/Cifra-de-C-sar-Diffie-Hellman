from socket import *
import random
 
def main():
    N = 999983 #primo
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
    
        sentenceCriptograda = cesar(sentence, K)
    
        clientSocket.send(bytes(sentenceCriptograda, "utf-8"))
    
        modifiedSentence = clientSocket.recv(65000)
    
        modifiedSentence = str(modifiedSentence,"utf-8")
    
        print ("Sentença criptograda recebida do servidor: ", modifiedSentence)
    
        sentenceDescriptograda = cesar(modifiedSentence, -K)
    
        print ("Sentença descriptograda recebida do servidor: ", sentenceDescriptograda)
    
        clientSocket.close()
    else:
         print ("Numero não é primo ", N)
 
def cesar(texto, k):
    out = []
    for ch in texto:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            out.append(ch)
    return ''.join(out)


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

