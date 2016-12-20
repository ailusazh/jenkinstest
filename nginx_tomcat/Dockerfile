FROM 10.8.65.156/baseimage_webtomcat/java1.6:jdk1.6_tomcat6

ADD ./*.war /home/CIJD.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
