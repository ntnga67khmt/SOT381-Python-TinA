#include <stdio.h>

int main() {
    int a, b;

    printf("Nhap a: ");
    scanf("%d", &a);

    printf("Nhap b: ");
    scanf("%d", &b);

    if (a > b) {
        printf("a max = %d\n", a);
        printf("b min = %d\n", b);
    } else {
        printf("a min = %d\n", a);
        printf("b max = %d\n", b);
    }

    return 0;
}