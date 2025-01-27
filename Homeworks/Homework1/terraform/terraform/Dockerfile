FROM hashicorp/terraform:latest

LABEL description="A Docker image for Terraform with AWS CLI"

WORKDIR /app

COPY ../.terraform /app

RUN apk add --no-cache python3 py3-pip && pip3 install awscli

ENTRYPOINT ["terraform"]