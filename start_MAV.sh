#!/bin/bash

cd /home/cormac/ATLAS/ardupilot/ArduCopter && x-terminal-emulator -e sim_vehicle.py -j4 -L AVC_copter --aircraft test --out=udp:127.0.0.1:14552


