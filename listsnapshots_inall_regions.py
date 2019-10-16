import boto3

client = boto3.client('ec2')
AWS_Regions=[]
for region in client.describe_regions()['Regions']:
	AWS_Regions.append(region['RegionName'])

print(AWS_Regions)

for i in range(len(AWS_Regions)):
	client = boto3.client('ec2',region_name=AWS_Regions[i])
	print("Region:",AWS_Regions[i])
	print("----------------------------------------Searching for Snapshots in This Region--------------------------------------------")
	account_id=str(boto3.client('sts').get_caller_identity().get('Account'))
	snapshots = client.describe_snapshots(OwnerIds=[account_id])
	print("Number of Snapshots in " + AWS_Regions[i] + " are",len(snapshots['Snapshots']))
	print()
	for i in range(len(snapshots['Snapshots'])):
		print ("Description:::",snapshots['Snapshots'][i]['Description'])
		print ("Encrypted Flag:::",snapshots['Snapshots'][i]['Encrypted'])
		print ("Owner ID:::",snapshots['Snapshots'][i]['OwnerId'])
		print ("Progress:::",snapshots['Snapshots'][i]['Progress'])
		print ("Snapshot ID:::",snapshots['Snapshots'][i]['SnapshotId'])
		print ("Start Time:::",snapshots['Snapshots'][i]['StartTime'])
		print ("State:::",snapshots['Snapshots'][i]['State'])
		print ("VolumeID:::",snapshots['Snapshots'][i]['VolumeId'])
		print ("Volume Size:::",snapshots['Snapshots'][i]['VolumeSize'])
		print()
		print()
	print()
	print("------------------------------------------Done Searching----------------------------------------------------------------")
	print()
	print()
	 

