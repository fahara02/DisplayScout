import os
import sys
from pathlib import Path

from displayscout.bootstrap import paths
from displayscout.gui import setGui

# Debugging: Print configured paths
print("Paths configured:")
for name, path in paths.items():
    print(f"{name}: {path}")



def main():
    print("Hello from powerguard!")
    print("Setting up database")

    setGui()
   


if __name__ == "__main__":
    main()
