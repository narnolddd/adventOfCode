import scala.io.Source
import scala.collection.mutable.ArrayBuffer

object rgc {
    def main(args: Array[String]) : Unit = {
        val jolts= Source.fromFile("rgcinput.txt").mkString.split("\n").map(_.toInt).sorted.toList
        //println(jolts)
        val diffs= (0 :: jolts).sliding(2).map(x=>x(1)-x(0)).toList
        val threes= diffs.filter(_ == 3).size+1
        val ones=diffs.filter(_ == 1).size
        println("Part 1:"+ones+" "+threes+" "+ (ones*threes))
        //println(diffs)
        println("Part 2:"+letMeCountTheWays(diffs))
    }
    def letMeCountTheWays(diffs : List[Int]) : Long = {
        var total=1L
        var path= ArrayBuffer[Int]()
        for (d<-diffs){
            if (d == 3) {
                //println(path)
                val c=countPath(0,path)
                
                total*=c
                //println(c,total)
                path= ArrayBuffer[Int]()
            } else {
                path.append(d)
            }
            //println("Total "+total)
        }
        //println(path)
        total*=countPath(0, path)
        return total
    }
    
    def countPath(start: Int, jumps : ArrayBuffer[Int]) : Int = {
        
        if (jumps.size < 1)
            return 1
        var i= 0
        var paths= 0
        while (i < jumps.size && start+jumps(i) <= 3) {
            paths+= countPath(start+jumps(i), jumps.slice(i+1,jumps.size))
            i+=1
        }
        return paths
    }
}




