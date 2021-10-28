data "local_file" "public_ssh_key" {
  filename = "/Users/gauthamnambi/.ssh/id_rsa.pub"
}

resource "aws_instance" "flask" {
  ami           = "ami-0c1a7f89451184c8b"
  instance_type = "t2.micro"

  iam_instance_profile = "EC2-ALL-ACCESS"
  key_name             = "gautham-nambi"

  security_groups = ["IAM-80", "launch-wizard-1"]


  user_data = <<-EOF
    #!/bin/bash
    sudo -u ubuntu bash -c 'echo "${data.local_file.public_ssh_key.content}" >> ~/.ssh/authorized_keys'
    EOF
}

resource "aws_s3_bucket" "s3_assignment" {
  bucket = "gautham-assignment-1"
  acl    = "private"
  tags = {
    Environment = "interview"
  }
}


resource "aws_s3_bucket_object" "file_upload" {
  bucket = "gautham-assignment-1"
  key    = "nginx.conf"
  source = "/Users/gauthamnambi/nginx.conf"
  etag   = "$(filemd5(/Users/gauthamnambi/nginx.conf))"
}