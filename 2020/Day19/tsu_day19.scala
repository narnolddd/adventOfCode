object tsu_day19 extends App {
  //  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/test.txt").trim
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d19.txt").trim
  val data = scala.io.Source.fromFile(fn).mkString.split("\n\n")
  val rules = data.head.split(Array('\n')).map(_.split(Array(':', '|')))
    .map(x => x.head.trim -> x.tail.map(_.trim.split(" "))).toMap
  val msgs = data.last.split("\n").map(_.trim)

  def matchR(key: String): Array[String] = {
    rules(key).flatMap { rule =>
      rule.map { k =>
        k.startsWith("\"") match {
          case true => Array(k.split("\"").last)
          case _ => matchR(k)
        }
      }.foldRight(Array("")) { (q, w) => for (x <- q; y <- w) yield List(x, y).mkString }
    }
  }

  val out = matchR("0")
  println("Uno: " + msgs.count(out.contains(_))) // 233

  val r42 = matchR("42")
  val r31 = matchR("31")
  val sl = r42.head.length

  println("Dos: " + msgs.filter { msg =>
    r42.contains( msg.take(sl) ) & r31.contains( msg.takeRight(sl) )
    }.count { msg =>
      var i = 0
      var s = ""
      while (i < msg.length) {
        val slice = msg.slice(i, i + sl)
        if (r42.contains(slice)) s += "4"
        else if (r31.contains(slice)) s += "3"
        else s += "x"
        i += sl
      }
      (!s.contains('x')) & (s.count(_ == '4') > s.count(_ == '3'))
    }
  ) // 396
}