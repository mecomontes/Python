"""La programación modular es un paradigma o estilo de programación que consiste en dividir un programa 
muy grande en programas de menor tamaño o subprogramas con la finalidad de hacerlo mas legible y manejable
 ya que, durante el desarrollo de un programa, el mismo puede tornarse muy largo. Para esto se implementa 
 el uso de clases, funciones y módulos.

Un módulo es un objeto que sirve como unidad para organizar el código de un proyecto desarrollado en Python. 
Los módulos tienen en su contenido los objetos (funciones, clases, definiciones, etc) que se definan en él.
 Para utilizar el contenido de un módulo es necesario importarlo.


Importar módulos en Python

Para que el contenido de un módulo esté disponible en otro, es necesario importarlo. La forma mas utilizada 
para importar en Python es con la palabra reservada import.

    import modulo    # En 'modulo' se escribe el nombre del módulo que vaya a ser importado

Es necesario que, en el directorio del módulo, se encuentre un archivo llamado ‘__init__.py’. Este es necesario
 para que Python trate los directorios que contienen los archivos como paquetes. Esto previene que los directorios
 con nombres comunes, como ‘string’, oculten involuntariamente los módulos válidos que aparecen más adelante en la 
 ruta de búsqueda del módulo. En el peor de los casos, ‘__init__.py’ puede estar vacío.

Un Paquete es una estructura de organización de Python que contiene módulos y otros paquetes.
‘from’

‘from’ es una palabra reservada que es utilizada en conjunto con ‘import’ para importar partes específicas
 de un paquete o módulo.

    from time import Time  # Importa la función 'Time' del módulo 'time'

Contenido de los Módulos en Python

Para mostrar todas las funciones a las que se pueden acceder en un módulo, se puede usar la siguiente linea de código:

    import modulo # Se sustituye "modulo" por el módulo que vaya a ser importado realmente
    print(dir(modulo)) # Se sustituye "modulo" por el nombre del módulo importado

En el caso de importar un modulo real, la salida sería la siguiente (se importará y mostrará el módulo
 ‘pygame’ y su contenido):

    ['ACTIVEEVENT', 'ANYFORMAT', 'ASYNCBLIT', 'AUDIODEVICEADDED', 'AUDIODEVICEREMOVED', 'AUDIO_ALLOW_ANY_CHANGE',
    'AUDIO_ALLOW_CHANNELS_CHANGE', 'AUDIO_ALLOW_FORMAT_CHANGE', 'AUDIO_ALLOW_FREQUENCY_CHANGE', 'AUDIO_S16', 
    'AUDIO_S16LSB', 'AUDIO_S16MSB', 'AUDIO_S16SYS', 'AUDIO_S8', 'AUDIO_U16', 'AUDIO_U16LSB', 'AUDIO_U16MSB', 
    'AUDIO_U16SYS', 'AUDIO_U8', 'BIG_ENDIAN', 'BLEND_ADD', 'BLEND_MAX', 'BLEND_MIN', 'BLEND_MULT', 'BLEND_PREMULTIPLIED', 
    'BLEND_RGBA_ADD', 'BLEND_RGBA_MAX', 'BLEND_RGBA_MIN', 'BLEND_RGBA_MULT', 'BLEND_RGBA_SUB', 'BLEND_RGB_ADD',
    'BLEND_RGB_MAX', 'BLEND_RGB_MIN', 'BLEND_RGB_MULT', 'BLEND_RGB_SUB', 'BLEND_SUB', 'BUTTON_LEFT', 'BUTTON_MIDDLE',
    'BUTTON_RIGHT', 'BUTTON_WHEELDOWN', 'BUTTON_WHEELUP', 'BUTTON_X1', 'BUTTON_X2', 'BufferError', 'BufferProxy', 
    'Color', 'DOUBLEBUF', 'DROPBEGIN', 'DROPCOMPLETE', 'DROPFILE', 'DROPTEXT', 'FINGERDOWN', 'FINGERMOTION',
    'FINGERUP', 'FULLSCREEN', 'GL_ACCELERATED_VISUAL', 'GL_ACCUM_ALPHA_SIZE', 'GL_ACCUM_BLUE_SIZE', 
    'GL_ACCUM_GREEN_SIZE', 'GL_ACCUM_RED_SIZE', 'GL_ALPHA_SIZE', 'GL_BLUE_SIZE', 'GL_BUFFER_SIZE', 'GL_DEPTH_SIZE', 
    'GL_DOUBLEBUFFER', 'GL_GREEN_SIZE', 'GL_MULTISAMPLEBUFFERS', 'GL_MULTISAMPLESAMPLES', 'GL_RED_SIZE', 
    'GL_STENCIL_SIZE', 'GL_STEREO', 'GL_SWAP_CONTROL', 'HAT_CENTERED', 'HAT_DOWN', 'HAT_LEFT', 'HAT_LEFTDOWN', 
    'HAT_LEFTUP', 'HAT_RIGHT', 'HAT_RIGHTDOWN', 'HAT_RIGHTUP', 'HAT_UP', 'HAVE_NEWBUF', 'HWACCEL', 'HWPALETTE',
    'HWSURFACE', 'IYUV_OVERLAY', 'JOYAXISMOTION', 'JOYBALLMOTION', 'JOYBUTTONDOWN', 'JOYBUTTONUP', 'JOYHATMOTION',
    'KEYDOWN', 'KEYUP', 'KMOD_ALT', 'KMOD_CAPS', 'KMOD_CTRL', 'KMOD_LALT', 'KMOD_LCTRL', 'KMOD_LMETA', 'KMOD_LSHIFT',
    'KMOD_META', 'KMOD_MODE', 'KMOD_NONE', 'KMOD_NUM', 'KMOD_RALT', 'KMOD_RCTRL', 'KMOD_RMETA', 'KMOD_RSHIFT', 
    'KMOD_SHIFT', 'K_0', 'K_1', 'K_2', 'K_3', 'K_4', 'K_5', 'K_6', 'K_7', 'K_8', 'K_9', 'K_AMPERSAND', 'K_ASTERISK', 
    'K_AT', 'K_BACKQUOTE', 'K_BACKSLASH', 'K_BACKSPACE', 'K_BREAK', 'K_CAPSLOCK', 'K_CARET', 'K_CLEAR', 'K_COLON', 
    'K_COMMA', 'K_DELETE', 'K_DOLLAR', 'K_DOWN', 'K_END', 'K_EQUALS', 'K_ESCAPE', 'K_EURO', 'K_EXCLAIM', 'K_F1', 
    'K_F10', 'K_F11', 'K_F12', 'K_F13', 'K_F14', 'K_F15', 'K_F2', 'K_F3', 'K_F4', 'K_F5', 'K_F6', 'K_F7', 'K_F8', 
    'K_F9', 'K_FIRST', 'K_GREATER', 'K_HASH', 'K_HELP', 'K_HOME', 'K_INSERT', 'K_KP0', 'K_KP1', 'K_KP2', 'K_KP3', 
    'K_KP4', 'K_KP5', 'K_KP6', 'K_KP7', 'K_KP8', 'K_KP9', 'K_KP_DIVIDE', 'K_KP_ENTER', 'K_KP_EQUALS', 'K_KP_MINUS', 
    'K_KP_MULTIPLY', 'K_KP_PERIOD', 'K_KP_PLUS', 'K_LALT', 'K_LAST', 'K_LCTRL', 'K_LEFT', 'K_LEFTBRACKET', 
    'K_LEFTPAREN', 'K_LESS', 'K_LMETA', 'K_LSHIFT', 'K_LSUPER', 'K_MENU', 'K_MINUS', 'K_MODE', 'K_NUMLOCK',
    'K_PAGEDOWN', 'K_PAGEUP', 'K_PAUSE', 'K_PERIOD', 'K_PLUS', 'K_POWER', 'K_PRINT', 'K_QUESTION',
    'K_QUOTE', 'K_QUOTEDBL', 'K_RALT', 'K_RCTRL', 'K_RETURN', 'K_RIGHT', 'K_RIGHTBRACKET', 'K_RIGHTPAREN', 
    'K_RMETA', 'K_RSHIFT', 'K_RSUPER', 'K_SCROLLOCK', 'K_SEMICOLON', 'K_SLASH', 'K_SPACE', 'K_SYSREQ', 'K_TAB', 
    'K_UNDERSCORE', 'K_UNKNOWN', 'K_UP', 'K_a', 'K_b', 'K_c', 'K_d', 'K_e', 'K_f', 'K_g', 'K_h', 'K_i', 'K_j', 
    'K_k', 'K_l', 'K_m', 'K_n', 'K_o', 'K_p', 'K_q', 'K_r', 'K_s', 'K_t', 'K_u', 'K_v', 'K_w', 'K_x', 'K_y', 'K_z',
    'LIL_ENDIAN', 'MOUSEBUTTONDOWN', 'MOUSEBUTTONUP', 'MOUSEMOTION', 'MOUSEWHEEL', 'MULTIGESTURE', 'Mask', 'NOEVENT',
    'NOFRAME', 'NUMEVENTS', 'OPENGL', 'OPENGLBLIT', 'Overlay', 'PREALLOC', 'PixelArray', 'PygameVersion', 'QUIT',
    'RESIZABLE', 'RLEACCEL', 'RLEACCELOK', 'Rect', 'SCRAP_BMP', 'SCRAP_CLIPBOARD', 'SCRAP_PBM', 'SCRAP_PPM', 
    'SCRAP_SELECTION', 'SCRAP_TEXT', 'SRCALPHA', 'SRCCOLORKEY', 'SWSURFACE', 'SYSWMEVENT', 'Surface', 'SurfaceType', 
    'TEXTEDITING', 'TEXTINPUT', 'TIMER_RESOLUTION', 'USEREVENT', 'USEREVENT_DROPFILE', 'UYVY_OVERLAY', 'VIDEOEXPOSE',
    'VIDEORESIZE', 'Vector2', 'Vector3', 'WINDOWEVENT', 'WINDOWEVENT_CLOSE', 'YUY2_OVERLAY', 'YV12_OVERLAY', 
    'YVYU_OVERLAY', '__builtins__', '__cached__', '__color_constructor', '__color_reduce', '__doc__', '__file__',
    '__loader__', '__name__', '__package__', '__path__', '__rect_constructor', '__rect_reduce', '__spec__',
    '__version__', 'base', 'bufferproxy', 'cdrom', 'color', 'colordict', 'compat', 'constants', 'cursors', 
    'display', 'draw', 'encode_file_path', 'encode_string', 'error', 'event', 'fastevent', 'font',
    'get_array_interface', 'get_error', 'get_init', 'get_sdl_byteorder', 'get_sdl_version', 'image', 
    'init', 'joystick', 'key', 'mask', 'math', 'mixer', 'mixer_music', 'mouse', 'movie', 'overlay', 
    'packager_imports', 'pixelarray', 'pixelcopy', 'quit', 'rect', 'register_quit', 'rev', 'rwobject',
    'scrap', 'segfault', 'set_error', 'sndarray', 'sprite', 'surface', 'surfarray', 'sysfont', 'threads',
    'time', 'transform', 'ver', 'vernum', 'version', 'warn_unwanted_files']

Estas son todas las funciones y variables disponibles del modulo ‘pygame‘. Cabe destacar que para cada módulo se 
tendrá una salida distinta.


Crear un Módulo en Python

Se crea un archivo con el nombre que uno desee (el nombre se escoge generalmente según el contenido del archivo) 
y dentro del archivo se coloca el contenido que vaya a ser utilizado en el programa base. Por ejemplo, se
 creará una función para calcular la raíz cuadrada de un número y las raíces de un polinomio cuadrático 
 en un archivo llamado “raices.py”:

    def raizCuadrada(i):  # Función que calcula la raíz cuadrada de un número
      return i**(1/2)
    def raices(a,b,c):  # Función que calcula las raíces de un polinomio cuadrático
      return ((-b+raiz(b**2-(4*a*c)))/(2*a)),((-b-raiz(b**2-(4*a*c)))/(2*a))

Se importan la funciones en el programa base de la siguiente forma:"""

