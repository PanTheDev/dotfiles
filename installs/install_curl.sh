#!/bin/bash

source "$(dirname "${BASH_SOURCE[1]}")/utils.sh"
source "$(this_folder)/.env.installs"

# Check if curl is available and install it otherwise
if [ -z $(command -v curl) ]; then
    apt-get download curl
    CURL_DEB=$(ls *curl*.deb)
    dpkg -x $CURL_DEB $USER_BINS
    if ! command -v curl &> /dev/null; then
        echo failed to install curl
        exit 1
    fi
fi