FROM python:3.8-alpine
EXPOSE 5000

COPY requirements.txt /abagdemo/requirements.txt
WORKDIR /abagdemo
RUN pip3 install -r requirements.txt

COPY . /abagdemo
ENTRYPOINT ["./boot.sh"]