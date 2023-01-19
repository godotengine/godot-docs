#!/bin/bash

check_git_history=false

rm -f tmp-unused-images
rm -f tmp-unused-images-history

# List images which might be unused.
# Exceptions are ignored, and for .svg files we also look for potential .png
# files with the same base name, as they might be sources.

exceptions="docs_logo.svg tween_cheatsheet.png"

files=$(find -name "_build" -prune -o \( -name "*.png" -o -name "*.jpg" -o -name "*.svg" -o -name "*.gif" \) -print | sort)

for path in $files; do
  file=$(basename $path)
  if echo "$exceptions" | grep -q "$file"; then
    continue
  fi
  ext=${file##*.}
  base=${file%.*}
  found=$(rg -l ":: .*[ /]$file")
  if [ -z "$found" -a "$ext" == "svg" ]; then
    # May be source file.
    found=$(rg -l ":: .*[ /]$base.png")
  fi
  if [ -z "$found" ]; then
    echo "$path" >> tmp-unused-images
  fi
done


if [ "$check_git_history" = true ]; then
  for file in $(cat tmp-unused-images); do
    echo "File: $file"
    git log --diff-filter=A --follow $file
    echo
  done > tmp-unused-images-history
fi
