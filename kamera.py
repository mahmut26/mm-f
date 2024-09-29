import cv2
import numpy as np
import face_recognition
import os

import webbrowser


video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_locations = []
face_encodings = []
face_names = []
known_person=[]
known_image=[]
known_face_encoding=[]

for file in os.listdir("friends"):
    try:
        #Extracting person name from the image filename eg: david.jpg
        known_person.append(file.replace(".jpg", ""))
        file=os.path.join("friends/", file)
        known_image = face_recognition.load_image_file(file)
        known_face_encoding.append(face_recognition.face_encodings(known_image)[0])
    except Exception as e:
        pass


while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for face_encoding in face_encodings:

        match = face_recognition.compare_faces(known_face_encoding, face_encoding)
        matches = np.where(match)[0]
        if len(matches) > 0:
            name = str(known_person[matches[0]])
            print("I see someone named {}!".format(name))

            if 'ma' in name:
                exec(open("dosyama.py").read())
                exit()





            elif 'biden' in name:
                exec(open("biden.py").read())
                quit()

                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    quit()
                video_capture.release()
                cv2.destroyAllWindows()





