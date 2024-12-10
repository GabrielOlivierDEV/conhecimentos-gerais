# Don't worry stranger looking my code, I know it's pretty disgusting, but I'm still learning python, and when I get better, I'll return
# And I'll make this code less bad
import pygame
import os
while True:
    pygame.mixer.init()
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'music', 'spookyfunnight.mp3')
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=-1)
    bemvindo = input(('Bem vindo! você gostaria de jogar um jogo? :) '))
    if bemvindo in ["Sim", "sim", "sim!", "Sim!"]:
        print('Vamos nessa!!!',end=' ')
    else:
        print('Você não tem escolha :3',end=' ')
    print('Vamos começar o jogo!')
    print('Responda escrevendo "a", "b", "c", etc;')
    p1 = input(('Sua primeira pergunta é: Qual é o maior planeta do Sistema Solar?\na) Saturno\nb) Júpiter\nc) Marte\nd) Terra\ne) Urano '))
    if p1 == "b":
        print('Resposta correta!')
        print ('Você é bom! Vamos para a próxima pergunta!')
        p2 = input('Em que ano aconteceu a Proclamação da República no Brasil?\na) 1879\nb) 1900\nc) 1889\nd) 1857\ne) 1895 ')
        if p2 == "c":
            print('Resposta correta!')
            p3 = (input('Qual é o elemento químico representado pelo símbolo "O"?\na) Oxigênio\nb) Ouro\nc) Osmium\nd) Hidrogênio\ne) Ozônio '))
            if p3 == "a":
                print('Resposta correta!')
                p4 = (input('Quem pintou a obra "A Última Ceia"?\na) Michelangelo\nb) Rafael\nc) Leonardo da Vinci\nd) Van Gogh\ne) Botticelli '))
                if p4 == "c":
                     print('Resposta correta, vamos para a última pergunta!')
                     p5 = (input('Qual país é conhecido como a "terra do sol nascente"?\na) China\nb) Coreia do Sul\nc) Japão\nd) Tailândia\ne) Indonésia '))
                     if p5 == "c":
                          retry = (input('VOCÊ GANHOU!!! Sua alma será poupada... por hoje :3\nRecomeçar? (s/n) '))
                          if retry == "s":
                               print('Retomando...')
                          else:
                                break
                     if p5 != "c":
                          retry = (input('ERROU!!!!!!!! Tentar novamente? (s/n) '))
                          if retry == "s":
                               print('Retomando...')
                          else:
                               break
                if p4 != "c":
                    retry = (input('ERROU!!!!!!!! Tentar novamente? (s/n) '))
                    if retry == "s":
                        print('Retomando...')
                    else:
                        break
            if p3 != "a":
                retry = (input('ERROU!!!!!!!! Tentar novamente? (s/n) '))
            if retry == "s":
                    print('Retomando...')
            else:
                break
        if p2 != "c":
            retry = (input('ERROU!!!!!!!! Tentar novamente? (s/n) '))
            if retry == "s":
                    print('Retomando...')
            else:
                break
    else:
        retry = (input('ERROU!!!!!!!! Tentar novamente? (s/n) '))
        if retry == "s":
            print('Retomando...')
        else:
            break
