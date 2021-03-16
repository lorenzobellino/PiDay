#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TOTAL_POINTS 100000
int main(){
char *c;
  float x,y,pi,distance;
  int circle_points=0;
  srand(time(NULL));
  for(int i=0; i<TOTAL_POINTS; i++){
      x=((double) rand()/RAND_MAX);
      y=((double) rand())/RAND_MAX;
      distance = x*x+y*y;
      if(distance<1) circle_points++;

  }
    pi=(double)4*((double) circle_points/TOTAL_POINTS);
    fprintf(stdout,"Approximated value of Pi : %f\n",pi);
}
