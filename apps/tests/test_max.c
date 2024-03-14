#include <stdio.h>

extern float max_pts(float a, float b);

int main() {
    float a = 3.0;
    float b = 14.0;
    float result = max_pts(a, b);
    printf("O maior valor é: %f\n", result);
    return 0;
}