1. pull the image
docker pull python:3.12.8

2. run the image in interactive with bash as enrtypoint
docker run -it --entrypoint bash python:3.12.8

3. one inside container, show pip version
pip --version

4. exit the container
exit

Version of pip is: 24.3.1

![Question 1](../screenshots/pip_version.jpg)