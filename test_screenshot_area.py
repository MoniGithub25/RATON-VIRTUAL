import cv2
import numpy as np
import pyautogui

while True:
	screenshot = pyautogui.screenshot(region=(200,100, 660, 450))
	screenshot = np.array(screenshot)
	screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
	cv2.imshow("screenshot", screenshot)
	if cv2.waitKey(1) & 0XFF ==27:
		break
cv2.destroyAllWindows()