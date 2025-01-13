include .env

.PHONY: up
up:
	@echo "Running $(APP) on port $(PORT) in $(FLASK_ENV) mode"
	docker build -t $(APP) .
	docker run -d -p $(PORT):5000 \
		-e FLASK_ENV=$(FLASK_ENV) \
		-e FLASK_DEBUG=$(FLASK_DEBUG) \
		$(APP)

.PHONY: down
down:
	@echo "Stopping $(APP)"
	docker ps -q --filter ancestor=$(APP) | xargs docker stop

.PHONY: clean
clean:
	@echo "Removing $(APP)"
	docker ps -q --filter ancestor=$(APP) | xargs -r docker stop
	docker ps -a -q --filter ancestor=$(APP) | xargs -r docker rm
	docker images -q $(APP) | xargs -r docker rmi

.PHONY: logs
logs:
	@echo "Showing logs for $(APP)"
	docker ps -q --filter ancestor=$(APP) | xargs docker logs -f
