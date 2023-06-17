# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:45:13 2023

@author: steta
"""

import cv2
import numpy as np

#carico l'immagine
imm = cv2.imread("wood_01.jpg")

#converto in scala di grigi e salvo l'immagine
imm_grigia = cv2.cvtColor(imm, cv2.COLOR_BGR2GRAY)
cv2.imwrite("imm_grigia.jpg", imm_grigia)

#applico il filtro e salvo l'immagine
imm_sfocata = cv2.blur(imm_grigia, (5, 5))
cv2.imwrite("imm_sfocata.jpg", imm_sfocata)

#mostro le 3 immagini
cv2.imshow("originale:", imm)
cv2.imshow("grigia:", imm_grigia)
cv2.imshow("sfocata:", imm_sfocata)
cv2.waitKey(0)
cv2.destroyAllWindows()


#le ultime 2 righe le inserisco altrimenti crasha l'applicazione quando eseguo il programma