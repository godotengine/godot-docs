#!/usr/bin/env bash

set -uo pipefail

output=$(grep -r -P '^(?!\s*\.\.).*\S::$' --include='*.rst' --exclude='docs_writing_guidelines.rst' .)
if [[ -n $output ]]; then
  echo 'The shorthand codeblock syntax (trailing `::`) is not allowed.'
  echo "$output"
  exit 1
fi
