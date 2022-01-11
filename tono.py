from pynput import keyboard as kb
import pyglet

def numero(tecla):
    tec = str(tecla)
    tec = tec.replace("'", " ")
    if tecla == kb.KeyCode.from_char('0'):
        music = pyglet.resource.media('t0.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('1'):
        music = pyglet.resource.media('t1.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('2'):
        music = pyglet.resource.media('t2.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('3'):
        music = pyglet.resource.media('t3.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('4'):
        music = pyglet.resource.media('t4.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('5'):
        music = pyglet.resource.media('t5.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('6'):
        music = pyglet.resource.media('t6.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('7'):
        music = pyglet.resource.media('t7.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('8'):
        music = pyglet.resource.media('t8.wav')
        music.play()
        print(tec, end="", flush=True)
    elif tecla == kb.KeyCode.from_char('9'):
        music = pyglet.resource.media('t9.wav')
        music.play()
        print(tec, end="", flush=True)
    else:
        return False

def sonar():
    with kb.Listener(numero) as LS:
        LS.join()

