FROM python:3.11-slim as builder

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends

# install requirements
COPY ./requirements.txt .
RUN pip3 install --upgrade --no-cache-dir pip
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /home/code
COPY . /home/code

# EXPOSE $DJANGO_PORT

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# /dev/shm is mapped to shared memory and should be used for gunicorn heartbeat
# this will improve performance and avoid random freezes
# CMD ["gunicorn","-b", "0.0.0.0:8000", "-w", "4", "-k", "gevent", "--worker-tmp-dir", "/dev/shm", "--chdir", "config config.wsgi:application"]

#CMD ["python", "/job_seeker_data/entrypoint.py"]

# for build image use these structure
# sudo docker build --build-arg requirement_file=production.txt --no-cache -t job_seeker_production:latest -f Dockerfile .