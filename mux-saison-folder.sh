#!/bin/bash
cd $1
List=$(ls *.mkv | grep -oP "S..E..")
for episode in $List
do
 FileName=$(echo *$episode*".mkv")
 oldTag="-Vyndros.mkv"
 newTag=".NoTag.mkv"
 outFileName=$(echo "${FileName/$oldTag/$newTag}")
 mkvmerge -o $outFileName *$episode*".mkv" --language "0:fre" *$episode*".srt"
done