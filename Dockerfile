# Use the lastest python version
FROM python:latest

# Set /app as your working directory
WORKDIR /app

# Copy everything from your local directory to the app
COPY . /app

ENV NAME rockpaperscissors

# Use python3 to run your rock paper scissors app
CMD [ "python3", "./rockpaperscissors.py" ]