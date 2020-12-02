object tsu_day02 {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d2.txt").trim

  def main(args: Array[String]): Unit = {
      val data = scala.io.Source.fromFile(fn).getLines.map(_.split(" ").map(_.trim))
      var cnt = 0
      var cnt2 = 0
    data.foreach{x=>
      val r = x.head.split("-").map(_.toInt)
      cnt = if (Range(r.head, r.last+1).contains(x.last.count(_==x(1).head))) cnt+1 else cnt
      cnt2 = if ((x.last(r.head-1)==x(1).head)^(x.last(r.last-1)==x(1).head)) cnt2+1 else cnt2
    }
      println("Number of valid passwords: "+ cnt)
      println("Number of valid passwords pt 2: "+ cnt2)
  }
}
