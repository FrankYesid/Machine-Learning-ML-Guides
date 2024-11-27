# Use the official Jupyter base image with Python and pre-installed libraries
FROM jupyter/scipy-notebook:latest

# Install additional machine learning libraries
RUN pip install --no-cache-dir \
    tensorflow \
    torch \
    scikit-learn \
    pandas \
    matplotlib \
    seaborn

# Expose the Jupyter port
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
