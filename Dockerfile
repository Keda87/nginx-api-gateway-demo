FROM nginx:1.19.0-alpine

COPY conf/nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/*
COPY conf/services/* /etc/nginx/conf.d/

EXPOSE 80