provider "aws" {
  region = "eu-central-1"
}

module "ec2" {
  source    = "./modules/free_tier_ec2"
  device_ip = var.device_ip
}