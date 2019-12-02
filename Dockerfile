FROM conanio/gcc7:latest

RUN sudo apt-get update && sudo apt-get install -y \
    lcov 

RUN sudo mkdir p /app
WORKDIR "/app"
