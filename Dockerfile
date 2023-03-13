# Start with a base image
FROM python:3.10.6-slim

ENV PYTHONUNBUFFERED 1
# Set the working directory
RUN mkdir /app
WORKDIR /app

# Install dependencies

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the source code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set the default command to start the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
