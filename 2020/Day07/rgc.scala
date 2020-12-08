import scala.io.Source
import collection.mutable.Map
import scala.util.matching.Regex

object rgc {
    def main(args: Array[String]) : Unit = {
        val data= Source.fromFile("rgcinput.txt").mkString
        var links= Map[String,Set[(String,Int)]]()
        data.split("\n").map(parseRule(_)).map(addLinks(links,_))
        //for (l <- links) {
            //println(l)
        //}
        val (types,count)= countBags(links,"shinygold")
        println("Part 1",types)
        println("Part 2",count)
    }
    
    def countBags (links : Map[String,Set[(String,Int)]], bag : String) : (Int, Int) = {
        var types= 0
        var count= 0
        //println("Eval "+bag)
        if (! links.contains(bag))
            return (0,0)
        for (l<-links(bag)) {
            //println("Counting "+l._1+" mult "+l._2)
            var (t,c) = countBags(links, l._1)
            types+=t+1
            count+=l._2*(c+1)
        }
        //println(bag+" contains "+types.toString()+" "+count.toString())
        return (types,count)
    
    }
    
    
    def addLinks(links : Map[String,Set[(String,Int)]], pairs : Array[(String,String,Int)]) : Unit = {
        for (oneLink <- pairs) {
            links(oneLink._1) = links.getOrElse (oneLink._1, Set[(String,Int)]()) + ((oneLink._2, oneLink._3))
        }   
    }

    def parseRule(rule: String) : Array[(String,String,Int)] = {
        val strs=rule.split(" ")
        var links=Array[(String,String,Int)]()
        val lhs=strs(0)+strs(1)
        for(i <-5 until strs.length by 4) {
            val str=strs(i)+strs(i+1)
            if (str != "otherbags" & str != "otherbags.") {
                links= links:+ (lhs,str,strs(i-1).toInt)
            }
        }
        //for (l <- links) {
            //println(l)
        //}
        return links
    }
}
