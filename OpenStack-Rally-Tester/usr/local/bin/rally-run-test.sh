#!/bin/bash

rally_test=$1

echo "This may take some time..."
rally_results_cmd=`rally task start $rally_test | grep "rally task report" | grep "json" | sed 's/output.json//g'`
echo "$rally_results_cmd"
if [[ $rally_results_cmd == *'task'* ]]
then
    rally_task_id=`echo $rally_results_cmd | cut -d" " -f 4`
    echo "$rally_task_id"
    mkdir -p /tmp/results
    rally_results_path="/tmp/results/$rally_task_id"
    echo $rally_results_path
    rally task results $rally_task_id > $rally_results_path;
else
    rally_results_path=$rally_task
    echo $rally_results_path
fi
echo $rally_results_path
rally_extract_command="/usr/local/bin/rally-extract-results.py $rally_results_path"
echo $rally_extract_command
$rally_extract_command

