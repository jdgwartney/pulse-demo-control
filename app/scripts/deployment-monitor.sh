#!/bin/bash
while : 
do
    aws opsworks describe-deployments  --app-id ae0a0232-a545-4250-99a3-5243d9b2c570 | jq '.Deployments | .[0]'
    sleep 10 
done

