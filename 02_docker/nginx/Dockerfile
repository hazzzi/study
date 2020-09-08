 # cat services/nginx/Dockerfile 
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive 

RUN apt update 

RUN apt install -y nginx libnginx-mod-http-headers-more-filter
RUN apt clean \
  && rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/ /etc/nginx/conf.d

# Forward request logs to Docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

# USER www-data

EXPOSE 80 443

# CMD ["nginx", "-g", "daemon off;"]
