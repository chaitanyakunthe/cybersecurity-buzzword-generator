import random
import json
from buzzword_lists import adjectives, nouns, endings

def generate_buzzword():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    ending = random.choice(endings)
    return f"{adj} {noun} {ending}"

# Generate buzzword and save to JSON
buzzword = generate_buzzword()
with open('buzzword.json', 'w') as f:
    json.dump({"buzzword": buzzword}, f)
