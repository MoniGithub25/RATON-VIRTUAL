# RATON-VIRTUAL
En este programa voy a utilizar Mediapipe como medio de reconocimiento de mi mano para cumplir con la función de raton. Lo primero que debo hacer es crear una clase (class) y definir las funciones para localizar la mano y los dedos de la mano.
Más concretamente hemos definido: encontrar manos, encontrar posicion, función para detectar y dibujar dedos arriba, función para detectar la distancia entre dedos y por ultimo la funcion principar que activa la camara y te detecta la mano.
Una vez creado este programa que define todo lo que necesitamos que detecte de la mano, la importamos en nuestro nuevo programa en la que le indicamos que es lo que tiene que hacer. En este nuevo programa importaré una nueva librería que se encargará de manipular el mouse y usaremos opencv para la detección general
Cuando tenga arriba el nodo 8 (dedo indice) el ratón se moverá y cuando el nodo 8 y 12 esten juntos hará click. Acordarse de suavizar la latencia para que el ratón virtual sea más preciso.

![NODOS](https://user-images.githubusercontent.com/111430658/187067350-467d4831-77ba-4828-a1b1-474c2c91b632.PNG)

![image](https://user-images.githubusercontent.com/111430658/187068659-0e03a04e-8d00-410f-b0bf-830d6e4688c6.png)

# JUEGO RATON VIRTUAL
Una vez que ya he usado mediapipe una vez para hacer un raton quería sseguir explorando poryectos con esta librería. Encontré la idea de jugar al SUPPER BABBLE SHOOTER (https://poki.com/es/g/super-bubble-shooter) con la mano, haciendo este la funcion de ratón. Esta vez los nodos usados son el 0, 9 y 8 (ver en la imagen anterior).
Lo primero que hacemos es usar un programa de testeo para tener solo una captura de la zona en la que se juega el juego SUPER BABBLE SHOOTER y después con esos valores, empezamos a hacer el programa principal definiendo la variables de los puntos de la pantalla. Hacemos las funciones necesarias para que nuestro programa se realice: funcion en la que se calcula la distancia, funcion de detección de los dedos, función de deteccion de cuando los dedos bajan y por ultimo con with ponemos los parametros necesarior para que se puedea dectarnos y después mientras eso se produzca que se active la videocamara para detectar la mano (solo te detectara una porque se ha puesto un max de deteccion de una mano) y en esa misma funcion definimos que cuando bajamos los dedos (más concretamente el del nodo 8) se produzca un click.

