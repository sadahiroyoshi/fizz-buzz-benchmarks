package main

import (
    "flag"
	"strconv"
    "fmt"
    // "time"
)

func main() {
    flag.Parse()
    n, _ := strconv.Atoi(flag.Args()[0])

    fizzbuzz := 0
    fizz := 0
    buzz := 0
    none := 0

	// start := time.Now()
	for i := 1; i <= n; i++ {
        switch {
        case i%15 == 0:
            fizzbuzz++;
        case i%3 == 0:
            fizz++;
        case i%5 == 0:
            buzz++;
        default:
            none++;
        }
    }
    // switch is faster than if-else.
	// for i := 1; i <= n; i++ {
	// 	if i % 3 == 0 && i % 5 == 0 {
	// 		fizzbuzz++
	// 	} else if i % 3 == 0 {
	// 		fizz++
	// 	} else if i % 5 == 0 {
	// 		buzz++
	// 	} else {
	// 		none++
	// 	}
	// }
    // fmt.Printf("elapsed_time:%.4f[sec]\n", time.Now().Sub(start).Seconds())
    fmt.Printf("fizzbuzz:%v\n", fizzbuzz)
    fmt.Printf("fizz:%v\n", fizz)
    fmt.Printf("buzz:%v\n", buzz)
    fmt.Printf("none:%v\n", none)
}
