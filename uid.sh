#!/bin/sh
# Author: Maik Glatki
# get highest UID on system, useful for ldap/pam, etc.

getent passwd | perl -e 'while (<>){@a = split(/:/); printf "%05d\n",$a[2];}' | sort
