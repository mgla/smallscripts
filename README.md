some smallscripts
============

Collection of small programs that I use every couple of months/years.
Not suitable for production enviroments. Badly written. Modify for your own use.

## backupslapd

Small script that simply calls `slapcat -o ldif-wrap=no -l ldap.diff`. I do not remember why i scripted that, but there it is. I am not proud of this.

## cronstrip

Makes filenames cron-compatible. Paul Vixie's cron expects crontab file names in a very specific format, which new users often do not know of. FILEs in a wrong format will be silently ignored.
Usage:

`cronstrip [FILE]`

## crontablist
## debian_remove_unused_kernels
## dnsbulkcompare
## fritzbox.remote.manager

Something I saw in a request in a webserver log files. Allows for remote root access on some FRITZ!Box versions.

## htmlsed
## memorybloat
## sshforward
## uid_sorted

Output a sorted and padded list of all uids used on a Linux system. Makes ugly use of `perl`, `sort` and `getent`.
Usage:
`uid_sorted`
