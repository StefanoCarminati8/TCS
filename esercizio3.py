# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 15:03:04 2023

@author: steta
"""

import cv2

#carico l'immagine
imm3 = cv2.imread("wood_02.jpg")

#applico il canny edge detection
listelle = cv2.Canny(imm3, 50, 150)
cv2.imwrite("listelle.jpg", listelle)

#converto in scala di grigi 
imm_grigia3 = cv2.cvtColor(imm3, cv2.COLOR_BGR2GRAY)

#applico il canny edge detection, stavolta all'immagine grigia
listelle_grigio = cv2.Canny(imm_grigia3, 50, 150)
cv2.imwrite("listelle_grigio.jpg", listelle_grigio)


#mostro le immagini e confronto il risultato per ciascuno dei due metodi
cv2.imshow("originale", imm3)
cv2.imshow("listelle", listelle)
cv2.imshow("listelle_grigio", listelle_grigio)

cv2.waitKey(0)
cv2.destroyAllWindows()

#le ultime 2 righe le inserisco altrimenti crasha l'applicazione quando eseguo il programma





