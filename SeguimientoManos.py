import math
import cv2
import mediapipe as mp
import time

class detectormanos():
	def __init__(self, mode=False, maxManos = 2, modelComplexity=1, Confdeteccion = 0.5, Confsegui = 0.5):
		self.mode = mode #Crar objeto y esta será su propia variable
		self.maxManos=maxManos #Lo mismo haremos con todos los objetos
		self.modelComplexity = modelComplexity
		self.Confdeteccion = Confdeteccion
		self.Confsegui = Confsegui
	
		#Creamos los objetos que identifican las manos y las dibujan
		self.mpmanos = mp.solutions.hands
		self.manos = self.mpmanos.Hands(self.mode, self.maxManos, self.modelComplexity, self.Confdeteccion, self.Confsegui)
		self.dibujo = mp.solutions.drawing_utils
		self.tip = [4,8,12,16,20] #Detectar abrir y cerrar mano y los dedos que levantamos

	#FUNCION ENCONTRAR MANOS
	def encontrarmanos(self, frame, dibujar = True):
		imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		self.resultados = self.manos.process(imgcolor)

		if self.resultados.multi_hand_landmarks:
			for mano in self.resultados.multi_hand_landmarks:
				if dibujar:
					self.dibujo.draw_landmarks(frame, mano, self.mpmanos.HAND_CONNECTIONS)
		return frame

	#FUNCION ENCONTRAR POSICION
	def encontrarposicion(self, frame, ManoNum = 0, dibujar = True):
		xlista=[]
		ylista=[]
		bbox=[]
		self.lista = []
		if self.resultados.multi_hand_landmarks:
			miMano = self.resultados.multi_hand_landmarks[ManoNum]
			for id, lm in enumerate(miMano.landmark):
				alto, ancho, c = frame.shape #Extraemos las dimensiones de los fps
				cx, cy = int(lm.x * ancho), int(lm.y * alto) #Convertimos la info en pixeles
				xlista.append(cx)
				ylista.append(cy)
				self.lista.append([id, cx, cy])
				if dibujar:
					cv2.circle(frame, (cx, cy), 5, (0,0,0), cv2.FILLED)
			
			xmin, xmax = min(xlista), max(xlista)
			ymin, ymax = min(ylista), max(ylista)
			bbox = xmin, ymin, xmax, ymax
			if dibujar:
				cv2.rectangle(frame,(xmin - 20, ymin-20), (xmax + 20, ymax + 20), (0,255,0), 2)
		return self.lista, bbox

	#FUNCION PARA DETECTAR Y DIBUJAR DEDOS ARRIBA
	def dedosarriba(self):
		dedos=[]
		if self.lista[self.tip[0]][1] > self.lista[self.tip[0]-1][1]:
			dedos.append(1)
		else:
			dedos.append(0)

		for id in range (1,5):
			if self.lista[self.tip[id]][2] < self.lista[self.tip[id]-2][2]:
				dedos.append(1)
			else:
				dedos.append(0)

		return dedos

	#FUNCION PARA DETECTAR LA DISTANCIA ENTRE DEDOS
	def distancia(self, p1, p2, frame, dibujar = True, r = 15, t=3):
		x1, y1 = self.lista[p1][1:]
		x2, y2 = self.lista[p2][1:]
		cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
		if dibujar:
			cv2.line(frame, (x1,y1), (x2,y2), (0,0,255), t)
			cv2.circle(frame, (x1, y1), r, (0,0,255), cv2.FILLED)
			cv2.circle(frame, (x2, y2), r, (0,0,255), cv2.FILLED)
			cv2.circle(frame, (cx, cy), r, (0,0,255), cv2.FILLED)
		length = math.hypot(x2-x1, y2-y1)

		return length, frame, [x1, y1, x2, y2, cx, cy]

#FUNCION PRICIPAL AL FIN
def main():
	ptiempo=0
	ctiempo = 0

	#Leer la camara web
	cap = cv2.VideoCapture(0)
	#Creamos el objeto
	detector = detectormanos()
	#Realizar deteccion de manos
	while True:
		ret, frame = cap.read()
		#Una vez que obtengamos la imagen la enviamos
		frame = detector.encontrarmanos(frame)
		lista, bbox =detector.encontrarposicion(frame)
		if len (lista) != 0:
			print(lista[4])
		#MOSTRAMOS LOS FPS
		ctiempo = time.time()
		fps = 1 / (ctiempo - ptiempo)
		ptiempo =ctiempo

		cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

		cv2.imshow("Manos", frame)
		k = cv2.waitKey(1)

		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()