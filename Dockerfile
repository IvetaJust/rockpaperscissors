# Using the lastest python version
FROM python:latest

# Setting /app as your working directory
WORKDIR /app

# Copying everything from local directory to the app
COPY . /app

ENV NAME rockpaperscissors

# Using python3 to run your rock paper scissors app
CMD [ "python3", "./rockpaperscissors.py" ]
