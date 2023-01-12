#seed
FROM python:3.8
#setup
ENV TZ=Europe/Minsk
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update
RUN apt-get install build-essential checkinstall
RUN apt-get -y install libffi-dev
RUN apt-get -y install apt-utils vim curl python3-dev
RUN ln /usr/bin/python3 /usr/bin/python
#Groups, Permissions and Ownership
RUN mkdir Athena
ADD ./Athena /Athena
ADD ./Athena/requirements.txt /Athena
#requirements
RUN pip install --upgrade pip
RUN pip install -r /Athena/requirements.txt 
#expose and run
EXPOSE 80 3500
CMD ["python","-V"]


