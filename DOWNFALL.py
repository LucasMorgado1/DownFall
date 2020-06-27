import pygame
import random


pygame.init()

class jogador():  # Classecom tudo que envolve o jogador
    def __init__(self, jogador_x, jogador_y):

        self.jogadori = pygame.image.load('Sheet_Jogador.png')
        self.jogador_x = jogador_x
        self.jogador_y = jogador_y
        self.arma = (self.jogador_x + 17, self.jogador_y - 60, 30, 60)
        self.vel = 5
        self.vida_jogador = 3
        self.disney = pygame.Rect(-200, -200, -200, -200)
        self.hitbox = pygame.Rect(self.jogador_x, self.jogador_y, 64, 64)
        self.colidiu = False
        self.cont_invencibilidade = 241
        self.vida_jogadori = pygame.image.load('vida_jogado.png')
        self.x_imagem_vida = 0
        self.x_imagem_jogador = 0
        self.y_imagem_jogador = 0
        self.cont_animacao = 0
        self.morte = False
        self.pegou_vida = False
        self.nova_vida = pygame.Rect(605, 390, 64, 64)
        self.buff_vidai = pygame.image.load('Buff_Vida.png')
        # Marlei Variaveis
        self.cont_socao = 0
        self.colidiu_socao = False
        self.espada = False
        self.espada_cont = 0

    def desenhar_jogador(self): 
        if self.vida_jogador > 0:
            self.hitbox = pygame.Rect((self.jogador_x + 13), (self.jogador_y + 6), 35,
                                      54)  # para ficar junto do jogador
            tela.blit(self.jogadori, (self.jogador_x + 11, self.jogador_y + 5),
                      (self.x_imagem_jogador, self.y_imagem_jogador, 40, 58))
            #pygame.draw.rect(tela, vermelho, self.hitbox, 1)
        if self.vida_jogador < 0:
            self.hitbox = self.disney

    def hud_vida(self):
        if self.pegou_vida == True:
            if self.vida_jogador == 4:
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 171, 39))
            if self.vida_jogador == 3:
                self.x_imagem_vida = 42
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 171, 39))
            if self.vida_jogador == 2:
                self.x_imagem_vida = 84
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 171, 39))
            if self.vida_jogador == 1:
                self.x_imagem_vida = 126
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 171, 39))
        else:
            if self.vida_jogador == 3:
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 128, 39))
            if self.vida_jogador == 2:
                self.x_imagem_vida = 42
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 128, 39))
            if self.vida_jogador == 1:
                self.x_imagem_vida = 84
                tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 128, 39))

    def hud_vida_buff(self):
        if self.pegou_vida == True:
            self.vida_jogador = 4
            self.vida_jogadori = pygame.image.load('vida_jogado_buff.png')
            self.x_imagem_vida = 0

    def movimento_jogador(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.jogador_x -= self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_d]:
            self.jogador_x += self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_w]:
            self.jogador_y -= self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_s]:
            self.jogador_y += self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_s] == False and keys[pygame.K_w] == False and keys[pygame.K_d] == False and keys[
            pygame.K_a] == False:
            self.x_imagem_jogador = 0
            self.cont_animacao = 0

    def colisao_jogador_parede(self):
        if self.jogador_x == 1100:
            self.jogador_x -= self.vel
        if self.jogador_x == 115:
            self.jogador_x += self.vel
        if self.jogador_y == 645:
            self.jogador_y -= self.vel
        if self.jogador_y == 205:
            self.jogador_y += self.vel

    def colisao_jogador_inimigo(self, inimigo_hitbox):
        self.cont_invencibilidade += 1

        if self.colidiu == False:
            # y              altura           y                  y                   y                      altura
            '''if self.hitbox[1] + self.hitbox[3] >= inimigo_hitbox[1] and self.hitbox[1] <= inimigo_hitbox[1] + inimigo_hitbox[3]:
                if self.hitbox[0] + self.hitbox[2] >= inimigo_hitbox[0] and self.hitbox[0] <= inimigo_hitbox[0] + inimigo_hitbox[2]:'''
            if self.hitbox.colliderect(inimigo_hitbox):
                print(self.vida_jogador)
                self.vida_jogador -= 1
                self.colidiu = True
                self.cont_invencibilidade = 0
        if self.cont_invencibilidade %10 == 0 and self.colidiu:
            self.y_imagem_jogador = 0
        else:
            self.y_imagem_jogador = 59
        if self.cont_invencibilidade > 240:
            self.colidiu = False
            self.y_imagem_jogador = 0

    def colisao_jogador_socao(self, inimigo_hitbox):
        if self.hitbox.colliderect(inimigo_hitbox):
            self.colidiu_socao = True
        if self.colidiu_socao == True:
            self.cont_socao += 1
            self.jogador_y += 12
        if self.cont_socao == 20:
            self.colidiu_socao = False
            self.cont_socao = 0

    def colisao_bloco(self, muro):
        if self.hitbox.colliderect(muro):
            # print('x: ', self.bixo_x, 'y: ', self.bixo_y)
            if self.hitbox[1] + self.hitbox[3] >= muro[1] and self.hitbox[1] + self.hitbox[3] <= muro[
                1] + 5:  # lado direito do x, certo
                self.jogador_y -= 5
            if self.hitbox[1] <= muro[1] + muro[3] and self.hitbox[1] >= muro[1] + muro[3] - 5:
                self.jogador_y += 5
            if self.hitbox[0] + self.hitbox[2] >= muro[0] and self.hitbox[0] + self.hitbox[2] <= muro[0] + 5:
                self.jogador_x -= 5
            if self.hitbox[0] <= muro[0] + muro[2] and self.hitbox[0] >= muro[0] + muro[2] - 5:
                self.jogador_x += 5

    def morre(self):
        if self.vida_jogador <= 0:
            self.morte = True
            self.jogador_x = 605
            self.jogador_y = 610
            self.x_imagem_vida = 0
            self.vida_jogadori = pygame.image.load('vida_jogado.png')
            self.vida_jogador = 3
            self.pegou_vida = False
            self.cont_invencibilidade = 241
        else:
            self.morte = False

    def melhorias_vida(self, jorge_1, jeorgia_1, jeorgia_2, roberto_1, roberto_2):
        if jorge_1 <= 0 and jeorgia_1 <= 0 and jeorgia_2 <= 0 and roberto_1 <= 0 and roberto_2 <= 0 and self.pegou_vida == False:
            tela.blit(self.buff_vidai, (605, 390))
            #pygame.draw.rect(tela, vermelho, self.nova_vida)
            if self.nova_vida.colliderect(self.hitbox):
                self.pegou_vida = True

class armamentos(pygame.sprite.Sprite):  # Classe para as armas do jogador
    def __init__(self):
        self.x = 0
        self.y = 0
        self.arma = pygame.image.load('espada.png')
        self.espaco = False
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.contador = 0
        self.desenhar = False
        self.disney = pygame.Rect(-200, -200, -200, -200)  # Disney é uma variavel que retica as coisa da tela.
        self.dano = 1
        self.buff_dano = False
        self.nova_espada = pygame.Rect(605, 390, 64, 64)
        self.pegou_espada = False
        self.buff_danoi = pygame.image.load('Espada_Buff.png')

    def hora_de_desenhar(self, cont):  # ferifica se o jogador não está espando o espaço, e depois libera para desenhar
        if cont > 80:
            self.desenhar = True

    def desenhar_espada(self, x_jogador, y_jogador):
        if self.contador <= 60 and self.desenhar:
            self.hitbox = (x_jogador + 28, y_jogador - 35, 16, 64)
            #pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            tela.blit(self.arma, (x_jogador + 2, y_jogador - 40))
            self.contador += 1  # contador que faz a espada ficar na tela por 1 segundo = 60 FPS

        elif self.contador >= 60:
            self.hitbox = self.disney  # nesse caso a disney esta removendo a hit.box da espada, tivemos alguns erros aqui.
            self.desenhar = False
            self.contador = 0

    def melhorias_espada(self, roberto_1, roberto_2, roberto_3, roberto_4, roberto_5, roberto_6, roberto_7,
                         jogador_hitbox):
        if roberto_1 <= 0 and roberto_2 <= 0 and roberto_3 <= 0 and roberto_4 <= 0 and roberto_5 <= 0 and roberto_6 <= 0 \
                and roberto_7 <= 0 and self.pegou_espada == False:
            tela.blit(self.buff_danoi, (605, 390))
            #pygame.draw.rect(tela, vermelho, self.nova_espada)
            if self.nova_espada.colliderect(jogador_hitbox):
                self.dano = 3
                self.pegou_espada = True

    def morre(self, morreu):
        if morreu == True:
            self.dano = 1
            self.pegou_espada = False

