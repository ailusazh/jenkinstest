FROM IMAGENAME
ADD *.zip /home/export/App/
ENTRYPOINT ./home/admin/start_container.sh 1 && /etc/init.d/crond restart && /etc/init.d/sshd restart && sleep 9999999d
