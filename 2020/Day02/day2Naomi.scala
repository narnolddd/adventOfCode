package Day02

import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object day2Naomi {
  def main(args: Array[String]) = {
    part1()
    part2()
  }

  def extractEntries() : Any = {
    val fileName = "Day02/inputnaomi.txt"
    Source.fromFile(fileName)
      .getLines()
      .map(record => parseLine(record))
      .to[ArrayBuffer]
  }

  def parseLine( record : String) : Any = {
    val parts = record.split(Array('-',' '))
    (parts(0).toInt, parts(1).toInt, parts(2).stripSuffix(":").charAt(0), parts(3))
  }

  def part1() : Unit = {
    val records = extractEntries()

    var totalValid =
    records.asInstanceOf[ArrayBuffer[(Int,Int,Char,String)]].count{
      rec =>
        val counts = rec._4.count(char => char==rec._3)
        counts >= rec._1 && counts <= rec._2
    }
    println("Number of valid passwords: "+totalValid)
  }

  def part2() : Unit = {
    val records = extractEntries()
    var totalValid =
    records.asInstanceOf[ArrayBuffer[(Int,Int,Char,String)]].count{
      rec =>
        val pWord = rec._4
        val pos1 = rec._1-1
        val pos2 = rec._2-1
        val letter = rec._3
        (pWord(pos1) == letter && pWord(pos2) != letter) || (pWord(pos1) != letter && pWord(pos2) == letter)
    }
    println("Number of valid passwords: "+totalValid)
  }

}
