.PHONY: clean
clean:
	rm -rfv *.egg-info __pycache__

test:
	pytest -vv tests/
