# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /cloudProject/todo_list

# Install the required dependencies
RUN pip install --no-cache-dir pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the Django project files into the image
COPY . .

# Expose the port that the Django server will be running on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
