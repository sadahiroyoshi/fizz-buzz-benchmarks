object FizzBuzzPrintln {
  def main(args: Array[String]): Unit = {
    var n:Int = args(0).toInt

    // val startTime = System.currentTimeMillis
    for(i <- 1 to n) {
      if (i%3==0 && i%5==0) {
        println("fizzbuzz")
      } else if (i%3==0) {
        println("fizz")
      } else if (i%5==0) {
        println("buzz")
      } else {
        printf("%d", i)
      }
    }

    // val endTime = System.currentTimeMillis()
    // println("elapsed_time:" + ((endTime - startTime)/1000.00) + "[sec]")
  }
}
