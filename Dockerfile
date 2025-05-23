# Use the official slim version of the Python 3.12 image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /scm_fastapi_project-master

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files into the working directory
COPY . .

# Expose port 8000 to allow access from outside the container
EXPOSE 8000

# Run the FastAPI application using Uvicorn with live reload (useful for development)
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
