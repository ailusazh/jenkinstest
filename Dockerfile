FROM jd_new_base_img_6.5_v852_nginx:base

ADD ./CIJD.war /home/

RUN tar2export && ./home/admin/auto-add-tomcat/add-nginx+tomcat.sh DOMAINNAME SERVERNUM && unzip /home/CIJD.war -d /export/App/DOMAINNAME/ && export2tar

ENTRYPOINT tar2export && ./home/start-nginx+tomcat.sh DOMAINNAME SERVERNAME && ./home/mount.sh && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
