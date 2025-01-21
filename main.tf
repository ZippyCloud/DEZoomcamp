terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "instance_1" {
  ami           = var.aws_ami_id
  instance_type = var.aws_instance_type

  tags = {
    Name = "TerraformTestInstance"
  }
}