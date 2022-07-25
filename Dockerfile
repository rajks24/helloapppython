FROM python:3.9-slim-bullseye

LABEL name="Helloapppython"
LABEL version="1.0"
LABEL description="The Helloapp with features to test devops and k8s clusters"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=0
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# pip modules determined from 'pip freeze' during local development
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN  pip install --upgrade pip
RUN set -ex \
    && pip install -r requirements.txt

COPY . /app

# default docker port to expose, '-p' flag is used to same effect
EXPOSE 8000

# Launch gunicorn
CMD [ "/opt/venv/bin/gunicorn", "--bind", ":8000", "--workers", "3", "app:app" ]
