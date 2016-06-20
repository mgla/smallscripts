some smallscripts
============

Collection of small programs that I use every couple of months/years.
Not suitable for production enviroments. Badly written. Modify for your own use.

## backupslapd

Small script that simply calls `slapcat -o ldif-wrap=no -l ldap.diff`.
I do not remember why i scripted that, but there it is. I am not proud of this.
I will keep it as a reminder.

## cronstrip

Makes filenames cron-compatible.
Paul Vixie's cron expects crontab file names in a very specific format, which new users often do not know of.
FILEs in a wrong format will be silently ignored.
Usage:

`cronstrip [FILE]`

## crontablist
## debian_remove_unused_kernels
## dnsbulkcompare

Used to automatically compare a list DNS entries to a given (wanted) result.
See --help for specifics..
## fritsh

Something I saw in a request in a webserver log files.
Allows for remote root access on some FRITZ!Box versions.

## htmlsed
## memorybloat

Script to allocate a specific amount of memory.
Useful to check if ulimits are actually working.
Can definitely kill other processes, use with caution.
Allocates 75 MB of memory by default. Change in source code.

## sshforward
## uid_sorted

Output a sorted and padded list of all uids used on a Linux system.
Makes ugly use of `perl`, `sort` and `getent`.
Usage:
`uid_sorted`
