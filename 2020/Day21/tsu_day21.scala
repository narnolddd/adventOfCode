import scala.collection.mutable

object tsu_day21 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d21.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().map(_.split(Array(')','('))).map(x=> (x.head.split(" ")
    , x(1).split("contains").last.split(",").map(_.trim))).toMap

  var allgmap = mutable.Map[String, Set[String]]()
  data.foreach{f=>
    val (ing,alg) = (f._1.toSet, f._2)
    alg.foreach{a=>
      if (allgmap.contains(a)) allgmap += a -> (allgmap(a) & ing) else allgmap += a -> ing
    }
  }

  val dangerZone = allgmap.values.flatten.toArray
  val gut = data.keySet.toArray.flatten.filterNot(dangerZone.contains(_))
  println("パート 1: " + gut.length)      // パート 1: 2125

  //maximum bipartite matching -- coding this from scratch was a pain! python libs where art thou? T-T
  var matchR = mutable.Map[String, String]()
  allgmap.keySet.foreach {col=>
    bpm(col, Array[String]())
  }
  def bpm(i: String, seen: Array[String]): Boolean = {
    dangerZone.foreach { cat =>
      if (!seen.contains(cat) & allgmap(i).contains(cat) &&
      (!matchR.contains(cat) || bpm(matchR.getOrElse(cat, "-1"), seen ++ Array(cat)))) {
          matchR += cat -> i
          return true
      }
    }
    false
  }

  println("パート 2: " + matchR.toSeq.sortBy(_._2).map(_._1).mkString(",")) //パート 2: phc,spnd,zmsdzh,pdt,fqqcnm,lsgqf,rjc,lzvh
}