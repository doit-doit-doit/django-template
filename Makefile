clean:
	docker container rm $$(docker ps -aq) -f
	rm -rf db/data/*
	
up: 
	docker-compose build
	docker-compose up

.PHONY: dockerbuild up clean 