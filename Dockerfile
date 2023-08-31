# Python base image
FROM python:3.11


# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr
# Install dependencies
RUN apt-get update \
  && apt-get install -y curl \
  && curl -sSL https://install.python-poetry.org | python -

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copying the project files into the container
COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



