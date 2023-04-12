import random
from replit import clear
from art import logo 

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards_in_hand):
  if sum(cards_in_hand) == 21 and len(cards_in_hand) == 2:
    return 0 

  if 11 in cards_in_hand and sum(cards_in_hand) > 21:
    cards_in_hand.remove(11)
    cards_in_hand.append(1)
  
  return sum(cards_in_hand)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You lose. 😢"
  
  if user_score == computer_score: 
    return "It's a draw. 😶"
  elif computer_score == 0:
    return "The opponent got a Blackjack! You lose. 😱"
  elif user_score == 0:
    return "You got a Blackjack! You win! 😎"
  elif user_score > 21: 
    return "Oops! You went over. You lose. 😭"
  elif computer_score > 21:
    return "The opponent went over. You win! 🥳"
  else: 
    if user_score > computer_score:
      return "Yay! You win! 🤩"
    elif computer_score > user_score:
      return "Oh no! You lose. 😤"

def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  end_of_game = False
  while not end_of_game: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
      end_of_game = True
    else:
      get_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if get_card == 'y':
        user_cards.append(deal_card()) 
      else: 
        end_of_game = True
        
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower() == "y":
  clear()
  play_game() 
