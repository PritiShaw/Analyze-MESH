#!/bin/bash
path_to_java=$1
path_to_disease=$2
email=$3
declare -a StringArray=("Aging" "CommunicableDiseases" "ComputationalBiology" "Neoplasms" "Neurosciences" )
for val in ${StringArray[@]}; do
    cp $path_to_disease/script.sh $path_to_disease/$val
    cd $path_to_disease/$val
    ./script.sh $path_to_java $path_to_disease/$val $email
done
