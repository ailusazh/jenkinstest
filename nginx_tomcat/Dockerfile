FROM 10.8.65.133:5050/jd_tomcat_nginx_base_img_v6

ADD ./*.war /home/CIJD.war

RUN sed -i 's#/mnt/${HOSTNAME}#/mnt/APPNAME/${HOSTNAME}#g' /home/admin/mount.sh

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
