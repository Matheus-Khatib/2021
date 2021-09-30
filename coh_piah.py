import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i=0
    temp=0
    while i<=5:
        temp=temp+abs((as_a[i]-as_b[i]))
        i=i+1
    return temp/6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal=tamanho_médio_palavra(texto)
    ttr=type_token(texto)
    hlr=hapax_legomana(texto)
    sal=tamanho_médio_sentença(texto)
    sac=complexidade_sentença(texto)
    pal=tamanho_médio_frase(texto)
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    b=0
    i=0
    a=0
    x=compara_assinatura(calcula_assinatura(textos[i]),ass_cp)
    while i<len(textos):
        if compara_assinatura(calcula_assinatura(textos[i]),ass_cp)<x:
            b=i
        i=i+1
    return(b+1)

def tamanho_médio_palavra(texto):
    sentenças = separa_sentencas(texto)
    a=0
    b=0
    c=0
    total_palavras=0
    total_letras=0
    while a<len(sentenças):
        b=0
        frases = separa_frases(sentenças[a])
        a=a+1
        while b<len(frases):
            c=0
            palavras = separa_palavras(frases[b])
            total_palavras=total_palavras+len(palavras)
            b=b+1
            while c<len(palavras):
                total_letras=total_letras+len(palavras[c])
                c=c+1
    return total_letras/total_palavras


def type_token(texto):
    sentenças = separa_sentencas(texto)
    a=0
    b=0
    total_palavras=0
    palavras_diferentes=0
    while a<len(sentenças):
        b=0
        frases = separa_frases(sentenças[a])
        a=a+1
        while b<len(frases):
            palavras = separa_palavras(frases[b])
            total_palavras=total_palavras+len(palavras)
            b=b+1
            palavras_diferentes=palavras_diferentes+n_palavras_diferentes(palavras)
    return palavras_diferentes/total_palavras

def hapax_legomana(texto):
    sentenças = separa_sentencas(texto)
    a=0
    b=0
    total_palavras=0
    palavras_únicas=0
    while a<len(sentenças):
        b=0
        frases = separa_frases(sentenças[a])
        a=a+1
        while b<len(frases):
            palavras = separa_palavras(frases[b])
            total_palavras=total_palavras+len(palavras)
            b=b+1
            palavras_únicas=palavras_únicas+n_palavras_unicas(palavras)
    return palavras_únicas/total_palavras

def tamanho_médio_sentença(texto):
    sentenças = separa_sentencas(texto)
    a=0
    b=0
    c=0
    total_caracteres=0
    total_sentenças=len(sentenças)
    while a<len(sentenças):
        b=0
        frases = separa_frases(sentenças[a])
        a=a+1
        while b<len(frases):
            c=0
            palavras = separa_palavras(frases[b])
            b=b+1
            while c<len(palavras):
                total_caracteres=total_caracteres+len(palavras[c])
                if c==len(palavras)-1:
                    c=c+1
                else:
                    total_caracteres=total_caracteres+1
                    c=c+1
    return total_caracteres/total_sentenças

def complexidade_sentença(texto):
    sentenças = separa_sentencas(texto)
    a=0
    b=0
    total_frases=0
    total_sentenças=len(sentenças)
    while a<len(sentenças):
        b=0
        frases = separa_frases(sentenças[a])
        a=a+1
        total_frases=len(frases)
        while b<len(frases):
            palavras = separa_palavras(frases[b])
            b=b+1
    return total_frases/total_sentenças

def tamanho_médio_frase(texto):
    sentenças = separa_sentencas(texto)
    a=0
    b=0
    c=0
    total_caracteres=0
    total_frases=0
    while a<len(sentenças):
        b=0
        frases = separa_frases(sentenças[a])
        a=a+1
        total_frases=len(frases)
        while b<len(frases):
            c=0
            palavras = separa_palavras(frases[b])
            b=b+1
            while c<len(palavras):
                total_caracteres=total_caracteres+len(palavras[c])
                if c==len(palavras)-1:
                    c=c+1
                else:
                    total_caracteres=total_caracteres+1
                    c=c+1
    return total_caracteres/total_frases



ass_cp=le_assinatura()
textos=le_textos()
avalia_textos(textos, ass_cp)




                     
                     
                     
                  
       
       
    
    
    


     
 

   
  
   
        
