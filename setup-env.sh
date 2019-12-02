#docker build . -t ypsomed/bluetoothlib -f ./Dockerfile
docker build . -t ypsomed/bluetoothlib_daemon -f ./Dockerfile-Build-Daemon
docker run --name bluetoothlib_daemon -p 7776:22 -p 7777:7777 -v /Users/stefan/CLionProjects/Modern-CPP-APP-Example:/app ypsomed/bluetoothlib_daemon
#todo pwd