import boto3
client = boto3.client('ec2')
addresses_dict = client.describe_addresses()
print addresses_dict
for eip_dict in addresses_dict['Addresses']:
	if "InstanceId" not in eip_dict:
		print (eip_dict['PublicIp'] +" doesn't have any instances associated, releasing")
        client.release_address(AllocationId=eip_dict['AllocationId'])