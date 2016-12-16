FROM 10.8.65.133:5050/jd_new_base_img_6.5_jdk1.7

RUN wget LINK -O /home/CIJD.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
