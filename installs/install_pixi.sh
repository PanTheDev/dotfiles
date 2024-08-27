#!/bin/bash

source ../utils.sh

# Install pixi
if [ -z $(command -v pixi) ]; then
    curl -fsSL https://pixi.sh/install.sh | bash
fi

prepend_to_PATH "$HOME/.pixi/bin"
