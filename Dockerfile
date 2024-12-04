# Use official Python image as base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files to the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the scraper script
CMD ["python", "scraper.py"]
