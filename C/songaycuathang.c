#include<stdio.h>
int main(){
	int n,y;
	scanf("%d\n%d",&n,&y);
	switch (n){
		case(1):case(3):case(5):case(7):case(8):case(10):
		case(12):printf("thang co 31 ngay");break;
		case(4):case(6):case(9):
		case(11):printf("thang co 30 ngay");break;
		case(2):
		if (y%100==0 ||(y%4==0&&y%100!=0)){
	 	printf("thang 2 co 29 ngay");break;
		}
		else{
	 	printf("thang 2 co 28 ngay");break;
		}
	default:printf("thang khong hop le");
	}
	return 0;
}