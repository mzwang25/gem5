import m5
from m5.objects import Process
import os

#Assumes current directory is in cpu/[BENCH]/run/run*/
suffix = "_base.mytest-m64"

#500.perlbench_r
perlbench_r = Process()
perlbench_r.executable = './perlbench_r' + suffix
perlbench_r.cmd = [perlbench_r.executable] + '-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1'.split(' ')

#502.gcc_r
gcc_r = Process()
gcc_r.executable = 'cpugcc_r' + suffix
gcc_r.cmd = [gcc_r.executable] + 'gcc-pp.c -O3 -finline-limit=0 -fif-conversion -fif-conversion2 -o gcc-pp.opts-O3_-finline-limit_0_-fif-conversion_-fif-conversion2.s'.split(' ')

#503.bwaves_r
bwaves_r = Process()
bwaves_r.executable = 'bwaves_r' + suffix
bwaves_r.cmd = [bwaves_r.executable] + '< bwaves_1.in'.split(' ')

#505.mcf_r
mcf_r = Process()
mcf_r.executable = 'mcf_r' + suffix
mcf_r.cmd = [mcf_r.executable] + 'inp.in'.split(' ')

#507.cactuBSSN_r
cactuBSSN_r = Process()
cactuBSSN_r.executable = 'cactusBSSN_r' + suffix
cactuBSSN_r.cmd = [cactuBSSN_r.executable] + 'spec_ref.par'.split(' ')

#508.namd_r
namd_r = Process()
namd_r.executable = 'namd_r' + suffix
namd_r.cmd = [namd_r.executable] + ' --input apoa1.input --output apoa1.ref.output --iterations 65 '.split(' ')

#510.parest_r
parest_r = Process()
parest_r.executable = 'parest_r' + suffix
parest_r.cmd = [parest_r.executable] + 'ref.prm'.split(' ')

#511.povray_r
povray_r = Process()
povray_r.executable = 'povray_r' + suffix
povray_r.cmd = [povray_r.executable] + 'SPEC-benchmark-ref.ini'.split(' ')

#519.lbm_r
lbm_r = Process()
lbm_r.executable = 'lbm_r' + suffix
lbm_r.cmd = [lbm_r.executable] + '3000 reference.dat 0 0 100_100_130_ldc.of'.split(' ')

#520.omnetpp_r
omnetpp_r = Process()
omnetpp_r.executable = 'omnetpp_r' + suffix
omnetpp_r.cmd = [omnetpp_r.executable] + ' -c General -r 0'.split(' ')

#521.wrf_r
wrf_r = Process()
wrf_r.executable = 'wrf_r' + suffix
wrf_r.cmd = [wrf_r.executable] + ''.split(' ')

#523.xalancbmk_r
xalancbmk_r = Process()
xalancbmk_r.executable = 'cpuxalan_r' + suffix
xalancbmk_r.cmd = [xalancbmk_r.executable] + '-v t5.xml xalanc.xsl'.split(' ')

#525.x264_r
x264_r = Process()
x264_r.executable = 'x264_r' + suffix
x264_r.cmd = [x264_r.executable] + '--pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720'.split(' ')

#526.blender_r
blender_r = Process()
blender_r.executable = 'blender_r' + suffix
blender_r.cmd = [blender_r.executable] + 'sh3_no_char.blend --render-output sh3_no_char_ --threads 1 -b -F RAWTGA -s 849 -e 849 -a'.split(' ')

#527.cam4_r
cam4_r = Process()
cam4_r.executable = 'cam4_r' + suffix
cam4_r.cmd = [cam4_r.executable] + ''.split(' ')

#531.deepsjeng_r
deepsjeng_r = Process()
deepsjeng_r.executable = 'deepsjeng_r' + suffix
deepsjeng_r.cmd = [deepsjeng_r.executable] + 'ref.txt'.split(' ')

#538.imagick_r
imagick_r = Process()
imagick_r.executable = 'imagick_r' + suffix
imagick_r.cmd = [imagick_r.executable] + '-limit disk 0 refrate_input.tga -edge 41 -resample 181% -emboss 31 -colorspace YUV -mean-shift 19x19+15% -resize 30% refrate_output.tga'.split(' ')

#541.leela_r
leela_r = Process()
leela_r.executable = 'leela_r' + suffix
leela_r.cmd = [leela_r.executable] + 'ref.sgf'.split(' ')

#544.nab_r
nab_r = Process()
nab_r.executable = 'nab_r' + suffix
nab_r.cmd = [nab_r.executable] + '1am0 1122214447 122'.split(' ')

#548.exchange2_r
exchange2_r = Process()
exchange2_r.executable = 'exchange2_r' + suffix
exchange2_r.cmd = [exchange2_r.executable] + '6'.split(' ')

#554.roms_r
roms_r = Process()
roms_r.executable = 'roms_r' + suffix
roms_r.cmd = [roms_r.executable] + '< ocean_benchmark2.in.x'.split(' ')

#557.xz_r
xz_r = Process()
xz_r.executable = 'xz_r' + suffix
xz_r.cmd = [gcc_r.executable] + 'cld.tar.xz 160 19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474 59796407 61004416 6'.split(' ')

#600.perlbench_s
perlbench_s = Process()
perlbench_s.executable = 'perlbench_s' + suffix
perlbench_s.cmd = [gcc_r.executable] + '-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1'.split(' ')

