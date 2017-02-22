FROM harbor.default.svc.n.jd.local/baseimage_web_tomcat/java-jd-centos6-jdk17-ngx197

RUN wget LINK -O /home/CIJD.war && unzip -d /home/export/App/DOMAINNAME/ /home/CIJD.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM APPNAME && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
