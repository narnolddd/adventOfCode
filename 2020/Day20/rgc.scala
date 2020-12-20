import scala.io.Source
import scala.collection.mutable.StringBuilder

object rgc {
    def main(args: Array[String]) : Unit = {
        var file="rgcinput.txt"
        if (args.size > 0)
            file=args(0)
        val tileSides= Source.fromFile(file).mkString.split("\n\n").map(_.split("\n")).map(getEdges(_))
        val tileMatches= tileSides.map(matchSides(_,tileSides))
        var answer= 1L
        for ((t,m) <- tileSides.zip(tileMatches)) {
            if (m == 2) {
                answer*=t(0).substring(5,9).toInt
                //println(t(0))
            }

        }
        println("Part1:"+answer)
    }
    
    def matchSides(sides : Array[String], allSides : Array[Array[String]]) : Int = {
        var matches=0
        for ((s,i) <-allSides.view.zipWithIndex) {
            if (s != sides && matchAny(s,sides))
                matches+=1
        }
        return matches
    }
    
    def matchAny(s1 : Array[String], s2 : Array[String]) : Boolean = {
        for (s <- s1) {
            if (s2.contains(s))
                return true
            }
        return false
    }
    
    // Return edges in order top, reversed, bottom, reversed, left, reversed right, reversed
    def getEdges(tile: Array[String]) : Array[String] = {
        val wide= tile(1).length()
        val high= tile.size
        var top= new StringBuilder()
        var bottom= new StringBuilder()
        for (i <- 0 until wide) {
            top += tile(1).charAt(i)
            bottom += tile(high-1).charAt(i)
        }
        var left= new StringBuilder()
        var right=new StringBuilder()
        for (i <- 1 until high) {
            left += tile(i).charAt(0)
            right += tile(i).charAt(wide-1)
        }
        //print(tile(0))
        //print(top,bottom,left,right)
        return Array(tile(0),top.toString(),top.reverse.toString(),bottom.toString(),
            bottom.reverse.toString(), left.toString(), left.reverse.toString(),
            right.toString(),right.reverse.toString())
    }
}





