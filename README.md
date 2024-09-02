# Notes

## Building and running docker file

### Build with dockerfile
`docker build --build-arg NODE_VERSION=22 -t ezekieltoh/cfdsa-fortune:v1.0 .`
- `-t`: tag


### List all images
`docker image ls`

### Push docker image
`docker push ezekieltoh/cfdsa-fortune:v1.0`

### Run docker image
`docker run -d -p 8080:3000 [-e APP_PORT=3000] [--name myapp] ezekieltoh/cfdsa-fortune:v1.0`

### List docker containers
`docker container ls -a`

### Enter docker container
`docker exec -ti <container-id> /bin/sh`

### Container metadata
`docker container inspect <container-id>`

### Container logs
`docker logs <container-id>`

## Networks and volumes

`docker volume create data-vol`
`docker network create mynet`

### Run the mysql database
```
docker run -d \
  --mount type=volume,src=data-vol,dst=/var/lib/mysql \
  --network mynet \
  --name mydb
  mysql:8
```

### Run the app to connect to the database
```
docker run -d -p 8080:3000 \
  --network mynet \
  -e DB_HOST=mydb \
  mywebapp:v1
```


