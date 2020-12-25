object tsu_day25 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d25.txt").trim
  val publicKeys = scala.io.Source.fromFile(fn).getLines().map(_.trim.toLong).toArray

  val loopSize = publicKeys.map(findLoops(7, _))
  println("Encryption key: " + encryption(publicKeys.head, loopSize.last)) // Encryption key: 7269858
  println("It's a wrap, Folks!")

  def encryption(subjNum: Long, lp: Int): Long = {    Range(0, lp).foldRight(1L) { (_, v) => (v * subjNum) % 20201227L }  }
  def findLoops(subjNum: Long, ekey: Long): Int = {
    var v = 1L
    Range(1, Int.MaxValue).find { _ => v = (v * subjNum) % 20201227L
      v == ekey }.get
  }
}