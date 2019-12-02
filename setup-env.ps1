docker build -t cpp-builder:latest .
docker run -it --rm -v ${pwd}:/app  cpp-builder:latest

