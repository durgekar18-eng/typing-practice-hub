#!/bin/bash
cd /home/z/my-project
export PATH="/home/z/.bun/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
export HOME="/home/z"

while true; do
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting Next.js dev server..." >> /home/z/my-project/dev.log
  /home/z/my-project/node_modules/.bin/next dev -p 3000 >> /home/z/my-project/dev.log 2>&1
  EXIT_CODE=$?
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Server exited (code=$EXIT_CODE). Restarting in 3s..." >> /home/z/my-project/dev.log
  sleep 3
done
