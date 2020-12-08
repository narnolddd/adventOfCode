import scala.io.Source
import collection.mutable.Map
import scala.util.matching.Regex

object rgc {
    def main(args: Array[String]) : Unit = {
        val data= Source.fromFile("rgcinput.txt").mkString
        var links= Map[String,Set[String]]()
        data.split("\n").map(parseRule(_)).map(addLinks(links,_))
        //for (l <- links) {
            //println(l)
        //}
        var toVisit= links("shinygold").toList
        var visited= Set[String]()
        while (toVisit.size > 0) {
            val visiting= toVisit(0)
            toVisit= toVisit.drop(1)
            visited += visiting
            if (links.contains(visiting)) {
                val add= links(visiting)
                for (a<-add) {
                    if (!(visited.contains(a))) {
                        toVisit ::=  a
                        //println("Adding",a)
                    }
                }
                
            }
            //for (v <- toVisit) {
                //print(v+" ")
            //}
            println()
        }
        //for (v <-visited) {
            //println(v)
        //}
        println("Part 1",visited.size)
    }
    
    def addLinks(links : Map[String,Set[String]], pairs : Array[(String,String)]) : Unit = {
        for (oneLink <- pairs) {
            links(oneLink._2) = links.getOrElse (oneLink._2, Set[String]()) + oneLink._1
        }   
    }

    def parseRule(rule: String) : Array[(String,String)] = {
        val strs=rule.split(" ")
        var links=Array[(String,String)]()
        val lhs=strs(0)+strs(1)
        for(i <-5 until strs.length by 4) {
            val str=strs(i)+strs(i+1)
            if (str != "otherbags" & str != "otherbags.") {
                links= links:+ (lhs,str)
            }
        }
        //for (l <- links) {
            //println(l)
        //}
        return links
    }
}
