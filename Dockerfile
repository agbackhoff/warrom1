FROM python:3.9-slim

WORKDIR /app

COPY first_project.py .

CMD ["python", "first_project.py"] 