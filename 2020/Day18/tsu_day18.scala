object tsu_day18 extends App {
  // This was excruciatingly painful! Had to change the way to approach this so many times :(
  // I admit I peaked at some solutions and they were hinting at
  // Recursive Descent parser -- for whoever is interested -- flew right by my head!
  // But it gave me the idea to start traversing in reverse and -- voila!
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d18.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().map(_.split(" ").flatMap(_.trim.grouped(1).toArray).reverse).toArray

  println("First: " + data.map(eqHandling(_, false)).sum)
  println("7th circle of Hell! " + data.map(eqHandling(_, true)).sum)

  def eqHandling(eq: Array[String], pt2: Boolean): Long = {
    var stack, op = Array[String]()
    eq.foreach {
      case "(" => {
        stack ++= op.takeWhile(_ != ")")
        op = op.dropWhile(_ != ")").drop(1)
      }
      case x@"*" => {
        if (pt2) {
          stack ++= op.takeWhile(_ == "+")
          op = x +: op.dropWhile(_ == "+")
        } else
          op = x +: op
      }
      case x@("+" | ")") =>
        op = x +: op
      case x =>
        stack ++= Array(x)
    }

    stack ++= op
    var accum = Array[Long]()
    stack.foreach {
      case "+" => accum = accum.take(2).sum +: accum.drop(2)
      case "*" => accum = accum.take(2).product +: accum.drop(2)
      case x => accum = x.toLong +: accum
    }
    accum.head
  }
}