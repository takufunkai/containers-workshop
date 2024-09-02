FROM node:22

WORKDIR /app

COPY main.js .
COPY package.json .
COPY package-lock.json .
COPY public public
COPY views views

RUN npm ci

ENV PORT=3000 
ENV INSTANCE_NAME="Ezekiel's app"
ENV INSTANCE_HASH=420079 

EXPOSE ${PORT}

ENTRYPOINT node main.js
