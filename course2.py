import pytesseract
from PIL import Image
import os
import cv2
import sys
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
            #print(voices[1].id)
engine.setProperty('voice', voices[0].id) # you can change to female voice just by replacing 0 by 1 in voices[0].



pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# text=pytesseract.image_to_string(img)
# print(text)

a=input("Enter Video Name:")
# Read the video from specified path
vid = cv2.VideoCapture(a)

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('text'):
        os.makedirs('text')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')
    

# frame
currentframe = 0

while currentframe<=900:

    # reading from frame
    success, frame = vid.read()

    if  currentframe%100==0:
        # continue creating images until video remains
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imshow('Output',frame)
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
    elif cv2.waitKey(1) and 0xFF==ord('q'):
        break
    
   
    currentframe += 1
def speak(audio):
                engine.say(audio)
                engine.runAndWait()
# Release all space and windows once done
for i in os.listdir('data'):
            print(str(i))
            my_example=Image.open('data'+"/"+i)
            text=pytesseract.image_to_string(my_example,lang='eng')
            print(text)
            speak(text)
            

            
            
            file=open('./text/'+str(i)+'.txt','w')
            file.write(text)

vid.release()
cv2.destroyAllWindows()
