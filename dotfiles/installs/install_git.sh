#!/bin/bash

source "$(dirname "${BASH_SOURCE[1]}")/utils.sh"

# Install git
if [ -z $(command -v git) ] || [ -z $(pixi global list | grep git ) ]; then
    pixi global install git
fi

# Copy git config
config_file="$HOME/.config/git/config"
includes_dir="$HOME/.config/git/includes"
mkdir -p "$includes_dir"

to_include=""
# includes the existing .config/git/config if it's not already the main one
if [ -f "$HOME/.gitconfig" ]; then
    existing_config="$includes_dir/found_gitconfig"
    mv "$HOME/.gitconfig" "$existing_config"
    to_include=$(append_to_list "$to_include" "$existing_config")
fi
# includes the existing .gitconfig if it's not already the main one
if [ -f "$config_file" ] && ! grep -q "# Pan's config" "$config_file"; then
    existing_config="$includes_dir/found_config"
    mv "$config_file" "$existing_config"
    to_include=$(append_to_list "$to_include" "$existing_config")
fi

if ! grep -q "# Pan's config" "$config_file"; then
    cp "$(parent_folder "$this_folder")/configs/.gitconfig" "$config_file"
fi

# Add an include at the beginning of a .gitconfig file without overriding existing includes
function add_include() {
    local include_path="$1"
    local gitconfig_path="$2"

    # Check if the include already exists in the gitconfig file
    if grep -q "^\[include\]" "$gitconfig_path"; then
        # Check if the include path is already present
        if grep -q "path = $include_path" "$gitconfig_path"; then
            return
        fi
        # Add the include at the beginning of the include section
        sed -i "/^\[include\]/a\path = $include_path" "$gitconfig_path"
    else
        # Create the include section and add the include
        sed -i "/^#/!{1,/^$/!{1,/^#/!b}}" "$gitconfig_path"
        sed -i "/^#/a\[include]\npath = $include_path" "$gitconfig_path"
    fi
}

for_item_in_list_do "$to_include" "add_include" "$config_file"
