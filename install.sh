#!/bin/bash

# Prevent install if root
if [ $(whoami) = 'root' ]; then
    echo 'Cannot run as root'
    exit 1
fi

source utils.sh

# Functions
function install_from_script() {
    local $to_install
    local $scripts_dir
    bash "$scripts_dir/install_$to_install.sh"
}

# Installs
source "$(this_folder)/installs/.env.installs"
mkdir_if "$USER_BINS"
prepend_to_PATH "$USER_BINS"

for_item_in_list_do "$INSTALLS" "install_from_script" "$(this_folder)/installs"


