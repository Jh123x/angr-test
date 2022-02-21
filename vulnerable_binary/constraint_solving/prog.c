#include <stdio.h>
#include <stdlib.h>

void main(int argc, char *argv[]){
    if (argc != 3) {
        printf("Usage: %s <int> <int>\n", argv[0]);
        exit(1);
    }
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    if (10 > a && a > 5 && 10 > b && b > 1 && 2 * b - a == 10){
        printf("Solved! %d, %d\n", a, b);
    }
}