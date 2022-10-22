FROM python:3.10-slim
 
RUN mkdir /opt/app
WORKDIR /opt/app

COPY ./requirements/fastapi.txt . 
RUN pip install --no-cache-dir --upgrade -r ./fastapi.txt

COPY ./requirements/nlp.txt . 
RUN pip install --no-cache-dir --upgrade -r ./nlp.txt

COPY ./requirements/ml.txt . 
RUN pip install --no-cache-dir --upgrade -r ./ml.txt

RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
