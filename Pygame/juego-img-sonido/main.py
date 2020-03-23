import pygame, random, sys
from pygame.locals import *
ANCHOVENTANA = 900
ALTOVENTANA = 900
COLORVENTANA = (255, 255, 255)
COLORTEXTO = (130, 130,130)
COLORFONDO = (0, 255, 255)
FPS = 40
TAMAÑOMINMISIL = 10
TAMAÑOMAXMISIL = 40
TAMAÑOMINNUBE = 50
TAMAÑOMAXNUBE = 90
VELOCIDADMINMISIL = 1
VELOCIDADMAXMISIL = 8
VELOCIDADMINNUBE = 1
VELOCIDADMAXNUBE = 3
TASANUEVOMISIL = 6
TASANUEVONUBE=12
TASAMOVIMIENTOJUGADOR = 5
def terminar():
  pygame.quit()
  sys.exit()
def esperarTeclaJugador():
  while True:
    for evento in pygame.event.get():
      if evento.type == QUIT:
        terminar()
      if evento.type == KEYDOWN:
        if evento.key == K_ESCAPE: # Quita al presionar ESCAPE
          terminar()
        return
def jugadorGolpeaMisil(rectanguloJugador, misiles):
  for v in misiles:
    if rectanguloJugador.colliderect(v['rect']):
      return True
  return False
def dibujarTexto(texto, font, superficie, x, y):
  objetotexto = font.render(texto, 1, COLORTEXTO)
  rectangulotexto = objetotexto.get_rect()
  rectangulotexto.topleft = (x, y)
  superficie.blit(objetotexto, rectangulotexto)
# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
pygame.display.set_caption('AprenderPython - InvaSion')
pygame.mouse.set_visible(False)
# establece los fonts
font = pygame.font.SysFont(None, 48)
# establece los sonidos
gameOverSound = pygame.mixer.Sound('juegoterminado.wav')
pygame.mixer.music.load('musicajuego.mp3')
# establece las imagenes
playerImage = pygame.image.load('war_cursovideojuegos-python_opt.png')
rectanguloJugador = playerImage.get_rect()
baddieImage = pygame.image.load('misil_cursovideojuegos-python_opt2.png')
nubeImage = pygame.image.load('nube-war_cursovideojuegos-python.png')
# Muestra la pantalla inicial
dibujarTexto('AprenderPython - InvaSion', font, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3))
dibujarTexto('Presione una tecla para comenzar el juego', font, superficieVentana, (ANCHOVENTANA / 3) - 180, (ALTOVENTANA / 3) + 50)
pygame.display.update()
esperarTeclaJugador()
puntajeMax = 0
while True:
  # establece el comienzo del juego
  misiles = []
  nubes = [] 
  puntaje = 0
  rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA - 50)
  moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
  trucoReversa = trucoLento = False
  contadorAgregarMisil = 0
  contadorAgregarNube = 0
  pygame.mixer.music.play(-1, 0.0)
  while True: # el ciclo del juego se mantiene mientras se este jugando
    puntaje += 1 # incrementa el puntaje
    for evento in pygame.event.get():
      if evento.type == QUIT:
        terminar()
      if evento.type == KEYDOWN:
        if evento.key == ord('z'):
          trucoReversa = True
        if evento.key == ord('x'):
          trucoLento = True
        if evento.key == K_LEFT or evento.key == ord('a'):
          moverDerecha = False
          moverIzquierda = True
        if evento.key == K_RIGHT or evento.key == ord('d'):
          moverIzquierda = False
          moverDerecha = True
        if evento.key == K_UP or evento.key == ord('w'):
          moverAbajo = False
          moverArriba = True
        if evento.key == K_DOWN or evento.key == ord('s'):
          moverArriba = False
          moverAbajo = True
      if evento.type == KEYUP:
       if evento.key == ord('z'):
          trucoReversa = False
          puntaje = 0
       if evento.key == ord('x'):
          trucoLento = False
          puntaje = 0
       if evento.key == K_ESCAPE:
          terminar()
       if evento.key == K_LEFT or evento.key == ord('a'):
         moverIzquierda = False
       if evento.key == K_RIGHT or evento.key == ord('d'):
         moverDerecha = False
       if evento.key == K_UP or evento.key == ord('w'):
         moverArriba = False
       if evento.key == K_DOWN or evento.key == ord('s'):
         moverAbajo = False
      if evento.type == MOUSEMOTION:
       # Si se mueve el ratón, este se mueve adonde el cursor esté.
        rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)
    # Añade misiles en la parte superior de la pantalla, de ser necesarios.
    if not trucoReversa and not trucoLento:
      contadorAgregarMisil += 1
    if contadorAgregarMisil == TASANUEVOMISIL:
      contadorAgregarMisil = 0
      baddieSize = random.randint(TAMAÑOMINMISIL, TAMAÑOMAXMISIL)
      newBaddie = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
      'speed': random.randint(VELOCIDADMINMISIL, VELOCIDADMAXMISIL),
      'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
      }
      misiles.append(newBaddie)
    # Añade nubes en la parte superior de la pantalla 
    if not trucoReversa and not trucoLento:
      contadorAgregarNube += 1 
    if contadorAgregarNube == TASANUEVONUBE:
      contadorAgregarNube = 0
      baddieSize1 = random.randint(TAMAÑOMINNUBE, TAMAÑOMAXNUBE)
      newBaddie1 = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize1), 0 - baddieSize1, baddieSize1, baddieSize1),
      'speed': random.randint(VELOCIDADMINNUBE, VELOCIDADMAXNUBE),
      'surface':pygame.transform.scale(nubeImage, (baddieSize1, baddieSize1)),
      }
      nubes.append(newBaddie1)
    # Mueve el jugador.
    if moverIzquierda and rectanguloJugador.left  > 0:
      rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
    if moverDerecha and rectanguloJugador.right < ANCHOVENTANA:
      rectanguloJugador.move_ip(TASAMOVIMIENTOJUGADOR, 0)
    if moverArriba and rectanguloJugador.top  > 0:
      rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
    if moverAbajo and rectanguloJugador.bottom < ALTOVENTANA:
      rectanguloJugador.move_ip(0, TASAMOVIMIENTOJUGADOR)
    # Mueve el cursor del ratón hacia el jugador.
    pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)
    # Mueve los misiles hacia abajo.
    for b in misiles:
      if not trucoReversa and not trucoLento:
        b['rect'].move_ip(0, b['speed'])
      elif trucoReversa:
        b['rect'].move_ip(0, -5)
      elif trucoLento:
        b['rect'].move_ip(0, 1)
    # Mueve las nubes hacia abajo.
    for b in nubes:
        b['rect'].move_ip(0, b['speed']) 
    # Elimina los misiles que han caido por debajo.
    for b in misiles[:]:
      if b['rect'].top > ALTOVENTANA:
        misiles.remove(b)
    # Elimina las nubes que han caido por debajo.
    for b in nubes[:]:
       if b['rect'].top > ALTOVENTANA:
          nubes.remove(b) 
    # Dibuja el mundo del juego en la ventana.
    superficieVentana.fill(COLORFONDO)
    # Dibuja el puntaje y el puntaje máximo
    dibujarTexto('Puntos: %s' % (puntaje), font, superficieVentana, 10, 0)
    dibujarTexto('Records: %s' % (puntajeMax), font, superficieVentana, 10, 40)
    # Dibuja el rectángulo del jugador
    superficieVentana.blit(playerImage, rectanguloJugador)
    # Dibuja cada misil
    for b in misiles:
      superficieVentana.blit(b['surface'], b['rect'])
    # Dibuja cada nube
    for b in nubes:
      superficieVentana.blit(b['surface'], b['rect']) 
    pygame.display.update()
    # Verifica si algún misil impactó en el jugador.
    if jugadorGolpeaMisil(rectanguloJugador, misiles):
      if puntaje > puntajeMax:
        puntajeMax = puntaje # Establece nuevo puntaje máximo
      break
    relojPrincipal.tick(FPS)
  # Frena el juego y muestra "Juego Terminado"
  pygame.mixer.music.stop()
  gameOverSound.play()
  dibujarTexto('Juego Terminado', font, superficieVentana, (ANCHOVENTANA / 3)-40, (ALTOVENTANA / 3))
  dibujarTexto('Presione una tecla para repetir.', font, superficieVentana, (ANCHOVENTANA / 3) - 150, (ALTOVENTANA / 3) + 50)
  pygame.display.update()
  esperarTeclaJugador()
  gameOverSound.stop()
  
  
  
  
  """  Detallamos el código del juego paso a paso:
Importamos los módulos

 import pygame, random, sys from pygame.locals import * 
Constantes del código

    ANCHOVENTANA = 900
    ALTOVENTANA = 900
    COLORVENTANA = (255, 255, 255)
    COLORTEXTO = (130, 130,130)
    COLORFONDO = (0, 255, 255)
    FPS = 40
    TAMAÑOMINMISIL = 10
    TAMAÑOMAXMISIL = 40
    TAMAÑOMINNUBE = 50
    TAMAÑOMAXNUBE = 90
    VELOCIDADMINMISIL = 1
    VELOCIDADMAXMISIL = 8
    VELOCIDADMINNUBE = 1
    VELOCIDADMAXNUBE = 3
    TASANUEVOMISIL = 6
    TASANUEVONUBE=12
    TASAMOVIMIENTOJUGADOR = 5

Estas constantes su propio nombre indica que hacen, solo comentar la FPS que es la velocidad del juego (frame per second)
Funciones del juego:

    def terminar():
      pygame.quit()
      sys.exit()

Pygame requiere que llames a pygame.quit() y sys.exit() por lo que las colocamos en lfunción terminar por comodidad.

 

    def esperarTeclaJugador():
      while True:
        for evento in pygame.event.get():

Funcion para crear la pausa del juego

         if evento.type == QUIT:
           terminar()

Este if se usa si el jugardor cierra la ventana y se llama a la función terminar

          if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE: # Sale del juego al presionar ESCAPE
              terminar()
            return

Si hay un KEYDOWN se chequea si pulsa escape para salir sino pues sigue igual

    def jugadorGolpeaMisil(rectanguloJugador, misiles):
       for v in misiles:
           if rectanguloJugador.colliderect(v['rect']):
             return True
       return False

Esta función devuelve true si hay colision enre el jugardor y los misiles y false si no hay colision. Misiles es una lista de estructuras que contiene un ‘rect’
que representa el tamaño y ubicacion del misil.
Rectangulo jugador tambien es un objeto ‘rect’. Estos objetos rect tienen el metodo ‘colliderect()’ (colision) que devuelve True o false como parametro en el caso de colisiom

El for está continuamente iterando para detectar si hay colision.

    def dibujarTexto(texto, font, superficie, x, y):
      objetotexto = font.render(texto, 1, COLORTEXTO)
      rectangulotexto = objetotexto.get_rect()
      rectangulotexto.topleft = (x, y)
      superficie.blit(objetotexto, rectangulotexto)

Para dibujar texto hay que seguir estos pasos. Llamamos al método render y se crea un objeto para dibujar el texto.
También necesitas saber el tamaño y la ubicación del objeto Surface, para ello hacemos uso del método get_rect de la clase surface.  Ahora se cambia la ubicacion del objeto Rect dando una nuevo valor de tupla para su atributo topleft.

El objeto Surface de dibuja con la ultima linea. Para mostrar un texto en Pygame hay que seguir estos pasos ya que no es tan simple como la funcion print.

 
Iniciando el juego

    # establece un pygame, la ventana y el cursor del ratón
    pygame.init()
    relojPrincipal = pygame.time.Clock()

pygame.init() esta es la funcion principal y esta ‘relojPrincipal = pygame.time.Clock()’ nos ayudara a controlar la velocidad del juego

    superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))

Se crea un objeto surface a partir de una tupla de dos enteros

    pygame.display.set_caption('AprenderPython - InvaSion')

Se añade el título a la ventana creada

    pygame.mouse.set_visible(False)

Ocultamos el cursor del ratón

    gameOverSound = pygame.mixer.Sound('juegoterminado.wav')
    pygame.mixer.music.load('musicajuego.mp3')

Con el objeto Sound añadimos la musica de cuando el jugador pierde mientras que la fondo seguira sonando. La funcion ‘pygame.mixer.Sound’
guarda una referencia a este objeto para ser ejecutada en el tiempo oportuno. La funcion ‘pygame.mixer.music.load()’ no devuelve ningun objeto solo carga la musica de fondo.

    playerImage = pygame.image.load('war_cursovideojuegos-python_opt.png')
    rectanguloJugador = playerImage.get_rect()
    baddieImage = pygame.image.load('misil_cursovideojuegos-python_opt2.png')
    nubeImage = pygame.image.load('nube-war_cursovideojuegos-python.png')

Con pygame.image.load cargamos las imagenes del juego

 
Pantalla de juego

    dibujarTexto('AprenderPython - InvaSion', font, superficieVentana, (ANCHOVENTANA / 3), (ALTOVENTANA / 3))
    dibujarTexto('Presione una tecla para comenzar el juego', font, superficieVentana, (ANCHOVENTANA / 3) - 180, (ALTOVENTANA / 3) + 50)
    pygame.display.update() 
    esperarTeclaJugador()

Con la funcion dibujarTexto escribimos el nombre del juego y le decimos como empezar a jugar, para ello le pasamos a la funcion
el texto, la fuente el objeto Surface donde dibujar y las coordenadas X e Y.
La funcion esperarTeclaJugador() deja el juego en pausa hasta nuevo evento

    puntajeMax = 0
    while True:
      # establece el comienzo del juego
      nubes = []
      misiles = []
      puntaje = 0

Establecemos el record del juego con un valor de 0, este despues se ira acumulando en cada partida.
El bucle while es un bucle infinito del juego el cual empezara de nuevo en cada partida del juego
Al principio misiles es una lista vacia aunque esta lista de objetos dispones de:
-‘rect’ = este objeto describe la posicion y el tamaño del misil
-‘velocidad’
-‘superficie’ = el objeto Surface que dibuja la imagen del misil devuelto por pygame.display.set_mode().

     rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA - 50)
     moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
     trucoReversa = trucoLento = False
     contadorAgregarMisil = 0
     contadorAgregarNube = 0
     pygame.mixer.music.play(10, 0.0)

Situamos el jugador en el centro inferior de la pantalla y se asigna false a los trucos y a otros movimientos para que el jugador empieze en el centro.

Tambien hemos puesto un contador de misiles para incrementar el nº de misiles en la pantalla.

La última línea ejecuta la música
Bucle de juego

El juego va a tiempo real por lo que debe actualizarse constantemente.

     while True: # el ciclo del juego se mantiene mientras se este jugando
       puntaje += 1 # incrementa el puntaje
     
       for evento in pygame.event.get():
         if evento.type == QUIT:
           terminar()

En el while se inicia el bucle y el puntuaje se va acumulando. Hay varios eventos en el juego y esta funcion devuelve una lista de los objetos Event ‘pygame.event.get()’. A contunuacion el if comprueba el atributo del evento y si es QUIT se termina el juego (el usuario ha cerrado el juego).

    if evento.type == KEYDOWN:
     if evento.key == ord('z'):
     trucoReversa = True
     if evento.key == ord('x'):
     trucoLento = True
     if evento.key == K_LEFT or evento.key == ord('a'):
     moverDerecha = False
     moverIzquierda = True
     if evento.key == K_RIGHT or evento.key == ord('d'):
     moverIzquierda = False
     moverDerecha = True
     if evento.key == K_UP or evento.key == ord('w'):
     moverAbajo = False
     moverArriba = True
     if evento.key == K_DOWN or evento.key == ord('s'):
     moverArriba = False
     moverAbajo = True
     
     if evento.type == KEYUP:
     if evento.key == ord('z'):
     trucoReversa = False
     puntaje = 0
     if evento.key == ord('x'):
     trucoLento = False
     puntaje = 0

Para los eventos KEYDOWN el jugador ha pulsado el teclado y con la funcion ‘ord()’ podemos saber que tecla es. Dependiendo
de la tecla que sea pasamos un valor false o true a otra funcion como trucos o movimientos.

El evento KEYUP se crea cuando el jugador suelta la tecla pulsada de ahí que el código tenga casi la misma parte repetida cambiando KEYDOWN por KEYUP

       if evento.key == K_ESCAPE:
       terminar()

De igual modo tenmos K_ESCAPE que se llama a la funcion terminar.

     if evento.key == K_LEFT or evento.key == ord('a'):
     moverIzquierda = False
     if evento.key == K_RIGHT or evento.key == ord('d'):
     moverDerecha = False
     if evento.key == K_UP or evento.key == ord('w'):
     moverArriba = False
     if evento.key == K_DOWN or evento.key == ord('s'):
     moverAbajo = False

La nave puede moverse pulsando las flechas del teclado o de igual modo con las letras de ‘a’, ‘d’, ‘w’ y ‘s’.

       if evento.type == MOUSEMOTION:
         # Si se mueve el ratón, este se mueve adonde el cursor esté.
          rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)

La nave, en este juego no solo se mueve con las teclas sino tambien con el raton. Este evento es el movimiento del raton. El metodo move_ip() para los objetos Rect modifica la posicion del objeto Rect en pixeles.
Añadiendo misiles y nubes

     if not trucoReversa and not trucoLento:
       contadorAgregarMisil += 1
     if contadorAgregarMisil == TASANUEVOMISIL:
       contadorAgregarMisil = 0
       baddieSize = random.randint(TAMAÑOMINMISIL, TAMAÑOMAXMISIL)
       newBaddie = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
       'speed': random.randint(VELOCIDADMINMISIL, VELOCIDADMAXMISIL),
       'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
       }
     
     misiles.append(newBaddie)
     # Añade nubes en la parte superior de la pantalla 
     if not trucoReversa and not trucoLento:
     contadorAgregarNube += 1 
     if contadorAgregarNube == TASANUEVONUBE:
     contadorAgregarNube = 0
     baddieSize1 = random.randint(TAMAÑOMINNUBE, TAMAÑOMAXNUBE)
     newBaddie1 = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize1), 0 - baddieSize1, baddieSize1, baddieSize1),
     'speed': random.randint(VELOCIDADMINNUBE, VELOCIDADMAXNUBE),
     'surface':pygame.transform.scale(nubeImage, (baddieSize1, baddieSize1)),
     }
     nubes.append(newBaddie1)

Leyendo el codigo podeis ver que se van agregando misiles en cada iteracion a exepcion si se tiene el truco activado.
El tamaño de los nuevos misiles es aleatorio entre los valores min y max. Se crea la nueva estructura con claves ‘rect’, ‘velocidad’,
y ‘superficie’. Asi la funcion pygame.Rect crea el misil bajo los parametros dados.
La última línea (‘ misiles.append(newBaddie)’) agrega el misil creado a la lista.

Idem con las nubes

     # Mueve el jugador.
     if moverIzquierda and rectanguloJugador.left &amp;gt; 0:
       rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
     if moverDerecha and rectanguloJugador.right &amp;lt; ANCHOVENTANA:
       rectanguloJugador.move_ip(TASAMOVIMIENTOJUGADOR, 0)
     if moverArriba and rectanguloJugador.top &amp;gt; 0:
       rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
     if moverAbajo and rectanguloJugador.bottom &amp;lt; ALTOVENTANA:
       rectanguloJugador.move_ip(0, TASAMOVIMIENTOJUGADOR)
     
     # Mueve el cursor del ratón hacia el jugador.
     pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery) 

Para mover al jugador se usa el mismo metodo antes comentado move_ip(). La función pygame.mouse.set_pos mueve el cursor del ratón
a la posición del jugador.

     # Mueve los misiles hacia abajo.
     for b in misiles:
        if not trucoReversa and not trucoLento:
           b['rect'].move_ip(0, b['speed'])
        elif trucoReversa:
           b['rect'].move_ip(0, -5)
        elif trucoLento:
           b['rect'].move_ip(0, 1)
     # Mueve las nubes hacia abajo.
     for b in nubes:
     b['rect'].move_ip(0, b['speed']) 
     # Elimina los misiles que han caido por debajo.
     for b in misiles[:]:
       if b['rect'].top &amp;gt; ALTOVENTANA:
          misiles.remove(b)
     # Elimina las nubes que han caido por debajo.
     for b in nubes[:]:
     if b['rect'].top &amp;gt; ALTOVENTANA:
     nubes.remove(b) 

En este primer for tenemos la implementacion de como se mueven los misles hacia abajo y del truco con el mismo método move_ip.
Los misiles que queden por debajo de la ventana tienen que ser eliminados de la lista, pero no iteramos sobre esa misma lista sino que hacemos una copia.
Si el atributo b[‘rect’].top es mayor que el ALTOVENTANA quitamos ese misil.

Idem para las nubes

     # Dibuja el mundo del juego en la ventana.
     superficieVentana.fill(COLORFONDO)
     
     # Dibuja el puntaje y el puntaje máximo
     dibujarTexto('Puntos: %s' % (puntaje), font, superficieVentana, 10, 0)
     dibujarTexto('Records: %s' % (puntajeMax), font, superficieVentana, 10, 40)
     
     # Dibuja el rectángulo del jugador
     superficieVentana.blit(playerImage, rectanguloJugador)
     # Dibuja cada misil
     for b in misiles:
       superficieVentana.blit(b['surface'], b['rect'])
     # Dibuja cada nube
     for b in nubes:
     superficieVentana.blit(b['surface'], b['rect']) 
     
     
     pygame.display.update()

A continuación añadimos el fondo del juego, los textos, jugador, misiles y nubes para hacer el dibujo de esta superficie con
pygame.display.update().
Como se detectan las colisiones

     # Verifica si algún misil impactó en el jugador.
     if jugadorGolpeaMisil(rectanguloJugador, misiles):
        if puntaje &amp;gt; puntajeMax:
            puntajeMax = puntaje # Establece nuevo puntaje máximo
        break
     
     relojPrincipal.tick(FPS)

Con la función jugadorGolpeaMisil que devuelve un boleano (true o false). En el caso de colision se actualiza el puntuaje
y se sale del juego.
Con relojPrincipal.tick(FPS) controlamos la velocidad del juego
Última pantalla “Game over / Fin de juego”

     # Frena el juego y muestra "Juego Terminado"
     pygame.mixer.music.stop()
     gameOverSound.play()
     
     dibujarTexto('Juego Terminado', font, superficieVentana, (ANCHOVENTANA / 3)-40, (ALTOVENTANA / 3))
     dibujarTexto('Presione una tecla para repetir.', font, superficieVentana, (ANCHOVENTANA / 3) - 150, (ALTOVENTANA / 3) + 50)
     pygame.display.update()
     esperarTeclaJugador()
     
     gameOverSound.stop()

Si el jugador pierde se para la música y se reproduce la música fin de juego. Con esta función avisamos al jugador que ha terminado y le decimos como puede seguir jugando."""
