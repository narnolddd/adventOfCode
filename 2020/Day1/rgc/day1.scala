import scala.io.Source
import scala.collection.mutable.ArrayBuffer


object day1 {
    def main(args: Array[String]) = {
        var nums = ArrayBuffer[Int]()
        val filename = "rgcinput.txt"
        for (line <- Source.fromFile(filename).getLines) {
            val i= line.toInt
            nums+= i
        }
        var i = 0
        var j = 0
        for (i <- 0 to nums.length-1) {
            for (j <- 0 to i) {

                if (nums(i) + nums(j) == 2020) {
                    println ("Two",nums(i)*nums(j))
                }
                for (k <- 0 to j) {
                    if (nums(i) + nums (j) + nums(k) == 2020) {
                        println ("Three",nums(i)*nums(j)*nums(k))
                    }
                }
            }
        }
    }
}
