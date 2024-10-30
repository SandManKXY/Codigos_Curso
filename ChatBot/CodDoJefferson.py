ChatBotStr = "Chatbot: "
ClienteStr = "Cliente: "
FimStr = "Fim"


def saidacoes(nome):
    import random
    frases = ["Ola "+nome+"" ,"Vai comprar um caminhão?", "compra logo um caminhão"]
    print(frases[random.randint(0,1)])

def filtrarTexto():
    texto = ClienteStr  + input(ClienteStr)
    palavrasCensuradas = ["Ajuda","Gerente","Fraco","Pobre","não vou comprar um caminhão"]
    for palavras in palavrasCensuradas:
        if palavras in texto:
            print("Inferlizmente não posso ajudar lhe com isso, tente novamente")
            return filtrarTexto()
    return texto

def buscaResporstas(nome, texto):
    with open("JeffersonCaminhoes.txt","a+") as dados:
        dados.seek(0)
        while True:
            viu = dados.readline()
            if viu != "": 
                if texto.replace(ClienteStr,"") == "Tchau":
                    return "Fim"
                elif viu.strip() == texto.strip():
                    proximalinha = dados.readline()
                    if ChatBotStr in proximalinha:
                        return proximalinha
            else:
                print("desculpe, não sei o que falar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                dados.write("\n" + texto )
                respostaCliente = input("O qwu wsperava de resposta ?")
                dados.write("\n" + ChatBotStr + respostaCliente)
                return "Compra concluida"
def exibeResposta(resposta):
    if resposta == FimStr:
        return FimStr
    return "Continua"

nomecliente = input("Digite seu nome: ")
saidacoes(nomecliente)

while True:
    texto = filtrarTexto()
    resposta = buscaResporstas(nomecliente, texto)
    if (exibeResposta(resposta) == FimStr):
        break
    else:
        print(resposta)