FROM python:3.11-slim-buster
COPY . /app
WORKDIR /app
RUN apt update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["uvicorn", "carina:app", "--host", "0.0.0.0"]
