FROM sgtwilko/rpi-raspbian-opencv:latest
#FROM mohaseeb/raspberrypi3-python-opencv:latest

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["/bin/bash"]
 
