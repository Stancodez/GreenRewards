# Specify the base image (e.g., Python with libraries)
FROM python:3.9-slim

# Create a working directory within the container
WORKDIR /app

# Copy your application code into the container
COPY . .

# Install any additional dependencies (e.g., using pip)
RUN pip install -r requirements.txt  # Assuming you have a requirements.txt file listing dependencies

# Define the command to start your application
CMD ["python", "app.py"]  # Replace "main.py" with your application's entry point script
