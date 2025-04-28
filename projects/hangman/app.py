import random as rd

words = [
    "balloon", "lollipop", "parallel", "alligator", "billiard", "illusion", "cellular", 
    "thriller", "brilliant", "scallop", "yellow", "umbrella", "chill", "till", "hill", 
    "install", "lullaby", "council", "skillful", "nullify", "pollute", "illegal", "alloy", 
    "trolley", "lovely", "bulldog", "collide", "mellow", "willow", "belligerent", "allocate", 
    "allegory", "millennium", "parallelism", "intellectual", "hallucination", "illumination",
    "libellous", "lull", "belly", "ballistic", "collarbone", "legally", "flawless", "label", 
    "fallacy", "lambent", "languish", "lapel", "lateral", "liberally", "likelihood", "locally", 
    "loll", "longhaul", "loneliness", "lovelorn", "lowball", "ludicrously", "lull", "lumbermill", 
    "macula", "mallard", "marvel", "megalomania", "melancholy", "metallurgy", "millionaire", 
    "miraculous", "monocle", "multipliable", "nullification", "palladium", "papillary", "parallelize", 
    "pavilion", "pedal", "perilous", "pillager", "politically", "pollination", "portfolio", "preamble", 
    "preliminary", "propeller", "rebellion", "regally", "relinquish", "scallion", "scandalously", 
    "soliloquy", "spellbinding", "stellar", "subliminal", "symbolically", "talismanic", "telepathically",
    "telltale", "thermally", "thrill", "trill", "turbulence", "umbellate", "unbelievably", "unparallel", 
    "valley", "village", "villainous", "volleyball", "wallet", "willful", "willowish", "zealously"
]

compChoice = rd.choice(words).upper()

print('Welcome to the Hangman!')
word =  '_ ' * len(compChoice)
print('Guess the word!')
print('You have 6 attempts to guess the word.')
print('The word has', len(compChoice), 'letters.')
attempts = 6
guessed_letters = []
correct_letters = []
while attempts > 0:
    print(compChoice)
    print('The word is:', word)
    print('Guessed letters:', ' '.join(guessed_letters))
    guess = input('Enter a letter:').upper()
    print('You guessed:', guess)
    if guess == compChoice:
        print('Congratulations! You guessed the word:', compChoice)
        break  
    elif not guess.isalpha():
        print('Invalid input. Please enter a single letter.')
        continue
    elif guess in guessed_letters:
        print('You have already guessed that letter.')
        continue
    elif guess not in compChoice:
        print('Incorrect guess.')
        attempts -= 1
        guessed_letters.append(guess)
        print('You have run out of attempts. The word was:', compChoice) if attempts == 0 else print('Attempts left:', attempts)
        continue
    elif guess in compChoice:
        print('Correct guess!')
        correct_letters.append(guess)
        guessed_letters.append(guess)
        print('Guessed letters:', ' '.join(guessed_letters))
        print('Attempts left:', attempts)
        word = ''.join([letter if letter in correct_letters else '_ ' for letter in compChoice])
    if '_' not in word:
            print('Congratulations! You guessed the word:', compChoice)
            break

        