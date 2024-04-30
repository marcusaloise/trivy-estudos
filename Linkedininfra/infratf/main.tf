terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

### EC2 ###

resource "aws_instance" "marcusServer" {
  ami = "ami-016eb5d644c333ccb"
  instance_type = "t2.micro"
  
  subnet_id = aws_subnet.marcuSubnet.id

  key_name = "id_rsa"
  

  tags = {
    Name = "marcusServer"
  }
}


### VPC ###

resource "aws_vpc" "marcusVPC" {
  cidr_block       = "10.0.0.0/16"

  tags = {
    Name = "Marcus VPC"
  }
}

### Subnet ###
resource "aws_subnet" "marcuSubnet" {
  vpc_id     = aws_vpc.marcusVPC.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "Marcus Subnet"
  }
}

### Internet Gateway ###
resource "aws_internet_gateway" "marcusGW" {
  vpc_id = aws_vpc.marcusVPC.id

  tags = {
    Name = "marcusVPC"
  }
}

### RT ###

resource "aws_route_table" "marcusRT" {
  vpc_id = aws_vpc.marcusVPC.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.marcusGW.id
  }

  tags = {
    Name = "RT-MARCUS"
  }
}

### RT Association Subnet ###

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.marcuSubnet.id
  route_table_id = aws_route_table.marcusRT.id
}



### SG ###

resource "aws_security_group" "allow_tudo" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.marcusVPC.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_tudo"
  }
}

resource "aws_network_interface_sg_attachment" "sg_attachment" {
  security_group_id = aws_security_group.allow_tudo.id
  network_interface_id = aws_instance.marcusServer.primary_network_interface_id
  
}




















































# module "ec2-rundeck" {
#   source         = "rundeck-io/ec2-rundeck/aws"
#   version        = "0.0.8"
#   aws_vpc_id     = data.aws_vpc.default.id
#   aws_subnet_id  = data.aws_subnet.default.id
#   key_pair_name  = "id_rsa"
  
#   # Optional - The IP addresses that are allowed to access the SSH service on the Rundeck instance.
#   # ip_allow_ssh   = ["0.0.0.0/0"]
  
#   # Optional - The IP addresses that are allowed to access the HTTPS service on the Rundeck instance.
#   # ip_allow_https = ["0.0.0.0/0"]
  
#   # Optional - The type of the EC2 instance to use for Rundeck.
#   # instance_type  = "c5.large"
# }

# # The "provider" block defines the AWS provider to be used for this Terraform code
# provider "aws" {
#   region = "us-east-1"
# }

# # Retrieve information about the default AWS VPC
# data "aws_vpc" "default" {
#   default = true
# }

# # Retrieve information about the available AWS availability zones
# data "aws_availability_zones" "available" {
#   state = "available"
# }

# # Retrieve information about a subnet in the default VPC
# data "aws_subnet" "default" {
#   availability_zone = data.aws_availability_zones.available.names[0]
#   vpc_id            = data.aws_vpc.default.id
# }

# # The server URL of the Rundeck instance
# output "server_url" {
#   value       = module.ec2-rundeck.server_url
#   description = "HTTPS endpoint of Rundeck host"
# }

