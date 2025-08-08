import random
import json
import os

class Game:
    def __init__(self):
        words_path = os.path.join(os.path.dirname(__file__), '../data/words.json')
        with open(words_path, 'r', encoding='utf-8') as f:
            self.words = json.load(f)

    def play(self):
        score = 0
        rounds = len(self.words)
        for _ in range(rounds):
            word_data = random.choice(self.words)
            word = word_data['word']
            hint = word_data['hint']
            print(f'Pista: {hint}')
            attempt = input('Adivina la palabra: ').strip().lower()
            if attempt == word:
                print('correcto')
                score += 1
            else:
                print(f'Incorrecto! La palabra era: {word}')

        print(f'Juego terminado, puntuación final: {score}/{rounds}')