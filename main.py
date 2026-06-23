import os
import sys
from typing import List, Dict
# adds type hints

def get_instance_state(instance_id: str) -> str:
  # returns the state of the specified instance
  mock_instances = {
    "i-1234567890abcdef0": "running",
    "i-0987654321fedcba0": "stopped",
    "i-11111111111111111": "terminated"
  }
  if instance_id not in mock_instances:
    raise ValueError(f"Instance ID {instance_id} not found.")
  return mock_instances[instance_id]

def download_log_from_s3(instance_id: str) -> str:
  # simulates downloading a log file from S3 for the specified instance
  log_file = "mockIISLog.txt"


  if not os.path.exists(log_file):
      raise FileNotFoundError(
         f"Log file '{log_file}' not found."
      )
  return log_file
  # error handles if log file does not exist

def parse_log_file(file_path: str) -> List[Dict]:
   # Parses IIS log entries and returns only HTTP 500 entries.
  errors = []

  with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
      line = line.strip()
    # tracks line numbers for debbugging and strips whitespace from each line
      if not line:
        continue
     # skip IIS metadata lines
      if line.startswith("#"):
        continue

      try:
        parts = line.split()
        # splits the log line into columns
        date = parts[0]
        time = parts[1]
 
        status_code = parts[-2]
        # gets HTTP status code.

        if status_code == "500":
          errors.append({
           "timestamp": f"{date} {time}"
        })
      except Exception:
        print(f"Warning: Malformed log line at line {line_number}")
  return errors

