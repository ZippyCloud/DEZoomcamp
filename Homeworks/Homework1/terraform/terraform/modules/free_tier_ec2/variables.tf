variable "region" {
  description = "The region to launch the instance. (Default: ue-central-1)"
  type        = string
  default     = "eu-central-1"
}

variable "security_group" {
  description = "The security group to use for the instance"
  type        = string
  default     = ""
}

variable "ami" {
  description = "The AMI to use for the instance"
  type        = string
  default     = ""
}

variable "instance_type" {
  description = "The type of instance to start"
  type        = string
  default     = "t2.micro"
}

variable "instance_name" {
  description = "The name of the instance"
  type        = string
  default     = "free-tier-instance"
}

variable "device_ip" {
  description = "The IP address of the device to allow SSH access"
  type        = string
  sensitive   = true
}

variable "user_data" {
  description = "The user data to provide when launching the instance"
  type        = string
  default     = ""
}