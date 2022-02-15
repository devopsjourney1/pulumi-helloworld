import pulumi
import pulumi_aws as aws
config = pulumi.Config()
from security import group


# Check Configuration
config.require('name')
config.require('instance_type')

project = pulumi.get_project()
env_name = config.get('name')

server_count = config.get_int('server_count')
print('test')

# https://www.pulumi.com/registry/packages/aws/api-docs/

instance_type = config.get('instance_type')
ami = aws.ec2.get_ami(most_recent="true",
                  owners=["137112412989"],
                  filters=[{"name":"name","values":["amzn-ami-hvm-*"]}])



for i in range(server_count):
    server_number = str(i+1)
    server = aws.ec2.Instance(f'webserver-{env_name}-{server_number}',
        instance_type=instance_type,
        vpc_security_group_ids=[group.id], # reference security group from above
        ami=ami.id,
        tags={
            "Name": f"{env_name}-Server-{server_number}",
        })

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
