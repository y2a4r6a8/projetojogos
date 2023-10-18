class Jogador:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.forca = 10
        self.inteligencia = 10
        self.destreza = 10
        self.ataque = 0
        self.defesa = 0

    def escolher_classe(self, classe_escolhida):
        self.classe = classe_escolhida

    def exibir_atributos(self):
        print(f"Atributos de {self.nome}: Vida - {self.vida}, Força - {self.forca}, Inteligência - {self.inteligencia}, Destreza - {self.destreza}")

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def exibir_status(self):
        print(f"Status de {self.nome}: Vida - {self.vida}, Ataque - {self.ataque}, Defesa - {self.defesa}")

class Jogo:
    def __init__(self, fases):
        self.fases = fases

    def desafio(self):
        print("Desafio! Enfrente um inimigo.")
        inimigo = Inimigo("Goblin", 20, 5, 2)
        inimigo.exibir_status()

    def batalha(self):
        jogador = Jogador("Herói", "Guerreiro")
        inimigo = Inimigo("Dragão", 50, 10, 5)
        print("Batalha!")
        jogador.exibir_atributos()
        inimigo.exibir_status()

# Exemplo de execução
if __name__ == "__main__":
    jogo = Jogo(10)
    jogo.desafio()
    jogo.batalha()
