FROM python:3.8
COPY . /app
WORKDIR /app
COPY requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["run.py"]