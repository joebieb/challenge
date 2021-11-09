# Coding Challenge API

## Project structure
    - main.py: entrypoint into application
    - config.py: application configuration, relies on .env file or enviroment variables
    - db.py: some mock data
    - routers: endpoint routes
        - auth.py: authorization endpoints
        - quotation.py: quotataion endpoints
    - schemas: schema objects for request and response validation
        - auth.py: auth related objects
        - quotation.py: quotation related objects
    - services: service layer
        - auth.py: auth related methods
        - quotation.py: quotation related methods
    - static: a place to host front end code
        - UI code has built and added to this location
    - shared: shared modules
        - http_responses.py: a bunch of custom responses
## For development
    - modern version of python 3 should be installed
    - create a virtual environment python -m venv venv
    - activate the environment ./venv/Scripts/activate.ps1 or source ./venv/Scripts/activate
    - pip install -r requirements.txt
    - create a .env file and add the following
        - API_VERSION=0.1.0
        - MODE=DEVELOPMENT
        - SECRET_KEY=some_secret_value
## How to run API
    - uvicorn main:app
    - navigate to localhost:8000/docs to access swagger page
## How to access the UI
    - I have copied the `ng build` files to the static folder to serve everything from one place    
    - navigate to localhost:8000 to access UI
## How to test
    - No tests have been writtten at this time 
## Other ways to run
    - docker run
        docker build . -t challengeapi
        docker run -t -i -p 8000:80 --name challengeapi -e API_VERSION=0.1.0 -e MODE=DEVELOPMENT -e SECRET_KEY=somesecretvalue challengeapi:latest
    - docker-compose
        docker-compose build
        docker-compose up
