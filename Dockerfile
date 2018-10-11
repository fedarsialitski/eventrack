# Use an official Python runtime as a parent image
FROM python:3.6

# Install non-python dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    # uWSGI needs mime-support to serve static files
    # with the correct content-type header
    mime-support \
    binutils libproj-dev gdal-bin libgeoip1 python-gdal \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Install python packages. Done in a separate step so Docker can cache it.
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy a script to run the application.
COPY bin/run.sh /run.sh
CMD ["/run.sh"]

# Copy the current directory contents into the container at /app
COPY . /app

# We need to include static files into a Docker image.
# SECRET_KEY is actually not so important for collectstatic,
# but Django now requires this to run these command.
RUN CFG_SECRET_KEY=fake python manage.py collectstatic --noinput


# Make port 8080 available to the world outside this container
EXPOSE 8080
