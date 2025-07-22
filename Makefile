REQ_DIR = requirements
PROD = $(REQ_DIR)/production.txt
DEV = $(REQ_DIR)/development.txt
DOCKER_IMAGE = CodeCrafters/app

# ✅ Install dependencies
install-prod:
	pip install -r $(PROD)

install-dev:
	pip install -r $(DEV)

# ✅ Ejecutar tests con coverage
test:
	coverage run manage.py test
	coverage report
	coverage xml

# 🔄 Update dependencies DEVELOPMENT.txt
sync-dev:
	@echo "↪️  Guardando dependencias del entorno actual a develop.tmp.txt..."
	pip freeze | grep -v "pkg-resources" > $(REQ_DIR)/develop.tmp.txt
	@echo "✅ Revisar $(REQ_DIR)/develop.tmp.txt y reemplazar develop.txt si es correcto."

# 🔄 Update dependencies PRODUCTION.txt
sync-prod:
	@echo "↪️  Guardando dependencias del entorno actual a production.tmp.txt..."
	pip freeze | grep -v "pkg-resources" > $(REQ_DIR)/production.tmp.txt
	@echo "✅ Revisar $(REQ_DIR)/production.tmp.txt y reemplazar production.txt si es correcto."

# 🧪 diff between current and saved dependencies
diff-dev:
	@echo "🔍 Comparando develop.txt con develop.tmp.txt..."
	@diff -u $(REQ_DIR)/develop.txt $(REQ_DIR)/develop.tmp.txt || echo "✔️ No hay diferencias."

diff-prod:
	@echo "🔍 Comparando production.txt con production.tmp.txt..."
	@diff -u $(REQ_DIR)/production.txt $(REQ_DIR)/production.tmp.txt || echo "✔️ No hay diferencias."

update_database:
	@echo "🔄 Actualizando la base de datos..."
	python manage.py makemigrations; \
	python manage.py migrate

# ✅ Docker
docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-run:
	docker run -p 8000:8000 $(DOCKER_IMAGE)