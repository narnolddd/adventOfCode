object tsu_day22 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d22.txt").trim
  val data = scala.io.Source.fromFile(fn).mkString.split("\n\n").map(_.split(Array('\n')).tail.map(_.trim.toLong))
  var (captain, crab) = (data.head, data.last)

  val List(pt1, pt2) = List(false, true).map(subgame(captain, crab, _)._2.reverse.zipWithIndex.map { case (a, b) => a * (b + 1) }.sum)
  println("En premier... " + pt1)
  println("...puis deux: " + pt2)

  def subgame(a: Array[Long], b: Array[Long], pt2: Boolean): (Int, Array[Long]) = {
    def checkOne(deck: Array[Long], i: Int): Boolean = {      deck.take(i).indexOfSlice(deck.drop(i)) != -1    }
    def checkTwo(deck: Array[Long], card: Long): Boolean = {      deck.length >= card    }

    var i = 0
    var (captain, crab) = (a, b)
    while (captain.drop(i).nonEmpty & crab.drop(i).nonEmpty) {
      if (pt2 & checkOne(captain, i) & checkOne(crab, i)) crab = crab.drop(crab.length)
      else {
        val (x, y) = (captain(i), crab(i))
        val win = if (pt2 & checkTwo(captain.drop(i + 1), x) & checkTwo(crab.drop(i + 1), y))
          subgame(captain.slice(i + 1, i + 1 + x.toInt), crab.slice(i + 1, i + 1 + y.toInt), true)._1
        else if (x > y) 1 else 2
        win match {
          case 1 => captain ++= Array(x, y)
          case 2 => crab ++= Array(y, x)
        }
        i += 1
      }
    }
    if (captain.drop(i).nonEmpty) (1, captain.drop(i)) else (2, crab.drop(i))
  }
}