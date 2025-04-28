story = """In a {adjective} kingdom far beyond {place}, a legendary {mystical_creature} \
was said to guard a hidden treasure. Many tried to find it, but none returned. \
That is, until one fateful day, when a brave traveler {verb} into the unknown.  

Along the way, they met {celebrity}, who whispered, '{silly_word}!'—a secret code that unlocked \
a portal to an ancient battlefield. There, warriors played {sport} instead of fighting. \
The traveler was mesmerized, but a sudden wave of {emotion} filled the air.  

Then, a chill ran down their {body_part} as a shadow loomed overhead. Slowly, they turned— \
only to find a giant {animal} staring right at them. 'Well,' they muttered, gripping their sword. \
'This just got interesting...'"""

print("Welcome to the Mad Libs game!")
print("Please provide the following words to complete the story.\n")
adjective = input("Adjective: ")
noun = input("Noun: ")
verb = input("Verb: ")
celebrity = input("Celebrity: ")
silly_word = input("Silly word: ")
sport = input("Sport: ")
emotion = input("Emotion: ")
body_part = input("Body part: ")
animal = input("Animal: ")
mystical_creature = input("Mystical creature: ")
place = input("Place: ")

story = story.format(
    adjective=adjective, noun=noun, verb=verb, celebrity=celebrity,
    silly_word=silly_word, sport=sport, emotion=emotion,
    body_part=body_part, animal=animal, mystical_creature=mystical_creature,
    place=place
)

print(story)