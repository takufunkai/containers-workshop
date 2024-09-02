FROM node:22

WORKDIR /app

COPY main.js .
COPY package.json .
COPY package-lock.json .
COPY public public
COPY views views

RUN npm ci

ENV PORT=3000 INSTANCE_NAME="Ezekiel's app" INSTANCE_HASH=270999

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
	CMD curl -s localhost:${PORT}/healthz || exit 1

EXPOSE ${PORT}

ENTRYPOINT node main.js
