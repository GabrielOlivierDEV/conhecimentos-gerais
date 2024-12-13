# Don't worry stranger looking at my code, I know it's pretty disgusting, but I'm still learning python, and when I get better, I'll return
# And I'll make this code less bad
import pygame
import os
pygame.mixer.init()
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'music', 'spookyfunnight.mp3')
pygame.mixer.music.load(file_path)
pygame.mixer.music.play(loops=-1)

acertou = 'Resposta correta!'
errou = 'ERROU!!!!!!!!'
p1 = 'Sua primeira pergunta é: Qual é o maior planeta do Sistema Solar?\na) Saturno\nb) Júpiter\nc) Marte\nd) Terra\ne) Urano '
p2 = 'Em que ano aconteceu a Proclamação da República no Brasil?\na) 1879\nb) 1900\nc) 1889\nd) 1857\ne) 1895 '
p3 = 'Qual é o elemento químico representado pelo símbolo "O"?\na) Oxigênio\nb) Ouro\nc) Osmium\nd) Hidrogênio\ne) Ozônio '
p4 = 'Quem pintou a obra "A Última Ceia"?\na) Michelangelo\nb) Rafael\nc) Leonardo da Vinci\nd) Van Gogh\ne) Botticelli '
p5 = 'Qual país é conhecido como a "terra do sol nascente"?\na) China\nb) Coreia do Sul\nc) Japão\nd) Tailândia\ne) Indonésia '
fim = 'VOCÊ GANHOU!!! Sua alma será poupada... por hoje :3\nRecomeçar? (s/n)'

bemvindo = input(('Bem vindo! você gostaria de jogar um jogo? (s/n) :) ')).strip().lower()
if bemvindo == 's':
        print('Vamos nessa!!!',end=' ')
else:
        print('Você não tem escolha :3',end=' ')

while True:        
    print(p1)
    r1 = input()

    if r1 == 'a':
        print(acertou)
        print('Você é bom! Vamos para a próxima pergunta!')
        print(p2)

        r2 = input()
        if r2 == 'c':
            print(acertou)
            print(p3)
            r3 = input()
            if r3 == 'a':
                 print(acertou)
                 print(p4)
                 r4 = input()
                 if r4 == 'c':
                      print(acertou)
                      print(p5)
                      r5 = input()
                      if r5 == 'c':
                           print(acertou)
                           print(fim)
                           end = input()
                           if end == 'n':
                                break

    else:
        print(errou)