import scala.io.Source
import scala.collection.mutable.StringBuilder

object rgc {
    def main(args: Array[String]) : Unit = {
        var file="rgcinput.txt"
        if (args.size > 0)
            file=args(0)
        val hands= Source.fromFile(file).mkString.split("\n\n").map(toHand(_))
        var hand1= hands(0)._2
        var hand2= hands(1)._2
        while (hand1.size > 0 && hand2.size > 0) {
            val c1= hand1(0)
            val c2= hand2(0)
            hand1= hand1.drop(1)
            hand2= hand2.drop(1)
            if (c1 > c2) {
                hand1= hand1 :+ c1 :+ c2
            } else {
                hand2= hand2 :+ c2 :+ c1
            }
        }
        var hand= Array[Int]()
        if (hand1.size > 0)
            hand= hand1.reverse
        else
            hand= hand2.reverse
        var tot= 0L
        var i= 1
        for (h<-hand) {
            tot+= h*i
            i+= 1
            hand= hand.drop(1)
        }
        println("Part 1 "+tot)
    }
  
  
    def toHand(alltext : String) : (Int, Array[Int]) = {
        val text= alltext.split("\n")
        var pno = text(0).substring(7,8).toInt
        var arr = new Array[Int](0)
        for (t <- text.drop(1)) {
                arr= arr :+ t.toInt
        }
        //println(pno)
        //for (a <-arr) 
            //println(a)
        return (pno,arr)
    }
}





