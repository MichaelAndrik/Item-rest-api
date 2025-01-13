FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the Flask app environment variable
ENV FLASK_APP=main.py

# Define command to run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
