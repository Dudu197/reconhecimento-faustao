import face_recognition
import pickle
import os.path
from os import listdir
from os.path import isfile, join
print("Iniciando treino")

dataset = "dataset.dat"
imagens_treino = "treino/"
rostos = []

if os.path.isfile(dataset):
	print("Dataset já existente, adicionando dados aos já existentes")
else:
	print("Dataset inexistente, um novo arquivo será criado")

arquivos = [f for f in listdir(imagens_treino) if isfile(join(imagens_treino, f))]

for arquivo in arquivos:
	print("Treinando " + arquivo)
	imagem = face_recognition.load_image_file(imagens_treino + arquivo)
	encodings = face_recognition.face_encodings(imagem)
	print(str(len(encodings)) + " rosto(s) encontrado(s)")
	for encoding in encodings:
		rostos.append(encoding)

print("Salvando dados treinados")



arquivo_dataset = open(dataset, 'wb')
pickle.dump(rostos, arquivo_dataset)
arquivo_dataset.close()

print("Treino conculuido com sucesso")
print(str(len(rostos)) + " rosto(s) encontrado(s)")



