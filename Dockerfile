
FROM python:3.11-slim

WORKDIR /scm_fastapi_project-master
 

COPY requirements.txt /scm_fastapi_project-master
 
RUN pip install --trusted-host pypi.python.org -r requirements.txt
 
COPY . /scm_fastapi_project-master
 

EXPOSE 8000
 
CMD ["uvicorn", "main:app", "--reload" ,"--host", "0.0.0.0", "--port", "8000"]