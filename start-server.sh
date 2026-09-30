#!/bin/bash
cd /home/z/my-project
while true; do
  echo "=== Starting dev server at $(date) ===" >> /home/z/my-project/dev.log
  bun run dev >> /home/z/my-project/dev.log 2>&1
  EXIT_CODE=$?
  echo "=== Server exited with code $EXIT_CODE, restarting in 3s ===" >> /home/z/my-project/dev.log
  sleep 3
done
