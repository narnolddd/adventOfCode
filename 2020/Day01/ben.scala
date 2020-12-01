object day1 extends App {
  val data = scala.io.Source.fromFile("day1data.txt").getLines.map(x=> x.toInt).toList
  println(
    (for(x <- data; y <- data) yield (x, y))
    .filter(pair => pair._1+pair._2==2020)
    .map(x=> x._1*x._2)
    .head)

  println(
    (for(x <- data; y <- data; z<-data) yield (x, y,z))
      .filter(triple => triple._1+triple._2+triple._3==2020)
      .map(x=> x._1*x._2*x._3)
      .head)

}
