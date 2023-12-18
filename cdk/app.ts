#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { BackendStack } from "./backendStack";

const app = new cdk.App();

const env: string = process.env.DEPLOY_ENV || "dev";

new BackendStack(app, `backend-stack-${env}`, {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
