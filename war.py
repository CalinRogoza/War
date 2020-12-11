import pygame, random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Jack", "Queen", "King"]
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
deck = []
deck_1 = []
deck_2 = []

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

player_score = 0
computer_score = 0

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("War")
icon = pygame.image.load('assets/cards.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score():
    score = font.render("Me: " + str(player_score), True, (0, 0, 0))
    screen.blit(score, (50, 550))
    score = font.render("Computer: " + str(computer_score), True, (0, 0, 0))
    screen.blit(score, (550, 550))


def draw_card_player():
    card_image = pygame.image.load('assets/2.png')
    card_image = pygame.transform.scale(card_image, (200, 300))
    screen.blit(card_image, (50, 150))


def draw_card_computer():
    card_image = pygame.image.load('assets/6.png')
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


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    screen.fill((255, 255, 205))
    show_score()
    draw_card_player()
    draw_card_computer()
    draw_button()
    draw_info(1)
    draw_info(2)
    draw_info(1)
    pygame.display.update()
