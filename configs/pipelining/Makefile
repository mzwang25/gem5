INC= -I/home/nanoproj/michael/gem5/include
LNK= -lm -L"/home/nanoproj/michael/gem5/util/m5/build/x86/out" -lm5
m5= ~/michael/gem5/util/m5

all: daxpy.o m5_map.o m5op.o
	#gc
	g++ daxpy.o m5_map.o m5op.o ${INC} ${LNK} --static -o2 -o daxpy

daxpy.o : daxpy.cc
	g++ $< -o $@ -c

m5_map.o : ${m5}/src/m5_mmap.c
	g++ $< -o $@ -c ${INC}

m5op.o : ${m5}/src/x86/m5op.S
	g++ $< -o $@ -c ${INC}

clean:
	rm -rf daxpy.o m5_map.o m5op.o daxpy