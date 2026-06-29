"""
Day 0 - Environment Check

Automation Engineering Bootcamp

Author: Abuzaid Khattak
"""

import os
import platform
import sys

print("=" * 50)
print("Automation Engineering Bootcamp")
print("=" * 50)

print(f"Python Version : {sys.version}")
print(f"Operating System : {platform.system()}")
print(f"OS Version : {platform.version()}")
print(f"Machine : {platform.machine()}")
print(f"Current Directory : {os.getcwd()}")

print("=" * 50)
print("Environment Ready ✅")