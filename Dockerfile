# Base image python
ARG Version_Name=python
FROM ${Version_Name}

#  specify the directory path where any subsequent commands will be executed.
WORKDIR /Assignment 2

# Copy all files to the working directory
COPY . .

# execute commands during the image build process
RUN pip install NLTK

# create command to run image
CMD ["python", "Python_script.py"]