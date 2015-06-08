#!/bin/sh
# remove unused kernels in debian. Included newer kernels than the running one.

apt-get remove $(dpkg -l| egrep '^ii  linux-(im|he)'| grep -v linux-image-virtual | awk '{print $2}'| grep -v $(uname -r))

echo "Done. Now run aptitude upgrade to fix broken stuff, please."
