# Personal Finance App

## Basic Requirements

three pages
1. single form with date/description/amount/category that submits to DB
2. page shows all transactions
3. page shows analysis of transactions (budget/category/etc)

## Advanced Requirements
1. login system to personalize transcations

## Techincal Requirements
1. qa/prod CI/CD with github actions

## Technical Notes
### CDK Notes
Construct - a single AWS resource or a higher-level abstraction for multiple resources

Stack - all constructs that represent AWS resources must be defined in a Stack. A stack needs to be deployed into an environment consisting of an account number and region

App - container for one or more Stacks

### Installation
```
$ npm install -g aws-cdk
```

OIDC https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/


```
$ cd cdk
$ cdk bootstrap aws://645293059982/us-east-1
$ cdk synth
$ cdk deploy
```
Account Number `645293059982`

Account Region `us-east-1`


cdk/
backend/
frontend/

