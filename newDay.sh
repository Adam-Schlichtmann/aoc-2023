YEAR=2023

SHORT_DAY=$1
echo "Downloading Day $SHORT_DAY"
FULL_DAY=$(printf "%02d" $SHORT_DAY)

mkdir DAY_$FULL_DAY
cd DAY_$FULL_DAY
touch $FULL_DAY.py 
touch INPUT_$FULL_DAY.txt
cd ../

SESSION=$(cat cookie.txt)
curl -s -b "session=${SESSION}" https://adventofcode.com/${YEAR}/day/${SHORT_DAY}/input > DAY_${FULL_DAY}/INPUT_${FULL_DAY}.txt