#!/bin/bash
set -e
# Build package release

increment_version() {
  local delimiter=.
  local array=($(echo "$1" | tr $delimiter '\n'))
  array[$2]=$((array[$2]+1))
  echo $(local IFS=$delimiter ; echo "${array[*]}")
}

release_string="$(python setup.py --version | grep -Eo '^[0-9]+\.[0-9]+\.[0-9]+')"

echo "Version (last) $release_string"
# $release_string
version_new="$(increment_version $release_string 2)"
echo "Version (new)  $version_new"
tag_name="$(echo -n "v$version_new")"
echo "Create git tag $tag_name"
git tag $tag_name
echo "Push tags"
git push --tags
