#For cam activation

"""import cv2
cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    cv2.imshow('Linkedin article',frame)
    cv2.waitKey(1)"""

""""#Knowing the face

import cv2
import mediapipe as mp #To detect the face and the eyes

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

while True:
    _,frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert video into different color
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    print(landmark_points)
    cv2.imshow('Linkedin article',frame)
    cv2.waitKey(1)"""

# Show the landmarks on the face

"""import cv2
import mediapipe as mp #To detect the face and the eyes

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()

while True:
    _,frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert video into different color
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark #landmark the first face
        for landmark in landmarks:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0,0,255)) #where, the center, the radius, the color
            print(x,y)
    print(landmark_points)
    cv2.imshow('Linkedin article',frame)
    cv2.waitKey(1)"""

# Detect the eyes only

"""import cv2
import mediapipe as mp #To detect the face and the eyes

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

while True:
    _,frame = cam.read()
    frame = cv2.flip(frame,1) #Pour changer la position de l'eoil detecté, sinon j'aurais le droite au lieu du gauche
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert video into different color
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark #landmark the first face
        for landmark in landmarks[474:478]: #detect a range of index (# you can detect only one of the eyes)
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0,0,255)) #where, the center, the radius, the color
            print(x,y)
    print(landmark_points)
    cv2.imshow('Linkedin article',frame)
    cv2.waitKey(1)"""

#

"""import cv2
import mediapipe as mp #To detect the face and the eyes
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _,frame = cam.read()
    frame = cv2.flip(frame,1) #Pour changer la position de l'eoil detecté, sinon j'aurais le droite au lieu du gauche
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert video into different color
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark #landmark the first face
        for id, landmark in enumerate(landmarks[474:478]): #enumerate for index and it's landmarks
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0,0,255)) #where, the center, the radius, the color
            if id == 1:
                screen_x = screen_w/ frame_w * x
                screen_y = screen_h/ frame_h * y
                pyautogui.moveTo(screen_x,screen_y)  #To help the cursos move anywhere in the screen

            print(x,y)
    print(landmark_points)
    cv2.imshow('Linkedin article',frame)
    cv2.waitKey(1)"""

#Detect the blonk operation

"""import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]] #the land marks for the other eye
        for landmark in left: #
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (255, 0, 255))
        if (left[0].y - left[1].y) < 0.004: #Calculate the position of the 2 points,if they are really close we will put as closed so we do actions
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Project', frame)
    cv2.waitKey(1)"""

import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 2, (250,250,160))
            if id == 1:
                screen_x = int(screen_w * landmark.x)
                screen_y = int(screen_h * landmark.y)
                pyautogui.moveTo(screen_x, screen_y)
        right = [landmarks[145], landmarks[159]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 5, (0,0,255))
        if(right[0].y - right[1].y ) < 0.01:
            pyautogui.click()
            pyautogui.sleep(2)
    cv2.imshow('Eye Project', frame)
    cv2.waitKey(1)




