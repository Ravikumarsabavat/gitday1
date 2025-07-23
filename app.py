import boto3
client = boto3.client('ec2')
response= client.run_instances(
   ImageId='ami-0150ccaf51ab55a51',
   InstanceType='t2.micro',
   KeyName='trst',
   MaxCount='1',
   MinCount='1
ssh -i your-key.pem ec2-user@your-ec2-public-ip
)



