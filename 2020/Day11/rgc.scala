import scala.io.Source
import scala.collection.mutable.ArrayBuffer

object Floor extends Enumeration {
    type Floor = Value
    val Free= Value('L')
    val Occupied= Value('#')
    val Empty=Value('.')
    val OutOfRange=Value('X')
}


import Floor._

object rgc {


    def main(args: Array[String]) : Unit = {
        var file="rgcinput.txt"
        if (args.size > 0) {
            file=args(0)
        }
        val seats= Source.fromFile(file).mkString.split("\n")
        var newSeats= seats.map(new StringBuilder(_))
        var oldSeats= newSeats.map(_.clone)
        do {
            oldSeats= newSeats.map(_.clone)
            val dirns=List((-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1))
            for(x <- 0 until seats(0).size; y<-0 until seats.size) {
                //println(occup((x,y),oldSeats))
                val surround= dirns.map(xy=> occup((x+xy._1, y+xy._2),oldSeats))
                //println(x+" "+y+" "+surround)
                if (occup((x,y),oldSeats) == Free && surround.filter(_ == Occupied).size == 0)
                    newSeats(y)(x)='#'
                if (occup((x,y),oldSeats) == Occupied && surround.filter(_ == Occupied).size >= 4)
                    newSeats(y)(x)='L'
            }
            //for (n<-newSeats) 
             //   println(n)
        }
        while (oldSeats.deep != newSeats.deep);
        println("Part 1",newSeats.map(_.count(_ == '#')).sum)
        newSeats= seats.map(new StringBuilder(_))
        oldSeats= newSeats.map(_.clone)
        do {
            oldSeats= newSeats.map(_.clone)
            val dirns=List((-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1))
            for(x <- 0 until seats(0).size; y<-0 until seats.size) {
                //println(occup((x,y),oldSeats))
                val surround= dirns.map(xy=> occupInDir((x,y),xy,oldSeats))
                //println(x+" "+y+" "+surround)
                if (occup((x,y),oldSeats) == Free && surround.filter(_ == Occupied).size == 0)
                    newSeats(y)(x)='#'
                if (occup((x,y),oldSeats) == Occupied && surround.filter(_ == Occupied).size >= 5)
                    newSeats(y)(x)='L'
            }
            //for (n<-newSeats) 
             //   println(n)
        }
        while (oldSeats.deep != newSeats.deep);
        println("Part 2",newSeats.map(_.count(_ == '#')).sum)
    }
    
    def occup(xy : (Int,Int), seats: Array[StringBuilder]) : Floor = {
        if (xy._1 < 0 || xy._2 < 0 || xy._1 >=seats(0).size || xy._2 >= seats.size)
            return OutOfRange
        return Floor(seats(xy._2).charAt(xy._1))
    }
    
    def occupInDir(xy : (Int,Int), dir : (Int,Int), seats: Array[StringBuilder]) : Floor = {
        implicit class TuppleAdd(t: (Int, Int)) {
            def +(p: (Int, Int)) = (p._1 + t._1, p._2 + t._2)
        }
        var xyn= xy+dir
        while (true) {
            if (xyn._1 < 0 || xyn._2 < 0 || xyn._1 >=seats(0).size || xyn._2 >= seats.size)
                return OutOfRange
            if (Floor(seats(xyn._2).charAt(xyn._1)) == Free)
                return Free
            if (Floor(seats(xyn._2).charAt(xyn._1)) == Occupied)
                return Occupied
            xyn=xyn+dir
        }
        return Empty
    }
 
}




