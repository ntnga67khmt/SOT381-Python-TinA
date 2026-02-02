#include <stdio.h>

int main() {
    float mark_1, mark_2, mark_3, rate_1, rate_2, TB;

    printf("Nhap diem qua trinh (mark_1): ");
    scanf("%f", &mark_1);

    printf("Nhap diem giua ky (mark_2): ");
    scanf("%f", &mark_2);

    printf("Nhap diem cuoi ky (mark_3): ");
    scanf("%f", &mark_3);

    printf("Nhap ty le diem qua trinh (rate_1): ");
    scanf("%f", &rate_1);

    printf("Nhap ty le diem giua ky (rate_2): ");
    scanf("%f", &rate_2);

    TB = mark_1 * rate_1 + mark_2 * rate_2 + (1 - rate_1 - rate_2) * mark_3;

    printf("Diem trung binh (TB) = %.2f", TB);

    if (TB >= 5)
        printf("Sinh vien DAT hoc phan NMLT");
    else
        printf("Sinh vien KHONG DAT hoc phan NMLT");

    return 0;
}
