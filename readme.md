

### Creating a Project
`pulumi new aws-python --name devec2`

### Stack Management
|`pulumi stack rm dev`|
`pulumi stack init staging`
`pulumi stack ls`
`pulumi stack select`

### Pulumi Config
`pulumi config set aws:region us-west-2`
`pulumi config get aws:region`

### Resource Management
`pulumi up`
`pulumi destroy`


### Outputing your export information
`pulumi stack output bucket_name`
`aws s3 ls $(pulumi stack output bucket_name)`

### Pulumi Console
`pulumi console`
