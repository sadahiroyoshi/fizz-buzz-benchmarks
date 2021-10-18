object FizzBuzzIncrement {
  def main(args: Array[String]): Unit = {
    var n:Int = args(0).toInt

    var fizzbuzz:Int = 0
    var fizz:Int = 0
    var buzz:Int = 0
    var none:Int = 0

    // val startTime = System.currentTimeMillis
    for(i <- 1 to n) {
      if (i%3==0 && i%5==0) {
        fizzbuzz += 1
      } else if (i%3==0) {
        fizz += 1
      } else if (i%5==0) {
        buzz += 1
      } else {
        none += 1
      }
    }
    // match is slower than simple for loop
    // for(i <- 1 to 100000) (i % 3, i % 5) match {
    //   case (0, 0) => fizzbuzz += 1
    //   case (0, _) => fizz += 1
    //   case (_, 0) => buzz += 1
    //   case _      => none += 1
    // }

    // val endTime = System.currentTimeMillis()
    // println("elapsed_time:" + ((endTime - startTime)/1000.00) + "[sec]")
    println("fizzbuzz:" + fizzbuzz)
    println("fizz:" + fizz)
    println("buzz:" + buzz)
    println("none:" + none)
  }
}
