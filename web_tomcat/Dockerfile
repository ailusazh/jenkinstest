FROM IMAGENAME 

RUN wget -q http://ngx2agenxt-agent.harbor.svc.n.jd.local/image-install.sh -O /root/image-install.sh && chmod +x /root/image-install.sh && ./root/image-install.sh && rm -rf /root/image-install.sh

ADD ./*.war /home/admin

RUN mkdir -p /home/export/App/DOMAINNAME && mv /home/admin/*.war /home/export/App/DOMAINNAME && cd /home/export/App/DOMAINNAME && /home/export/servers/jdk1.6.0_25/bin/jar -xvf *.war

ENTRYPOINT ./home/admin/start_container.sh DOMAINNAME SERVERNUM APPNAME APPID && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d 
