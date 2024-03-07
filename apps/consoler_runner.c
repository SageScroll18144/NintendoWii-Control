#include <stdio.h>
#include <stdlib.h>
#include <omp.h>


int main(){

    printf("* HELLO TO OUR CONSOLE *\n");

    #pragma omp parallel num_threads(2)
    {
        #pragma omp single
        {
            printf("\n* loading boot...\n");
            system("python3 boot.py");
        }
        
        #pragma omp single
        {
            printf("\n* loading application...\n");
            system("python3 menu.py");
        }
    }

    return 0;
}