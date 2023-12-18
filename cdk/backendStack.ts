import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

export class BackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const env: string = process.env.DEPLOY_ENV || "dev";

    const table = new dynamodb.TableV2(this, `table-${env}`, {
      partitionKey: { name: "pk", type: dynamodb.AttributeType.STRING },
      billing: dynamodb.Billing.onDemand(),
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      tags: [{ key: "deployEnv", value: env }],
    });

    const apiHandler = new lambda.Function(this, `function-${env}`, {
      code: lambda.Code.fromAsset("../backend/lambda"),
      handler: "handler.handler",
      runtime: lambda.Runtime.PYTHON_3_10,
    });

    table.grantReadWriteData(apiHandler);
    apiHandler.addEnvironment("TABLE_NAME", table.tableName);
  }
}
