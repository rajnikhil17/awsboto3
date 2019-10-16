import boto3

AWS_Regions=[]
client = boto3.client('ec2',region_name='us-east-1')
for region in client.describe_regions()['Regions']:
	AWS_Regions.append(region['RegionName'])



account_id=str(boto3.client('sts').get_caller_identity().get('Account'))



for region_list in range(len(AWS_Regions)):
	client = boto3.client('ec2', region_name=AWS_Regions[region_list])
	images = client.describe_images(Owners=[account_id])
	for i in range(len(images['Images'])):
		print("Region is:",AWS_Regions[region_list])
		print("-------------------------------------Searching in a Region--------------------------------------------")
		print("Architecture is:",images['Images'][i]['Architecture'])
		print("Created At:",images['Images'][i]['CreationDate'])
		print("AMI ID is:",images['Images'][i]['ImageId'])
		print("Image Location:",images['Images'][i]['ImageLocation'])
		print("Image Type:",images['Images'][i]['ImageType'])
		print("Public or Not:",images['Images'][i]['Public'])
		print("OwnerID:",images['Images'][i]['OwnerId'])
		print("Current State:",images['Images'][i]['State'])
		print("Disk Mappings:",images['Images'][i]['BlockDeviceMappings'])
		print("Image Description:",images['Images'][i]['Description'])
		print("Hypervisor:",images['Images'][i]['Hypervisor'])
		print("Image Name:",images['Images'][i]['Name'])
		print("Root Device Name:",images['Images'][i]['RootDeviceName'])
		print("Root Device Type:",images['Images'][i]['RootDeviceType'])
		if "Tags" in images['Images'][i]:
			for j in range(len(images['Images'][i]['Tags'])):
				print("Tags are:",images['Images'][i]['Tags'][j])

		if "EnaSupport" in images['Images'][i]:
			print("Ena Support:",images['Images'][i]['EnaSupport'])
		if "SriovNetSupport" in images['Images'][i]:
			print("SriovNetSupport:",images['Images'][i]['SriovNetSupport'])
		print("Virtualization Type:",images['Images'][i]['VirtualizationType'])

		print("------------------------------------------Done For the Region--------------------------------------------")
		print()
		print()
		print()