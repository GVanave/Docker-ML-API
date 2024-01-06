FROM python:3.9
COPY ./flask_api /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python/
RUN pip install -r requirement.txt
CMD python flask_predict_api.py