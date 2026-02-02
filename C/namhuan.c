#include<stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	if (n%100==0 ||(n%4==0&&n%100!=0)){
	 	printf("%d la nam nhuan");
	}
	else{
	 	printf("%d khong la nam nhuan");
	}
	return 0;
}
