# Use the official PyTorch image
FROM pytorch/pytorch:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the model API
EXPOSE 8080

# Run the serve.py script
CMD ["python", "serve.py"]
