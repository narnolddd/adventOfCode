import scala.collection.mutable

object tsu_day16 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d16.txt").trim
  //  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/test.txt").trim
  val data = scala.io.Source.fromFile(fn).mkString.split("\n\n")
  val rules = data.head.split("\n").map(_.split(":"))
    .map { x =>
      val a = """\d+""".r.findAllIn(x.last).toArray.map(_.toInt)
      x.head.trim -> (Range(a.head, a(1) + 1) ++ Range(a(2), a.last + 1)).map(_.toLong).toArray
    }.toMap
  val myticket = """\d+""".r.findAllIn(data(1)).toArray.map(_.toLong)
  val tickets = data.last.split("\n").map("""\d+""".r.findAllIn(_).toArray.map(_.toLong)).tail

  println("パート 1: " + tickets.flatten.filterNot(rules.values.toArray.flatten.contains(_)).sum)      // パート 1: 23009

  val valid = tickets.filter { x => x.forall(rules.values.toArray.flatten.contains(_)) } ++ Array(myticket)
  val assoc = valid.transpose.map { cat =>
    rules.filter { x => cat.forall(x._2.contains(_)) }.keySet
  }.zipWithIndex.map(_.swap).toMap

  //maximum bipartite matching -- coding this from scratch was a pain! python libs where art thou? T-T
  var matchR = mutable.Map[String, Int]()
  for (col <- Range(0, assoc.size)) {
    bpm(col, Array[String]())
  }

  def bpm(i: Int, seen: Array[String]): Boolean = {
    rules.keySet.foreach { cat =>
      if (!seen.contains(cat) & assoc(i).contains(cat) &&
      (!matchR.contains(cat) || bpm(matchR.getOrElse(cat, -1), seen ++ Array(cat)))) {
          matchR += cat -> i
          return true
      }
    }
    false
  }

  println("パート 2: " + ((matchR.filter(_._1.startsWith("departure")) values).toList map myticket).product) //パート 2: 10458887314153
}