import raices  # Importa el módulo 'raices'
A = float(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = float(input("Ingrese el coeficiente de la variable lineal\n"))
C = float(input("Ingrese el término independiente\n"))
r1 = 0
r2 = 0
r1,r2 = raices.raizCuadratico(A,B,C) # Llamado a la función 'raices' del módulo 'raices'
print(f"La primera raíz es: {r1}") 
print(f"La segunda raíz es: {r2}")

#Ya que se importó el módulo ‘raices’, para hacer un llamado a una función de este módulo, hay que utilizar 
#como prefijo al nombre de la función, el nombre del modulo (raices.raices).

#Una practica mas sencilla es importar todos los elementos pertenecientes al módulo ‘raices’ utilizando ‘from’ 
#de la siguiente forma:

#from raices import raiz, raizCuadrada

#De esta forma, los llamados a la función ‘raices’ ya no necesitan utilizar como prefijo el nombre del 
#módulo al cual pertenecen:

from raices import raices, raizCuadrada
A = float(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = float(input("Ingrese el coeficiente de la variable lineal\n"))
C = float(input("Ingrese el término independiente\n"))
r1 = 0
r2 = 0
r1,r2 = raices(A,B,C) # Llamado a la función sin el prefijo del módulo
print(f"La primera raiz es: {r1}") 
print(f"La segunda raiz es: {r2}")
