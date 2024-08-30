#!/bin/bash
NULL_FILE='.null'
THIS_FILE=$( if [ -n "${BASH_SOURCE[1]}" ]; then echo $(realpath "${BASH_SOURCE[1]}"); else echo "$(realpath $(dirname "${BASH_SOURCE[0]}"))/$NULL_FILE"; fi)

function for_item_in_list_do() {
    local list=$1
    local action=$2
    local args="${@:3}"
    for item in $list; do
        eval "$action $item $args"
    done
}

function append_to_list() {
    local list=$1
    local new_item=$2
    if [ -z "$list" ]; then
        list="$new_item"
    else
        list+=" $new_item"
    fi
    echo "$list"
}

function parent_folder() {
    local path=$1
    realpath "$(dirname "$path")"
}

function this_folder() {
    parent_folder $(this_file) || echo $THIS_FILE
}

function this_file() {
    local file_name=$(basename "$THIS_FILE")
    if [ "$file_name" == "$NULL_FILE" ]; then
        return 1
    else
        echo "$THIS_FILE"
    fi
}

function replace_or_add_line() {
    local file_path=$1
    local prefix=$2
    local new_line=$3

    if grep -q "^$prefix" "$file_path"; then
        sed -i "s|^$prefix.*|$new_line|" "$file_path"
    else
        printf "$new_line" >> "$file_path"
    fi
}

function insert_after_prefix_in_file() {
    local file_path=$1
    local prefix=$2
    local to_insert=$3
    if grep -q "^$prefix" "$file_path"; then
        sed -i "s|^$prefix\(.*\)|$prefix$to_insert\1|" "$file_path"
    else
        printf "%s%s" "$prefix" "$to_insert" >> "$file_path"
    fi
}

function insert_after_line_in_file() {
    local file_path=$1
    local prefix=$2
    local to_insert=$3
    if grep -q "^$prefix" "$file_path"; then
        sed -i "s|^$prefix.*|&$to_insert|" "$file_path"
    else
        printf "%s%s\n" "$prefix" "$to_insert" >> "$file_path"
    fi
}

function get_line_after_prefix() {
    local file_path=$1
    local prefix=$2
    grep "^$prefix" "$file_path" | sed "s/^$prefix//"
}

function add_quotes_to_rest_in_line() {
    local file_path=$1
    local prefix=$2
    if ! grep -q "^$prefix\"" "$file_path"; then
        sed -i "s/^$prefix\([^\"]*\)/$prefix\"\1\"/" "$file_path"
    fi
}

function prepend_to_PATH() {
    local to_prepend=$1
    local bashrc_file="$HOME/.bashrc"
    insert_after_prefix_in_file "$bashrc_file" 'export PATH="' "$to_prepend:"
    add_quotes_to_rest_in_line "$bashrc_file" 'export PATH='
}

# function append_to_PATH() {
#     local to_append=$1
#     local bashrc_file="$HOME/.bashrc"
#     insert_after_line_in_file "$bashrc_file" 'export PATH=' ":$to_append"
#     add_quotes_to_rest_in_line "$bashrc_file" 'export PATH='
# }

function mkdir_if() {
    local dirname=$1
    mkdir -p "$dirname"
}

function install_tar_gz() {
    local tar_file=$1
    local install_dir=$2

    # Extract the tar.gz file to the install directory
    tar -xvzf "$tar_file" -C "$install_dir" || return $?
}