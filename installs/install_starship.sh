#!/bin/bash
source "$(dirname "${BASH_SOURCE[1]}")/utils.sh"

# Install starship
if [ -z $(pixi global list | grep starship ) ]; then
    pixi global install starship
fi

# Configure starship
cp -p "$(parent_folder "$(this_folder)")/configs/starship.toml" "$HOME/.config/starship.toml"