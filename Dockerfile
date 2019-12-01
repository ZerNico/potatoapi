FROM python:3.7-alpine

# Set environment varibles
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update --no-cache postgresql-client zlib-dev jpeg-dev libwebp-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libffi-dev libc-dev linux-headers postgresql-dev

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install pipenv gunicorn django pipenv-to-requirements
RUN pipenv run pipenv_to_requirements
RUN pip install -r requirements.txt
#RUN pipenv install
RUN apk del .tmp-build-deps

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.1/wait /wait
RUN chmod +x /wait

# Create user for execution
RUN adduser -D user
RUN chmod +x /app/entrypoint.sh && chown user:user -R /app
USER user

ENTRYPOINT ["sh", "entrypoint.sh"]
