FROM python:3.9.17-slim

WORKDIR /app

RUN pip install matplotlib
RUN pip install numpy
RUN pip install pandas
RUN pip install flask
RUN pip install requests
RUN pip install Jinja2

CMD ["python", "main.py"]