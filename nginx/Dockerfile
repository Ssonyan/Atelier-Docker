FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost/api/health || exit 1