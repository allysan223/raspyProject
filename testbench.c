#include <stdio.h> 
#include <sys/time.h>

int fib(int n) { 
    if (n <= 1) 
        return n; 
    return fib(n - 1) + fib(n - 2); 
} 
  
int main() { 
    int i;
    struct timeval stop, start;
    unsigned long runTimes[10];

    for (i = 0; i < 10; ++i){
        gettimeofday(&start, NULL);
        int fibNum = fib(30);
        gettimeofday(&stop, NULL);
        runTimes[i] = (stop.tv_sec - start.tv_sec) * 1000 + (stop.tv_usec - start.tv_usec) / 1000;
    }

    // printf("took %lu ms\n", (stop.tv_sec - start.tv_sec) * 1000 + (stop.tv_usec - start.tv_usec) / 1000); 

    for (i = 0; i < 10; ++i){
        printf("took %lu ms\n", runTimes[i]);
    }

    return 0; 
} 