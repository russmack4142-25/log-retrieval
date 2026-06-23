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