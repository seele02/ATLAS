#!/bin/bash

CONFIGFILE="env.cfg"

#echo "Reading config...." >&2
#source ./env.cfg
#echo "Config for the username: $cool_username" >&2
#echo "Config for the target host: $cool_host" >&2


$HOME/ATLAS/start_flightgear.sh & $HOME/ATLAS/start_MAV.sh && fg
