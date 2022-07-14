FROM python:3.8-slim-buster
USER root

# Install system level dependencies
RUN apt-get update &&\
    apt-get install\
    ffmpeg\
    gcc\
    git-all\
    libsm6\
    libxext6\
    musl-dev\
    nano\
    nginx\
    python3-dev\
    python3-pip\
    systemd\
    unzip\
    wget\
    zip\
    -y\
    && apt-get autoremove -y\
    && apt-get clean -y\
    && rm -rf /var/lib/apt/lists/*

# copy nginx configuration file, pip requirements, and entrypoint to be used when starting Docker container
ADD nginx_host /etc/nginx/sites-enabled/default
ADD entrypoint.sh /entrypoint.sh
ADD config.py /app/config.py
ADD app/requirements.txt /app/requirements.txt

# install pip and dependencies
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && python3 -m pip install -U pip \
    && python3 -m pip install -r /app/requirements.txt \
	&& rm get-pip.py

# copy app to be used when starting Docker container, and set permissions
COPY ./app /app
RUN chmod +x entrypoint.sh && chmod -R 755 /app

EXPOSE 80
WORKDIR /app
CMD  ["/entrypoint.sh"]
