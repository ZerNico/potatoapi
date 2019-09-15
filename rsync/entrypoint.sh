#!/bin/sh
while inotifywait -r -e modify,create,delete /public; do
    sleep 5s
    sshpass -p $SF_PASSWORD rsync -rpvz -e 'ssh -o StrictHostKeyChecking=no -p 22' --progress --delete-after --exclude 'baked' --exclude 'aligot' --exclude 'posp-sign-migrate.zip' /public/. $SF_USER@frs.sourceforge.net:/home/frs/project/posp
done
