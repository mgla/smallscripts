#!/bin/sh
# Ugly script to backup a slapd ldap database.

FILE=ldap.diff
if [ ! -e $FILE ]; then
	echo "creating backup as $FILE"
	slapcat -v -l ldap.diff
	exit 0
else
	echo "$FILE exists, aborting."
	exit 1
fi