class staticos():
    def __init__(self, objeto_x, objeto_y, largura, altura):
        self.objeto_x = objeto_x
        self.objeto_y = objeto_y
        self.altura = altura
        self.largura = largura
        self.muro = pygame.Rect(self.objeto_x, self.objeto_y, self.largura, self.altura)
        self.muro_1 = pygame.Rect(self.objeto_x, self.objeto_y+30, self.largura, self.altura)
        self.muro_dois = pygame.Rect(self.objeto_x, self.objeto_y+30, self.largura, self.altura -29)
        self.espinhosi_empe = pygame.image.load('Espinhos_Linha_Esquerda.png')
        self.espinhosi_deitado = pygame.image.load('Espinhos_Linha_Deitado.png')
        self.espinhosi_dois = pygame.image.load('Espinho_Dois.png')
        self.espinhosi_um = pygame.image.load('Espinho_Um.png')
        self.paredei = pygame.image.load('Parede.png')

    def desenhar(self):
        #pygame.draw.rect(tela, azul, self.muro,1)
        tela.blit(self.espinhosi_empe, (self.objeto_x+ 10, self.objeto_y))

    def desenhar_deitado(self):
        #pygame.draw.rect(tela, azul, self.muro_1,1)
        tela.blit(self.espinhosi_deitado, (self.objeto_x, self.objeto_y))

    def densenhar_dois(self):
        #pygame.draw.rect(tela, azul, self.muro_dois, 1)
        tela.blit(self.espinhosi_dois, (self.objeto_x, self.objeto_y))

    def desenhar_um(self):
        #pygame.draw.rect(tela, azul,  self.muro_dois, 1)
        tela.blit(self.espinhosi_um, (self.objeto_x, self.objeto_y))

    def desenhar_parede(self):
        tela.blit(self.paredei, (self.objeto_x, self.objeto_y))

