#!/usr/bin/env bash
# Test script

# Make test directory
mkdir test/

# Copy code to test directory
cp yiffer-dl.py test/

# Move the the test directory and run the code
cd test/
python3 yiffer-dl.py https://yiffer.xyz/Trust%20Me%20-%20alt.%20ending

# Assert the './dl/ exists
if [ -d dl/ ]; then 
  # List the directory and open it in feh
  ls -al dl/
  feh dl/
else
  echo "Test fail, no dl directory"
fi

echo "Press enter to continue"
read

echo "Cleaning up..."

cd ..
rm -r test
