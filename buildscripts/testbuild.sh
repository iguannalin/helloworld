docker kill $(docker ps -q)
docker build -t app .
docker run -p 8083:8080 --net=mynet --ip=10.0.0.20 -e IP=10.0.0.20 -e PORT=8080 -d app
