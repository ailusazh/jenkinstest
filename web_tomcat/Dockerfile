FROM IMAGENAME 

RUN mkdir -p /home/export/App/DOMAINNAME

ADD ./*.war /home/export/App/DOMAINNAME/

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM APPNAME && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 