class inimigos():  # Classe para definir movimento e imprirmir os inimigo
    def __init__(self, bixo_x, bixo_y, vida):
        self.bixo_x = bixo_x
        self.bixo_y = bixo_y
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.bixo_hit = False  # Faz com que o bixo vá para tras quando é atingido
        self.disney = pygame.Rect(-200, -200, -200, -200)


        # Variaveis Jorge
        self.bateu = False
        self.vida_inimigo = vida
        self.cont = 0  # cont para não dar hit.kill no inimigo, fazendo muitas colisões ela serve para mandar o inimigo para tras tbm
        self.jorgei_frente = pygame.image.load('JorgeSheet.png')
        self.jorgei_costas = pygame.image.load('JorgeSheetCostas.png')
        self.x_animacao_jorge = 0
        self.y_animacao_jorge = 0
        self.cont_animacao = 0

        # Variaveis Roberto
        self.campo_visao = pygame.Rect(self.bixo_x - 125, self.bixo_y - 125, 250, 250)
        self.robertoi_direita = pygame.image.load('Cachorro_Sheet.png')
        self.robertoi_esquerda = pygame.image.load('Cachorro_Sheet_Contrario.png')
        self.x_animacao_roberto = 0
        self.y_animacao_roberto = 0
        self.avistado = False

        # Variaveis Jeorgia
        self.jeorgiai_direita = pygame.image.load('Jeorgia_Sheet_Contrario.png')
        self.jeorgiai_esquerda = pygame.image.load('Jeorgia_Sheet.png')
        self.x_animacao_jeorgia = 0
        self.y_animacao_jeorgia = 0

        # Variaveis Carlos
        self.carlos = (self.bixo_x, self.bixo_y)
        self.tiro_x = self.bixo_x
        self.tiro_y = self.bixo_y
        self.atirou_x = False
        self.atirou_y = False
        self.tiro_hitbox = pygame.Rect(0, 0, 0, 0)
        self.campo_visao_carlos_x_direto = pygame.Rect(self.bixo_x + 32, self.bixo_y - 32, 1025, 64)
        self.campo_visao_carlos_y_baixo = pygame.Rect(self.bixo_x - 32, self.bixo_y + 32, 64, 500)
        self.campo_visao_carlos_y_cima = pygame.Rect(self.bixo_x - 32, self.bixo_y - 532, 64, 500)
        self.campo_visao_carlos_x_esquerdo = pygame.Rect(self.bixo_x - 1032, self.bixo_y - 32, 1000, 64)
        self.cima = False
        self.baixo = False
        self.negativo = False
        self.carlosi_normal = pygame.image.load('Carlos_Sheet_1.png')
        self.carlosi_invertido = pygame.image.load('Carlos_Sheet Inverso.png')
        self.carlosi_baixo = pygame.image.load('Carlos_Sheet_Baixo.png')
        self.carlosi_cima = pygame.image.load('Carlos_Sheet_cima.png')
        self.x_animacao_carlos = 0
        self.x_animacao_carlos_inevrso = 847
        self.y_animacao_carlos = 0
        self.tiroi = pygame.image.load('Tiros.png')

    def desenhar_inimigo_jorge(self):
        if self.vida_inimigo > 0:
            self.hitbox = pygame.Rect(self.bixo_x - 24, self.bixo_y - 32, 46, 64)
            # pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            self.cont_animacao += 1
            if self.bateu == False:
                tela.blit(self.jorgei_frente, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_jorge, self.y_animacao_jorge, 49, 64))
                if self.cont_animacao == 10:
                    if self.x_animacao_jorge == 400:
                        self.x_animacao_jorge = 0
                        self.cont_animacao = 0
                    self.x_animacao_jorge += 50
                    self.cont_animacao = 0
            if self.bateu == True:
                tela.blit(self.jorgei_costas, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_jorge, self.y_animacao_jorge, 49, 64))
                if self.cont_animacao == 10:
                    if self.x_animacao_jorge == 400:
                        self.x_animacao_jorge = 0
                        self.cont_animacao = 0
                    self.x_animacao_jorge += 50
                    self.cont_animacao = 0
        else:
            self.hitbox = self.disney

    def desenhar_inimigo_carlos(self,jogador_hitbox):
        if self.vida_inimigo > 0:
            self.hitbox = pygame.Rect(self.bixo_x - 32, self.bixo_y - 32, 90, 62)
            #pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            if self.campo_visao_carlos_x_direto.colliderect(jogador_hitbox):
                self.cont_animacao+=1
                tela.blit(self.carlosi_normal, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_carlos, self.y_animacao_carlos, 90, 62))
                if self.cont_animacao == 10:
                    self.x_animacao_carlos += 95
                    self.cont_animacao = 0
                if self.x_animacao_carlos >= 821:
                    self.x_animacao_carlos = 0
            elif self.campo_visao_carlos_y_baixo.colliderect(jogador_hitbox):
                self.cont_animacao += 1
                tela.blit(self.carlosi_baixo, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_carlos, self.y_animacao_carlos, 65, 62))
                if self.cont_animacao == 20:
                    self.x_animacao_carlos += 66
                    self.cont_animacao = 0
                if self.x_animacao_carlos >= 194:
                    self.x_animacao_carlos = 0
            elif self.campo_visao_carlos_y_cima.colliderect(jogador_hitbox):
                self.cont_animacao += 1
                tela.blit(self.carlosi_cima, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_carlos, self.y_animacao_carlos, 65, 62))
                if self.cont_animacao == 20:
                    self.x_animacao_carlos += 66
                    self.cont_animacao = 0
                if self.x_animacao_carlos >= 234:
                    self.x_animacao_carlos = 0
            elif self.campo_visao_carlos_x_esquerdo.colliderect(jogador_hitbox):
                self.cont_animacao+=1
                tela.blit(self.carlosi_invertido, (self.bixo_x - 26, self.bixo_y - 32),
                        (self.x_animacao_carlos_inevrso, self.y_animacao_carlos, 90, 62))
                if self.cont_animacao == 10:
                    self.x_animacao_carlos_inevrso -= 95
                    self.cont_animacao = 0
                if self.x_animacao_carlos_inevrso <= 87:
                    self.x_animacao_carlos_inevrso = 847
            else:
                tela.blit(self.carlosi_normal, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_carlos, self.y_animacao_carlos, 90, 62))
                self.x_animacao_carlos_inevrso = 847
                self.x_animacao_carlos = 0
                self.cont_animacao = 0


            # pygame.draw.rect(tela, azul, self.campo_visao_carlos_x_direto, 1)
            # pygame.draw.rect(tela, azul, self.campo_visao_carlos_y_baixo, 1)
            # pygame.draw.rect(tela, azul, self.campo_visao_carlos_y_cima, 1)
            # pygame.draw.rect(tela, azul, self.campo_visao_carlos_x_esquerdo, 1)
        else:
            self.hitbox = self.disney

    def desenhar_inimigo_roberto(self, jogador_x, jogador_y):
        if self.vida_inimigo > 0:
            self.hitbox = pygame.Rect(self.bixo_x - 32, self.bixo_y - 32, 62, 44)
            self.campo_visao = pygame.Rect(self.bixo_x - 125, self.bixo_y - 125, 250, 250)
            if jogador_x + 32 >= self.bixo_x:
                tela.blit(self.robertoi_direita, (self.bixo_x - 32, self.bixo_y - 32),
                          (self.x_animacao_roberto, self.y_animacao_roberto, 60, 44))
            if jogador_x + 32 < self.bixo_x:
                tela.blit(self.robertoi_esquerda, (self.bixo_x - 32, self.bixo_y - 32),
                          (self.x_animacao_roberto, self.y_animacao_roberto, 60, 44))
            # pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            # pygame.draw.rect(tela, vermelho, self.campo_visao, 1)
            if self.avistado == True:
                self.cont_animacao += 1
                if self.cont_animacao == 10:
                    if self.x_animacao_roberto == 549:
                        self.x_animacao_roberto = 0
                        self.cont_animacao = 0
                    self.x_animacao_roberto += 61
                    self.cont_animacao = 0
        else:
            self.hitbox = self.disney

    def desenhar_inimigo_jeorgia(self):
        if self.vida_inimigo > 0:
            self.hitbox = pygame.Rect((self.bixo_x - 30), (self.bixo_y - 32), 50, 62)
            # pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            self.cont_animacao += 1
            if self.bateu == False:
                tela.blit(self.jeorgiai_direita, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_jeorgia, self.y_animacao_jeorgia, 44, 62))
                if self.cont_animacao == 10:
                    if self.x_animacao_jeorgia == 270:
                        self.x_animacao_jeorgia = 0
                        self.cont_animacao = 0
                    self.x_animacao_jeorgia += 45
                    self.cont_animacao = 0
            if self.bateu == True:
                tela.blit(self.jeorgiai_esquerda, (self.bixo_x - 26, self.bixo_y - 32),
                          (self.x_animacao_jeorgia, self.y_animacao_jeorgia, 44, 62))
                if self.cont_animacao == 10:
                    if self.x_animacao_jeorgia == 270:
                        self.x_animacao_jeorgia = 0
                        self.cont_animacao = 0
                    self.x_animacao_jeorgia += 45
                    self.cont_animacao = 0
        else:
            self.hitbox = self.disney

    def movimento_inimigo_jorge(self):
        if self.bixo_y == 668:
            self.bateu = True

        if self.bateu == True:
            self.bixo_y -= 2
            if self.bixo_hit:
                self.bixo_y -= 20

        if self.bateu == False:
            self.bixo_y += 2
            if self.bixo_hit:
                self.bixo_y -= 20

        if self.bixo_y == 240 or self.bixo_y < 240:
            self.bateu = False

    def movimento_inmigo_roberto(self, x_jogador, y_jogador, jogador_hitbox):

        if self.campo_visao.colliderect(jogador_hitbox):
            if x_jogador + 32 > self.bixo_x:
                self.bixo_x += 3
            if x_jogador + 32 < self.bixo_x:
                self.bixo_x -= 3
            if y_jogador + 32 > self.bixo_y:
                self.bixo_y += 3
            if y_jogador + 32 < self.bixo_y:
                self.bixo_y -= 3
            self.avistado = True
        else:
            self.avistado = False

    def movimento_inimigo_jeorgia(self):
        if self.bixo_x >= 1130:
            self.bateu = True

        if self.bateu == True:
            self.bixo_x -= 4
            if self.bixo_hit and self.bixo_y > 200:
                self.bixo_y -= 20

        if self.bateu == False:
            self.bixo_x += 4
            if self.bixo_hit and self.bixo_y > 200:
                self.bixo_y -= 20

        if self.bixo_x <= 150:
            self.bateu = False

    def tiro_carlos(self, jogador_hitbox):
        if self.vida_inimigo > 0:
            if self.campo_visao_carlos_y_cima.colliderect(jogador_hitbox):
                self.negativo = True
                self.atirou_y = True
            if self.atirou_y == True and self.negativo == True:
                self.tiro_hitbox = pygame.Rect(self.tiro_x-26, self.tiro_y-32, 16,16)
                tela.blit(self.tiroi, (self.tiro_x - 26, self.tiro_y - 32))
                pygame.draw.rect(tela, vermelho, self.tiro_hitbox,1)
                self.tiro_y -= 10
                if self.tiro_y <= 200:
                    self.atirou_y = False
                    self.negativo = False
                    self.tiro_y = self.bixo_y
                    self.tiro_x = self.bixo_x + 25

            if self.campo_visao_carlos_x_direto.colliderect(jogador_hitbox) and self.atirou_y == False:
                self.atirou_x = True
            if self.atirou_x == True and self.negativo == False:
                self.tiro_hitbox = pygame.Rect(self.tiro_x-26, self.tiro_y-32, 16, 16)
                tela.blit(self.tiroi, (self.tiro_x - 26, self.tiro_y - 32))
                pygame.draw.rect(tela, vermelho, self.tiro_hitbox,1)
                self.tiro_x += 10
                if self.tiro_x >= 1150:
                    self.atirou_x = False
                    self.tiro_x = self.bixo_x + 90
                    self.tiro_y = self.bixo_y + 7

            if self.campo_visao_carlos_y_baixo.colliderect(jogador_hitbox) and self.atirou_x == False:
                self.atirou_y = True
            if self.atirou_y == True and self.negativo == False:
                self.tiro_hitbox = pygame.Rect(self.tiro_x-26, self.tiro_y-32, 16, 16)
                tela.blit(self.tiroi, (self.tiro_x - 26, self.tiro_y - 32))
                pygame.draw.rect(tela, vermelho, self.tiro_hitbox,1)
                self.tiro_y += 10
                if self.tiro_y >= 730:
                    self.atirou_y = False
                    self.tiro_y = self.bixo_y + 15
                    self.tiro_x = self.bixo_x + 25

            if self.campo_visao_carlos_x_esquerdo.colliderect(jogador_hitbox):
                self.atirou_x = True
                self.negativo = True
            if self.atirou_x == True and self.negativo == True:
                self.tiro_hitbox = pygame.Rect(self.tiro_x-26, self.tiro_y-32, 16, 16)
                tela.blit(self.tiroi, (self.tiro_x - 26, self.tiro_y - 32))
                pygame.draw.rect(tela, vermelho, self.tiro_hitbox,1)
                self.tiro_x -= 10
                if self.tiro_x <= 150:
                    self.atirou_x = False
                    self.tiro_x = self.bixo_x
                    self.negativo = False

    def colisao_bloco_inimigos(self, muro):
        if self.hitbox.colliderect(muro):
            # print('x: ', self.bixo_x, 'y: ', self.bixo_y)
            if self.hitbox[1] + self.hitbox[3] >= muro[1] and self.hitbox[1] + self.hitbox[3] <= muro[1] + 3:  # lado direito do x, certo
                self.bixo_y -= 1
            if self.hitbox[1] <= muro[1] + muro[3] and self.hitbox[1] >= muro[1] + muro[3] - 3:
                self.bixo_y += 1
            if self.hitbox[0] + self.hitbox[2] >= muro[0] and self.hitbox[0] + self.hitbox[2] <= muro[0] + 3:
                self.bixo_x -= 1
            if self.hitbox[0] <= muro[0] + muro[2] and self.hitbox[0] >= muro[0] + muro[2] - 3:
                self.bixo_x += 1

    def colisao_espada(self, espada_hitbox, dano):
        self.cont += 1
        if self.hitbox.colliderect(espada_hitbox) and self.cont > 30:
            self.y_animacao_jeorgia = 64
            self.y_animacao_jorge = 64
            self.y_animacao_roberto = 45
            self.vida_inimigo -= dano
            self.bixo_hit = True
            self.cont = 0
            print(self.vida_inimigo)
        if self.cont > 5:
            self.bixo_hit = False

        if self.cont > 25:
            self.y_animacao_jeorgia = 0
            self.y_animacao_jorge = 0
            self.y_animacao_roberto = 0

