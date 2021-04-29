import cv2
import numpy as np
import os
import string

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists("data/train"):
    os.makedirs("data/train")
if not os.path.exists("data/test"):
    os.makedirs("data/test")
for i in range(10):
    if not os.path.exists("data/train/" + str(i)):
        os.makedirs("data/train/"+str(i))
    if not os.path.exists("data/test/" + str(i)):
        os.makedirs("data/test/"+str(i))

for i in string.ascii_uppercase:
    if not os.path.exists("data/train/" + i):
        os.makedirs("data/train/"+i)
    if not os.path.exists("data/test/" + i):
        os.makedirs("data/test/"+i)
    

mode = 'train'
directory = 'data/'+mode+'/'
minValue = 70

cap = cv2.VideoCapture(0)
interrupt = -1  

while True:
    _, frame = cap.read()
    
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {
             # 'zero': len(os.listdir(directory+"/0")),
             # 'one': len(os.listdir(directory+"/1")),
             # 'two': len(os.listdir(directory+"/2")),
             # 'three': len(os.listdir(directory+"/3")),
             # 'four': len(os.listdir(directory+"/4")),
             # 'five': len(os.listdir(directory+"/5")),
             # 'six': len(os.listdir(directory+"/6")),
             # 'seven': len(os.listdir(directory+"/7")),
             # 'eight': len(os.listdir(directory+"/8")),
             # 'nine': len(os.listdir(directory+"/9")),
             'a': len(os.listdir(directory+"/A")),
             'b': len(os.listdir(directory+"/B")),
             'c': len(os.listdir(directory+"/C")),
             'd': len(os.listdir(directory+"/D")),
             'e': len(os.listdir(directory+"/E")),
             'f': len(os.listdir(directory+"/F")),
             'g': len(os.listdir(directory+"/G")),
             'h': len(os.listdir(directory+"/H")),
             'i': len(os.listdir(directory+"/I")),
             'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/K")),
             'l': len(os.listdir(directory+"/L")),
             'm': len(os.listdir(directory+"/M")),
             'n': len(os.listdir(directory+"/N")),
             'o': len(os.listdir(directory+"/O")),
             'p': len(os.listdir(directory+"/P")),
             'q': len(os.listdir(directory+"/Q")),
             'r': len(os.listdir(directory+"/R")),
             's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/T")),
             'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/Y")),
             'z': len(os.listdir(directory+"/Z"))
             }
    
    # Printing the count in each set to the screen
    # cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "IMAGE COUNT", (10, ), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "0 : "+str(count['zero']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "1 : "+str(count['one']), (10, 85), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "2 : "+str(count['two']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "3 : "+str(count['three']), (10, 115), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "4 : "+str(count['four']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "5 : "+str(count['five']), (10, 145), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "6 : "+str(count['six']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "7 : "+str(count['seven']), (10, 175), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "8 : "+str(count['eight']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    # cv2.putText(frame, "9 : "+str(count['nine']), (10, 205), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "a : "+str(count['a']), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "b : "+str(count['b']), (10, 85), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "c : "+str(count['c']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "d : "+str(count['d']), (10, 115), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "e : "+str(count['e']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "f : "+str(count['f']), (10, 145), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "g : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "h : "+str(count['h']), (10, 175), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "i : "+str(count['i']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "j : "+str(count['j']), (10, 205), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "k : "+str(count['k']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "l : "+str(count['l']), (10, 235), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "m : "+str(count['m']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "n : "+str(count['n']), (90, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "o : "+str(count['o']), (90, 85), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "p : "+str(count['p']), (90, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "q : "+str(count['q']), (90, 115), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "r : "+str(count['r']), (90, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "s : "+str(count['s']), (90, 145), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "t : "+str(count['t']), (90, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "u : "+str(count['u']), (90, 175), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "v : "+str(count['v']), (90, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "w : "+str(count['w']), (90, 205), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "x : "+str(count['x']), (90, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "y : "+str(count['y']), (90, 235), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "z : "+str(count['z']), (90, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    
    # Drawing the ROI
    cv2.rectangle(frame, (220-1, 9), (620+1, 419), (255,0,0) ,1)
    
    # Extracting the ROI
    roi = frame[10:410, 220:520]
    
    cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray,(5,5),2)
    
    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, test_image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
      
    test_image = cv2.resize(test_image, (300,300))
    cv2.imshow("test", test_image)
        

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    # if interrupt & 0xFF == ord('0'):
    #     cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    # if interrupt & 0xFF == ord('1'):
    #     cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    # if interrupt & 0xFF == ord('2'):
    #     cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)       
    # if interrupt & 0xFF == ord('3'):
    #     cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    # if interrupt & 0xFF == ord('4'):
    #     cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    # if interrupt & 0xFF == ord('5'):
    #     cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
    # if interrupt & 0xFF == ord('6'):
    #     cv2.imwrite(directory+'6/'+str(count['six'])+'.jpg', roi)
    # if interrupt & 0xFF == ord('7'):
    #     cv2.imwrite(directory+'7/'+str(count['seven'])+'.jpg', roi)   
    # if interrupt & 0xFF == ord('8'):
    #     cv2.imwrite(directory+'8/'+str(count['eight'])+'.jpg', roi)   
    # if interrupt & 0xFF == ord('9'):
    #     cv2.imwrite(directory+'9/'+str(count['nine'])+'.jpg', roi)  
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'A/'+str(count['a'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'B/'+str(count['b'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'C/'+str(count['c'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'D/'+str(count['d'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'E/'+str(count['e'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'F/'+str(count['f'])+'.jpg', roi)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'G/'+str(count['g'])+'.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'H/'+str(count['h'])+'.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'I/'+str(count['i'])+'.jpg', roi)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'J/'+str(count['j'])+'.jpg', roi)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'K/'+str(count['k'])+'.jpg', roi)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'L/'+str(count['l'])+'.jpg', roi)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'M/'+str(count['m'])+'.jpg', roi)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'N/'+str(count['n'])+'.jpg', roi)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'O/'+str(count['o'])+'.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'P/'+str(count['p'])+'.jpg', roi)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'Q/'+str(count['q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'R/'+str(count['r'])+'.jpg', roi)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'S/'+str(count['s'])+'.jpg', roi)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'T/'+str(count['t'])+'.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'U/'+str(count['u'])+'.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'V/'+str(count['v'])+'.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'W/'+str(count['w'])+'.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'X/'+str(count['x'])+'.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'Y/'+str(count['y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'Z/'+str(count['z'])+'.jpg', roi)        
    
cap.release()
cv2.destroyAllWindows()
