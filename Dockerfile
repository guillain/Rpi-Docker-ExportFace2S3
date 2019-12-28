FROM sgtwilko/rpi-raspbian-opencv:latest
#FROM mohaseeb/raspberrypi3-python-opencv:latest

RUN pip install boto3

RUN pip install awscli

RUN pip install pillow 

CMD ["/bin/bash"]
 
