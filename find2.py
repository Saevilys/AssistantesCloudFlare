#!/usr/bin/env python3
"""Find Mentari and Suchada images anywhere on desk."""
import os, subprocess

result = subprocess.run(["find", "/images", "/images-keep", "-name", "*mentari*", "-o", "-name", "*suchada*"], 
                       capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
