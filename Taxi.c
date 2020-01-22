#include<stdio.h>
int main(void){
  double x = 0;
  int n = 0;
  scanf("%lf", &x);
  if(x < 5){
    printf("800");
  }else{
    n = (int)((x-5)/2) + 1;
    printf("%d", 800+n*400);
  }
  return 0;
}
