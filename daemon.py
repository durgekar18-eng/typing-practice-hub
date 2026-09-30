#!/usr/bin/env python3
"""Double-fork daemon that keeps the Next.js dev server alive."""
import os, sys, time, subprocess, signal

def main():
    # First fork
    if os.fork() > 0:
        sys.exit(0)
    os.setsid()
    # Second fork
    if os.fork() > 0:
        sys.exit(0)
    os.chdir('/home/z/my-project')
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    
    while True:
        proc = subprocess.Popen(
            ['npx', 'next', 'dev', '-p', '3000'],
            stdout=open('/home/z/my-project/dev.log', 'w'),
            stderr=subprocess.STDOUT,
            cwd='/home/z/my-project'
        )
        proc.wait()
        with open('/home/z/my-project/dev.log', 'a') as f:
            f.write(f'\n[DAEMON] Server exited code={proc.returncode}. Restarting...\n')
        time.sleep(2)

if __name__ == '__main__':
    main()
