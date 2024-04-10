FROM python:3.10

COPY Projet_Flask/ /src

WORKDIR /src

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

CMD ["python3", "script_app.py"]
