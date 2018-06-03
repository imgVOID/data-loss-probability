# Servers failure simulator with data loss probability calculation.
Prints results to command line.
Has 2 modes:
1) "-n num --random" num servers with random allocation of 2 replicas of 0 < data < 100.
2) "-n num --mirror" num servers with num\2 servers with evenly allocated 0 < data < 100, and full backup servers 1 per each server.
