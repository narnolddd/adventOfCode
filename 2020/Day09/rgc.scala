import scala.io.Source
import scala.collection.mutable.ListBuffer

object rgc {
    def main(args: Array[String]) : Unit = {
        val data= Source.fromFile("rgcinput.txt").mkString.split("\n").map(_.toLong)
        var i= 25
        while  (validate(data,i) ) {
            i+= 1
        }
        println("Part 1", data(i))
        val seekit= data(i)
        for (i <-0 to data.size-1) {
            var tot= 0L
            var j=i
            while (tot < seekit) {
                tot+= data(j)
                j+=1
            }
            if (tot == seekit) {
                val min=data.slice(i,j).min
                val max=data.slice(i,j).max
                println("Part 2",max+min)
                return
            }
        }
    }
    
    // HORRENDOUSLY INEFFICIENT but it is quick to write
    def validate(data : Array[Long], i : Int) : Boolean = {
        val list= for(x <- i-25 to i-1; y <- i-25 to x-1) yield (data(x)+data(y)==data(i))
        list.contains(true)
    }
}




