# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the Nginx configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files
COPY static /usr/share/nginx/html/static

# Copy media files
COPY media /usr/share/nginx/html/media