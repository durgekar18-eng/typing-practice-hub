#!/bin/bash
# Persistent dev server runner
while true; do
  node ./node_modules/.bin/next dev -p 3000 2>&1 | tee dev.log
  echo "Server crashed, restarting in 2s..."
  sleep 2
done
