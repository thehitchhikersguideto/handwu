

make env
	python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt


make env-win
	python3 -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt


