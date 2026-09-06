#!/bin/bash

# Script to generate self-signed SSL certificates for local development
# This creates certificates valid for localhost and 127.0.0.1

set -e

echo "Generating self-signed SSL certificates for local development..."

# Create the directory structure that nginx-local.conf expects
# (mounted into the container at /etc/letsencrypt via docker-compose)
mkdir -p ./certs/conf/live/localhost

# Generate a self-signed certificate and key
# Valid for 365 days
# Subject Alternative Names include localhost and 127.0.0.1
# Filenames match what Let's Encrypt normally produces (fullchain.pem / privkey.pem)
# so nginx-local.conf and nginx.conf can point at the same paths either way.
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ./certs/conf/live/localhost/privkey.pem \
  -out ./certs/conf/live/localhost/fullchain.pem \
  -subj "/C=US/ST=State/L=City/O=Development/OU=Dev/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

# Set appropriate permissions
chmod 600 ./certs/conf/live/localhost/privkey.pem
chmod 644 ./certs/conf/live/localhost/fullchain.pem

echo "Self-signed certificates generated successfully!"
echo "Certificate: ./certs/conf/live/localhost/fullchain.pem"
echo "Private Key: ./certs/conf/live/localhost/privkey.pem"
echo ""
echo "Note: These certificates are for local development only."
echo "Browsers will show security warnings because these are self-signed."