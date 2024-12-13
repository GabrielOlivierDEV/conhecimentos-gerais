import pygame
import os
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

def fazer_perguntas(perguntas):
    
     for pergunta in perguntas:
          print(pergunta["texto"])
          resposta = input().strip().lower()
          if resposta == pergunta["resposta"]:
               print(acertou)
          else:
               print(errou)
               error() 
               return False
     return True

def ost():
    spooky = os.path.join(base_path, 'music', 'spookyfunnight.mp3')
    pygame.mixer.music.load(spooky)
    pygame.mixer.music.play(loops=-1)

def error():
     faustão = os.path.join(base_path, 'music', 'errou.mp3')
     error_sound = pygame.mixer.Sound(faustão)
     error_sound.play()

ost()

bemvindo = input(('Bem vindo! você gostaria de jogar um jogo? (s/n) :) ')).strip().lower()
if bemvindo == 's':
        print('Vamos nessa!!!',end=' ')
else:
        print('Você não tem escolha :3',end=' ')

while True:        
    venceu = fazer_perguntas(perguntas)
    if venceu:
        print(fim)
        end = input()
        if end == 'n':
              break