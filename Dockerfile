FROM python:3.10-buster

ENV HOST="0.0.0.0"
ENV PORT="8080"
ENV POETRY_VERSION="1.3.1"
ENV BACKEND_URL="http://backend:8000"
WORKDIR /front
EXPOSE $PORT
RUN pip install poetry==$POETRY_VERSION

COPY pyproject.toml /front/pyproject.toml
COPY poetry.toml /front/poetry.toml
COPY poetry.lock /front/poetry.lock
COPY .streamlit /front/.streamlit
RUN poetry install

COPY src /front/src

ENV PYTHONPATH=/front

CMD poetry run streamlit run src/streamlit_frontend.py
