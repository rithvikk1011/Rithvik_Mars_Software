mkdir rover_mission
cd rover_mission
touch log1.txt
touch log2.txt
touch log3.txt
mv log1.txt mission_log.txt
find *.txt
cat mission_log.txt
grep "error" mission_log.txt
wc -l mission_log.txt
date
top -o cpu
sudo shutdown +10
