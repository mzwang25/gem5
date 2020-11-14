# ex. ./mkstats.sh RESULTS/ 
# Assumes dir consists of a list of gem5 outputs
# Goes inside each of those dir and prints all sim_seconds as csv

DIR=$1

for BENCH in `ls $DIR`
do
    echo -n "${BENCH},"
    cat ${DIR}${BENCH}/stats.txt \
        | grep "sim_seconds" \
        | grep -o "[0-9.]*" \
        | tr "\n" "," \
        | sed '$s/,$/\n/'
done




