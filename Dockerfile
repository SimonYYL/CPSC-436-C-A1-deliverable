FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.12

COPY word_similarity_lambda.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY spacy_models /spacy_models

ENV SPACY_MODEL_PATH=/spacy_models/en_core_web_md/en_core_web_md-3.8.0

CMD [ "word_similarity_lambda.lambda_handler" ]