#!/bin/sh

docker stop blog
cd Website
git pull
cd ..
docker run -d -p 443:443/tcp -p 80:80/tcp --restart always -v $PWD/Website/BlockWorks/public:/var/www/html -t blog 


