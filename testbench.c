#include <stdio.h> 
#include <sys/time.h>

int fib(int n) { 
    if (n <= 1) 
        return n; 
    return fib(n - 1) + fib(n - 2); 
} 
  
int main() { 

    struct timeval stop, start;
    gettimeofday(&start, NULL);

    int n = 30;
    int fibNum = fib(n);

    gettimeofday(&stop, NULL);
    printf("took %lu us\n", (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec); 


    return 0; 
} 