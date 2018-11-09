FROM nginx:1.14.1
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY smartuse.conf /etc/nginx/conf.d/
