FROM python:3.9-slim

WORKDIR /app

COPY first_project.py .

# Asegurar que el usuario tiene permisos de escritura
RUN chmod 777 /app

CMD ["python", "first_project.py"] 