class marlei():
    def __init__(self, bixo_x, bixo_y, vida):
        self.vida_inimigo = vida
        self.bixo_x = bixo_x
        self.bixo_y = bixo_y
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.bixo_hit = False  # Faz com que o bixo vá para tras quando é atingido
        self.disney = pygame.Rect(-200, -200, -200, -200)
        self.cont = 0
        self.ataques = ['tiro']
        self.cont_ataques = 0
        self.acabou_ataque = False
        self.cooldown = 0
        self.vel = 4
        self.marleii = pygame.image.load('Sheet_Boss_Movimento.png')
        self.cont_animacao = 0
        self.x_imagem = 0
        self.y_imagem = 0
        # Variaveis Ataque Dash
        self.bateu = False
        self.visao_avanco = pygame.Rect(0, 0, 0, 0)
        self.cont_cansado = 0
        self.colidiu = False
        self.cansado = False
        self.cont_dash = 0
        self.muda_tela = False
        # Variaveis Ataque Tiro
        self.visao_tiro = pygame.Rect(0, 0, 0, 0)
        self.tiros = []
        self.tiro_x = self.bixo_x
        self.tiro_y = self.bixo_y
        self.metralha = False
        self.cadencia = 0
        self.bala = 0
        self.cont_tiro = 0
        self.cont_animacao_tiro = 0
        self.tirosi = []
        # Variaveis Ataque Socao
        self.socao_hitbox = pygame.Rect(0, 0, 0, 0)
        self.socaoi = pygame.image.load('Soco_boss.png')
        self.cont_socao = 0


    def randomizador_ataques(self, jogador_hitbox):
        if self.acabou_ataque:
            self.cooldown += 1

        if self.acabou_ataque == True and self.cooldown >= 120:
            self.acabou_ataque = False
            self.cont_ataques = 0
            self.cooldown = 0

        if self.cooldown == 30:
            self.y_imagem = 0
            self.x_imagem = 0

        if self.cont_ataques == 0:
            random.shuffle(self.ataques)
            print(self.ataques[0])
        if self.ataques[0] == 'socao':
            self.ataque_socao()
            self.cont_ataques += 1
        if self.ataques[0] == 'dash':
            self.ataque_dash(jogador_hitbox)
            self.cont_ataques += 1
        if self.ataques[0] == 'tiro':
            self.ataque_tiro(jogador_hitbox)
            self.cont_ataques += 1

    def desenhar(self):
        if self.vida_inimigo > 0:
            self.cont_animacao +=1
            self.hitbox = pygame.Rect(self.bixo_x - 64, self.bixo_y - 64, 115, 109)
            self.visao_avanco = pygame.Rect(self.bixo_x - 64, self.bixo_y - 64, 128, 490)
            self.visao_tiro = pygame.Rect(self.bixo_x - 32, self.bixo_y - 64, 64, 490)
            tela.blit(self.marleii, (self.bixo_x- 64 , self.bixo_y-64),
                      (self.x_imagem, self.y_imagem, 115, 109))
            if self.cont_animacao >= 10 and self.cooldown >30:
                self.x_imagem += 116
                self.cont_animacao = 0
            if self.x_imagem >= 463 and self.cooldown >30:
                self.x_imagem = 0
                self.cont_animacao = 0
            #pygame.draw.rect(tela, vermelho, self.visao_avanco, 1)
            #pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            #pygame.draw.rect(tela, verde, self.socao_hitbox)
            #pygame.draw.rect(tela, vermelho, self.visao_tiro, 1)
            #pygame.draw.circle(tela, branco, (self.bixo_x, self.bixo_y), 64)
        else:
            self.hitbox = self.disney
            self.visao_avanco = self.disney

    def movimento_marlei(self):

        if self.bixo_x >= 998:
            self.bateu = True

        if self.bateu == True:
            self.bixo_x -= self.vel

        if self.bateu == False:
            self.bixo_x += self.vel

        if self.bixo_x <= 267:
            self.bateu = False

    def ataque_dash(self, jogador_hitbox):
        self.cont_dash += 1
        # print(self.cont_dash)
        if self.cont_dash >=260:
            self.y_imagem = 329
            self.x_imagem = 0
        if self.cont_dash >= 300:
            if self.visao_avanco.colliderect(jogador_hitbox) and self.bixo_y < 555 and self.cansado == False:
                self.colidiu = True
            if self.colidiu == True:
                self.bixo_y += 13
                self.cont_cansado += 1
            if self.bixo_y >= 550:
                self.colidiu = False
                self.muda_tela = True
                self.cont_cansado += 1
            if self.cont_cansado >= 120 and self.bixo_y > 275:
                self.cansado = True
                self.bixo_y -= 5
            if self.bixo_y <= 275 and self.cansado == True:
                self.cont_cansado = 0
                self.acabou_ataque = True
                self.cansado = False
                self.cont_dash = 0
                self.muda_tela = False

    def ataque_tiro(self, jogador_hitbox):
        self.cont_animacao_tiro +=1
        if self.bixo_x < 998 and self.metralha == False:
            self.bateu = False
        if self.bixo_x == 1000:
            self.vel = 0
            self.cont_tiro += 1
            self.y_imagem = 221
            if self.cont_tiro >= 30:
                self.x_imagem = 116
            if self.cont_tiro < 30:
                self.x_imagem = 0
        if self.cont_tiro >= 60:
            self.vel = 4
            self.metralha = True

        '''if self.visao_tiro.colliderect(jogador_hitbox):
            self.metralha = True'''
        if self.metralha == True:
            self.cadencia += 1
            if self.cadencia >= 25 and self.bala < 10:
                self.cria_tiro()
                self.cadencia = 0
                self.bala += 1

    def atualiza_tiro(self):
        for tiro in self.tiros:
            pygame.draw.rect(tela, roxo, tiro)
            tiro.y += 5
        for tiro in self.tiros:
            if tiro.y >= 645:
                self.tiros.remove(tiro)
        if self.bala >= 9:
            self.acabou_ataque = True
            self.metralha = False
            self.bala = 0
            self.cont_tiro = 0
            self.x_imagem = 0

    def cria_tiro(self):
        self.tiro_x = self.bixo_x
        self.tiros.append(pygame.Rect(self.tiro_x, self.tiro_y, 20, 20))

    def colisao_espada(self, espada_hitbox, dano):
        self.cont += 1
        if self.hitbox.colliderect(espada_hitbox) and self.cont > 30:
            self.vida_inimigo -= dano
            self.bixo_hit = True
            self.cont = 0
            print(self.vida_inimigo)
        if self.cont > 5:
            self.bixo_hit = False

    def ataque_socao(self):
        self.cont_socao += 1
        if self.cont_socao >= 100 and self.cont_socao < 150:
            self.y_imagem = 110
            self.x_imagem = 0
        if self.cont_socao >= 150 and self.cont_socao < 200:
            self.y_imagem = 110
            self.x_imagem = 116
        if self.cont_socao >= 200:
            self.x_imagem = 232
            tela.blit(self.socaoi, (self.bixo_x - 32, self.bixo_y + 64))
            self.socao_hitbox = pygame.Rect(self.bixo_x - 32, self.bixo_y + 64, 64, 80)
        if self.cont_socao >= 260:
            self.acabou_ataque = True
            self.socao_hitbox = self.disney
            self.cont_socao = 0

