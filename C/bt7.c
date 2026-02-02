#include <stdio.h>

int main() {

    int N, n1, n2, n3, n4, n5,S;

    printf("Nhap so xe N (gom 5 chu so): ");
    scanf("%d", &N);

    n5 = N % 10;
    N = N / 10;

    n4 = N % 10;
    N = N / 10;

    n3 = N % 10;
    N = N / 10;

    n2 = N % 10;
    N = N / 10;

    n1 = N;

    S = (n1 + n2 + n3 + n4 + n5) % 10;

    printf("So nut S = %d\n", S);

    return 0;
}