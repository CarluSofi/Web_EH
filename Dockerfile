# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8


# Allows docker to cache installed dependencies between builds
RUN python -m pip install --upgrade pip==24.0
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

WORKDIR /holmes_web/holmes_web

# Mounts the application code to the image
COPY . /holmes_web

EXPOSE 8000

WORKDIR /holmes_web

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]