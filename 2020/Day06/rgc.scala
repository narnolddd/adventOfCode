import scala.io.Source
import collection.mutable.Map
import scala.util.matching.Regex

object rgc {
    def main(args: Array[String]) = {
        val data= Source.fromFile("rgcinput.txt").mkString
        val ps= data.split("\n\n").map(_.trim).map(_.filterNot("\n".toSet)).map(_.toSet).map(_.size).sum
        println("Part 1",ps)
        val ps2= data.split("\n\n").map(_.trim).map(countSet).sum
        println("Part 2",ps2)
    }

    def countSet(lists: String) : Int = {
        
        lists.split("\n").map(_.toSet).reduceRight(_ & _).size
    }
}
