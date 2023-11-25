FROM python:3.11-alpine
MAINTAINER Eytes

# install poetry
RUN pip install "poetry==1.7.1"

# copy dependecies
WORKDIR "/code"
COPY poetry.lock pyproject.toml /code/

# install dependecies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /code

CMD ["poetry", "run", "python3", "app/main.py"]