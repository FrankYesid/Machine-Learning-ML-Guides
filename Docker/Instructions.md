Instructions for Running the Docker Containers
For each project, follow the instructions below:

Clone the repository:

bash
Copiar código
git clone https://github.com/yourusername/MachineLearningProjects.git
cd MachineLearningProjects/Docker
Install Docker: Follow the installation instructions for Docker and Docker Compose.

Build and run the containers:

For Dockerized Jupyter Notebook, run:
bash
Copiar código
cd dockerized_jupyter
docker-compose up
For Flask API, run:
bash
Copiar código
cd flask_api
docker build -t flask_api .
docker run -p 5000:5000 flask_api
For TensorFlow Serving, run:
bash
Copiar código
cd tensorflow_serving
docker build -t tf_serving .
docker run -p 8501:8501 -v $(pwd)/model:/models/model -e MODEL_NAME=model tf_serving
For Streamlit App, run:
bash
Copiar código
cd streamlit_app
docker build -t streamlit_app .
docker run -p 8501:8501 streamlit_app
For PyTorch Deployment, run:
bash
Copiar código
cd pytorch_deployment
docker build -t pytorch_deployment .
docker run -p 8080:8080 pytorch_deployment
These Dockerfiles should cover the use cases you mentioned and allow you to containerize each project with a consistent environment.