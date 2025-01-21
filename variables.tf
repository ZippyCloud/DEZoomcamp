variable "aws_instance_type" {
  description = "Type of the EC2 instance."
  type        = string
  default     = "t2.micro"
}

variable "aws_ami_id" {
  description = "The AMI ID to use for the EC2 instance."
  type        = string
  default     = "ami-0cdd6d7420844683b"
}

variable "aws_region" {
  description = "Default region to be used for AWS resources. (Frankfurt)"
  type        = string
  default     = "eu-central-1"
}