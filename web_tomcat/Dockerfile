FROM IMAGENAME 

ADD ./*.war /home/admin

RUN mkdir -p /home/export/App/DOMAINNAME && mv /home/admin/*.war /home/export/App/DOMAINNAME && cd /home/export/App/DOMAINNAME && /home/export/servers/jdk1.6.0_25/bin/jar -xvf *.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM APPNAME APPID && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
