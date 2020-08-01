#include <stdio.h>
#include <stdlib.h>

// Sieve of Eratosthenes
int main(int argc, char** argv) {


    if(argc != 2)
    {
        printf("usage: ./thisprog <prime num>\n");
        exit(1);
    }

    unsigned int n = atoi(argv[1]);
    unsigned int* values = malloc(sizeof(unsigned int) * n / 8 + 1); 

    unsigned long p = 2;
    unsigned int prime_count = 0;

    while(p < n) {
        prime_count++;
        unsigned int i;

        for(i = 2; i * p < n; i++) {
            values[i * p / 8] |= 0x1 << (i * p) % (8);
        }

        char isFound = 0;
        for(i = p + 1; i < n; i++) {
            if(!(values[i / 8] & (0x1 << (i) % 8))) {
                p = i;
                isFound = 1;
                break;
            }
        }
        if(!isFound) {
            break;
        }
    }

    printf("%d\n", prime_count);
    return 0;
}