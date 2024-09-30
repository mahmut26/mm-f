import RPi.GPIO as GPIO
import face_recognition
import picamera
import numpy as np
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(17,GPIO.OUT)

GPIO.output(17,0)
while True:
ifGPIO.input(23)==1:
whileGPIO.input(23)==0:
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

face_locations = []
face_encodings = []
face_names = []

known_person=[]
known_image=[]
known_face_encoding=[]

for file in os.listdir("kullanicilar"):
try:
known_person.append(file.replace(".jpg", ""))
file=os.path.join("kullanicilar/", file)
known_image = face_recognition.load_image_file(file)
known_face_encoding.append(face_recognition.face_encodings(known_image)[0])
exceptException as e:
pass
while True:

camera.capture(output, format="rgb")
face_locations = face_recognition.face_locations(output)
face_encodings = face_recognition.face_encodings(output, face_locations)
forface_encoding in face_encodings:
						
match = face_recognition.compare_faces(known_face_encoding, face_encoding)
matches=np.where(match)[0] #Checking whichimage is matched
							
iflen(matches)>0:
name = str(known_person[matches[0]])
print("I seesomeonenamed {}!".format(name))
if '1' in name:
GPIO.output(17,1)
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./1.sh')
										
elif '2' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./2.sh')

elif '3' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./3.sh')

elif '4' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./4.sh')

elif '5' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./5.sh')

elif '6' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./6.sh')

elif '7' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./7.sh')

elif '8' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./8.sh')

elif '9' in name:
GPIO.output(17,1)
										
camera.close()
os.system("cd /home/ayna/Desktop")
os.system('./9.sh')




