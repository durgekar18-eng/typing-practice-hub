#!/bin/bash
cd /home/z/my-project

# Double-fork to properly daemonize
(
  trap "" SIGHUP SIGTERM SIGINT
  while true; do
    bun run dev >> /home/z/my-project/dev.log 2>&1
    sleep 3
  done
) &
echo $!
