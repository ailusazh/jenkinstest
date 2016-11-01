FROM jd_new_base_img_6.5_v852_nginx:base2

ADD ./CIJD.war /home/

RUN tar2export && ./home/admin/auto-add-tomcat/add-nginx+tomcat.sh live.jd.com 2 && unzip /home/CIJD.war -d /export/App/live.jd.com/ && export2tar

ENTRYPOINT tar2export && ./home/start-nginx+tomcat.sh live.jd.com 2 && ./home/mount.sh && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
