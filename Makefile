test:
		pytest --tb=short

build:
		docker build . -t blog

run: 
		docker run -it -p 5005:80 blog:latest

all: build run 