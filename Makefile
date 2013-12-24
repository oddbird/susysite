clean:
	find content -name *~ -delete
	rm -rf output/*

build: clean
	python run.py build content/

serve: build
	python run.py serve content/

