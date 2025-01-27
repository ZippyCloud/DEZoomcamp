#!/bin/bash
sudo apt-get update
sudo apt-get install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
echo "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>My Basic Webpage</title></head><body><h1>Welcome to My Basic Webpage</h1><p>This is a simple webpage hosted on my cluster.</p></body></html>" | sudo tee /var/www/html/index.html