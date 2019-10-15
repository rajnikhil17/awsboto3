import boto3

def getInstancesPerRegion(region_name):
	client = boto3.client('ec2',region_name)
	instances = client.describe_instances() 
	for reservations in instances['Reservations']:
		for instance in reservations['Instances']:
			print ("DNS Name is :",instance['PublicDnsName'])
			print ("EBS Optimized or Not :" ,instance['EbsOptimized'])
			print ("Private IP Address :" ,instance['PrivateIpAddress'])
			print ("VPC Id : " ,instance['VpcId'])
			print ("Subnet Id : ",instance['SubnetId'])
			print ("CPU Configurations :" ,instance['CpuOptions'])
			print ("Instance Id is :" ,instance['InstanceId'])
			print ("AMI Id is : " ,instance['ImageId'])
			print ("Private DNS Name : " ,instance['PrivateDnsName'])
			print ("Attached Key Name : " ,instance['KeyName'])
			print ("Security Groups Attached are : ",instance['SecurityGroups'])
			print ("Instance Type : " ,instance['InstanceType'])
			print ("Architecture : " ,instance['Architecture'])
			print (instance['RootDeviceType'])
			print (instance['RootDeviceName'])
			print (instance['VirtualizationType'])
			print ("Tags are : " ,instance['Tags'])
			print ("Network Configuration : " ,instance['NetworkInterfaces'])
			print ("Private DNS Name is :" , instance['NetworkInterfaces'])
			# for i in range(len(instance['Tags'])):
			# 	for key,value in instance['Tags'][i].items():
			# 		print value
			# print instance['Tags']


client = boto3.client('ec2')
for region in client.describe_regions()['Regions']:
	region_name = region['RegionName']
	if region_name == "ap-east-1":
		print ("API Call Not allowed For this " + region_name)
	else:
		print ("VM's in this " + region_name + " are : ", getInstancesPerRegion(region_name))	
		print ("************************************************************************")
		print ("########################################################################")
