#!/bin/bash
# Keepalive wrapper for the Next.js dev server
# Monitors the server process and restarts it if it dies

LOGFILE="/home/z/my-project/dev.log"
SERVER_CMD="next dev -p 3000"

while true; do
  echo "[$(date)] Starting Next.js dev server..." >> "$LOGFILE"
  $SERVER_CMD >> "$LOGFILE" 2>&1
  EXIT_CODE=$?
  echo "[$(date)] Server exited with code $EXIT_CODE. Restarting in 3s..." >> "$LOGFILE"
  sleep 3
done
