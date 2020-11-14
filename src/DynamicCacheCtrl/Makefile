CWD=/home/nanoproj/michael/gem5/src/DynamicCacheCtrl
OUTDIR=${CWD}/RESULTS

build:
	~/michael/bin/g5b

test:
	./run_gem5_spec17_benchmark.sh lbm_r ${OUTDIR}/test 3000000

lbm_r:
	./run_gem5_spec17_benchmark.sh lbm_r ${OUTDIR}/lbm_r 5000000

gcc_r:
	./run_gem5_spec17_benchmark.sh gcc_r ${OUTDIR}/gcc_r 5000000

mcf_r:
	./run_gem5_spec17_benchmark.sh mcf_r ${OUTDIR}/mcf_r  5000000

cactuBSSN_r:
	./run_gem5_spec17_benchmark.sh cactuBSSN_r ${OUTDIR}/cactuBSSN_r 5000000

namd_r:
	./run_gem5_spec17_benchmark.sh cactuBSSN_r ${OUTDIR}/namd_r  5000000

parest_r:
	./run_gem5_spec17_benchmark.sh parest_r ${OUTDIR}/parest_r  5000000

povray_r:
	./run_gem5_spec17_benchmark.sh parest_r ${OUTDIR}/povray_r  5000000


omnetpp_r:
	./run_gem5_spec17_benchmark.sh omnetpp_r ${OUTDIR}/omnetpp_r  5000000

spec:
	make lbm_r&
	make gcc_r&
	make mcf_r&
	make cactuBSSN_r&
	make namd_r&
	make parest_r&
	make povray_r&
	make omnetpp_r&
