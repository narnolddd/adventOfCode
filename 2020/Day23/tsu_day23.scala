import scala.collection.mutable.HashMap

object tsu_day23 extends App {
  //  var data = "389125467".grouped(1).map(_.toInt).toArray
  var data = "952438716".grouped(1).map(_.toInt).toArray
  val INC = 1000000
  val ROUNDS = 10000000

  def CrabCups(rounds: Int, inc: Int): HashMap[Int, Int] = {
    data = data ++ Range(data.length + 1, inc + 1)
    var map = new HashMap[Int, Int]
    (data zip data.tail).foreach { p => map.put(p._1, p._2) }
    map.put(data.last, data.head)
    var q = data.head
    for (_ <- 0 until rounds) {
      val pick = Range(0, 2).scan(map(q)) { case (a, _) => map(a) }.toArray
      var dest = if (q == 1) data.length else q - 1
      while (pick.contains(dest)) {
        dest = if (dest == 1) data.length else dest - 1
      }
      map += q -> map(pick.last)
      q = map(pick.last)
      map += pick.last -> map(dest)
      map += dest -> pick.head
    }
    map
  }
  val pt1 = CrabCups(100, 0)
  println(" パート 1: " + Range(0, pt1.size - 2).scan(pt1(1)) { case (a, _) => pt1(a) }.mkString)     // パート 1: 97342568
  val pt2 = CrabCups(10000000, 1000000)
  println("パート 2: " + pt2(1), pt2(pt2(1)), pt2(1) * pt2(pt2(1)).toLong)                          // パート 2: 978763, 921784, 902208073192
}