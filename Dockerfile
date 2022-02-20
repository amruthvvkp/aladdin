# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN pip install -U pip
COPY requirements/production.txt requirements/production.txt
RUN pip install --no-cache-dir --upgrade -r requirements/production.txt

WORKDIR /aladdin
COPY . /aladdin

RUN pip install .
RUN pip list

RUN ls

# Creates a non-root user with an explicit UID and adds permission to access the /aladdin folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /aladdin
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
WORKDIR /aladdin/aladdin
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
RUN pip list
