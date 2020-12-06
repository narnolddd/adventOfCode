object tsu_day06 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d6.txt").trim
  val data = scala.io.Source.fromFile(fn).mkString.split("\n\n").map(_.split(Array('\n')).map(_.trim))

  println(data.map(_.mkString.distinct.length).sum)
  println(data.map { x => x.fold(x.head) { (a, b) => a.intersect(b) }.length }.sum)
}