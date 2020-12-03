package Day03

import scala.io.Source

object day3Naomi {
  def main(args: Array[String]) = {
    part1()
    part2()
  }

  def extractEntries() : Any = {
    val fileName = "Day03/inputnaomi.txt"
    Source.fromFile(fileName)
      .getLines()
      .to[Array]
  }

  def noTrees(hjump: Int, vjump: Int) : Int = {
    val records = extractEntries().asInstanceOf[Array[String]]
    var pointer = 0
    var trees = 0
    for (i <- records.indices by vjump) {
      trees = if (records(i)(pointer % records(i).length) == '#') trees + 1 else trees
      pointer += hjump
    }
    trees
  }

  def part1() : Unit = {
    println(noTrees(3,1))
  }

  def part2() : Unit = {
    var product = 1L
    List((1,1),(3,1),(5,1),(7,1),(1,2))
      .map(x => noTrees(x._1, x._2))
      .map(x => x.longValue())
      .product

    println(product)
  }
}
