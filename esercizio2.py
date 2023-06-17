# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:56:01 2023

@author: steta
"""

import cv2
import numpy as np

#carico l'immagine
imm2 = cv2.imread("wood_04.jpg")

#converto in scala di grigi e salvo l'immagine
imm_grigia2 = cv2.cvtColor(imm2, cv2.COLOR_BGR2GRAY)
cv2.imwrite("imm_grigia2.jpg", imm_grigia2)

#applico un filtro di sharpening e salvo l'immagine

sharpening_kernel = np.array([[-1, -1, -1],
                              [-1, 9, .1],
                              [-1, -1, -1]])
imm_sharp2 = cv2.filter2D(imm_grigia2, -1, sharpening_kernel)
cv2.imwrite("imm_sharp2.jpg", imm_sharp2)

#mostro le immagini
cv2.imshow("originale:", imm2)
cv2.imshow("grigia:", imm_grigia2)
cv2.imshow("sharp:", imm_sharp2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#le ultime 2 righe le inserisco altrimenti crasha l'applicazione quando eseguo il programma