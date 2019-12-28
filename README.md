# Rpi - Docker - FacialRecognition
_How to run easily the face recognition on Raspberry with the help of Docker*

All **congrats for M. Marcelo** who has done the dev, I've just put that in container.

https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826

X11 externalized, means you have the graphical output from your docker ;)

## Pre-requisite
- Raspberry min 3
- docker installed and running with the *pi* user
- camera up and running

## Easy Run
After have cloned the repository localy (`git clone https://github.com/guillain/Rpi-Docker-FacialReco.git`)
and enter in the new directory (`cd Rpi-Docker-FacialReco`), execute the following commands:

1/ create your dataset with your face: `./run 01_face_dataset.py`
  - enter the index corresponding to the person to recognize
  - place the faceof this person in front of your camera to take 30 pictures as reference for the recognition
  - to run for each face to identify

2/ train and create model: `./run 02_face_training.py`
  - based on the previous pictures, the model will be trained
  
3/ run the recognition: `./run 03_face_recognition.py`
  - to have the name of th person on the picture according to the index, thanks to update the script (sorry)
  - run the facial recognition in live
  
## Toplay with OpenCV
- `./run` ... and jump in the container to play with
 
## Support
- Original post:
  - https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
  - https://github.com/Mjrovai/OpenCV-Face-Recognition
- Raspberry: https://www.raspberrypi.org
- Docker: https://www.docker.com
- OpenCV: https://opencv.org
- OpenCV image: https://hub.docker.com/r/sgtwilko/rpi-raspbian-opencv/

