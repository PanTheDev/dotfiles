#!/bin/bash

source "$(dirname "${BASH_SOURCE[1]}")/utils.sh"
source "$(this_folder)/.env.installs"

# Install jq
if [ -z $(command -v jq) ]; then
    pixi global install jq
fi

function get_value_from_json() {
    local json_string=$1
    local key=$2

    echo $(echo "$json_string" | jq -r ".$key")
}

# Get url of latest tarball
tarball_url=$(get_value_from_json "$(curl -s 'https://api.github.com/repos/funtoo/keychain/releases/latest')" 'tarball_url')

# download tarball
mkdir -p "$HOME/downloads/"
curl -o "$HOME/downloads/keychain.tar.gz" "$tarball_url"

# install
install_tar_gz "$HOME/downloads/keychain.tar.gz" "$USER_BINS/keychain"



