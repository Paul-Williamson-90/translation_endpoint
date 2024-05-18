FROM continuumio/miniconda3
WORKDIR /app
ADD . /app
RUN conda env create -f conda.yml
SHELL ["conda", "run", "-n", "example", "/bin/bash", "-c"]
EXPOSE 8000
CMD ["conda", "run", "-n", "example", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]