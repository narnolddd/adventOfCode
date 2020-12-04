
object  day3 extends App{

  trait Position
  case class Open() extends Position
  case class Tree() extends Position
  case class Level(positions:Array[Position]){
    def getpos(x:Int) = positions(x%positions.length)
  }
  case class Location(x:Int,y:Int){
    def moveRight(right:Int) = Location(x+right,y)
    def moveDown(down:Int) = Location(x,y+down)
  }
  case class Mountain(levels:Array[Level]){
    def TreesInPath(right:Int,down:Int,location: Location):Long ={
      val newLocation = location moveDown down moveRight right
      if((newLocation y) < (levels length))
        if(levels(newLocation y).getpos(newLocation x).isInstanceOf[Tree])
          TreesInPath(right,down,newLocation) +1
        else TreesInPath(right,down,newLocation)
      else
        0
    }
  }

  val mountain = Mountain(
    scala.io.Source.fromFile("day3.txt")
    .getLines()
    .map(line=>
      Level(line.toCharArray
        .map(pos=>
          if(pos=='.') Open() else Tree()
        )
      )
    ).toArray
  )

  val Paths = Array((1,1), (3,1), (5,1), (7,1), (1,2))
  println(Paths.map(path => mountain.TreesInPath(path._1, path._2, Location(0, 0))).product)


}
