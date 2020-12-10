object tsu_day10 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d10.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().map(_.trim.toLong).toArray
  val datax = Array(0L) ++ data.sorted ++ Array(data.max + 3)

  val diff = datax.sliding(2).map { x => x.last - x.head }.toArray
  println("Uno: " + (diff.count(_ == 1) * diff.count(_ == 3)))

  var dp = Array(1L)
  Range(1, datax.length).foreach { i =>
    val i_paths = datax.take(i).filter(_ + 3 >= datax(i))
    val count = dp.reverse.take(i_paths.length).sum
    dp ++= Array(count)
  }

  println("Dos: " + dp.last)
}