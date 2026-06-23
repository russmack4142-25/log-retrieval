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
 
        status_code = parts[-4]
        # gets HTTP status code.

        if status_code == "500":
          errors.append({
           "timestamp": f"{date} {time}"
        })
      except Exception:
        print(f"Warning: Malformed log line at line {line_number}")
  return errors

def print_summary(
    instance_id: str,
    instance_state: str,
    errors: List[Dict]
) -> None:
  # prints a summary of the log retrieval process
  print("\n===========Diagnostic summary===========")
  print(f"Instance ID: {instance_id}")
  print(f"Instance State: {instance_state}")
  print(f"Number of HTTP 500 errors found: {len(errors)}")
  
  if errors:
    print("Timestamps of HTTP 500 errors:")
    
    for error in errors:
      print(f"- {error['timestamp']}")

def main():
  if len(sys.argv) != 2:
    print("Usage: python main.py <instance_id>")
    sys.exit(1)

  instance_id = sys.argv[1]

  try:
    instance_state = get_instance_state(instance_id)
    log_file_path = download_log_from_s3(instance_id)
    errors = parse_log_file(log_file_path)
    print_summary(instance_id, instance_state, errors)
  except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

if __name__ == "__main__":
  main()

