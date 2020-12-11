object tsu_day11 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d11.txt").trim
  var data = scala.io.Source.fromFile(fn).getLines().map(_.grouped(1).toArray).toArray
  var area = Array.fill(data.length,data.head.length)("")

  def rules(adj: Array[String], pos: String): String = {
    pos match {
      case "L" => if (!adj.contains("#")) "#" else "L"
      case "#" => if (adj.count(_ == "#") >= 4) "L" else "#"
      case "." => "."
    }
  }
  def getAjd1(mat:Array[Array[String]], px: Int, py: Int): Array[String] ={
    val adj = mat.slice(px - 1, px + 2).flatMap(_.slice(py - 1, py + 2))
    adj.filterNot(_=="X")
  }

  def checkSeat(dt: Array[Array[String]], px: Int, py: Int): Int = {
    val dt2 = dt.clone()
    val seat = dt2(px)(py)
    dt2(px)(py) = "X"
   val adj = getAjd1(dt2, px,py)
    val change = rules(adj, seat)

      dt2(px)(py) = seat
      area(px)(py) = change
      if (seat == change) {
        0
      } else {
        1
      }
  }

  var stop = 1
  while (stop!=0) {
    stop = 0
    area = Array.fill(data.length,data.head.length)("")
    area.indices.foreach { px =>
      area.head.indices.foreach { py =>
        stop+=checkSeat(data, px, py)
      }
    }
    data = area.clone()
  }
  println("하나: "+ area.flatten.count(_=="#"))
  println("둘 : ")
}
