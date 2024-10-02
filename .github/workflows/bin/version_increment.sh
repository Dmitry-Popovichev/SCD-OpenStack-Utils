#!/usr/bin/bash

echo "Hello World!"
echo ~0
echo "..."
echo ~0/OpenStack-Rabbit-Consumer/version.txt
echo "..."
echo ~/OpenStack-Rabbit-Consumer/version.txt
echo "Bye"

version=`cat ~0/OpenStack-Rabbit-Consumer/version.txt` #reads the version.txt file and sets the version to the current version

# cuts the $version variable into major, minor and patch numbers removing the fullstop
major=$(echo $version | cut -f1 -d.)
minor=$(echo $version | cut -f2 -d.)
patch=$(echo $version | cut -f3 -d.)

echo $major
echo $minor
echo $patch

#increments the patch by 1
patch=$((patch + 1))

echo $patch

#concatenate the version
newversion="$major.$minor.$patch"

echo $newversion

#overwrites the version.txt file with new new version
printf "$newversion" > ~0/OpenStack-Rabbit-Consumer/version.txt

cat ~0/OpenStack-Rabbit-Consumer/version.txt
