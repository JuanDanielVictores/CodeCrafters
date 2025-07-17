REQ_DIR = requirements
PROD = $(REQ_DIR)/production.txt
DEV = $(REQ_DIR)/development.txt

# Install dependencies
install-prod:
	pip install -r $(PROD)

install-dev:
	pip install -r $(DEV)

# Update dependencies txt
sync-txt:
	pip freeze | grep -v "pkg-resources" > $(PROD)

clean:
	find . -type d -name "__pycache__" -exec rm -r {} + && \
	find . -type f -name "*.pyc" -delete
