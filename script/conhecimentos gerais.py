import pygame
import os
from time import sleep
pygame.mixer.init()
base_path = os.path.dirname(__file__)

acertou = 'Resposta correta!'
errou = 'ERROU!!!!!!!!'
fim = 'VOCÊ GANHOU!!! Sua alma será poupada... por hoje :3\nRecomeçar? (s/n)'

perguntas = [
    {"texto":'Sua primeira pergunta é: Qual é o maior planeta do Sistema Solar?\na) Saturno\nb) Júpiter\nc) Marte\nd) Terra\ne) Urano',"resposta":'a'},
    {"texto":'Em que ano aconteceu a Proclamação da República no Brasil?\na) 1879\nb) 1900\nc) 1889\nd) 1857\ne) 1895',"resposta":'c'},
    {"texto":'Qual é o elemento químico representado pelo símbolo "O"?\na) Oxigênio\nb) Ouro\nc) Osmium\nd) Hidrogênio\ne) Ozônio',"resposta":'a'},
    {"texto":'Quem pintou a obra "A Última Ceia"?\na) Michelangelo\nb) Rafael\nc) Leonardo da Vinci\nd) Van Gogh\ne) Botticelli',"resposta":'c'},
    {"texto":'Qual país é conhecido como a "terra do sol nascente"?\na) China\nb) Coreia do Sul\nc) Japão\nd) Tailândia\ne) Indonésia',"resposta":'c'},
    {"texto":'Qual é o rio mais longo do mundo?\na) Nilo\nb) Mississippi\nc) Yangtzé\nd) Amazonas\ne) Danúbio',"resposta":'d'},
    {"texto":'Quem escreveu "Dom Quixote"?\na) William Shakespeare\nb) Miguel de Cervantes\nc) Gabriel García Márquez\nd) Eça de Queirós\ne) Machado de Assis',"resposta":'b'},
    {"texto":'Qual é a fórmula química da água?\na) H2O2\nb) CO2\nc) H2O\nd) CH4\ne) NaCl',"resposta":'c'},
    {"texto":'Qual é o maior oceano do planeta?\na) Oceano Atlântico\nb) Oceano Índico\nc) Oceano Ártico\nd) Oceano Antártico\ne) Oceano Pacífico',"resposta":'e'},
    {"texto":'Em que continente está localizado o Deserto do Saara?\na) América do Norte\nb) Ásia\nc) Austrália\nd) África\ne) Europa',"resposta":'d'}

]

def fazer_perguntas(perguntas): # Função para o modo difícil
    print('MODO DIFÍCIL ATIVADO!!!')
    sleep(2)
    pontuacao = 0  # Inicializa a pontuação

    for pergunta in perguntas: # Loop para as perguntas
        print(pergunta["texto"]) # Exibe a pergunta
        resposta = input().strip().lower() # Recebe a resposta do jogador
        if resposta == pergunta["resposta"]: # Verifica se a resposta está correta
            print(acertou)
            pontuacao += 1  # Incrementa a pontuação            
            sleep(2)
        else: # Se a resposta estiver errada
            print(errou)
            sleep(2)
            return False

    print(f'Sua pontuação final é: {pontuacao} de {len(perguntas)}') # Exibe a pontuação final
    return True
    

def fazer_perguntas_normal(perguntas): # Função para o modo normal
    print('MODO NORMAL ATIVADO!!! Você tem direito a pular uma pergunta. Para pular, digite "p"')
    sleep(2)
    pontuacao = 0  # Inicializa a pontuação

    for pergunta in perguntas: # Loop para as perguntas
        print(pergunta["texto"]) # Exibe a pergunta
        resposta = input().strip().lower() # Recebe a resposta do jogador
        if resposta == pergunta["resposta"]: # Verifica se a resposta está correta
            print(acertou)
            pontuacao += 1  # Incrementa a pontuação
            sleep(2)
        elif resposta == 'p': # Verifica se o jogador deseja pular a pergunta
            print('Pulou a pergunta')
            continue
        else: # Se a resposta estiver errada
            print(errou)
            sleep(2)

    print(f'Sua pontuação final é: {pontuacao} de {len(perguntas)}') # Exibe a pontuação final
    return True

def ost(): # Função para a música de fundo
    spooky = os.path.join(base_path, 'music', 'spookyfunnight.mp3')
    pygame.mixer.music.load(spooky)
    pygame.mixer.music.play(loops=-1)

def error(): # Função para o som de erro
     faustão = os.path.join(base_path, 'music', 'errou.mp3')
     error_sound = pygame.mixer.Sound(faustão)
     error_sound.play()

ost() # Inicia a música de fundo

bemvindo = input(('Bem vindo! você gostaria de jogar um jogo? (s/n) :) ')).strip().lower() # Pergunta se o jogador deseja jogar
if bemvindo == 's':
        print('Vamos nessa!!!')
        sleep(2)
else:
        print('Você não tem escolha :3')
        sleep(2)

ajuda = input('Você gostaria de saber sobre o jogo? (s/n) ').strip().lower() # Pergunta se o jogador deseja saber sobre o jogo
if ajuda == 's':
     print('O jogo é simples, você terá que responder perguntas de conhecimentos gerais.')
     sleep(2)
     print('Você terá duas opções de dificuldade: normal e difícil.')
     sleep(2)
     print('Na dificuldade normal, se você errar perderá pontos, e você terá direito a pular uma pergunta.')
     sleep(2)
     print('Na dificuldade difícil, você não terá direito a pular nenhuma pergunta. E se você perder, reiniciará o jogo.')
     sleep(2)
     print('Boa sorte!!!')
else:
     print('Então vamos lá!!!')
     sleep(2)

while True: # Loop para o jogo
     dificuldade = input('Escolha a dificuldade: normal, difícil (n/d) ').strip().lower() # Pergunta a dificuldade
     if dificuldade == 'n':
          venceu = fazer_perguntas_normal(perguntas)
     elif dificuldade == 'd':
          venceu = fazer_perguntas(perguntas)
     else:
          print("Dificuldade inválida. Escolha 'normal' ou 'difícil'.") # Mensagem de erro
          break

     if venceu: # Verifica se o jogador venceu
          print(fim) # Exibe a mensagem de vitória
          end = input() # Pergunta se o jogador deseja jogar novamente
          if end == 'n': # Verifica se o jogador deseja jogar novamente
               break # Encerra o jogo
