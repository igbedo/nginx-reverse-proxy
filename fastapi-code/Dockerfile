# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app
#RUN useradd -ms /bin/bash myuser
#USER myuser
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container (metadata)
#EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
#CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
#CMD ["uvicorn", "main:app", "--reload"]