class Transisao():
    def __init__(self):
        self.inimigos = True
        self.porta = pygame.Rect(605, 160, 64, 64)
        self.f_1 = False
        self.f_2 = False
        self.f_3 = False
        self.f_4 = False
        self.f_5 = False
        self.f_6 = False
        self.f_7 = False
        self.jorge = []
        self.jeorgia = []
        self.roberto = []
        self.carlos = []
        self.parede = []
        self.marlei = []
        self.randomizador_jorge = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
        self.randomizador_jeorgia = [300, 400, 500, 564]
        self.menu = True
        self.creditos = False
        self.tela_morte = False
        self.cont_menu = 0
        #menu
        self.jogar = True
        self.sair = False
        self.opcoes = 0
        self.tela_tutorial = False
        self.tutorial = False
        self.tela_vitoria =  False
        #morte


    def Nivel_2(self, jorge_0, jorge_1, jorge_2, jogador_hitbox):
        if jorge_0 <= 0 and jorge_1 <= 0 and jorge_2 <= 0:
            #pygame.draw.rect(tela, vermelho, self.porta)
            if self.porta.colliderect(jogador_hitbox):
                self.f_1 = False
                self.f_2 = True
                personagem.jogador_x = 605
                personagem.jogador_y = 610

    def recarregar_f1(self):
        #pygame.mixer.music.play(loops=-1, start=0.0)
        self.jorge = []
        random.shuffle(self.randomizador_jorge)
        for zonas in range(3):
            self.jorge.append(inimigos(self.randomizador_jorge[zonas], 240, 3))

    def recarregar_f2(self):
        self.jeorgia = []
        random.shuffle(self.randomizador_jeorgia)
        for zonas in range(2):
            self.jeorgia.append(inimigos(200, self.randomizador_jeorgia[zonas], 3))

        self.jorge = []
        self.jorge.append(inimigos(600, 160, 3))

        self.roberto = []
        self.roberto.append(inimigos(640, 400, 1))
        self.roberto.append(inimigos(840, 400, 1))

    def recarregar_f3(self):
        self.jeorgia = []
        self.jeorgia.append(inimigos(200, 600, 4))  # aumentar a vida pq ja eh mais dificil

        random.shuffle(self.randomizador_jorge)

        self.jorge = []
        for zonas in range(3):
            self.jorge.append(inimigos(self.randomizador_jorge[zonas], 240, 4))  # mesmo de cima

        self.roberto = []
        self.roberto.append(inimigos(250, 530, 2))
        self.roberto.append(inimigos(680, 530, 2))
        self.roberto.append(inimigos(1000, 530, 2))

    def recarregar_f4(self):
        self.jeorgia = []

        self.jorge = []

        self.parede = []
        self.parede.append(staticos(480, 455, 256, 128))

        self.roberto = []
        self.roberto.append(inimigos(340, 530, 2))
        self.roberto.append(inimigos(930, 530, 2))
        self.roberto.append(inimigos(330, 400, 2))
        self.roberto.append(inimigos(930, 400, 2))
        self.roberto.append(inimigos(170, 250, 2))
        self.roberto.append(inimigos(1100, 250, 2))
        self.roberto.append(inimigos(640, 420, 2))

    def recarregar_f5(self):
        self.jeorgia = []
        self.jeorgia.append(inimigos(252, 390, 5))
        self.jeorgia.append(inimigos(252, 595, 5))

        self.jorge = []
        self.jorge.append(inimigos(510, 250, 5))
        self.jorge.append(inimigos(765, 250, 5))

        self.roberto = []
        self.roberto.append(inimigos(425, 455, 2))
        self.roberto.append(inimigos(1020, 525, 2))

        self.paredes = []

        self.carlos = []
        self.carlos.append(inimigos(170, 250, 3))

    def recarregar_f6(self):
        self.jeorgia = []
        self.jeorgia.append(inimigos(252, 325, 5))
        self.jeorgia.append(inimigos(252, 540, 5))
        self.jeorgia.append(inimigos(252, 610, 5))
        self.jeorgia.append(inimigos(1020, 390, 5))
        self.jeorgia.append(inimigos(1020, 530, 5))

        self.jorge = []

        self.roberto = []

        self.paredes = []

        self.espinho = []
        self.espinho.append(staticos(470, 635, 64, 64))
        self.espinho.append(staticos(560, 495, 128, 64))
        self.espinho.append(staticos(720, 635, 64, 64))

        self.carlos = []
        self.carlos.append(inimigos(170, 250, 3))
        self.carlos.append(inimigos(165, 540, 3))
        self.carlos.append(inimigos(1080, 460, 3))

    def recarregar_f7(self):
        #pygame.mixer.music.load('musica_boss.mp3')
        #pygame.mixer.music.play(loops=-1, start=0.0)
        self.jeorgia = []

        self.carlos = []

        self.jorge = []

        self.roberto = []

        self.paredes = []

        self.espinho = []
        self.espinho.append(staticos(133, 215, 75, 485))
        self.espinho.append(staticos(1065, 215, 82, 485))
        self.espinho.append(staticos(210, 634, 852, 68))

        self.marlei = []
        self.marlei.append(marlei(640, 275, 30))

    def iniciar(self):
        self.menu = False
        self.f_1 = True

    def menu_creditos(self):
        self.menu = False
        self.creditos = True

    def Nivel_3(self, jorge_1, jeorgia_1, jeorgia_2, roberto_1, roberto_2, jogador_hitbox):
        if jorge_1 <= 0 and jeorgia_1 <= 0 and jeorgia_2 <= 0 and roberto_1 <= 0 and roberto_2 <= 0:
            #pygame.draw.rect(tela, vermelho, self.porta)
            if self.porta.colliderect(jogador_hitbox):
                self.f_2 = False
                self.f_3 = True
                personagem.jogador_x = 605
                personagem.jogador_y = 610

    def Nivel_4(self, jorge_1, jorge_2, jorge_3, jeorgia_1, roberto_1, roberto_2, roberto_3, jogador_hitbox):
        if jorge_1 <= 0 and jorge_2 <= 0 and jorge_3 <= 0 and jeorgia_1 <= 0 and roberto_1 <= 0 and roberto_2 <= 0 and roberto_3 <= 0:
            #pygame.draw.rect(tela, vermelho, self.porta)
            if self.porta.colliderect(jogador_hitbox):
                self.f_3 = False
                self.f_4 = True
                personagem.jogador_x = 605
                personagem.jogador_y = 610
                print("bateu")

    def Nivel_5(self, roberto_1, roberto_2, roberto_3, roberto_4, roberto_5, roberto_6, roberto_7, jogador_hitbox):
        if roberto_1 <= 0 and roberto_2 <= 0 and roberto_3 <= 0 and roberto_4 <= 0 and roberto_5 <= 0 and roberto_6 <= 0 and roberto_7 <= 0:
            #pygame.draw.rect(tela, vermelho, self.porta)
            if self.porta.colliderect(jogador_hitbox):
                self.f_4 = False
                self.f_5 = True
                personagem.jogador_x = 605
                personagem.jogador_y = 610
                print("bateu")

    def Nivel_6(self, roberto_1, roberto_2, jeorgia_1, jeorgia_2, jorge_1, jorge_2, carlos_1, jogador_hitbox):
        if roberto_1 <= 0 and roberto_2 <= 0 and jeorgia_1 <= 0 and jeorgia_2 <= 0 and jorge_1 <= 0 and jorge_2 <= 0 and carlos_1 <= 0:
            #pygame.draw.rect(tela, vermelho, self.porta)
            if self.porta.colliderect(jogador_hitbox):
                self.f_5 = False
                self.f_6 = True
                personagem.jogador_x = 605
                personagem.jogador_y = 610
                print("bateu")

    def Nivel_7(self, jeorgia_1, jeorgia_2, jeorgia_3, jeorgia_4, jeorgia_5, carlos_1, carlos_2, carlos_3,
                jogador_hitbox):
        if jeorgia_1 <= 0 and jeorgia_2 <= 0 and jeorgia_3 <= 0 and jeorgia_4 <= 0 and jeorgia_5 <= 0 and carlos_1 <= 0 and carlos_2 <= 0 and carlos_3 <= 0:
            #pygame.draw.rect(tela, vermelho, self.porta)
            if self.porta.colliderect(jogador_hitbox):
                self.f_6 = False
                self.f_7 = True
                personagem.jogador_x = 605
                personagem.jogador_y = 560
                print("bateu")

    def morre(self, morte):
        if morte == True:
            self.f_1 = False
            self.f_2 = False
            self.f_3 = False
            self.f_4 = False
            self.f_5 = False
            self.f_6 = False
            self.f_7 = False
            self.tela_morte = True


    def pular(self):
        self.f_1 = False
        self.f_2 = False
        self.f_3 = False
        self.f_4 = False
        self.f_5 = False
        self.f_6 = False
        self.f_7 = True

