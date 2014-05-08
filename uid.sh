#!/bin/sh
# Author: Maik Glatki
# List UIDs on system, sorted. Useful for ldap/pam, etc.

getent passwd | perl -e 'while (<>){@a = split(/:/); printf "%05d\n",$a[2];}' | sort
