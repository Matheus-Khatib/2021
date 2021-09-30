def partida():
   n = int(input("Quantas peças? "))
   m = int(input("Limite de peças por jogada? "))
   if n%(m+1) == 0:
      print()
      print("Você começa!")
      print()
      acabou=False
      while n>=1 and acabou==False:
         x =(usuario_escolhe_jogada(n,m))
         if x == 1:
            print("Você tirou uma peça")
         else:
            print("Você tirou",x,"peças")
         n = n - x
         print()
         if n==1:
            print("Agora resta uma peça no tabuleiro")
         elif n==0:
            acabou = True
            return("Fim do jogo! vocè ganhou!")
         else:
            print("Agora restam",n,"peças no tabuleiro.")
         print()
         a=(computador_escolhe_jogada(n,m))
         if a == 1:
            print("O computador tirou uma peça.")
         else:
            print("o computador tirou",a,"peças.")
         n = n-a
         if n==1:
            print("Agora resta uma peça no tabuleiro")
            print()
         elif n==0:
            acabou = True
            return("Fim do jogo! O computador ganhou!")
         else:
            print("Agora restam",n,"peças no tabuleiro.")
            print()
   else:
      print()
      print("Computador começa!")
      print()
      acabou = False
      while n>=1 and acabou==False: 
         a=(computador_escolhe_jogada(n,m))
         if a == 1:
            print("O computador tirou uma peça.")
         else:
            print("o computador tirou",a,"peças.")
         n = n-a
         if n==1:
            print("Agora resta uma peça no tabuleiro")
            print()
         elif n==0:
            acabou=True
            return("Fim do jogo! O computador ganhou!")
         else:
            print("Agora restam",n,"peças no tabuleiro.")
            print()
         x=(usuario_escolhe_jogada(n,m))
         if x == 1:
            print("Você tirou uma peça")
         else:
            print("Você tirou",x,"peças")
         n = n - x
         if n==1:
            print("Agora resta uma peça no tabuleiro")
            print()
         elif n==0:
            acabou=True
            print()
            return("Fim do jogo! Você ganhou!")
            print()
         else:
            print("Agora restam",n,"peças no tabuleiro.")
            print()

def campeonato():
   vc = 0
   vu = 0
   print("Voce escolheu um campeonato!")
   print()
   print("**** Rodada 1 ****") 
   print()
   if partida() == ("Fim do jogo! Você ganhou!"):
      vu = vu + 1
      print("Fim do jogo! Você ganhou!")
   else:
      vc = vc + 1
      print("Fim do jogo! O computador ganhou!")  
   print()
   print("**** Rodada 2 ****")
   print()
   if partida() == ("Fim do jogo! Você ganhou!"):
      vu = vu + 1
      print("Fim do jogo! Você ganhou!")
   else:
      vc = vc + 1
   print("Fim do jogo! O computador ganhou!")         
   print()
   print("**** Rodada 3 ****")
   print()
   if partida() == ("Fim do jogo! Você ganhou!"):
      vu = vu + 1
      print("Fim do jogo! Você ganhou!")
   else:
      vc = vc + 1
      print("Fim do jogo! O computador ganhou!")
   print()
   print("**** Final do campeonato! ****")
   print()
   print("Placar: Você",vu,"X",vc,"Computador")

def computador_escolhe_jogada(n,m):
      acabou = False
      if n<m:
         a=n
         return a
      else:
         a = m
         while a>=0 and acabou==False:
            if (n-a)%(m+1)==0 and a!=0:
               acabou=True
               return a
            a = a-1   
            if a==0:
               a=m
               return a

def usuario_escolhe_jogada(n,m):
   x = int(input("Quantas peças você vai tirar? "))
   while x<0 or x>m or x>n:
      print("Oops! Jogada inválida! Tente de novo.")
      print()
      x = int(input("Quantas peças você vai tirar? "))
   return x

print("Bem-vindo ao jogo do NIM! Escolha: ")
print()
print("1 - para jogar uma partida isolada ")
j = int(input("2 - para jogar um campeonato "))   
if j==2:
   print()
   print(campeonato())
if j==1:
   print()
   print(partida())
