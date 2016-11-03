FROM base_nginx_tomcat

ADD ./CIJD.war /home/

RUN tar2export && ./home/admin/auto-add-tomcat/add-nginx+tomcat.sh DOMAINNAME SERVERNUM && unzip /home/CIJD.war -d /export/App/DOMAINNAME/ && export2tar

ENTRYPOINT tar2export && ./home/start-nginx+tomcat.sh DOMAINNAME SERVERNUM && ./home/mount.sh && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
