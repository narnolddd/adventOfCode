object tsu_day11 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d11.txt").trim
  var data = scala.io.Source.fromFile(fn).getLines().map(_.grouped(1).toArray).toArray
  var area = Array[Array[String]]()
  val (bx, by) = (data.length, data.head.length)
  var offset = Array(Array(+1, +1), Array(-1, -1), Array(+1, -1), Array(-1, +1), Array(0, +1), Array(0, -1), Array(+1, 0), Array(-1, 0))
  val limit = 5

  def rules(adj: Array[String], pos: String): String = {
    pos match {
      case "L" => if (!adj.contains("#")) "#" else "L"
      case "#" => if (adj.count(_ == "#") >= limit) "L" else "#"
      case "." => "."
    }
  }

  def filterForBorders(array: Array[Array[Int]], px: Int, py: Int, n: Int, m: Int, layer: Int): Array[Array[Int]] = {
    array.filterNot { a => (px + a.head * layer >= n) | (py + a.last * layer >= m) | (px + a.head * layer < 0) | (py + a.last * layer < 0) }
  }
  //pt1 adj
  def getAdj(mat: Array[Array[String]], px: Int, py: Int): Array[String] = {
    var ofs = offset.clone()
    ofs = filterForBorders(ofs, px, py, bx, by, 1)
    ofs.map { a => mat(px + a.head)(py + a.last) }
  }
  //pt2 adj
  def getAdj2(mat: Array[Array[String]], px: Int, py: Int): Array[String] = {
    var ofs = offset.clone()
    var i = 0
    var diag = Array[String]()
    while (ofs.nonEmpty) {
      i += 1
      ofs = filterForBorders(ofs, px, py, bx, by, i)
      ofs = ofs.filter { a =>
        val check = List("L", "#").contains(mat(px + a.head * i)(py + a.last * i))
        if (check)
          diag ++= Array(mat(px + a.head * i)(py + a.last * i))
        !check
      }
    }
    diag
  }

  def checkSeat(dt: Array[Array[String]], px: Int, py: Int): Int = {
    val seat = dt(px)(py)
    val change = rules( getAdj2(dt, px, py), seat )
    area(px)(py) = change
    if (seat == change) 0 else 1
  }

  var stop = 1
  while (stop != 0) {
    stop = 0
    area = Array.fill(bx,by)("")
    area.indices.foreach { px =>
      area.head.indices.foreach { py =>
        stop += checkSeat(data, px, py)
      }
    }
    data = area.clone()
  }
  println("ハッシュタグ: " + area.flatten.count(_ == "#"))
}