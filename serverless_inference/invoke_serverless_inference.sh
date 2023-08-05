#!/bin/sh

outfile="output.txt"
endpoint_name="play-with-aws-sagemaker-serverless-inference"
body=`echo -n "test" | base64`

aws sagemaker-runtime invoke-endpoint --endpoint-name ${endpoint_name} --body ${body} ${outfile}

cat ${outfile}
