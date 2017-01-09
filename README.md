# twitter-spam
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Lambda functions that, when deployed via the included CloudFormation template, will endlessly post spam to a twitter account. Two functions are included:

- _text_: Tweets a random UUID
- _qrcode_: Tweest an image containing a QR code of a random UUID

## Services Used

These are all of the services assembled to make this work.

### AWS

- [CloudFormation](https://aws.amazon.com/cloudformation/)
- [Lambda](https://aws.amazon.com/lambda/)
- [CodePipeline](https://aws.amazon.com/codepipeline/)
- [CodeBuild](https://aws.amazon.com/codebuild/)
- [SAM](http://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html)
- [S3](https://aws.amazon.com/s3/)

## Contact

If you've got questions or want to chat about this project, the best bet is to @mention me on twitter. My handle is [@ywxwy](https://twitter.com/ywxwy). All other public contact info is on [tom.horse](https://tom.horse).
