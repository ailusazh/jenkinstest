FROM IMAGENAME 

ADD ./*.war /home/admin

RUN mkdir -p /home/export/App/DOMAINNAME && unzip -d /home/export/App/DOMAINNAME /home/admin/*.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM APPNAME && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
