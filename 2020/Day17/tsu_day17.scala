object tsu_day17 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d17.txt").trim
  var data = Array(Array(scala.io.Source.fromFile(fn).getLines().map(_.grouped(1).map(_ == "#").toArray).toArray))
  val (bw, bx, by, bz) = (data.length, data.head.length, data.head.head.length, data.head.head.head.length)
  val cyc = 7

  var mat = Array.fill(cyc * 2 + bw)(Array.fill(cyc * 2 + bx)(Array.fill(cyc * 2 + by)(Array.fill(cyc * 2 + bz)(false))))
  Range(0, by).foreach { x => Range(0, bz).foreach { y => mat(cyc)(cyc)(cyc + x)(cyc + y) = data(0)(0)(x)(y) } }

  val offset = Range(-1, 2).flatMap(w => Range(-1, 2).flatMap(x => Range(-1, 2).flatMap(y => Range(-1, 2).map(z => Array(w, x, y, z))))).toArray.filterNot(_.sameElements(Array(0, 0, 0, 0)))

  println("パート 1: " + getActive(mat.slice(cyc-1, cyc+2),offset.filter(_.head==0) )) // パート 1: 269
  println("パート 2: " + getActive(mat, offset))                                       // パート 2: 1380

  def getActive(mat: Array[Array[Array[Array[Boolean]]]], offset: Array[Array[Int]]): Int = {
    var dt = mat.clone()
    val (bw, bx, by, bz) = (dt.length, dt.head.length, dt.head.head.length, dt.head.head.head.length)
    Range(0, 6).foreach { i =>
      val area = Array.fill(bw)(Array.fill(bx)(Array.fill(by)(Array.fill(bz)(false))))
      area.indices.tail.init.foreach { pw =>
        area.head.indices.tail.init.foreach { px =>
          area.head.head.indices.tail.init.foreach { py =>
            area.head.head.head.indices.tail.init.foreach { pz =>
              area(pw)(px)(py)(pz) = rules(getAdj(dt, offset, pw, px, py, pz), dt(pw)(px)(py)(pz))
            }
          }
        }
      }
      dt = area.clone()
    }
    dt.flatten.flatten.flatten.count(_ == true)
  }

  def rules(adj: Array[Boolean], pos: Boolean): Boolean = {
    pos match {
      case true => if (List(2, 3).contains(adj.count(_ == true))) pos else !pos
      case false => if (adj.count(_ == true) == 3) !pos else pos
    }
  }

  def getAdj(mat: Array[Array[Array[Array[Boolean]]]], offset: Array[Array[Int]], pw: Int, px: Int, py: Int, pz: Int): Array[Boolean] = {
    offset.map { a => mat(pw + a.head)(px + a(1))(py + a(2))(pz + a.last) }
  }
}