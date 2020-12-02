CWD=/home/nanoproj/michael/gem5/src/DynamicCacheCtrl
OUTDIR=${CWD}/RESULTS

build:
	~/michael/bin/g5b

stat:
	@./mkstats.sh ${OUTDIR}/

test:
	./run_one.sh lbm_r ${OUTDIR}/test 3000000


spec:
	#rm -rf ${OUTDIR}
	./run_all.sh ${OUTDIR} 7000000

