terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_security_group" "default_sg" {
  name        = "default_security_group"
  description = "Allow inbound and outbound traffic"

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [format("%s/32", var.device_ip)]
  }

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [format("%s/32", var.device_ip)]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [format("%s/32", var.device_ip)]
  }

  egress {
    description = "All outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = [format("%s/32", var.device_ip)]
  }
}

data "aws_ami" "free_tier_ami" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "free_tier_instance" {
  ami                    = var.ami != "" ? var.ami : data.aws_ami.free_tier_ami.id
  instance_type          = var.instance_type
  vpc_security_group_ids = var.security_group != "" ? [var.security_group] : [aws_security_group.default_sg.id]
  user_data = var.user_data
  tags = {
    Name = var.instance_name
  }
}


