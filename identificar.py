import face_recognition
import pickle
import cv2
import sys


caminho_dataset = "dataset.dat"

arquivo = open(caminho_dataset, 'rb')
dataset = pickle.load(arquivo)
arquivo.close()

for  i in range(1, len(sys.argv)):
	print("Analisando a imagem " + sys.argv[i])
	imagem = face_recognition.load_image_file(sys.argv[i])
	frame = cv2.imread(sys.argv[i])

	face_locations = face_recognition.face_locations(imagem)
	encodings = face_recognition.face_encodings(imagem)
	quantidade = 0
	rostos = []
	for j, face_encoding in enumerate(encodings):
		matches = face_recognition.compare_faces(dataset, face_encoding)
		if True in matches:
			rostos.append(face_locations[j])

	quantidade = 0
	for (top, right, bottom, left) in rostos:
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

	cv2.imshow('image', frame)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	input("Press Enter to continue...")
