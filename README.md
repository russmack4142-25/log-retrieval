# EC2 IIS Diagnostic Tool

## Overview

This script automates the initial diagnostic process for EC2 instances experiencing CPU spikes.

It:

1. Accepts an EC2 Instance ID
2. Mocks EC2 state retrieval
3. Mocks downloading IIS logs from S3
4. Parses IIS logs
5. Filters HTTP 500 errors
6. Outputs a summary

---

## Requirements

Python 3.9+ or later

---

## Run

```bash
python main.py i-1234567890abcdef0
```