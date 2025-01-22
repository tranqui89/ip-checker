# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the app code and templates into the container
COPY . .

# Start the Flask app
CMD ["python", "app.py"]
