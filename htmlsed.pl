#!/usr/bin/perl
# Small script for converting bad written html
# author: Maik Glatki
# example usage:
# find . -iname '*.html' | perl ~/sed.pl

use Tie::File;

use strict;
use warnings;

while(<>)
{ 
  chomp;
  print "tie-ing file $_\n";
  my $filename = $_;
  my @array;
  tie @array, 'Tie::File', $filename or die "Can not tie file: $filename\n";
  foreach (@array)
  {
    s/Plone Default/PloneDefault/g;
    s/ü/&uuml;/g;
    s/Ü/&Uuml;/g;
    s/Ä/&Auml;/g;
    s/ä/&auml;/g;
    s/ö/&ouml;/g;
    s/Ö/&Ouml;/g;
    s/ß/&szlig;/g;
    s/á/&aacute;/g;
    s/Á/&Aacute;/g;
    s/€/&euro;/g;
  }
  untie @array;  
}
print "done\n";
