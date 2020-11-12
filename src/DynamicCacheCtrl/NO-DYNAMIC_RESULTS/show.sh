DIR=$1
cat ${DIR}_b/stats.txt | grep "sim_seconds"
cat ${DIR}_m/stats.txt | grep "sim_seconds"
cat ${DIR}_e/stats.txt | grep "sim_seconds"
cat ${DIR}_f/stats.txt | grep "sim_seconds"
