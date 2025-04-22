# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Jupyter and any other dependencies you need
RUN pip install --no-cache-dir jupyter

# Install other libraries you need for your notebook
# For example, pandas, numpy, etc.
RUN pip install pandas numpy matplotlib

# Expose the port Jupyter runs on
EXPOSE 8888

# Command to start Jupyter Notebook when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]



