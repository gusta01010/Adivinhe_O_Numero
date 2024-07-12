import random
import os

class Game:

    leaderboard = []
    def __init__(self, nome):
        self.dificuldade = {'1': 10, '2': 8, '3': 6}
        self.tentativas = 0
        self.nome = nome
        self.randnum = random.randint(0,100)
    
    def EscolhaDificuldade(self):
        self.escolha = (input("Digite o número da dificuldade desejada: "))
        while self.escolha is not int and self.escolha not in self.dificuldade:
            self.escolha = (input("Digite o número da dificuldade desejada: "))
            
        self.escolha = self.dificuldade[self.escolha]
        
    def BatataQuente(self, valor):
        pulo = [20, 10, 5, 3, 1]
        if valor >= self.randnum+pulo[0]:
            print("Valor muito alto")
        elif valor >= self.randnum+pulo[1]:
            print("Valor um pouco alto")
        elif valor >= self.randnum+pulo[2]:
            print("Valor bem próximo alto")
        elif valor >= self.randnum+pulo[3]:
            print("Valor muito próximo alto!")
        elif valor >= self.randnum+pulo[4]:
            print("Valor muito muito próximo alto!")
            
        elif valor <= self.randnum-pulo[0]:
            print("Valor muito baixo")
        elif valor <= self.randnum-pulo[1]:
            print("Valor um pouco baixo")
        elif valor <= self.randnum-pulo[2]:
            print("Valor bem próximo baixo")
        elif valor <= self.randnum-pulo[3]:
            print("Valor muito próximo baixo!")
        elif valor <= self.randnum-pulo[4]:
            print("Valor muito muito baixo!")
        
        else:
            print(f"Você acertou o valor! O número da vez foi {self.randnum}")
            layout = ("Tentativas: " + str(self.tentativas) + " Nome: " + str(self.nome))
            leaderboard.append(layout)
            self.tentativas = 0
                
            
            
    
    def Start(self):
        print(f"\nBem vindo ao jogo de adivinhação de número, {self.nome}! Tente adivinhar o número no intervalo entre 0 - 100!\n\nAntes de iniciarmos, selecione o nível de dificuldade que deseja jogar.\n\n1: (Fácil - 10 tentativas), 2: (Médio - 8 tentativas), 3: (Difícil - 6 tentativas)")
        self.EscolhaDificuldade()
        os.system('cls')
        
        self.valor = None
        while True:
            while self.tentativas != self.escolha and self.valor != self.randnum:
                self.valor = int(input("Digite o valor: "))
                self.tentativas += 1
                self.BatataQuente(self.valor)
        
            self.valor = input(("Deseja continuar? (s/n)"))
            if self.valor == "s":
                self.tentativas = 0
                self.valor = None
                self.randnum = random.randint(0, 100)
            else:
                os.system("cls || clear")
                leaderboard.sort
                print("|   Tabela de classificação   |")
                for i in leaderboard:
                    print(i)
                input("Pressione enter para voltar ao menu")
                return False
            
leaderboard = []    
while True:
    os.system("cls || clear")
    nome = str(input("Digite o nome do jogador: "))
    Jogador = Game(nome)
    Jogador.Start()