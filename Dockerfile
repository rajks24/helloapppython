FROM python:3.9.13-slim

# Make dir app and install dependencies
RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the executable
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]