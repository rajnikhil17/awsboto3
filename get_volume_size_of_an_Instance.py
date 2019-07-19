import boto3
ec2 = boto3.resource('ec2', region_name='ap-southeast-2')
instance = ec2.Instance('i-05b30a7a287e30f4f')
volumes = instance.volumes.all()
print volumes
for v in volumes:
    print("Size in GB:"v.size)