FROM python:3.7
ADD app.py /
ADD templates /templates
RUN pip install -r requirements.txt 
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
CMD ["python", "app.py"]
EXPOSE 5000
