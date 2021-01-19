from m5.util import addToPath

addToPath("/home/nanoproj/michael/gem5/configs/sys-emu/config-files")
addToPath("/home/nanoproj/michael/gem5/configs/")

import spec17_benchmarks

def getBenchmark(options):
    print("Selected SPEC_CPU2017 Benchmark")
    if(options == '500.perlbench_r'):
        print("--> 500.perlbench_r")
        process = spec17_benchmarks.perlbench_r
    elif(options == '502.gcc_r'):
        print("--> 502.gcc_r")
        process = spec17_benchmarks.gcc_r
    elif(options == '503.bwaves_r'):
        print("--> 503.bwaves_r")
        process = spec17_benchmarks.bwaves_r
    elif(options == '505.mcf_r'):
        print("--> 505.mcf_r")
        process = spec17_benchmarks.mcf_r
    elif(options == '507.cactuBSSN_r'):
        print("--> 507.cactuBSSN_r")
        process = spec17_benchmarks.cactuBSSN_r
    elif(options == '508.namd_r'):
        print("--> 508.namd_r")
        process = spec17_benchmarks.namd_r
    elif(options == '510.parest_r'):
        print("--> 510.parest_r")
        process = spec17_benchmarks.parest_r
    elif(options == '511.povray_r'):
        print("--> 511.povray_r")
        process = spec17_benchmarks.povray_r
    elif(options == '519.lbm_r'):
        print("--> 519.lbm_r")
        process = spec17_benchmarks.lbm_r
    elif(options == '520.omnetpp_r'):
        print("--> 520.omnetpp_r")
        process = spec17_benchmarks.omnetpp_r
    elif(options == '521.wrf_r'):
        print("--> 521.wrf_r")
        process = spec17_benchmarks.wrf_r
    elif(options == '523.xalancbmk_r'):
        print("--> 523.xalancbmk_r")
        process = spec17_benchmarks.xalancbmk_r
    elif(options == '525.x264_r'):
        print("--> 525.x264_r")
        process = spec17_benchmarks.x264_r
    elif(options == '526.blender_r'):
        print("--> 526.blender_r")
        process = spec17_benchmarks.blender_r
    elif(options == '527.cam4_r'):
        print("--> 527.cam4_r")
        process = spec17_benchmarks.cam4_r
    elif(options == '531.deepsjeng_r'):
        print("--> 531.deepsjeng_r")
        process = spec17_benchmarks.deepsjeng_r
    elif(options == '538.imagick_r'):
        print("--> 538.imagick_r")
        process = spec17_benchmarks.imagick_r
    elif(options == '541.leela_r'):
        print("--> 541.leela_r")
        process = spec17_benchmarks.leela_r
    elif(options == '544.nab_r'):
        print("--> 544.nab_r")
        process = spec17_benchmarks.nab_r
    elif(options == '548.exchange2_r'):
        print("--> 548.exchange2_r")
        process = spec17_benchmarks.exchange2_r
    elif(options == '554.roms_r'):
        print("--> 554.roms_r")
        process = spec17_benchmarks.roms_r
    elif(options == '557.xz_r'):
        print("--> 557.xz_r")
        process = spec17_benchmarks.xz_r
    elif(options == '600.perlbench_s'):
        print("--> 600.perlbench_s")
        process = spec17_benchmarks.perlbench_s
    elif(options == '602.gcc_s'):
        print("--> 602.gcc_s")
        process = spec17_benchmarks.gcc_s
    elif(options == '603.bwaves_s'):
        print("--> 603.bwaves_s")
        process = spec17_benchmarks.bwaves_s
    elif(options == '605.mcf_s'):
        print("--> 605.mcf_s")
        process = spec17_benchmarks.mcf_s
    elif(options == '607.cactuBSSN_s'):
        print("--> 607.cactuBSSN_s")
        process = spec17_benchmarks.cactuBSSN_s
    elif(options == '619.lbm_s'):
        print("--> 619.lbm_s")
        process = spec17_benchmarks.lbm_s
    elif(options == '620.omnetpp_s'):
        print("--> 620.omnetpp_s")
        process = spec17_benchmarks.omnetpp_s
    elif(options == '621.wrf_s'):
        print("--> 621.wrf_s")
        process = spec17_benchmarks.wrf_s
    elif(options == '623.xalancbmk_s'):
        print("--> 623.xalancbmk_s")
        process = spec17_benchmarks.xalancbmk_s
    elif(options == '625.x264_s'):
        print("--> 625.x264_s")
        process = spec17_benchmarks.x264_s
    elif(options == '627.cam4_s'):
        print("--> 627.cam4_s")
        process = spec17_benchmarks.cam4_s
    elif(options == '628.pop2_s'):
        print("--> 628.pop2_s")
        process = spec17_benchmarks.pop2_s
    elif(options == '631.deepsjeng_s'):
        print("--> 631.deepsjeng_s")
        process = spec17_benchmarks.deepsjeng_s
    elif(options == '638.imagick_s'):
        print("--> 638.imagick_s")
        process = spec17_benchmarks.imagick_s
    elif(options == '641.leela_s'):
        print("--> 641.leela_s")
        process = spec17_benchmarks.leela_s
    elif(options == '644.nab_s'):
        print("--> 644.nab_s")
        process = spec17_benchmarks.nab_s
    elif(options == '648.exchange2_s'):
        print("--> 648.exchange2_s")
        process = spec17_benchmarks.exchange2_s
    elif(options == '649.fotonik3d_s'):
        print("--> 649.fotonik3d_s")
        process = spec17_benchmarks.fotonik3d_s
    elif(options == '654.roms_s'):
        print("--> 654.roms_s")
        process = spec17_benchmarks.roms_s
    elif(options == '657.xz_s'):
        print("--> 657.xz_s")
        process = spec17_benchmarks.xz_s
    elif(options == '996.specrand_fs'):
        print("--> 996.specrand_fs")
        process = spec17_benchmarks.specrand_fs
    elif(options == '997.specrand_fr'):
        print("--> 997.specrand_fr")
        process = spec17_benchmarks.specrand_fr
    elif(options == '998.specrand_is'):
        print("--> 998.specrand_is")
        process = spec17_benchmarks.specrand_is
    elif(options == '999.specrand_ir'):
        print("--> 999.specrand_ir")
        process = spec17_benchmarks.specrand_ir
    else:
        print("--> Invalid Benchmark Name Exiting.")
        sys.exit(1)

    return process