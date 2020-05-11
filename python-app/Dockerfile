FROM python:3.7
ADD app.py /
ADD templates /templates
RUN pip install flask
EXPOSE 5000
CMD [ "python", "./app.py" ]
