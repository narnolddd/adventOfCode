object tsu_day07 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d7.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines()
  val fdata = data.map { line =>
    val d = line.filter(c => c.isLetter || c.isWhitespace || c.isDigit).split("bags contain ").flatMap(_.split("bags")).flatMap(_.split(("bag"))).map(_.trim)
    d.head -> d.tail.map { x => if (x == "no other") List[String]("0", "") else """\d+|\D+""".r.findAllIn(x).toList }
  }.toMap
  val color = "shiny gold"

  //+=+=+=+=+=+=+=+=+

  var cnt = Set[String]()
  cnt ++ findParent(color)
  println("First go: \t" + cnt.size)

  def findParent(v: String): Set[String] = {
    val parents = fdata.filter { x => x._2.map(_ (1).trim).contains(v) }.keySet
    val selc = parents.diff(cnt)
    if (selc.nonEmpty) {
      cnt = cnt ++ parents
      val nxparent = selc.map(findParent).fold(Set())(_ ++ _)
      cnt ++ nxparent
    } else {
      Set[String]()
    }
  }

  //+=+=+=+=+=+=+=+=+

  var cnt2 = 0
  var elem = Array(List("1", color))
  while (elem.nonEmpty) {
    val parent = elem.head
    elem = elem.tail
    val child = fdata.getOrElse(parent.last.trim, Array[List[String]]())
    child.foreach { c =>
      val w = c.head.toInt * parent.head.toInt
      cnt2 += w
      elem = elem ++ Array(List(w.toString, c.last.trim))
    }
  }
  println("Second go: " + cnt2)
}