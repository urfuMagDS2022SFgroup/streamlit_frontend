# Streamlit Frontend for our ML api
Streamlit  based frontend for UrFU Master's machine learning program, first semester

## Basic steps:
- clone the repository
- go to repo folder

### build using Docker
- [install Docker](https://docs.docker.com/engine/install/)
- run `docker build -t streamlit .`
- when the build will be finished run `docker run -p 8501:8501 streamlit`

The app will be on `localhost:8501`

### Local buid
- install poetry `pip install poetry`
- run `poetry install`
- run `streamlit run src/streamlit_frontend.py`

The app will be on `localhost:8501`
