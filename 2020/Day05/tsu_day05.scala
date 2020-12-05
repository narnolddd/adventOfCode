object tsu_day05 extends App{
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d5.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().map(_.trim)
  val repl = Map('B'->'1', 'F'->'0', 'R'->'1', 'L'->'0')

  val passes = data.map{pass=>
    val bin = pass.map{s=>repl.getOrElse(s,s)}
      .grouped(7).map(Integer.parseInt(_, 2)).toArray
    bin.head * 8 + bin.last
  }.toArray
  println(passes.max)
  println(Range(passes.min, passes.max).filter(!passes.contains(_)).head)
}