FROM 10.8.65.133:5050/jd_tomcat_nginx_base_img_v5

RUN wget http://10.8.65.133:9999/dd -O /home/dd

RUN wget LINK -O /home/CIJD.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
