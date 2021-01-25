# FastAPI_CRUD
Working on a crud application using pythons asynchronous web framework, Fast API. 

# Installation Process.
1. Create an env folder using:
	python -m venv env
2. Activate the virtual environment using:
	env\Scripts\activate
3. Upgrade pip using:
	python -m pip install -U pip
4. Install fastapi using:
	pip install fastapi
5. Install uvicorn using:
	pip install uvicorn[standard]
6. Install postgresql using:
	pip install databases[postgresql] (optional).
7. Install mysql using:
	pip install databases[mysql]
8. Optional Installation gunicorn:
	pip install gunicorn
9. Get requirements and version using:
    pip freeze > requirements.txt
10. Start up the application using:
    uvicorn main:app --reload