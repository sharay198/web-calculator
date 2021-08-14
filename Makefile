build:
	docker build -t web_calculator .
docker-run:
	 docker run --rm -p 8000:8000 web_calculator
ps:
	docker ps -aq
docker-stop:
	docker stop $(docker ps -aq)
rm:
	docker rm $(docker ps -aq)
rmi:
	docker rmi $(docker images -q)
runserver:
	python -m manage runserver 127.0.0.1:8000