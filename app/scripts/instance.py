#!/usr/bin/env python
import boto3

ec2 = boto3.resource('ec2')

# Boto 3
# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
instances = ec2.instances.filter()
for instance in instances:
	    print(instance.id, instance.instance_type)
