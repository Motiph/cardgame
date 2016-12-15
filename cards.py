import random

class Card(object):
    """
    Clase para cartas
    """
    def __init__(self, name, hp, attack_dmg):
        self.name = name
        self.hp = hp
        self.attack_dmg = attack_dmg

    def __str__(self):
        return "{}\n Vida: {} | Ataque: {}".format(self.name, self.hp, self.attack_dmg)

    def attack(self, my_card, target_card):
        """
        FALTA QUE RECIBA LA CARTA QUE ATACARA AL OBJETIVO
        """
        target_card.hp -= self.my_card.attack_dmg
        self.my_card.hp -= target_card.attack_dmg

        return"{} ataco a {}".format(target.name, self.name)




class Player(object):
    """
    Clase para los jugadores
    """
    def __init__(self, name, hp=None):
        self.name = name
        self.hp = hp
        self.card_list = []
        self.cards_on_table = []
        self.deleted_cards = []
        self.available_cards = []
        self.cards_in_deck = []

    def __str__(self):
        return self.name

    def add_card(self, card):
        """
        Agrega cartas a la coleccion del jugador "card_list[]".
        """
        self.card_list.append(card)

    def place_a_card(self):
        """
        Selecciona una carta para ponerla en la mesa.
        """
        while True:
            try:
                card_index = int(input("Seleccione una carta para atacar: \n"))
                try:
                    card_desc = self.card_list[card_index]
                    print("{} ha seleccionado: \n {}".format(self.name, card_desc))
                    self.cards_on_table.append(card_desc)
                    print("La carta {} fue agregada al tablero".format(self.cards_on_table[0].name))
                    break
                except IndexError:
                    print("La carta no existe...Seleccione una valida")
            except ValueError:
                print("Ingrese un valor valido")

        return self.card_list[card_index]

    def select_card(self):
        """
        Selecciona una carta para usarla o un objetivo al cual atacar.
        """
        while True:
            try:
                card_index = int(input("Seleccione una carta para atacar: \n"))
                try:
                    card_desc = self.card_list[card_index]
                    print("{} ha seleccionado: \n {}".format(self.name, card_desc))
                    break
                except IndexError:
                    print("La carta no existe...Seleccione una valida")
            except ValueError:
                print("Ingrese un valor valido")

        return self.card_list[card_index]

    def cards(self):
        """
        Imprime las cartas del jugador
        """
        return " \n".join([str(carta) for carta in self.card_list])

    def card_names(self):
        """
        Imprime solo los nombres de las cartas
        """
        return " \n".join([str(carta.name) for carta in self.card_list])



class Game(object):

    GAME_ON = True

    def __init__(self):
        self.players = []

    def __str__(self):
        return self.players

    # def get_players(self):
    #     for player in self.players:
    #         print(players[player])
    #     # return ", \n".join([player.nombre for player in self.players])

    def add_players(self, player):
        self.players.append(player)

    def turno_inicial(self):
        """
        Se decide de modo aleatorio quien inicia
        """
        turn = random.randint(0,1)
        player_start = self.players[turn]

        return player_start


minion1 = Card("Minion 1", 20, 5)
minion2 = Card("Minion 2", 45, 2)
minion3 = Card("Minion 3", 17, 3)
minion4 = Card("Minion 4", 30, 6)
minion5 = Card("Minion 5", 12, 2)
minion6 = Card("Minion 6", 18, 7)

player1 = Player("Player 1")
player2 = Player("Player 2")

juego = Game()
juego.add_players(player1)
juego.add_players(player2)



cartas = {
    1: minion1,
    2: minion2,
    3: minion3,
    4: minion4,
    5: minion5,
    6: minion6,
}

#se gregan 2 cartas al jugador 1
player1.add_card(cartas[1])
player1.add_card(cartas[2])

print(player1.card_names.__doc__)

#se agregan 2 cartas al jugador 2
player2.add_card(cartas[3])
player2.add_card(cartas[6])


play = True
start = True

while play:
    inicia_jugada = juego.turno_inicial()

    print("{} juega primero".format(inicia_jugada))

    if inicia_jugada == juego.players[0]:
        print(player1.cards())
        print("Player 1 - Selecciona carta")
        player1.place_a_card()
    else:
        print(player2.cards())
        print("Player 2 - Selecciona carta")
        player2.place_a_card()





    #print("Cartas de {}".format(player1))
    #player1.cards()

    print(" ")
    #print("Cartas de {}".format(player2))
    #player2.cards()


    while True:
        t = 1
        if t == 1:
            #print(player1)
            #print(player1.cards())

            use = player1.select_card()


            objetivo = int(input("22Selecciona un objetivo a atacar: \n"))
            try:
                atacar_a = player2.card_list[objetivo]
                print("Objetivo: \n", atacar_a)
            except IndexError:
                print("el objetivo no existe...")

            print("{} tiene {} puntos de vida".format(jugar_con.name, jugar_con.hp))
            print("{} tiene {} puntos de vida".format(atacar_a.name, atacar_a.hp))

            jugar_con.attack(atacar_a)

            print("{} tiene {} puntos de vida".format(jugar_con.name, jugar_con.hp))
            print("{} tiene {} puntos de vida".format(atacar_a.name, atacar_a.hp))




    play = False
