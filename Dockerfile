# Use a Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . /app

# Expose the port the app runs on
EXPOSE 80

# Command to run the app
CMD ["python", "app.py"]
