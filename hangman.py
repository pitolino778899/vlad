import random 
from word import word_list
global pontuacao
pontuacao = 0
def get_word ():
    word = random.choice(word_list)
    print( len (word))
    return word.upper()

def display_hangman(tries):
    stages = ['''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
              ''',
              '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
              ''',
              '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
              ''',
              '''
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
              ''',
              '''
                --------
                |      |
                |      O
                |      |
                |      |
                |     
              ''',
              '''
                --------
                |      |
                |      O
                |      
                |      
                |     
              ''',
              '''
                --------
                |      |
                |     
                |    
                |     
                |     
              ''',
              ]
    return stages[tries]


def play(word):
    word_completion = '_'*len (word)
    
    
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 6 
    print('jogo da forca')
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries >0:
        guess = input('adivinhe a palavra : ').upper()
        if len (guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('você ja tentou adivinhar essa letra', guess)
            elif guess not in word :
                print(guess,'não é uma letra da palavra')
                tries -=1
                guessed_letters.append(guess)
            else:
                print('parabens ',guess,'é uma letra da palavra ')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index]=guess
                    word_completion = ''.join(word_as_list)
                    if '_' not in word_completion:
                        guessed  =True
        elif len (guess )== len(word)and guess.isalpha():
            if guess in guessed_word:
                print('você ja tentou adivinhar essa letra', guess)
            elif guess != word :
                print(guess,'não pertence a palavra')
                tries-=1
                guessed_word.append( guess)
            else :
                guessed = True
                word_completion = word
        else :
            print('adivinhação não valida')
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
       
    if guessed:
        print('parabens! você acertou a palavra') 
        pontuacao+=1
        
        
     
    else :
        print('você perdeu, a palavra era :'+word)
        
def main ():  
    play(get_word())
    print(pontuacao)
    while input('jogar denovo (s/n)').upper()== 'S':
        word = get_word ()
        play (word)
if __name__ == '__main__':
   
    main()

'''
!!!criar sistema de pontuação que a cada vitoria some um ponto e quando perder mostre os pontos!!!
'''



