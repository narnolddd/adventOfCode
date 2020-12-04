import scala.io.Source

object rgc {
    def main(args: Array[String]) = {
        val map= Source.fromFile("rgcinput.txt").getLines().to[Array]
        println("part1 ",pcount(3,1,map))
        println("part2 ",1L*pcount(1,1,map)*pcount(3,1,map)*pcount(5,1,map)*
            pcount(7,1,map)*pcount(1,2,map))
        
    }
    
    def pcount(xstep: Int, ystep: Int, map: Array[String]) : Int = {
        val width=map(0).length
        val height=map.length
        var y= 0
        var count= 0
        for(h <- 0 to ((height/ystep)-1)) {
            if (hit(h*xstep,h*ystep,width,map))
                count+=1
        }
        count
    }
    
    def hit(x: Int, y: Int, width: Int, map: Array[String]) : Boolean = {
        if (map(y).charAt(x%width) == '#')
            true
        else
            false
    }
    
}
