# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files to the appropriate directory
COPY static /usr/share/nginx/html/static
COPY templates /usr/share/nginx/html/templates
