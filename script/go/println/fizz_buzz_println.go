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

	// start := time.Now()
    for i := 1; i <= n; i++ {
        switch {
        case i%15 == 0:
            fmt.Printf("fizzbuzz\n")
        case i%3 == 0:
            fmt.Printf("fizz\n")
        case i%5 == 0:
            fmt.Printf("buzz\n")
        default:
            fmt.Printf("%d", i)
        }
    }
    // fmt.Printf("elapsed_time:%.4f[sec]\n", time.Now().Sub(start).Seconds())
}
