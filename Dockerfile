#python3 image install from docker hub
FROM python:3

#for optimization container 1 -> True
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#workdir is project Root derictory
WORKDIR /app

#copy dependencies in workdir
COPY requirements.txt /app/

#install dependencies
RUN pip install -r requirements.txt

#copy our project to workdir
COPY . /app/
#add 

