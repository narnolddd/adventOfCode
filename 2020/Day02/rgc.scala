import scala.io.Source

object rgc {
    def main(args: Array[String]) = {
       
        val filename = "rgcinput.txt"
        var lc= 0
        var lc2= 0
        for (line <- Source.fromFile(filename).getLines) {
            val parts= line.split(" ")
            assert(parts.length == 3)
            val minmax=parts(0).split("-").map((s: String) => s.toInt)
            val cc= parts(2).count(_ == parts(1).charAt(0))
            //println(cc,minmax(0),minmax(1))
            if ((cc >= minmax(0)) && (cc <= minmax(1))) 
                lc= lc+ 1
            if (parts(2).charAt(minmax(0)-1) == parts(1).charAt(0) ^
                parts(2).charAt(minmax(1)-1) == parts(1).charAt(0) )
                lc2= lc2+ 1
        }
        println("Matches part 1", lc)
        println("Matches part 2", lc2)
    }
}