#620.gcc_s
gcc_s = Process()
gcc_s.executable = 'sgcc' + suffix
gcc_s.cmd = [gcc_s.executable] + 'gcc-pp.c -O5 -fipa-pta -o gcc-pp.opts-O5_-fipa-pta.s'.split(' ')

#603.bwaves_s
bwaves_s = Process()
bwaves_s.executable = 'speed_bwaves' + suffix
bwaves_s.cmd = [bwaves_s.executable] + 'bwaves_1 < bwaves_1.in'.split(' ')

#605.mcf_s
mcf_s = Process()
mcf_s.executable = 'mcf_s' + suffix
mcf_s.cmd = [mcf_s.executable] + 'inp.in'.split(' ')

#607.cactuBSSN_s
cactuBSSN_s = Process()
cactuBSSN_s.executable = 'cactuBSSN_s' + suffix
cactuBSSN_s.cmd = [cactuBSSN_s.executable] + 'spec_ref.par'.split(' ')

#619.lbm_s
lbm_s = Process()
lbm_s.executable = 'lbm_s' + suffix
lbm_s.cmd = [lbm_s.executable] + '2000 reference.dat 0 0 200_200_260_ldc.of'.split(' ')

#620.omnetpp_s
omnetpp_s = Process()
omnetpp_s.executable = 'omnetpp_s' + suffix
omnetpp_s.cmd = [omnetpp_s.executable] + '-c General -r 0 '.split(' ')

#621.wrf_s
wrf_s = Process()
wrf_s.executable = 'wrf_s' + suffix
wrf_s.cmd = [wrf_s.executable] + ''.split(' ')

#623.xalancbmk_s
xalancbmk_s = Process()
xalancbmk_s.executable = 'xalancbmk_s' + suffix
xalancbmk_s.cmd = [xalancbmk_s.executable] + '-v t5.xml xalanc.xsl'.split(' ')

#625.x264_s
x264_s = Process()
x264_s.executable = 'x264_s' + suffix
x264_s.cmd = [x264_s.executable] + '--pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720 '.split(' ')

#627.cam4_s
cam4_s = Process()
cam4_s.executable = 'cam4_s' + suffix
cam4_s.cmd = [cam4_s.executable] + ''.split(' ')

#628.pop2_s
pop2_s = Process()
pop2_s.executable = 'speed_pop2' + suffix
pop2_s.cmd = [pop2_s.executable] + ''.split(' ')

#631.deepsjeng_s
deepsjeng_s = Process()
deepsjeng_s.executable = 'deepsjeng_s' + suffix
deepsjeng_s.cmd = [deepsjeng_s.executable] + 'ref.txt'.split(' ')

#638.imagick_s
imagick_s = Process()
imagick_s.executable = 'imagick_s' + suffix
imagick_s.cmd = [imagick_s.executable] + 'limit disk 0 refspeed_input.tga -resize 817% -rotate -2.76 -shave 540x375 -alpha remove -auto-level -contrast-stretch 1x1% -colorspace Lab -channel R -equalize +channel -colorspace sRGB -define histogram:unique-colors=false -adaptive-blur 0x5 -despeckle -auto-gamma -adaptive-sharpen 55 -enhance -brightness-contrast 10x10 -resize 30% refspeed_output.tga'.split(' ')

#641.leela_s
leela_s = Process()
leela_s.executable = 'leela_s' + suffix
leela_s.cmd = [leela_s.executable] + 'ref.sgf'.split(' ')

#644.nab_s
nab_s = Process()
nab_s.executable = 'nab_s' + suffix
nab_s.cmd = [nab_s.executable] + '3j1n 20140317 220 '.split(' ')

#648.exchange2_s
exchange2_s = Process()
exchange2_s.executable = 'exchange2_s' + suffix
exchange2_s.cmd = [exchange2_s.executable] + '6'.split(' ')

#649.fotonik3d_s
fotonik3d_s = Process()
fotonik3d_s.executable = 'fotonik3d_s' + suffix
fotonik3d_s.cmd = [fotonik3d_s.executable] + ''.split(' ')

#654.roms_s
roms_s = Process()
roms_s.executable = 'sroms' + suffix
roms_s.cmd = [roms_s.executable] + ''.split(' ')

#657.xz_s
xz_s = Process()
xz_s.executable = 'xz_s' + suffix
xz_s.cmd = [xz_s.executable] + 'cpu2006docs.tar.xz 6643 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1036078272 1111795472 4'.split(' ')

#996.specrand_fs
specrand_fs = Process()
specrand_fs.executable = 'specrand_fs' + suffix
specrand_fs.cmd = [specrand_fs.executable] + '1255432124 234923'.split(' ')

#997.specrand_fr
specrand_fr = Process()
specrand_fr.executable = 'specrand_fr' + suffix
specrand_fr.cmd = [specrand_fr.executable] + '1255432124 234923'.split(' ')

#998.specrand_is
specrand_is = Process()
specrand_is.executable = 'specrand_is' + suffix
specrand_is.cmd = [specrand_is.executable] + '1255432124 234923'.split(' ')

#999.specrand_ir
specrand_ir = Process()
specrand_ir.executable = 'specrand_ir' + suffix
specrand_ir.cmd = [specrand_ir.executable] + '1255432124 234923'.split(' ')
