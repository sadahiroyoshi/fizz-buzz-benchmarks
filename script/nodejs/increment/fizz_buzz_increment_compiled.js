var a=process.argv[2],b=0,c=0,d=0,e=0;for(i=1;i<=a;i++)0===i%15?b++:0===i%3?c++:0===i%5?d++:e++;console.log("fizzbuzz:"+b);console.log("fizz:"+c);console.log("buzz:"+d);console.log("none:"+e);
