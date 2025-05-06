# Use an official Python base image
FROM python:3.11-sim

# Set the working directory inside the container
WORKDIR /app

# Copy the calculation script
COPY calc.py .

# Run the script on container start

CMD ["python", "calc.py"]
