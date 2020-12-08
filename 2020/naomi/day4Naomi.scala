package naomi

import scala.collection.mutable.ArrayBuffer
import scala.io.Source

class day4Naomi extends PuzzleSolver {

  def extractEntries( fileName : String ) : Array[String] = {
    Source.fromFile(fileName)
      .mkString
      .split("\n\n")
  }

  override def part1(): Unit = {
    println("Possibly ok passports: "+findValidEntries().length)
  }

  override def part2(): Unit = {
    println("Really valid entries: "+findValidEntries()
      .map(x => if (isValid(x)) 1 else 0)
      .sum)
  }
  def findValidEntries() : ArrayBuffer[Map[String,String]] = {
    val entries = extractEntries("Day04/inputnaomi.txt")
    val pattern = """(\w+):(\S+)""".r
    var valid = new ArrayBuffer[Map[String,String]]
    entries.foreach{
      entry =>
        val passport = pattern.findAllIn(entry)
          .map( x => x.split(":"))
          .map( x => x(0) -> x(1))
          .toMap
        if (passport.keys.size == 8 || passport.keys.size == 7 & !passport.keySet.contains("cid"))
          valid.append(passport)
    }
    valid
  }

  def isValid(passport: Map[String,String]): Boolean = {
    if (!(1920 to 2002 contains passport("byr").toInt))
      return false
    if (!(2010 to 2020 contains passport("iyr").toInt))
      return false
    if (!(2020 to 2030 contains passport("eyr").toInt))
      return false
    if (passport("hgt").contains("cm")) {
      if (!(150 to 193 contains passport("hgt").stripSuffix("cm").toInt ))
        return false
    } else if (passport("hgt").contains("in")) {
      if (!(59 to 76 contains passport("hgt").stripSuffix("in").toInt ))
        return false
    } else return false
    val hcl = """#([a-f]|[0-9]){6}""".r
    if (hcl.findAllIn(passport("hcl")) isEmpty)
      return false
    if (!(List("amb","blu","brn","gry","grn","hzl","oth") contains passport("ecl")))
      return false
    if (passport("pid").length !=9)
      return false
    true
  }
}
