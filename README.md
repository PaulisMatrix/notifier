Please note the project is not finished yet so it maybe having some breaking changes. 

Also Docker doesn't work on my system after a failed update of docker-desktop. 
So Im yet to test those dockerfiles. Have added it right now for reference. 



# Steps to run the app locally.

* Make sure you have redis installed.
* Create a virtual env and install all the python dependencies. If you run into dependencies issues, keep trying till time runs out OR magically it works. 
* cd to src
* Run fastapi server: `python3 app.py`
* Run celery worker: `celery -app worker.celery_app worker --loglevel=INFO`
* Make some request with a valid json payload. Viola!


