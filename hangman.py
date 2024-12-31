import random
import pygame

def get_word():
    words = ['питон', 'программирование', 'виселица', 'алгоритм']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """    
               
    \ /   /\      
     |   /  \      
     O      
        """,
        """
       O     
      /|\    
      / \    
     /   \    
        """,
        """
         O     
        /|\    
      /\/ \    
     /  \  
        """,
        """
            O     
           /|\    
      /\   / \    
     /  \    
        """,
        """
             O     
            /|\    
      /\    / \    
     /  \  
        """,
        """
                 O     
                /|\    
      /\        / \    
     /  \           
        """,
        """   
                      O     
                     /|\    
      /\             / \    
     /  \           
        """
    ]
    return stages[tries]

def play_game():
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давайте играть в игру Прыжок со скалы!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Введите букву или слово: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже пробовали эту букву:", guess)
            elif guess not in word:
                print(guess, "нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отлично! Буква", guess, "есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже пробовали это слово:", guess)
            elif guess != word:
                print(guess, "неверное слово.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Неверный ввод. Попробуйте снова.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Поздравляем, вы угадали слово! Вы выжили!")
    else:
        pygame.mixer.init()
        # Загрузка и воспроизведение песни
        pygame.mixer.music.load('prygnu-so-skaly.mp3')
        pygame.mixer.music.play()
        print("Вы не угадали слово. Человек прыгнул со скалы. Слово было:", word)

if __name__ == "__main__":
    play_game()