tela = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("DOWNFALL")

fase_4 = pygame.image.load('Fase4.png')
fase_3 = pygame.image.load('Fase3.png')
fase_2 = pygame.image.load('Fase2.png')
fase_1 = pygame.image.load('Fase1.png')

fase_4_Fechada = pygame.image.load('Fase4_Fechada.png')
fase_3_Fechada = pygame.image.load('Fase3_Fechada.png')
fase_2_Fechada = pygame.image.load('Fase2_Fechada.png')
fase_1_Fechada = pygame.image.load('Fase1_Fechada.png')


menui = pygame.image.load('menu.png')
mortei = pygame.image.load('Tela-morte.png')
creditosi = pygame.image.load('Tela_de_Creditos.png')
tutoriali = pygame.image.load('Tutorial2.png')
tela_ganhoui = pygame.image.load('Vencer.png')

preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 160, 0)
branco = (255, 255, 255)
roxo = (136, 123, 225)
cont = 0  # cont para o ataque do jogador serve para impedir que o jogador fique apertando espaço que nem um demente

run = True
personagem = jogador(605, 610)  # Variavel que recebe a classe Jogador
nivel = Transisao()

combate = armamentos()  # Classe das Armas            #Inimigo que persegue o jogador

clock = pygame.time.Clock()
frame = 60

#volume = 0.5 # de 0.0 Até 1.0
#pygame.mixer.init()
#pygame.mixer.music.load('musica_tela.mp3')
#pg.mixer.music.load('musica/Música2.wav')
# Quantas vezes vai tocar
# -1 = Loop eterno, 0 = Toca só 1 vez, +1 = toca mais x vezes
#pygame.mixer.music.set_volume(volume)

# pygame.draw.rect(tela, vermelho, 50, 50)

