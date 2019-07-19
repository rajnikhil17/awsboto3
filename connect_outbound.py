import boto3
client = boto3.client('connect',region_name='us-east-1')

response = client.start_outbound_voice_contact(
    DestinationPhoneNumber='+17034660228',
    ContactFlowId='29df94d0-6be3-4006-bf87-19f284d9563d',
    InstanceId="25d71216-667d-4103-99bb-d76589bc30df",
    SourcePhoneNumber='+18668952551'
)

print(response)


