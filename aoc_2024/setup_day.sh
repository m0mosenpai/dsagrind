#!/bin/sh

new_dir="day_$1"
mkdir $new_dir && cd $new_dir
touch "$1.in" "$1.ex" "$1.go"
