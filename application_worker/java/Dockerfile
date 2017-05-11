FROM IMAGENAME

RUN wget -q http://ngx2agenxt-agent.harbor.svc.n.jd.local/image-install.sh -O /root/image-install.sh && chmod +x /root/image-install.sh && ./root/image-install.sh && rm -rf /root/image-install.sh

ADD *.zip /home/export/App

RUN unzip -d /home/export/App/ /home/export/App/*.zip && chmod +x /home/export/App/bin/* && dos2unix /home/export/App/bin/*.sh

ENTRYPOINT /etc/init.d/crond restart && /etc/init.d/sshd restart && bash /home/admin/start_container.sh SERVERNUM APPNAME APPID && sleep 9999999d
