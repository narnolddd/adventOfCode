package aoc2020

object tsu_day01 {
  val fn = System.getenv().getOrDefault("FILE_PATH", "input-tsu.txt").trim

  def main(args: Array[String]): Unit = {
    pt1()
    pt2()
  }
    def pt1():Unit={
    val data = scala.io.Source.fromFile(fn).getLines.map(_.toInt).toArray
    data.foreach{x=>
      val y = data.filter(_==2020-x)
      if (y.nonEmpty) {
        println(x*y(0))
      return}
    }
  }

  def pt2(): Unit = {
    val data = scala.io.Source.fromFile(fn).getLines.map(_.toInt).toArray
    data.foreach{x=>
      data.foreach{y=>
        val z = data.filter(_==2020-x-y)
        if (z.nonEmpty) {
          println(x*y*z(0))
          return
        }
      }
    }
  }
}
