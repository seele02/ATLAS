#!/bin/bash

cd /home/cormac/ATLAS/ardupilot/ArduCopter && x-terminal-emulator -e sim_vehicle.py -j4 -L KSFO --aircraft test --out=udp:127.0.0.1:14552


