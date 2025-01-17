import pygame
import random
import time

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Jack", "Queen", "King"]
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
deck = []
deck_1 = []
deck_2 = []
player_score = 26
computer_score = 26


def initialize_decks():
    card_value = 2
    for rank in ranks:
        for suit in suits:
            deck.append([rank, suit, card_value])
        card_value = card_value + 1

    random.shuffle(deck)  # Amestecam cartile

    for card in range(0, len(deck) // 2):  # Impartim cartile
        deck_1.append(deck[card])
    for card in range(len(deck) // 2, len(deck)):
        deck_2.append(deck[card])


def show_score():
    screen.fill((255, 255, 205), (0, 550, 800, 50))  # Pentru a sterge informatiile de dinainte (stergem toata linia de scor)
    score = font.render("Me: " + str(player_score), True, (0, 0, 0))
    screen.blit(score, (50, 550))
    score = font.render("Computer: " + str(computer_score), True, (0, 0, 0))
    screen.blit(score, (550, 550))
    pygame.display.update()


def draw_card_player(value):
    card_image = pygame.image.load('assets/' + str(value) + '.png')
    card_image = pygame.transform.scale(card_image, (200, 300))
    screen.blit(card_image, (50, 150))


def draw_card_computer(value):
    card_image = pygame.image.load('assets/' + str(value) + '.png')
    card_image = pygame.transform.scale(card_image, (200, 300))
    screen.blit(card_image, (550, 150))


def draw_button():
    pygame.draw.rect(screen, (0, 0, 0), (310, 10, 200, 50), 2)
    text = font.render("Next round!", True, (0, 0, 0))
    screen.blit(text, (320, 20))


def draw_info(player):
    screen.fill((255, 255, 205), (260, 80, 300, 50))  # Pentru a sterge informatiile de dinainte
    pygame.draw.rect(screen, (0, 0, 0), (260, 80, 300, 50), 1)
    font2 = pygame.font.Font('freesansbold.ttf', 20)
    if player == 1:
        text = font2.render("You take the cards!", True, (0, 0, 0))
        screen.blit(text, (270, 95))
    elif player == 2:
        text = font2.render("Computer takes the cards!", True, (0, 0, 0))
        screen.blit(text, (270, 95))
    elif player == 0:
        text = font2.render("Equal! Let's start the war!", True, (0, 0, 0))
        screen.blit(text, (270, 95))
        pygame.display.update()
        print("equal")


def draw_winner(number):
    global running
    if number == 2:
        screen.fill((255, 255, 205))
        text = font.render("COMPUTER WINS!", True, (255, 0, 0))  # Afisam castigatorul
        screen.blit(text, (250, 270))
        pygame.display.update()
        time.sleep(2)
        running = False
    elif number == 1:
        screen.fill((255, 255, 205))
        text = font.render("YOU WIN!", True, (0, 154, 0))
        screen.blit(text, (300, 270))
        pygame.display.update()
        time.sleep(2)
        running = False


def is_final():
    if len(deck_1) == 0:
        draw_winner(2)
        return 2
    elif len(deck_2) == 0:
        draw_winner(1)
        return 1
    return 0


def is_final_equal(value):
    global deck_1, deck_2, player_score, computer_score
    if len(deck_1) - value < 0:
        player_score = 0
        computer_score = 52
        show_score()
        time.sleep(3)       # pentru a afisa scorul, jucatorul putandu-si da seama cine a castigat vazand scorul actualizat
        draw_winner(2)      # castiga calculatorul
        return 2
    if len(deck_2) - value < 0:
        player_score = 52
        computer_score = 0
        show_score()
        time.sleep(3)
        draw_winner(1)      # castiga jucatorul
        return 1
    return 0


def next_turn():
    global deck_1, deck_2, player_score, computer_score
    if is_final() == 0:  # Daca jucatorii mai au carti, extragem una de la fiecare
        player_card = deck_1.pop(0)
        computer_card = deck_2.pop(0)
        print(player_card[2])
        print(computer_card[2])
        draw_card_player(player_card[2])
        draw_card_computer(computer_card[2])
        if player_card[2] > computer_card[2]:
            draw_info(1)
            computer_score = computer_score - 1
            player_score = player_score + 1
            deck_1.append(computer_card)  # se iau ambele carti de pe masa
            deck_1.append(player_card)
        elif player_card[2] < computer_card[2]:
            draw_info(2)
            computer_score = computer_score + 1
            player_score = player_score - 1
            deck_2.append(player_card)
            deck_2.append(computer_card)
        else:                                               # Cand sunt egale
            if is_final_equal(player_card[2]) == 0:
                draw_info(0)
                table_deck = [player_card, computer_card]
                print("EGALE")
                time.sleep(5)
                are_equal(player_card, computer_card, table_deck)
                table_deck.clear()  # stergem cartile de joc de pe masa
        show_score()


def are_equal(player_card, computer_card, table_deck):
    global deck_1, deck_2, player_score, computer_score
    for i in range(player_card[2]):
        player_card = deck_1.pop(0)
        computer_card = deck_2.pop(0)
        table_deck.append(player_card)
        table_deck.append(computer_card)

    draw_card_player(player_card[2])
    draw_card_computer(computer_card[2])

    if player_card[2] > computer_card[2]:
        draw_info(1)
        player_score = player_score + len(table_deck)//2
        computer_score = computer_score - len(table_deck)//2
        deck_1.extend(table_deck)
    elif player_card[2] < computer_card[2]:
        draw_info(2)
        computer_score = computer_score + len(table_deck)//2
        player_score = player_score - len(table_deck)//2
        deck_2.extend(table_deck)
    else:                                   # Iar sunt egale, apelam recursiv
        if is_final_equal(player_card[2]) == 0:
            draw_info(0)
            print("Egale iar!")
            time.sleep(5)
            are_equal(player_card, computer_card, table_deck)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("War")
icon = pygame.image.load('assets/cards.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)

screen.fill((255, 255, 205))  # Initializam fereastra de joc
pygame.draw.rect(screen, (0, 0, 0), (260, 80, 300, 50), 1)
font2 = pygame.font.Font('freesansbold.ttf', 20)
text = font2.render("Press 'Next round!' to start!", True, (0, 0, 0))
screen.blit(text, (270, 95))
draw_button()
show_score()
initialize_decks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 310 <= pygame.mouse.get_pos()[0] <= 510:
                if 10 <= pygame.mouse.get_pos()[1] <= 60:
                    print("CLiCKED")
                    next_turn()
    pygame.display.update()
