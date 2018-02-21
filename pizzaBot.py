import pyautogui as pyg
import time

pyg.PAUSE = 1.5
pizzaURL = "bit.ly/113thHousingSurvey"

pyg.click(468, 842)
for i in range(10):
	pyg.hotkey('ctrl', 't')
	pyg.typewrite(pizzaURL + '\n')
	pyg.click(483, 590)
	pyg.press('pagedown')
	pyg.click(483, 161)
	pyg.click(485, 586)
	pyg.press('pagedown')
	pyg.click(516, 727)
	pyg.hotkey('ctrl', 'w')

