import random
import pgzrun
from pgzero.actor import Actor
from pgzero.loaders import sounds

background = Actor('background')
plastico = Actor('plastico')
vidro = Actor('vidro')
metal = Actor('metal')
papel = Actor('papel')
confirm = Actor('vazio')
atores = [plastico, vidro, metal, papel]
ator_ativo = random.choice(atores)
ator_ativo.topright = 0, 10
life = 3

WIDTH = 480
HEIGHT = 180

def draw():
    screen.clear()
    background.draw()
    ator_ativo.draw()
    confirm.draw()
    pontuacao(score)
    vidas(life)

def pontuacao(score):
    screen.draw.text(
        "Pontos:" +str(int(score)),
        (10, 105),  # posição
        color=(0, 0, 0),
    )

def vidas(life):
    screen.draw.text(
        "Vidas:" + str(int(life)),
        (400, 105),  # posição
        color=(0, 0, 0),
    )
    if life > 0:
        screen.draw.text(
            "Clique no resíduo quando ele passar sobre o coletor correto!",
            (45, 135),  # posição
            color=(255, 255, 255),
            fontsize=20,
        )
    else:
        screen.draw.text(
            "Pressione R para reiniciar o jogo!",
            (140, 135),  # posição
            color=(255, 255, 255),
            fontsize=20,
        )

def update():
    if life > 0:
        ator_ativo.left += 2
        if ator_ativo.left > WIDTH:
            ator_ativo.right = 0
            resetar_ator()

score = 0

def on_mouse_down(pos):
    global score
    global life
    if ator_ativo.collidepoint(pos):
        x, y = pos
        print(x, y)
        print(ator_ativo.image)
        if (ator_ativo.image == ('plastico')):
            if (x <= 120):
                set_confirm('check')
                score += 1
                pontuacao(score)
                print(score)
            else:
                life -= 1
                set_confirm('erro')
                vidas(life)
                print(life)

        if (ator_ativo.image == ('vidro')):
            if (x > 120 and x <= 240):
                set_confirm('check')
                score += 1
                pontuacao(score)
                print(score)
            else:
                life -= 1
                set_confirm('erro')
                vidas(life)
                print(life)

        if (ator_ativo.image == ('metal')):
            if (x > 240 and x <= 346):
                set_confirm('check')
                score += 1
                pontuacao(score)
                print(score)
            else:
                life -= 1
                set_confirm('erro')
                vidas(life)
                print(life)

        if (ator_ativo.image == ('papel')):
            if (x >= 380):
                set_confirm('check')
                score += 1
                pontuacao(score)
                print(score)
            else:
                life -= 1
                set_confirm('erro')
                vidas(life)
                print(life)


def set_confirm(img):
    global ator_ativo
    print(ator_ativo.image)
    confirm.pos = ator_ativo.pos
    confirm.image = img
    if (img == 'check'):
        sounds.check.play()
    else:
        sounds.erro.play()

    if (life <= 0):
        background.image = 'gameover'
        ator_ativo.image = 'vazio'
        confirm.image = 'vazio'
        screen.draw.text(
            #"Clique no resíduo quando ele passar sobre o coletor correto!",
            "Pressione R para reiniciar o jogo!",
            (45, 135),  # posição
            color=(255, 255, 255),
            fontsize=20,
        )
        print('jogo finalizado')
    else:
        clock.schedule(resetar_ator, 0.3)

def criar_ator_ativo():
    # cria um ator novo a cada vez
    return Actor(random.choice(['plastico', 'vidro', 'metal', 'papel']), pos=(0,50))

def resetar_ator():
    global ator_ativo
    confirm.image = 'vazio'
    if(life <=0):
        return
    ator_ativo = criar_ator_ativo()

def reiniciar_jogo():
    global score, life, ator_ativo, confirm, background
    score = 0
    life = 3
    ator_ativo = random.choice(atores)
    ator_ativo.pos = 0, 50
    confirm.image = 'vazio'
    background.image = 'background'
    ator_ativo = criar_ator_ativo()

def on_key_down(key):
    if key == keys.R:
        reiniciar_jogo()

pgzrun.go()

