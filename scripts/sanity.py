import sys
import platform
import os
from importlib.metadata import version, PackageNotFoundError

packages = ["numpy", "pandas", "matplotlib", "scipy", "requests", "pytest"]

print("=== Python Environment Sanity Check ===")
print("Python version:", sys.version)
print("Platform:", platform.platform())
print("Working directory:", os.getcwd())

print("\nPackage versions:")
for pkg in packages:
    try:
        print(f"{pkg}: {version(pkg)}")
    except PackageNotFoundError:
        print(f"{pkg}: NOT FOUND")

