

### Creating a Project
|Command|
|----|
`pulumi new aws-python --name devec2`

### Stack Management
|Command|
|----|
`pulumi stack rm dev`
`pulumi stack init staging`
`pulumi stack ls`
`pulumi stack select`

### Pulumi Config
|Command|
|----|
`pulumi config set aws:region us-west-2`
`pulumi config get aws:region`

### Resource Management
|Command|
|----|
`pulumi up`
`pulumi destroy`


### Outputing your export information
|Command|
|----|
`pulumi stack output bucket_name`
`aws s3 ls $(pulumi stack output bucket_name)`

### Pulumi Console
|Command|
|----|
`pulumi console`
