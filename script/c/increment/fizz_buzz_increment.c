#include <stdio.h>
#include <stdlib.h>
// #include <time.h>

int main(int argc, char *argv[])
{
   int n = atoi(argv[1]); // messy code

   int i;
   int fizzbuzz = 0;
   int fizz = 0;
   int buzz = 0;
   int none = 0;
   for (i = 1; i <= n; i++)
   {
      if (i % 15 == 0)
      {
         fizzbuzz++;
      }
      else if (i % 3 == 0)
      {
         fizz++;
      }
      else if (i % 5 == 0)
      {
         buzz++;
      }
      else
      {
         none++;
      }
   }
   //  printf("elapsed_time:%.2f[sec]\n", ((double)clock()) / CLOCKS_PER_SEC);
   printf("fizzbuzz:%d\n", fizzbuzz);
   printf("fizz:%d\n", fizz);
   printf("buzz:%d\n", buzz);
   printf("none:%d\n", none);
}
