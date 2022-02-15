

### Creating a Project
`pulumi new aws-python`


### Resource Management
`pulumi up`
`pulumi destroy`


### Outputing your export information
`pulumi stack output bucket_name`


### Pulumi Console

`pulumi console`
aws s3 ls $(pulumi stack output bucket_name)