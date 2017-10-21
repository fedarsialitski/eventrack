# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Install non-python dependencies
RUN apt-get update && apt-get install -y \
    gcc

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy a script to run the application.
COPY bin/run.sh /run.sh
CMD ["/run.sh"]

# Make port 80 available to the world outside this container
EXPOSE 80