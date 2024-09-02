FROM golang:1.23-alpine3.20 AS builder

WORKDIR /src

COPY go.* .
COPY main.go .

RUN go build -o main main.go

# container to run the application
FROM alpine:3.20

LABEL maintainer="Ezekiel"

WORKDIR /app

# copy the binary from the build container
COPY --from=builder /src/main .
COPY public public
COPY templates templates

ENV PORT=3000 INSTANCE_NAME=my-dov-bear INSTANCE_HASH=abcd1234

EXPOSE ${PORT}

ENTRYPOINT /app/main

