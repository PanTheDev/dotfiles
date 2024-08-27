#!/bin/bash

# Install openssh
if [ -z $(command -v ssh) ] || [ -z $(pixi global list | grep openssh ) ]; then
    pixi global install openssh
fi
