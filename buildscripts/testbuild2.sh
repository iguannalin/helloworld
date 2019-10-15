docker run -p 8084:8080 --net=mynet --ip=10.0.0.21 -e IP=10.0.0.21 -e PORT=8080 -e MAINIP=10.0.0.20:8080 -d app
