#!/usr/bin/bash


version=`cat /home/runner/work/SCD-OpenStack-Utils/SCD-OpenStack-Utils/OpenStack-Rabbit-Consumer/version.txt`       #reads the version.txt file and sets the version to the current version


# cuts the $version variable into major, minor and patch numbers removing the fullstop
major=$(echo $version | cut -f1 -d.)
minor=$(echo $version | cut -f2 -d.)
patch=$(echo $version | cut -f3 -d.)


#increments the patch by 1
patch=$((patch + 1))


#concatenate the version
newversion="$major.$minor.$patch"


#overwrites the version.txt file with new new version
printf "$newversion" > /home/runner/work/SCD-OpenStack-Utils/SCD-OpenStack-Utils/OpenStack-Rabbit-Consumer/version.txt