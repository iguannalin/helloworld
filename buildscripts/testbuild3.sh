docker run -p 8085:8080 --net=mynet --ip=10.0.0.22 -e IP=10.0.0.22 -e PORT=8080 -e MAINIP=10.0.0.20:8080 -d app
