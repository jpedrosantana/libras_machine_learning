#Bibliotecas utilizadas
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

# Carregamento do arquivo criado no jupyter notebook
with np.load(file='knn_data_libras.npz') as dados:
    print(dados.files)
    treino_recuperado = dados['treino']
    treino_recuperado_labels = dados['treino_labels']

knn = cv2.ml.KNearest_create()
knn.train(treino_recuperado, cv2.ml.ROW_SAMPLE, treino_recuperado_labels)


# Definir area a ser rastreada
x, y, w, h = 30, 80, 200, 250
track_window = (x, y, w, h)

camera = cv2.VideoCapture(0)
res = ''

while True:
    time.sleep(0.1)
    ret, frame = camera.read()
    if res == '':
        res = '???'
    
    x,y,w,h = track_window
    imagem = cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 3) #Desenha o retângulo de 200x250
    cv2.putText(imagem,res,(250,450),cv2.FONT_HERSHEY_SIMPLEX,1.0,(11,255,255),2)
    cv2.imshow('LIBRAS', imagem)

    k = cv2.waitKey(10)

    #Corta a Imagem
    imagem_cortada = imagem[y:y+h, x:x+w]

    #Prepara Imagem
    imagem_pb = cv2.cvtColor(imagem_cortada, cv2.COLOR_BGR2GRAY)
    retmi, threshmi = cv2.threshold(imagem_pb,55,200,cv2.THRESH_BINARY) #Talvez precise ajustar o Thresh dependendo da luminosidade e ruido de fundo
    imagens_teste = np.array(threshmi).reshape(-1,50000).astype(np.float32) #Transforma a imagem em array para o teste
    cv2.imshow('BINARIO', threshmi) #Criação de uma janela para visualizar a binarização da imagem

    #Teste
    ret, res, viz, dist = knn.findNearest(imagens_teste, k=3)

    #Atribuição dos labels numéricos para letras
    viz, res = viz.astype(str), res.astype(str)
    viz[viz == '0.0'], res[res == '0.0'] = 'A', 'A' 
    viz[viz == '1.0'], res[res == '1.0'] = 'B', 'B'
    viz[viz == '2.0'], res[res == '2.0'] = 'C', 'C'
    
    res = str(res)[3]
       

    
    if k == 27: # esc para fechar
        break

camera.release()
cv2.destroyAllWindows()
