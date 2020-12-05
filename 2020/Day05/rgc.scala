import scala.io.Source
import collection.mutable.Map
import scala.util.matching.Regex

object rgc {
    def main(args: Array[String]) = {
        val seats= Source.fromFile("rgcinput.txt").getLines().to[Array]
        //println(getSeatId("BFFFBBFRRR"))
        println("Part 1",(seats.map(getSeatId(_)).reduceLeft(_ max _)))
        val slist= seats.map(getSeatId(_)).sorted
        object Done extends Exception {}
        try { 
            for (i <- 0 until slist.length -1) {
                if (slist(i) +1 != slist(i+1) ) {
                    println ("Part 2",slist(i) + 1) 
                    throw Done //This is not the scala way really
                }
            }
        } catch {
            case Done =>
        }
    }
    
    def getSeatId (seat : String) : Int = {
        var rowId= 0
        var colId= 0
        for(i <- 0 until 7) {
            if (seat.charAt(i)=='B') 
                rowId= rowId+Math.pow(2,(6-i)).toInt
        }
        for (i <- 0 until 3) {
            if (seat.charAt(i+7) =='R')
                colId= colId+Math.pow(2,(2-i)).toInt
        }
        //println(rowId,colId)
        return rowId*8+colId
    }

}
