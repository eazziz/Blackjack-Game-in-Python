import random
import time

# Sleep function for visual purposes
def sleep_one_second():
    time.sleep(1)  # 1 second

# Defining deck
deck = [
    (11, 'Hearts', 'Ace (can be 1 or 11)'), (10, 'Hearts', 'King'), (10, 'Hearts', 'Queen'), (10, 'Hearts', 'Jack'),
    (10, 'Hearts', '10'), (9, 'Hearts', '9'), (8, 'Hearts', '8'), (7, 'Hearts', '7'), (6, 'Hearts', '6'),
    (5, 'Hearts', '5'), (4, 'Hearts', '4'), (3, 'Hearts', '3'), (2, 'Hearts', '2'),
    (11, 'Diamonds', 'Ace (can be 1 or 11)'), (10, 'Diamonds', 'King'), (10, 'Diamonds', 'Queen'), (10, 'Diamonds', 'Jack'),
    (10, 'Diamonds', '10'), (9, 'Diamonds', '9'), (8, 'Diamonds', '8'), (7, 'Diamonds', '7'), (6, 'Diamonds', '6'),
    (5, 'Diamonds', '5'), (4, 'Diamonds', '4'), (3, 'Diamonds', '3'), (2, 'Diamonds', '2'),
    (11, 'Clubs', 'Ace (can be 1 or 11)'), (10, 'Clubs', 'King'), (10, 'Clubs', 'Queen'), (10, 'Clubs', 'Jack'),
    (10, 'Clubs', '10'), (9, 'Clubs', '9'), (8, 'Clubs', '8'), (7, 'Clubs', '7'), (6, 'Clubs', '6'),
    (5, 'Clubs', '5'), (4, 'Clubs', '4'), (3, 'Clubs', '3'), (2, 'Clubs', '2'),
    (11, 'Spades', 'Ace (can be 1 or 11)'), (10, 'Spades', 'King'), (10, 'Spades', 'Queen'), (10, 'Spades', 'Jack'),
    (10, 'Spades', '10'), (9, 'Spades', '9'), (8, 'Spades', '8'), (7, 'Spades', '7'), (6, 'Spades', '6'),
    (5, 'Spades', '5'), (4, 'Spades', '4'), (3, 'Spades', '3'), (2, 'Spades', '2')
]

# Defining variables & creating empty list for player hands
player_score = 0
dealer_score = 0
player_money = 0
bet_amount = 0
player_hand = []
dealer_hand = []

# Drawing phrases for the player
drawing_phrases = [
    "You take a deep breath and draw another card...",
    "You feel the excitement and draw another card...",
    "With anticipation, you decide to draw another card..."
]

# Drawing phrases for the dealer
dealer_draw_phrases = [
    "The dealer smoothes out the cards and draws a new one...",
    "With a poker face, the dealer draws another card...",
    "The dealer nods slightly and draws another card..."
]

# Winning responses
winning_responses = [
    "Congratulations! You're on fire!",
    "You did it! Luck is on your side!",
    "What a win! You're a blackjack pro!"
]

# Losing responses
losing_responses = [
    "Oh no! Better luck next time!",
    "That didn't go as planned. Don't give up!",
    "It's all in the game! You'll get them next time."
]

# Nearby player interaction phrases
interaction_phrases = [
    "A nearby player leans over and says, 'You’ve got a solid hand! Are you going to hold?'",
    "A fellow gambler nudges you, whispering, 'With that score, it might be time to hold!'",
    "A seasoned player at the next table smiles and says, 'You’re close! Be careful with your next move.'",
    "A player beside you raises their eyebrows and asks, 'Thinking of drawing again?'",
    "A nearby player grins and says, 'You’re on the edge! What’s your next move?'"
]

# Atmosphere details
atmosphere_details = [
    "The sound of chips clinking fills the air as players cheer.",
    "The smell of expensive cigars wafts around the table.",
    "Laughter and chatter create a lively ambiance.",
    "A jazz band plays softly in the background, enhancing the mood.",
    "You hear the shuffle of cards and the occasional laughter from nearby tables.",
    "A couple of players discuss their strategies animatedly.",
    "The dealer's focused expression adds to the tension at the table."
]

# Initialize function
def initialize():
    print("\nWelcome to Blackjack!\n")
    sleep_one_second()

    print("\nYou step into a luxurious casino...\n")
    sleep_one_second()

    print("\nAs you approach the Blackjack tables, you see players eagerly placing their bets...\n")
    sleep_one_second()

    table_choice = input("\nWould you like to play at the High Rollers table (H) or the Normal table (N)? \n").lower()
    global player_money

    # If player enters H, they get 10000 to start. If N, then 2000
    if table_choice == 'h':
        player_money = 10000 
        print("\nWelcome to the High Rollers table! As you sit down, you feel the intensity in the air.\n")
        sleep_one_second()
        print("\nThe dealer shuffles a fresh deck of cards with speed & finesse.\n")
        sleep_one_second()
        print("\nYou notice a couple of high rollers, their stacks of chips towering like skyscrapers.\n")
        sleep_one_second()
        input("\nAs a high roller, you'll start with $10000. Press any button to start...\n")
    elif table_choice == 'n':
        player_money = 2000 
        print("\nWelcome to the Normal table! As you take a seat, you feel right at home.\n")
        sleep_one_second()
        print("\nThe dealer greets you with a friendly smile and begins to shuffle the cards with care.\n")
        sleep_one_second()
        print("\nThe soft chatter of players and the clinking of chips create a relaxed vibe.\n")
        sleep_one_second()
        input("\nAs a new player, you'll start with $2000. Press any button to start...\n")
    else:
        print("Invalid choice. Please enter 'H' or 'N'.")
        initialize()  # Restart if the input is invalid

