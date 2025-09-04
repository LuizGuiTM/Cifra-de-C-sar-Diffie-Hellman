# Comunicação Cliente-Servidor com Diffie-Hellman + Cifra de César

Este projeto implementa uma comunicação **Cliente-Servidor em Python** utilizando **sockets TCP**, com criptografia baseada na **Cifra de César**.  
A chave de deslocamento usada na cifra é negociada dinamicamente entre cliente e servidor através do algoritmo de **Diffie-Hellman**.

---

## 📌 Estrutura do Projeto

- `simple_tcpServer.py` → Servidor (Bob)
- `simple_tcpClient.py` → Cliente (Alice)

---

## ⚙️ Funcionamento

### 🔹 Etapa 1 — Conexão TCP
- O servidor abre a porta `1300` e aguarda conexões.
- O cliente conecta no IP/porta do servidor.

### 🔹 Etapa 2 — Troca de Chaves (Diffie-Hellman)
1. Ambos concordam com dois números:
   - `N`: número primo grande
   - `G`: base
2. O cliente gera um número secreto `x` e envia `R1 = (G^x) mod N` para o servidor.
3. O servidor gera um número secreto `y` e responde com `R2 = (G^y) mod N`.
4. Ambos calculam a mesma chave `K`:
   - Cliente: `K = (R2^x) mod N`
   - Servidor: `K = (R1^y) mod N`

### 🔹 Etapa 3 — Criptografia com Cifra de César
- O cliente envia uma mensagem cifrada com `K`.
- O servidor decifra, transforma em **maiúsculas**, cifra novamente e devolve ao cliente.
- O cliente decifra a resposta final.

---

## 🖥️ Execução

### 1. Inicie o Servidor
Na máquina **Bob**:

```bash
python simple_tcpServer.py
```

Saída esperada:
```
Servidor TCP aguardando conexão...

Conectado com: ('10.1.70.2', 54321)
R1 recebido: 372271
R2 enviado: 491956
Chave K: 123456
Recebido do cliente (cifrado): ...
Decifrado no servidor: ...
Mensagem em UPPER: ...
Enviado ao cliente (cifrado): ...
```

---

### 2. Inicie o Cliente
Na máquina **Alice**:

```bash
python simple_tcpClient.py
```

Digite uma frase quando solicitado, por exemplo:

```
Digite a sentença: teste de mensagem
```

Saída esperada:
```
R1 enviado: 372271
R2 recebido: 491956
Chave K: 123456
Enviado ao servidor (cifrado): ...
Recebido do servidor (cifrado): ...
Resposta decifrada: TESTE DE MENSAGEM
```

---

## 🔎 Análise com Wireshark

Para verificar a comunicação:

1. Abra o **Wireshark** na interface de rede usada.
2. Use o filtro:
   ```
   tcp.port == 1300
   ```
3. Observe:
   - `R1` enviado do cliente para o servidor.
   - `R2` enviado do servidor para o cliente.
   - Mensagens trocadas cifradas (não legíveis em claro).

---

## 📚 Tecnologias Utilizadas
- Python `3.x`
- Biblioteca padrão `socket`
- Algoritmo de **Diffie-Hellman** para troca de chaves
- **Cifra de César** (implementação própria, sem bibliotecas externas)
- **Wireshark** para análise do tráfego

---

## 👨‍💻 Autoria
Código desenvolvido para fins acadêmicos, visando demonstrar:
- Criptografia simétrica simples
- Negociação de chaves
- Comunicação segura Cliente-Servidor em Python
