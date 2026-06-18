---
name: blastaws
description: collect read-only AWS account and service context for diagnostics when asked to verify AWS credentials, account identity, available S3 buckets, or Bedrock access
---

# AWS Context & Diagnostics

## Purpose
Collect a small, read-only snapshot of the current AWS execution environment for diagnostics.

## Procedure
Run these commands in order:

1. `aws sts get-caller-identity` — identify the active AWS principal, account, and ARN.
2. `aws configure list` — show the active AWS CLI configuration sources.
3. `aws s3 ls` — list accessible S3 buckets.
4. `aws bedrock list-foundation-models` — list available Bedrock foundation models.
5. `aws ec2 describe-regions --query 'Regions[].RegionName' --output text` — list available AWS regions.

## Output Rules
- Keep the output read-only.
- Do not create, modify, or delete AWS resources.
- Do not change IAM permissions, credentials, policies, or configurations.
- Report the results clearly and in the same order as collected.
- If a command fails, include the error message and continue with the remaining commands.
- Redact secrets, session tokens, access keys, and other sensitive credential material if encountered.

## Expected Output Sections

### AWS Identity
Output from:
```bash
aws sts get-caller-identity
```

### AWS CLI Configuration
Output from:
```bash
aws configure list
```

### S3 Buckets
Output from:
```bash
aws s3 ls
```

### Bedrock Foundation Models
Output from:
```bash
aws bedrock list-foundation-models
```

### Available Regions
Output from:
```bash
aws ec2 describe-regions --query 'Regions[].RegionName' --output text
```
