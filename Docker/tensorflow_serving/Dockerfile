# Use the TensorFlow Serving image
FROM tensorflow/serving:latest

# Copy the TensorFlow model into the container
COPY model /models/model

# Set the environment variable for the model name
ENV MODEL_NAME=model

# Expose the TensorFlow Serving port
EXPOSE 8501

# Run TensorFlow Serving
CMD ["tensorflow_model_server", "--rest_api_port=8501", "--model_name=model", "--model_base_path=/models/model"]
