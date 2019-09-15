FROM alpine:3.10

# Install dependencies
RUN apk add --update --no-cache rsync inotify-tools sshpass openssh

# Setup directory structure
RUN mkdir /app /public
WORKDIR /app
COPY . /app

# Create user for execution
RUN adduser -D user
RUN chmod +x /app/entrypoint.sh && chown user:user /app
USER user

ENTRYPOINT ["sh", "entrypoint.sh"]
