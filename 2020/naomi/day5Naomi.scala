package naomi

import scala.io.Source

class day5Naomi extends PuzzleSolver {

  override def part1(): Unit = {
    val passports = extractEntries()
    var maxId = 0
    passports.foreach{
      pp =>
        val id = rowOrCol(pp.take(7),'F', 'B') * 8 + rowOrCol(pp.takeRight(3),'L','R')
        maxId = if (id > maxId) id else maxId
    }
    println("Biggest id: "+maxId)
  }

  override def part2(): Unit = {
    val takenSeats = extractEntries()
      .map (x => rowOrCol(x.take(7),'F','B')*8 + rowOrCol(x.takeRight(3),'L','R'))
    val emptySeats = (for {
      row <- 0 to 128
      col <- 0 to 8
    } yield row * 8 + col)
      .toList
      .filter(x => !(takenSeats contains x) && (takenSeats contains x+1) && (takenSeats contains x-1) )
    println("Empty seat id: "+emptySeats.head)
  }

  def extractEntries() : Array[String] = {
    Source.fromFile("day05/inputnaomi.txt")
      .getLines()
      .toArray
  }

  def rowOrCol(pass : String, lower: Char, upper : Char) : Int = {
    Integer.parseInt(pass.map(Map(lower -> "0", upper -> "1"))
      .mkString, 2)
  }

}
