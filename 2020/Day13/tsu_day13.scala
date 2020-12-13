object tsu_day13 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d13.txt").trim
  var data = scala.io.Source.fromFile(fn).getLines().toArray
  var ED = data.head.toInt
  var buses = data(1).split(",").view.zipWithIndex.filter(_._1 != "x").map(x => (x._1.trim.toLong, x._2)).toMap //Map(Bus ID -> position)

  def gcd(a: Long, b: Long): Long = if (b == 0) a.abs else gcd(b, a % b)
  def lcm(a: Long, b: Long): Long = (a * b).abs / gcd(a, b)

  val a = buses.keys.map { x => (x, x - ED % x) }
  println("パート 1: " + a.find(_._2 == a.map(_._2).min).map { case (x, y) => x * y }.get)   // パート 1: 2045

  var rem, t, nlcm = 1L
  for ((x, p) <- buses) {
    rem = 1L
    while (rem != 0) {
      t += nlcm
      rem = (t + p) % x
    }
    nlcm = lcm(nlcm, x)
  }
  println("パート 2: " + t)      // パート 2: 402251700208309
}