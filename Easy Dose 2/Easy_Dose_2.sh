#!/bin/bash

battery=$((RANDOM % 101))
echo "Battery level: $battery%"

if [ $battery -lt 20 ]; then
    echo "Battery low! Return to base!"
    exit 1
fi

ping -c 1 google.com > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Communication failure!"
    exit 1
fi

echo "All systems operational!"
