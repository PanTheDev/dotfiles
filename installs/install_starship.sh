#!/bin/bash

# Install starship
if [ -z $(pixi global list | grep starship ) ]; then
    pixi global install starship
fi

# Configure starship
cp -p ./configs/starship.toml "$HOME/.config/starship.toml"