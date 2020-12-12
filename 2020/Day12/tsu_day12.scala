object tsu_day12 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d12.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().map("""\d+|\D+""".r.findAllIn(_).toArray).toArray
  val compass = Map("E" -> (1, 0), "W" -> (-1, 0), "N" -> (0, 1), "S" -> (0, -1))

  def RainRisk(solution: Int, st: (Int, Int)): Int = {
    var pos = (0, 0)
    var wp = st
    data.foreach { ins =>
      val dir = ins.head
      val value = ins.last.toInt
      dir match {
        case "F" => pos = (pos._1 + wp._1 * value, pos._2 + wp._2 * value)
        case "L" | "R" => {
          val rot = if (dir == "L") 4 - (value / 90) % 4 else (value / 90) % 4
          for (i <- 0 until rot) {
            wp = (wp._2, -wp._1)
          }
        }
        case _ => if (solution == 1) pos = (compass(dir)._1 * value + pos._1, compass(dir)._2 * value + pos._2)
        else wp = (compass(dir)._1 * value + wp._1, compass(dir)._2 * value + wp._2)
      }
    }
    pos._2.abs + pos._1.abs
  }
  println("一: " + RainRisk(1, compass("E")))
  println("二: " + RainRisk(2, (10, 1)))
}