def tela_menu(tela):
    tela.blit(menui, (0, 0))

    nivel.cont_menu += 1

    if nivel.opcoes == 0 and nivel.cont_menu >= 10:
        pygame.draw.rect(tela, roxo, (60, 380, 720, 153), 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if nivel.tutorial == True:
                nivel.recarregar_f1()
                nivel.iniciar()
                nivel.cont_menu = 0
            if nivel.tutorial ==  False:
                nivel.menu = False
                nivel.tela_tutorial = True
                nivel.cont_menu = 0
        if keys[pygame.K_s]:
            nivel.cont_menu = 0
            nivel.opcoes += 1

    if nivel.opcoes == 1 and nivel.cont_menu >= 10:
        pygame.draw.rect(tela, roxo, (190, 571, 535, 100), 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            nivel.menu_creditos()
            nivel.cont_menu = 0
        if keys[pygame.K_w]:
            nivel.cont_menu = 0
            nivel.opcoes -= 1
        if keys[pygame.K_s]:
            nivel.cont_menu = 0
            nivel.opcoes += 1

    if nivel.opcoes == 2 and nivel.cont_menu >= 10:
        pygame.draw.rect(tela, roxo, (258, 693, 402, 100), 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            nivel.cont_menu = 0
            nivel.opcoes -= 1
        if keys[pygame.K_SPACE]:
            pygame.quit()

    pygame.display.update()

def tela_tutorial_ta(tela):
    tela.blit(tutoriali, (0, 0))

    nivel.cont_menu += 1

    if nivel.tutorial == False and cont >=119:
        nivel.tutorial = True

    if nivel.cont_menu == 120:
        nivel.tela_tutorial = False
        nivel.recarregar_f1()
        nivel.iniciar()
        nivel.cont_menu = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and nivel.cont_menu >= 10:
        nivel.tela_tutorial = False
        nivel.recarregar_f1()
        nivel.iniciar()
        nivel.cont_menu = 0


    pygame.display.update()

def tela_creditos(tela):
    tela.blit(creditosi, (0, 0))

    nivel.cont_menu += 1

    keys = pygame.key.get_pressed()
    pygame.draw.rect(tela, roxo, (0, 25, 350, 82), 1)
    if keys[pygame.K_SPACE] and nivel.cont_menu >= 10:
        nivel.creditos = False
        nivel.menu = True
        nivel.cont_menu = 0

    pygame.display.update()

def tela_morte(tela):
    tela.blit(mortei , (0, 0))

    nivel.cont_menu += 1


    if nivel.opcoes == 0 and nivel.cont_menu >= 10:
        pygame.draw.rect(tela, roxo, (243, 386, 720, 153), 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            nivel.tela_morte = False
            nivel.menu = True
            nivel.cont_menu = 0
        if keys[pygame.K_s]:
            nivel.opcoes = 1

    if nivel.opcoes == 1 and nivel.cont_menu >= 10:
        pygame.draw.rect(tela, roxo, (390, 565, 535, 100), 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            nivel.opcoes = 0
        if keys[pygame.K_SPACE]:
            pygame.quit()

    pygame.display.update()

def primeira_fase(tela, fase_1, personagem, combate):
    if nivel.jorge[0].vida_inimigo <= 0 and nivel.jorge[1].vida_inimigo <= 0 and nivel.jorge[2].vida_inimigo <= 0:
        tela.blit(fase_1, (0, 0))  # Pinta a tela de preto
    else:
        tela.blit(fase_1_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.hud_vida()
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.colisao_jogador_inimigo(nivel.jorge[0].hitbox)  # verifica se o jogador foi atingido pelo inimigo
        personagem.colisao_jogador_inimigo(nivel.jorge[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[2].hitbox)
        personagem.desenhar_jogador()

    for jorges in nivel.jorge:
        # if jorges.vida_inimigo >=0:
        jorges.movimento_inimigo_jorge()  # Movimento do Inimigo (Vertical)
        jorges.desenhar_inimigo_jorge()  # Imprime o inimigo
        jorges.colisao_espada(combate.hitbox, combate.dano)

    nivel.Nivel_2(nivel.jorge[0].vida_inimigo, nivel.jorge[1].vida_inimigo
                  , nivel.jorge[2].vida_inimigo, personagem.hitbox)

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    pygame.display.update()  # Update em tudo

    if nivel.f_2 == True:
        nivel.recarregar_f2()

def segunda_fase(tela, fase_1, personagem, combate):
    if nivel.jorge[0].vida_inimigo <= 0 and nivel.jeorgia[0].vida_inimigo <= 0 and nivel.jeorgia[1].vida_inimigo <= 0 \
            and nivel.roberto[1].vida_inimigo <= 0 and nivel.roberto[0].vida_inimigo <= 0:
        tela.blit(fase_1, (0, 0))  # Pinta a tela de preto
    else:
        tela.blit(fase_1_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_jogador_inimigo(nivel.roberto[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.roberto[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[0].hitbox)
        personagem.hud_vida()

    for robertos in nivel.roberto:
        # if robertos.vida_inimigo >= 0:
        robertos.desenhar_inimigo_roberto(personagem.jogador_x, personagem.jogador_y)
        robertos.colisao_espada(combate.hitbox, combate.dano)
        robertos.movimento_inmigo_roberto(personagem.jogador_x, personagem.jogador_y, personagem.hitbox)

    for jeorgias in nivel.jeorgia:
        # if jeorgias.vida_inimigo >= 0:
        jeorgias.desenhar_inimigo_jeorgia()
        jeorgias.colisao_espada(combate.hitbox, combate.dano)
        jeorgias.movimento_inimigo_jeorgia()

    for jorges in nivel.jorge:
        # if jorges.vida_inimigo >= 0:
        jorges.movimento_inimigo_jorge()  # Movimento do Inimigo (Vertical)
        jorges.desenhar_inimigo_jorge()  # Imprime o inimigo
        jorges.colisao_espada(combate.hitbox, combate.dano)

    personagem.melhorias_vida(nivel.jorge[0].vida_inimigo, nivel.jeorgia[0].vida_inimigo, nivel.jeorgia[1].vida_inimigo,
                              nivel.roberto[0].vida_inimigo, nivel.roberto[1].vida_inimigo)

    personagem.hud_vida_buff()

    nivel.Nivel_3(nivel.jorge[0].vida_inimigo, nivel.jeorgia[0].vida_inimigo, nivel.jeorgia[1].vida_inimigo,
                  nivel.roberto[0].vida_inimigo, nivel.roberto[1].vida_inimigo, personagem.hitbox)

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    if nivel.f_3 == True:
        nivel.recarregar_f3()

    pygame.display.update()  # Update em tudo

def terceira_fase(tela, fase_2, personagem, combate):
    if nivel.jorge[0].vida_inimigo <= 0 and nivel.jorge[1].vida_inimigo <= 0 and nivel.jorge[2].vida_inimigo <= 0 \
            and nivel.jeorgia[0].vida_inimigo <= 0 and nivel.roberto[0].vida_inimigo <= 0 \
            and nivel.roberto[1].vida_inimigo <= 0 and nivel.roberto[2].vida_inimigo <= 0:
        tela.blit(fase_2, (0, 0))
    else:
        tela.blit(fase_2_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_jogador_inimigo(nivel.roberto[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.roberto[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.roberto[2].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[2].hitbox)
        personagem.hud_vida()

    for robertos in nivel.roberto:
        # if robertos.vida_inimigo >= 0:
        robertos.desenhar_inimigo_roberto(personagem.jogador_x, personagem.jogador_y)
        robertos.colisao_espada(combate.hitbox, combate.dano)
        robertos.movimento_inmigo_roberto(personagem.jogador_x, personagem.jogador_y, personagem.hitbox)

    for jeorgias in nivel.jeorgia:
        # if jeorgias.vida_inimigo >= 0:
        jeorgias.desenhar_inimigo_jeorgia()
        jeorgias.colisao_espada(combate.hitbox, combate.dano)
        jeorgias.movimento_inimigo_jeorgia()

    for jorges in nivel.jorge:
        # if jorges.vida_inimigo >= 0:
        jorges.movimento_inimigo_jorge()  # Movimento do Inimigo (Vertical)
        jorges.desenhar_inimigo_jorge()  # Imprime o inimigo
        jorges.colisao_espada(combate.hitbox, combate.dano)

    nivel.Nivel_4(nivel.jorge[0].vida_inimigo, nivel.jorge[1].vida_inimigo, nivel.jorge[2].vida_inimigo,
                  nivel.jeorgia[0].vida_inimigo, nivel.roberto[0].vida_inimigo, nivel.roberto[1].vida_inimigo,
                  nivel.roberto[2].vida_inimigo, personagem.hitbox)

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    if nivel.f_4 == True:
        nivel.recarregar_f4()

    pygame.display.update()

def quarta_fase(tela, fase_2, personagem, combate):
    if nivel.roberto[0].vida_inimigo <= 0 and nivel.roberto[1].vida_inimigo <= 0 and nivel.roberto[2].vida_inimigo <= 0 \
            and nivel.roberto[3].vida_inimigo <= 0 and nivel.roberto[4].vida_inimigo <= 0 \
            and nivel.roberto[5].vida_inimigo <= 0 and nivel.roberto[6].vida_inimigo <= 0:
        tela.blit(fase_2, (0, 0))
    else:
        tela.blit(fase_2_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_bloco(nivel.parede[0].muro)
        for robertos in nivel.roberto:
            personagem.colisao_jogador_inimigo(robertos.hitbox)

        personagem.hud_vida()

    for robertos in nivel.roberto:
        robertos.desenhar_inimigo_roberto(personagem.jogador_x, personagem.jogador_y)
        robertos.colisao_espada(combate.hitbox, combate.dano)
        robertos.movimento_inmigo_roberto(personagem.jogador_x, personagem.jogador_y, personagem.hitbox)
        robertos.colisao_bloco_inimigos(nivel.parede[0].muro)

    for paredes in nivel.parede:
        paredes.desenhar_parede()

    combate.melhorias_espada(nivel.roberto[0].vida_inimigo, nivel.roberto[1].vida_inimigo,
                             nivel.roberto[2].vida_inimigo,
                             nivel.roberto[3].vida_inimigo, nivel.roberto[4].vida_inimigo,
                             nivel.roberto[5].vida_inimigo,
                             nivel.roberto[6].vida_inimigo, personagem.hitbox)

    nivel.Nivel_5(nivel.roberto[0].vida_inimigo, nivel.roberto[1].vida_inimigo, nivel.roberto[2].vida_inimigo,
                  nivel.roberto[3].vida_inimigo, nivel.roberto[4].vida_inimigo, nivel.roberto[5].vida_inimigo,
                  nivel.roberto[6].vida_inimigo, personagem.hitbox)

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    if nivel.f_5 == True:
        nivel.recarregar_f5()

    pygame.display.update()

def quinta_fase(tela, fase_3, personagem, combate):
    if nivel.roberto[0].vida_inimigo <= 0 and nivel.roberto[1].vida_inimigo <= 0 and nivel.jeorgia[0].vida_inimigo <= 0 \
            and nivel.jeorgia[1].vida_inimigo <= 0 and nivel.jorge[0].vida_inimigo <= 0 \
            and nivel.jorge[1].vida_inimigo <= 0 and nivel.carlos[0].vida_inimigo <= 0:
        tela.blit(fase_3, (0, 0))
    else:
        tela.blit(fase_3_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_jogador_inimigo(nivel.roberto[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.roberto[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[0].tiro_hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[0].hitbox)

        personagem.hud_vida()

    for robertos in nivel.roberto:
        # if robertos.vida_inimigo >= 0:
        robertos.desenhar_inimigo_roberto(personagem.jogador_x, personagem.jogador_y)
        robertos.colisao_espada(combate.hitbox, combate.dano)
        robertos.movimento_inmigo_roberto(personagem.jogador_x, personagem.jogador_y, personagem.hitbox)

    for jeorgias in nivel.jeorgia:
        # if jeorgias.vida_inimigo >= 0:
        jeorgias.desenhar_inimigo_jeorgia()
        jeorgias.colisao_espada(combate.hitbox, combate.dano)
        jeorgias.movimento_inimigo_jeorgia()

    for jorges in nivel.jorge:
        # if jorges.vida_inimigo >= 0:
        jorges.movimento_inimigo_jorge()  # Movimento do Inimigo (Vertical)
        jorges.desenhar_inimigo_jorge()  # Imprime o inimigo
        jorges.colisao_espada(combate.hitbox, combate.dano)

    for carloss in nivel.carlos:
        carloss.desenhar_inimigo_carlos(personagem.hitbox)
        carloss.colisao_espada(combate.hitbox, combate.dano)
        carloss.tiro_carlos(personagem.hitbox)

    nivel.Nivel_6(nivel.roberto[0].vida_inimigo, nivel.roberto[1].vida_inimigo, nivel.jeorgia[0].vida_inimigo,
                  nivel.jeorgia[1].vida_inimigo, nivel.jorge[0].vida_inimigo, nivel.jorge[1].vida_inimigo,
                  nivel.carlos[0].vida_inimigo, personagem.hitbox)

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    if nivel.f_6 == True:
        nivel.recarregar_f6()

    pygame.display.update()

def sexta_fase(tela, fase_3, personagem, combate):
    if nivel.jeorgia[0].vida_inimigo <= 0 and nivel.jeorgia[1].vida_inimigo <= 0 and nivel.jeorgia[2].vida_inimigo <= 0 \
            and nivel.jeorgia[3].vida_inimigo <= 0 and nivel.jeorgia[4].vida_inimigo <= 0 \
            and nivel.carlos[0].vida_inimigo <= 0 and nivel.carlos[1].vida_inimigo <= 0 and nivel.carlos[2].vida_inimigo <= 0:
        tela.blit(fase_3, (0, 0))
    else:
        tela.blit(fase_3_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_jogador_inimigo(nivel.jeorgia[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[2].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[3].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[4].hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[0].tiro_hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[1].tiro_hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[2].tiro_hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.carlos[2].hitbox)
        personagem.colisao_jogador_inimigo(nivel.espinho[0].muro_dois)
        personagem.colisao_jogador_inimigo(nivel.espinho[1].muro_dois)
        personagem.colisao_jogador_inimigo(nivel.espinho[2].muro_dois)
        personagem.hud_vida()

    for jeorgias in nivel.jeorgia:
        # if jeorgias.vida_inimigo >= 0:
        jeorgias.desenhar_inimigo_jeorgia()
        jeorgias.colisao_espada(combate.hitbox, combate.dano)
        jeorgias.movimento_inimigo_jeorgia()

    for carloss in nivel.carlos:
        carloss.desenhar_inimigo_carlos(personagem.hitbox)
        carloss.colisao_espada(combate.hitbox, combate.dano)
        carloss.tiro_carlos(personagem.hitbox)


    nivel.espinho[0].desenhar_um()
    nivel.espinho[1].densenhar_dois()
    nivel.espinho[2].desenhar_um()

    nivel.Nivel_7(nivel.jeorgia[0].vida_inimigo, nivel.jeorgia[1].vida_inimigo, nivel.jeorgia[2].vida_inimigo,
                  nivel.jeorgia[3].vida_inimigo, nivel.jeorgia[4].vida_inimigo, nivel.carlos[0].vida_inimigo,
                  nivel.carlos[1].vida_inimigo,
                  nivel.carlos[2].vida_inimigo, personagem.hitbox)

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    if nivel.f_7 == True:
        nivel.recarregar_f7()

    pygame.display.update()

def setima_fase(tela, fase_4, fase_1, personagem, combate):
    if nivel.marlei[0].muda_tela == True:
        tela.blit(fase_1_Fechada, (0, 0))
    else:
        if nivel.marlei[0].vida_inimigo <= 0:
            tela.blit(fase_4, (0, 0))
        else:
            tela.blit(fase_4_Fechada, (0, 0))

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_jogador_inimigo(nivel.marlei[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.espinho[0].muro)
        personagem.colisao_jogador_inimigo(nivel.espinho[1].muro)
        personagem.colisao_jogador_inimigo(nivel.espinho[2].muro_1)
        personagem.colisao_jogador_socao(nivel.marlei[0].socao_hitbox)
        for tiros in nivel.marlei[0].tiros:
            personagem.colisao_jogador_inimigo(tiros)
        personagem.hud_vida()


    nivel.espinho[0].desenhar()
    nivel.espinho[1].desenhar()
    nivel.espinho[2].desenhar_deitado()

    for marleis in nivel.marlei:
        marleis.desenhar()
        marleis.movimento_marlei()
        marleis.randomizador_ataques(personagem.hitbox)
        marleis.colisao_espada(combate.hitbox, combate.dano)
        marleis.atualiza_tiro()

    if nivel.marlei[0].vida_inimigo <=0:
        nivel.f_7 = False
        nivel.tela_vitoria = True
        nivel.cont_menu = 0

    personagem.morre()

    nivel.morre(personagem.morte)

    combate.morre(personagem.morte)

    pygame.display.update()

def tela_vitoria(tela):
    tela.blit(tela_ganhoui, (0, 0))

    nivel.cont_menu += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and nivel.cont_menu >= 300:
        nivel.tela_vitoria = False
        nivel.menu = True
        nivel.cont_menu = 0

    pygame.display.update()

while run:

    clock.tick(frame)  # roda o game loop 60 vezes em 1 segundo


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Detectar as Teclas
        elif event.type == pygame.KEYDOWN:
            # verifica se as setas foram apertadas e muda a velocidade
            if event.key == pygame.K_SPACE and cont > 80 and nivel.menu == False:  # limita a espada/ataque do jogador
                combate.hora_de_desenhar(cont)
                cont = 0  # zeramos para conseguir obter um timer de quando o jogador poderá utilizar a espada novamente
            if event.key == pygame.K_p:
                nivel.recarregar_f7()
                nivel.pular()




    if nivel.menu == True:
        tela_menu(tela)

    if nivel.creditos == True:
        tela_creditos(tela)

    if nivel.tela_morte ==  True:
        tela_morte(tela)

    if nivel.tela_tutorial == True:
        tela_tutorial_ta(tela)

    if nivel.f_1 == True:
        primeira_fase(tela, fase_1, personagem, combate)

    if nivel.f_2 == True:
        segunda_fase(tela, fase_1, personagem, combate)

    if nivel.f_3 == True:
        terceira_fase(tela, fase_2, personagem, combate)

    if nivel.f_4 == True:
        quarta_fase(tela, fase_2, personagem, combate)

    if nivel.f_5 == True:
        quinta_fase(tela, fase_3, personagem, combate)

    if nivel.f_6 == True:
        sexta_fase(tela, fase_3, personagem, combate)

    if nivel.f_7 == True:
        setima_fase(tela, fase_4, fase_1, personagem, combate)

    if nivel.tela_vitoria == True:
        tela_vitoria(tela)


    cont += 1  # incrementação do cont do ataque do jogador

pygame.quit()