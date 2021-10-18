#include <stdio.h>
#include <stdlib.h>
// #include <time.h>

int main(int argc, char *argv[])
{
   int n = atoi(argv[1]); // messy code

   int i;
   for (i = 1; i <= n; i++)
   {
      if (i % 15 == 0)
      {
         puts("fizzbuzz");
      }
      else if (i % 3 == 0)
      {
         puts("fizz");
      }
      else if (i % 5 == 0)
      {
         puts("buzz");
      }
      else
      {
         printf("%d\n", i);
      }
   }
   //  printf("elapsed_time:%.2f[sec]\n", ((double)clock()) / CLOCKS_PER_SEC);
}