def calculate_score(hand):
    score = 0  # Initialize the total score to 0
    aces = 0   # Initialize the count of Aces to 0

    # Check each card in the player's hand
    for card in hand:
        value = card[0]  # Get the value of the card (first element of the tuple)

        if value == 11:  # Check if the card is an Ace
            aces += 1  # If card is an ace, add 1 to the ace counter
        else:
            score += value  # Else, add the value of the card to the total score

    # The for loop below allows us to decide if aces will count as 11 or 1. It depends if 11 would bust the player score.
    for _ in range(aces):
        if score + 11 > 21:  # If adding 11 would bust the score, then count the ace as 1
            score += 1 
        else:
            score += 11  # Count the Ace as 11
            
    return score  # Return the calculated score

def place_bet():
    global bet_amount, player_money
    while True:
        bet_amount = int(input(f"You have ${player_money}. Enter your bet amount: "))
        if 0 < bet_amount <= player_money:
            player_money -= bet_amount
            break
        else:
            print("Invalid bet amount. Please try again.")

def draw_another_card():
    global player_score, dealer_score, player_money

    while True:
        if player_score >= 18:
            print(random.choice(interaction_phrases))  # Nearby player interaction
            sleep_one_second()
        
        user_input = input("\nPress any button to draw a card or 'q' to hold: ").lower()

        if user_input == 'q':
            print("You hold.\n")
    
            while dealer_score < 17:
                card = random.choice(deck)
                deck.remove(card)
                dealer_hand.append(card)  # Update dealer_hand for score calculation
                dealer_score = calculate_score(dealer_hand)  # Calculate score for dealer
                print(random.choice(dealer_draw_phrases))  # Random dealer draw phrase
                sleep_one_second()
                print(f"Dealer drew: {card[2]} of {card[1]}" if len(card) > 2 else f"Dealer drew: {card[0]} of {card[1]}")
                print(f"Dealer Score: {dealer_score}\n")
        
            if dealer_score > 21:
                print("Dealer busts! You win!")
                player_money += bet_amount * 2  # Double the bet for a win
                print(random.choice(winning_responses))  # Random winning response
                if random.random() < 0.2:
                    print(random.choice(atmosphere_details)) 
                return True  # Player wins
            elif dealer_score > player_score:
                print("Dealer wins!")
                print(random.choice(losing_responses))  # Random losing response
                return False  # Dealer wins
            elif dealer_score == player_score:
                print("It's a tie!")
                player_money += bet_amount  # Return the bet amount
                return False  # Tie, not a win
            else:
                print("You win!")
                player_money += bet_amount * 2  # Double the bet for a win
                print(random.choice(winning_responses))  # Random winning response
                if random.random() < 0.2:
                    print(random.choice(atmosphere_details)) 
                return True  # Player wins

        else:
            card = random.choice(deck)
            deck.remove(card)  # Remove the card from the deck
            player_hand.append(card)  # Add the drawn card to the player's hand
            player_score = calculate_score(player_hand)  # Calculate player's score
            print(random.choice(drawing_phrases))  # Random drawing phrase
            sleep_one_second()
            print(f"You drew: {card[2]} of {card[1]}" if len(card) > 2 else f"You drew: {card[0]} of {card[1]}")
            print(f"Your Score: {player_score}\n")

            if player_score > 21:
                print("Busted! Your score exceeds 21.")
                print(random.choice(losing_responses))  # Random losing response
                return False  # Player loses
            
           

def main():
    initialize()

    while True:
        global player_score, dealer_score, player_hand, dealer_hand
        player_score = 0
        dealer_score = 0
        player_hand = []
        dealer_hand = []

        place_bet()
        
        # Draw initial hands
        for _ in range(2):
            card = random.choice(deck)
            deck.remove(card)
            player_hand.append(card)
            print(f"You drew: {card[2]} of {card[1]}")
        player_score = calculate_score(player_hand)
        print(f"Your Score: {player_score}\n")

        card = random.choice(deck)
        deck.remove(card)
        dealer_hand.append(card)
        print(f"Dealer shows: {card[2]} of {card[1]}")
        dealer_score = calculate_score(dealer_hand)
        print(f"Dealer Score: {dealer_score} (hidden)\n")

        # Player's turn to draw cards
        draw_another_card()

        # Check if the player has run out of money
        if player_money <= 0:
            sleep_one_second()
            print("\n\nYou look at your empty chip tray and sigh, realizing you have run out of money.\n")
            sleep_one_second()
            print("\nThe dealer gives you a sympathetic smile and says, 'It happens to the best of us.'\n")
            sleep_one_second()
            print("\nNearby players chime in with playful banter, 'Guess the big gambler lost their luck tonight!'\n")
            sleep_one_second()
            print("\nAs you gather your things & prepare to leave, one player adds, 'Don't forget to bring your winning streak next time!'\n")
            sleep_one_second()
            print("\nThanks for playing Blackjack! Until next time!\n")
            break

        # Ask the player if they want to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'n':
            sleep_one_second()
            print("\nYou look at the dealer & tell them, 'I'm done for the night.'\n")
            sleep_one_second()
            print("\nNearby players overhear and tease, 'Done already? What happened to the big gambler?'\n")
            sleep_one_second()
            print("\nYou chuckle and gather your chips with a playful grin.\n")
            sleep_one_second()
            print("\nAs you walk to the front to cash out, one of the players shouts, 'Next time, bring your luck with you!'\n")
            sleep_one_second()
            print("\nThanks for playing Blackjack! Until next time!\n")
            break


main()
