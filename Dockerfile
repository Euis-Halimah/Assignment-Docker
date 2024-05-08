# Use Python 3.9 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy etl.py into the container
COPY etl.py .

# Run the Python script
CMD ["python", "etl.py"]