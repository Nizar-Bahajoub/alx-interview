#!/usr/bin/python3
""" Script That Reads From stdin and compute metrics """


import sys
import signal
import re


""" Initializations """
lines_count = 0
total_size = 0
status_code_counts = {
        '200' : 0,
        '301' : 0,
        '400' : 0,
        '401' : 0,
        '403' : 0,
        '404' : 0,
        '405' : 0,
        '500' : 0
}

#The pattern that the line should follow
"""log_pattern = r'''^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3)} - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "GET /projects/260 HTTP/1.1" (200|301|400|401|403|404|405|500) (\d+)$'''
pattern = re.compile(log_pattern)
"""

#Signal Hundler for (Ctrl + C)
def interrupt_handler(sig, frame):
    print_metrics()
    sys.exit(0)


#Print_metrics Function
def print_metrics():
    global total_size, status_code_counts
    print("Total file size: {}".format(total_size))

    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


#Adding Signal Hundler
signal.signal(signal.SIGINT, interrupt_handler)


#Reading Input lines
try:
    while True:

        """ Pattern check """
        line = sys.stdin.readline().strip()
        #match = pattern.match(line)

        '''if not match:
            continue'''

        file_size = int(line.split()[-1])
        status_code = line.split()[-2]

        total_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] +=1

        lines_count +=1


        if lines_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
        print_metrics()
        sys.exit(0)
