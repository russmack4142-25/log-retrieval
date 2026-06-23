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
python3 main.py i-1234567890abcdef0
```

## ERROR HANDLING

- Invalid EC2 Instance ID's
- Missing log files
- Empty log files
- Malformed log entries

---

## LIMITATIONS

This script does not handle any of the following:

- AWS authentication
- Real S3 downloads
- Multiple IIS log formats
- Compressed ZIP extraction
- Possible timezone conversion
- Very large log files (>GB scale).

_This project was written in Python as it's the only programming language i have used on a day
to day basis.  I can convert this into a typescript version using ChatGPT if necessary but i wouldn't
be able to explain the code if needed, in an interview.  I am more than willing to expand my knowledge by
learning typescript prior to any role i am offered._

