object tsu_day03 {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d3.txt").trim

  def main(args: Array[String]): Unit = {
      val data = scala.io.Source.fromFile(fn).getLines.map(_.trim.toArray).toArray
      var cnt2 = 1L
      for ((i,j) <- List((1, 1),(3, 1),(5, 1),(7, 1),(1, 2))){
        cnt2 *= countTrees(data, i,j)
      }
      println("Solution One : " + countTrees(data, 3,1))
      println("Solution Two : " + cnt2)
  }

  def countTrees(data:Array[Array[Char]], right:Int, down:Int): Long ={
    var cnt = 0
    val len = data.head.length
    var cursor = -right
    for (line <- data.indices by down){
      cursor+=right
      cnt = if(data(line)(cursor%len)=='#') cnt+1 else cnt
    }
    cnt
  }
}
