FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /sourcecode
COPY main.py /sourcecode

EXPOSE 8000

CMD ["python", "main.py"]