#!/bin/sh
# Ugly script to backup a slapd ldap database.
set -u

FILE=ldap.diff
if [ ! -e $FILE ]; then
	echo "creating backup as $FILE"
	slapcat -o ldif-wrap=no -l ldap.diff
	exit 0
else
	echo "$FILE exists, aborting."
	exit 1
fi
