import pygame
import random
import sys 

######################
#     CONSTANTES     #
######################
# Dimensiones de la ventana
ANCHO, ALTO = 800, 600

#FPS 
LaVelocidad=15


# Colores
Elcolor=(0, 255, 0) # Por defecto seraa verde
NEGRO = (0, 0, 0)
BLANCO= (255,255, 255)
#VERDE = (0, 255, 0)
#AMBAR = (255,126, 0)
#GRIS = (212,212,212)
#AZUL = (184,202,212)

# Lista de caracteres que caeran en la pantalla
caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()-_=+[]{}|;:'<>,.?/~`"
caracteres = list(caracteres)


# Lista para almacenar las posiciones Y de cada columna
TotalColumnas= ANCHO // 20

ypos =[random.randint(-100,200) for _ in range(TotalColumnas)] ## arreglo que guarla las posiciones y de todas las columnas
ind = 0  #  contador  inicia en 0

#########################
# Lectura de paraametros#
#########################
y = 1
if len(sys.argv) == 1:
    #t.color(col) 
    #clockjac()
    Elcolor=(0, 255, 0)
    LaVelocidad=15
else:
    for n in sys.argv:
        #print('n'+ n)
        #print(sys.argv[y])
        if n=="-c":
            #print('x =',sys.argv)
            h= (sys.argv[y]).lstrip('#')
            #print('h =',h)
            Elcolor=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
            #print('RGB =',Elcolor)

        elif  n=="-v":
            #print('x =',sys.argv)
            LaVelocidad =int(sys.argv[y])
            #print('veloc =',LaVelocidad)
        elif  n=="--help" :
            print("Modo de empleo:  [opciones]...")
            print("")           
            print("Programa de consola que genera una pantalla tipo matrix, Para eso utiliza la fuente \"Matrix Code NFI\"; la cual hay que instalar en el sistema.")
            print("")
            print("Las siguientes opciones activan una cuenta regresiva:")
            print("-c   Color de los caracteres, por defecto es VERDE")
            print("-v   Velocidad de la animacion por defecto 15 FPS")
            print("")
            print("Ejemplo:")
            print("")
            print("matrix -c \"#ff7e00\" 5 -v 10")
            print("Efecto matrix con caracteres color AMBAR y velocidad de 5 FPS")
            print("")
            
            exit();
        y=y+1





##############################
# Configuracin de la pantalla#
##############################
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Efecto Matrix")
reloj = pygame.time.Clock()
# Definicin de la fuente y tamao del texto
fuente = pygame.font.SysFont("Matrix Code NFI", 20)

#############################
#       Bucle principal     #
#############################
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
    # Actualizar la posicion de los caracteres en cada columna
    for y in ypos:

        x = ind * 20 # La posicion x depende del contador ind
        c=random.choice(caracteres) # se escoje aleatoriamente un caracter
        #c = str(x/10) + "," +str(y/10)
        #print (x , y, c, ind)        

        # A contiuacion se aplica un cuadrado semitransparente (canal alpha) para ir difuminando los caracteres desde arriba
        s = pygame.Surface((20,ALTO))  # tamano del cuadro
        s.set_alpha(50)                # nivel alpha
        s.fill(NEGRO)           # llena el cuadrado de color negro RGB(0,0,0)
        ventana.blit(s, (x,y-ALTO))    # coordenadas donde inicia el cuadrado alpha, le quito un poco de altura se ve mejor
       
        #Pinto un cuadro en negro para borrar el caracter blanco de inicio de columna
        s = pygame.Surface((20,20))  # tamano del cuadro
        #s.set_alpha(200)                # nivel alpha
        s.fill(NEGRO)           # llena el cuadrado de color negro RGB(0,0,0)
        ventana.blit(s, (x,y))    #
       
        #Pinta caracter actual
        caracter = fuente.render(c, False, Elcolor) # pinta caracter en color verde
        ventana.blit(caracter, (x , y)) # pinta caracter en color verde
       
     
       
        #Cuadrado para difumirar caracteres de mas abajo de la columna
        s = pygame.Surface((20,ALTO))  # tamano del cuadro
        s.set_alpha(50)                # nivel alpha
        s.fill(NEGRO)           # llena el cuadrado de color negro RGB(0,0,0)
        ventana.blit(s, (x,y+20))    # coordenadas donde inicia el cuadrado alpha, le quito un poco de altura se ve mejor
             
        if y > 100 + random.randint(1, 5000): # si la altura es mayor de 100, aleatoriamente puede volver a iniciar, es decir volver a la linea superior
            ypos[ind] = 0
        else:        
          #Pinto caracter blanco el inicio de la columna
            caracter2 = fuente.render(c, False, BLANCO) # pinta caracter en BLANCO
            ventana.blit(caracter2, (x , y+20)) # pinta caracter en color verde
            ypos[ind] = y + 20 # en caso contrario salte a una nueva linea hacia abajo 
           
       
        if ind < TotalColumnas-1: # control de la variable indicador, no debe pasarse del total de columnas
            ind=ind+1
           
        else:
           ind=0;
           

    pygame.display.flip()

    # Controlar la velocidad de la animacin
    reloj.tick(LaVelocidad)

pygame.quit()

