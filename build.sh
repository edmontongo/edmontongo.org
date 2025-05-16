#!/bin/bash
[ -z "${1}" ] && BURL="https://edmontongo.org" || BURL="${1}"
echo "${BURL}"
export HUGO_ENVIRONMENT="production"
export HUGO_ENV="production"
hugo --gc --minify -F -b "${BURL}"
