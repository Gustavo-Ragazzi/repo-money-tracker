run:
	poetry run streamlit run src/main.py

code-check:
	poetry run pre-commit run --all-files
