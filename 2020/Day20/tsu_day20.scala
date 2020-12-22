object tsu_day20 extends App { // I pity the soul that wants to go through this..go on my child! May the force be with yee!
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d20.txt").trim
  var tiles = scala.io.Source.fromFile(fn).mkString.split("\n\n").map(_.split(":"))
    .map(x => x.head.split(" ").last.toLong -> x.last.trim.split("\n").map(_.trim.grouped(1).toArray)).toMap
  val (bx, by) = (tiles.head._2.length, tiles.head._2.head.length)
  val bordTiles = tiles.map { tile => (tile._1, getBorders(tile._2)) }
  val cntEdges = bordTiles.map { tile =>    (tile._1, checkBorders(tile._2, bordTiles.removed(tile._1).values.flatten.toArray))  }
  var borders = cntEdges.values.flatten.toArray
  val st = cntEdges.filter(_._2.length == 2).head
  // orienting the 1st tile so common borders are facing right and bottom
  val (led, bot) = (st._2.head, st._2.last)
  var tile = fitREdge(tiles(st._1), led)
  val List(b, br, t, tr) = List(tile.last, tile.last.reverse, tile.head, tile.head.reverse).map(_.mkString)
  tile =    if (bot == b) flip(tile).transpose
            else if (bot == br) flip(tile)
            else if (bot == t) rotate(rotate(tile))
            else rotate(flip(tile))
  tiles += st._1 -> tile

  var img = Array(Array(st._1)) //stores IDs of tiles in order
  var bte = getedge(tiles(img.last.head), false)
  while (borders.contains(bte) || borders.contains(bte.reverse)) {
    var red = getedge(tiles(img.last.last), true)
    while (borders.contains(red) || borders.contains(red.reverse)) {
      // get the one tile that fits with right edge
      val nt = bordTiles.removed(img.last.last).find(x => x._2.contains(red) || x._2.contains(red.reverse)).get
      var tile = fitREdge(tiles(nt._1), red)
      if ((img.length > 1) & (img.last.length > 0)) {
        // orient tile to fit its top to bottom of tile above it
        val bt = getedge(tiles(img(img.length - 2)(img.last.length)), false)
        if (tile.head.mkString != bt) tile = flipUp(tile)
      }
      tiles += nt._1 -> tile
      img = img.init ++ Array(img.last ++ Array(nt._1))
      red = getedge(tiles(nt._1), true)
    }
    bte = getedge(tiles(img.last.head), false)
    //find tile to start new row
    val nt = bordTiles.removed(img.last.head).find(x => x._2.contains(bte) || x._2.contains(bte.reverse))
    if (nt.isDefined) {
      val ntile = nt.get
      tiles += ntile._1 -> fitBEdge(tiles(ntile._1), bte)
      img ++= Array(Array(ntile._1))
    }
  }

  val image = makeImage(img)
  val Monster = ("                  # \n" +
                 "#    ##    ##    ###\n" +
                 " #  #  #  #  #  #   ").split("\n").map(_.grouped(1).toArray)
  val sz = Monster.head.length
  val MonsterMania = faces(image).map { img =>
    var monsterCount = 0
    img.take(img.length - 2).zipWithIndex.foreach { case (row, i) =>
      row.sliding(sz).zipWithIndex.foreach { case (col, j) =>
        val top = col.zip(Monster.head).collect { case (v, "#") => v }
        if (!top.toSet.contains(".")) {
          val m2 = Range(1, 3).toArray.map { q =>
            img(i + q).slice(j, j + sz).zip( Monster(q) ).collect { case (v, "#") => v }
          }
          if (!m2.flatten.toSet.contains(".")) monsterCount += 1
        }
      }
    }
    monsterCount
  }.max

  println("パート 1: " + cntEdges.filter(_._2.length == 2).keySet.product)                                   // パート 1: 45079100979683
  println("パート 2: " + (image.flatten.count(_ == "#") - MonsterMania * Monster.flatten.count(_ == "#")))   // パート 2: 1946

  //LOOK AT YALL THOSE CHICKEN *cough* defs i mean defs...
  def makeImage(ids: Array[Array[Long]]): Array[Array[String]] = {
    ids.flatten.foreach { t => tiles += t -> tiles(t).init.tail.map(_.init.tail) } // removes borders
    ids.foldLeft(Array[Array[String]]()) { (q, row) =>        // concat op
      q ++ row.tail.foldLeft(tiles(row.head)) { (a, tid) =>
        (a zip tiles(tid)).map { case (x, y) => x ++ y }
      }
    }
  }
  def fitBEdge(tile: Array[Array[String]], edge: String): Array[Array[String]] = {    faces(tile).find ( _.head.mkString == edge ).get  }
  def fitREdge(tile: Array[Array[String]], edge: String): Array[Array[String]] = {    faces(tile).find ( _.map(_.head).mkString == edge    ).get  }
  def getedge(tile: Array[Array[String]], right: Boolean): String = {    if (right) tile.map(_.last).mkString    else tile.last.mkString  }
  def rotate(tile: Array[Array[String]]): Array[Array[String]] = {    flip(tile.transpose)  }
  def flip(tile: Array[Array[String]]): Array[Array[String]] = {    tile.map(_.reverse)  }
  def flipUp(tile: Array[Array[String]]): Array[Array[String]] = {    flip(tile.transpose).transpose }
  def checkBorders(tilebord: Array[String], borders: Array[String]): Array[String] = {    tilebord.filter(x => borders.contains(x) | borders.contains(x.reverse))  }
  def getBorders(tile: Array[Array[String]]): Array[String] = {    Array(tile.head, tile.last, tile.transpose.head, tile.transpose.last).map(_.mkString)  }
  def faces(tile:Array[Array[String]]): Array[Array[Array[String]]] ={    Array.fill(3)(Array(tile,flip(tile))).scan(Array(tile,flip(tile))){ case (a,_) => a.map(rotate)}.flatten  }
}