#!/bin/sh
# remove unused kernels in debian. Included newer kernels than the running one.

apt-get remove $(dpkg -l| egrep '^ii  linux-(im|he)'|awk '{print $2}'| grep -v $(uname -r))
