import face_recognition
import pickle
import sys

caminho_dataset = "dataset.dat"

arquivo = open(caminho_dataset, 'rb')
dataset = pickle.load(arquivo)
arquivo.close()

for  i in range(1, len(sys.argv)):
	print("Analisando a imagem " + sys.argv[i])
	imagem = face_recognition.load_image_file(sys.argv[i])
	encodings = face_recognition.face_encodings(imagem)
	quantidade = 0

	for encoding in encodings:
		matches = face_recognition.compare_faces(dataset, encoding)
		try:
		    matches.index(True)
		    quantidade += 1
		except ValueError:
			pass
	if quantidade == 0:
		print("Nenhum Faustão encontrado")
	else:
		if quantidade == 1:
			print("Orra meu, sou eu!")
		else:
			print("Orra meu, quantos Faustões nesta foto, " + str(quantidade) + " Faustões")