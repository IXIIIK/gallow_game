from visual_gallow import lives_visual_dict
from words import words
import random

WORD = random.choice(words('../russian-words/russian.utf-8'))



def correct_word():
    visible_word = WORD
    invisible_word = visible_word
    for i in invisible_word:
        invisible_word = invisible_word.replace(i, '_')
    return invisible_word, visible_word
    
def gallow():
    invisible_word, visible_word = correct_word()
    live = 7
    user_word = ''
    invisible_word = list(invisible_word)

    while live != 0:
        print('\n', ''.join(invisible_word))
        print(f'\nИспользованные буквы: {user_word}')
        usr_answer = input('Ваша буква: ')
        index = [i for i, c in enumerate(visible_word) if c == usr_answer.lower()]
        if index != []:
            for i in index:
                invisible_word[i] = usr_answer.lower()
        elif '_' not in invisible_word:
            return 'You won!'
        elif len(usr_answer) > 1:
            print('Нужно указывать одну букву!')
        else: 
            live -= 1
            user_word += usr_answer
            print(lives_visual_dict[live])
            print(f'Не правильно. Жизней осталось: {live}')
    print(f'\nВы проиграли. Правельное слово: {visible_word}\n')

    

if __name__ == '__main__':
    gallow()