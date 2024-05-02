#!/usr/bin/env bash

set -uo pipefail
IFS=$'\n\t'

check_git_history=false

rm -f tmp-unused-images
rm -f tmp-unused-images-history

# List images which might be unused.
# Exceptions are ignored, and for .svg files we also look for potential .png
# files with the same base name, as they might be sources.

files=$(find -name "_build" -prune -o \( -iname "*.png" -o -iname "*.webp" -o -iname "*.jpg" -o -iname "*.svg" -o -iname "*.gif" \) -print | sort)

for path in $files; do
  file=$(basename "$path")
  if [[ "$path" == *./img/* ]]; then
    continue
  fi
  ext=${file##*.}
  base=${file%.*}
  found=$(rg -l ":: .*[ /]$file")
  if [ -z "$found" ] && [ "$ext" == "svg" ]; then
    # May be source file.
    found=$(rg -l ":: .*[ /]$base.png")
  fi
  if [ -z "$found" ]; then
    echo "$path" >> tmp-unused-images
  fi
done

echo "Wrote list of unused images to: tmp-unused-images"

if [ "$check_git_history" = true ]; then
  for file in $(cat tmp-unused-images); do
    echo "File: $file"
    git log --diff-filter=A --follow "$file"
    echo
  done > tmp-unused-images-history
  echo "Wrote list of unused images in Git history to: tmp-unused-images-history"
fi
