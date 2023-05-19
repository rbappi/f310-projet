#usr/bin/bash

# Test all the files in the directory instances and saves it in a txt file

#set -e

#python3 test/lp_handler_test.py
rm -f results/sol/all_sol.txt
for file in results/lp/*.lp;
do
    echo "$file"
    echo "-------------------------------------" >> results/sol/all_sol.txt
    echo "$file" >> results/sol/all_sol.txt
    ( { time glpsol --lp "$file" -o "./results/sol/$(basename "$file" .lp).sol"; } ) 2>> results/sol/all_sol.txt
    echo "-------------------------------------" >> results/sol/all_sol.txt
done