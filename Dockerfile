FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD .env /code/
RUN pip install -r requirements.txt
ADD . /code/
ADD .bash_history /root
CMD ["/bin/bash"]