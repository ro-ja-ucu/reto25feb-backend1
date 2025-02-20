FROM python:3.12-alpine
WORKDIR /code
RUN pip install uv
COPY ./.python-version /code/.python-version
COPY ./pyproject.toml /code/pyproject.toml
COPY ./uv.lock /code/uv.lock
COPY ./main.py /code/main.py
RUN uv sync
CMD ["uv", "run", "uvicorn", "main:app", "--port", "8088", "--host", "0.0.0.0"]