import random

class Game:
    def __init__(self):
        self.words = [
            {'palabra': 'chamo', 'pista': 'joven, amigo'},
            {'palabra': 'pana', 'pista': 'amigo, compañero'}
        ]

    def play(self):
        score = 0
        rounds = 3
        for _ in range(rounds):
            word_data = random.choice(self.words)
            word = word_data['palabra']
            hint = word_data['pista']
            print(f'Pista: {hint}')
            attempt = input('Adivina la palabra: ').strip().lower()
            if attempt == word:
                print('correcto')
                score += 1
            else:
                print(f'Incorrecto! La palabra era: {word}')

        print(f'Juego terminado, puntuación final: {score}/{rounds}')