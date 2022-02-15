import pulumi
import pulumi_aws as aws
config = pulumi.Config()

# Check Configuration
config.require('name')
env_name = config.get('name')


group = aws.ec2.SecurityGroup(f'webserver-{env_name}-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
    ])
