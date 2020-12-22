object tsu_day15 extends App {
  //TODO: optimize for pt2
  var data = Array(0, 13, 1, 16, 6, 17)

  println("パート 1: " + findLast(2020L))      // パート 1: 234
  println("パート 2: " + findLast(30000000L))  // パート 2: 8984

  def findLast(end: Long): Int = {
    var mem = scala.collection.mutable.Map[Int, Int]()
    data.init.zipWithIndex.foreach { case (x, y) => mem(x) = y }
    var i = mem.size
    var lastNum = data.last
    while (i < (end - 1)) {
      val num = mem.get(lastNum).map(x => i-x).getOrElse(0)
      mem += lastNum -> i
      lastNum = num
      i += 1
    }
    lastNum
  }
}