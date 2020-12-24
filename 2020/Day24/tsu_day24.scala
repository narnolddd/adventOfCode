import scala.collection.mutable

object tsu_day24 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d24.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().toArray.map(_.split("((?=s)|(?=n))")
    .flatMap(x => if ("sn".contains(x.head)) x.take(2) +: x.drop(2).grouped(1).toArray else x.split("")))
  val coord = Map("e" -> (2, 0), "se" -> (1, -1), "sw" -> (-1, -1), "w" -> (-2, 0), "nw" -> (-1, 1), "ne" -> (1, 1))
  var floor = new mutable.HashMap[(Int, Int), Boolean]() {    override def default(key: (Int, Int)) = false  }

  data.foreach { path =>
    val (x, y) = path.foldLeft((0, 0)) { case ((x, y), move) => (x + coord(move)._1, y + coord(move)._2) }
    floor.put((x, y), !floor((x, y)))
  }
  println("Initial Design: " +floor.count(_._2)) //391

  val xc = floor.clone()
  for (i <- 0 until 100) {
    val adjCount = floor.filter(_._2).map { case (tile, _) =>  tile -> getAdj(tile).map { floor.getOrElseUpdate(_, false) }    }
    floor.foreach { case (t, state) => xc.put(t, newState(adjCount, t, state)) }
    floor = xc.clone()
    if ((i + 1) % 10 == 0) println(i + 1, floor.count(_._2))
  }
  println("Final Design: "+ floor.count(_._2)) //3876

  def getAdj(t: (Int, Int)): Array[(Int, Int)] = {   coord.values.toArray.map (ofs => (t._1 + ofs._1, t._2 + ofs._2) )  }
  def newState(adj: mutable.HashMap[(Int, Int), Array[Boolean]], t: (Int, Int), state: Boolean): Boolean = {
    val a = adj.getOrElse(t, getAdj(t).map {  floor.getOrElse(_, false) }).count(a => a)
    if ((state & ((a == 0) | (a > 2))) | (!state & (a == 2))) !state else state
  }
}