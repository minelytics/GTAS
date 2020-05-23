FROM adoptopenjdk/maven-openjdk8 as scheduler-builder

RUN apt-get -y update && apt-get install -y git
RUN git clone https://github.com/US-CBP/GTAS.git /root/GTAS

RUN cp -R /root/GTAS/gtas-parent/ /gtas-parent
WORKDIR /gtas-parent
RUN mvn clean install --projects gtas-job-scheduler-war -am

RUN apt-get -y update && apt-get -y install dos2unix
RUN mkdir /temp-dos
RUN cp  /root/GTAS/gtas-parent/docker-resources/setenv-scheduler.sh /temp-dos/setenv-scheduler.sh
RUN dos2unix /temp-dos/setenv-scheduler.sh




