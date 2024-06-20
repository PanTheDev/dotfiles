#!/bin/bash

# Prevent install if root
if [ $(whoami) = 'root' ]; then
    echo 'Cannot run as root'
    exit 1
fi

USER_HOME=/home/$(whoami)
USER_BINS=/home/$(whoami)/bin
mkdir -p $USER_BINS
export PATH=$PATH:$USER_BINS

# Check if curl is available and install it otherwise
if command -v curl &> /dev/null; then
    apt-get download curl
    CURL_DEB=$(ls *curl*.deb)
    dpkg -x $CURL_DEB $USER_BINS
    if ! command -v curl &> /dev/null; then
        echo failed to install curl
        exit 1
    fi
fi

# Install pixi
if ! command -v pixi &> /dev/null; then
    curl -fsSL https://pixi.sh/install.sh | bash
fi

# Install chezmoi
(cd $USER_HOME; curl -fsLS get.chezmoi.io | bash )
if ! command -v chezmoi &> /dev/null; then
    echo failed to install chezmoi
    exit 1
fi

