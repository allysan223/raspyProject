#include <stdio.h> 
#include <sys/time.h>

int fib(int n) { 
    int a = 0, b = 1, temp, i; 
    if (n == 0) 
        return a; 
    for (i = 2; i <= n; i++) { 
        temp = a + b; 
        a = b; 
        b = temp; 
    } 
    return b;
}
