FROM python:3.6.1
COPY . /app/roomba600_open_interface/
WORKDIR /app/roomba600_open_interface/
RUN pip install -r requirements.txt
CMD [ "python", "./client.py" ]