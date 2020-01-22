#include<stdio.h>
int main(void){
  int N, A, B, sum, ans = 0;
  scanf("%d %d %d", &N, &A, &B);
  for(int i=0;i<=N;i++){
    int j=i;
    sum=0;
    while(j!=0){
      sum=sum+(j%10);
      j=j/10;
    }
    if(sum>=A && sum<=B){
      ans=ans+i;
    }
  }
  printf("%d\n", ans);
  return 0;
}
