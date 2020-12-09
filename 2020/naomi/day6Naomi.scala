package naomi

import scala.io.Source

class day6Naomi extends PuzzleSolver {

  override def part1(): Unit = {
    println("Counts: "+ extractEntries()
      .map(_.replaceAll("\n",""))
      .map(x => x.groupBy(identity).size)
      .sum)
  }

  override def part2(): Unit = {
    println("Counts: "+ extractEntries()
      .map(_.split("\n").map(x => x.toSet))
        .map(x => x.fold(x.head)((A, B) => A intersect B).size)
        .sum
      )
  }

  def extractEntries(): Array[String] = {
    Source.fromFile("Day06/inputnaomi.txt")
      .mkString
      .split("\n\n")
  }
}
