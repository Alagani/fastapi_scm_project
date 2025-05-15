FROM python:3.12-slim
 
WORKDIR /kafka/server
 
RUN pip install python-dotenv
 
COPY . /kafka/server
 
EXPOSE 6000
 
CMD ["python", "server.py"]