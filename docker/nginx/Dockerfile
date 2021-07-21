FROM nginx



COPY ssl /etc/ssl/certs

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
