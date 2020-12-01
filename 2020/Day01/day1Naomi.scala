package Day01

import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object day1Naomi {

  def main(args: Array[String]) = {
    part1()
    part2()
  }

  def extractEntries( fileName : String ) : ArrayBuffer[Int] = {
    Source.fromFile(fileName)
      .getLines()
      .toArray
      .map(x => Integer.parseInt(x))
      .to[ArrayBuffer]
  }

  def part1() : Unit = {
    val fileName = "Day01/inputnaomi.txt"
    val entries = extractEntries(fileName)
    entries.foreach{ x =>
      entries.foreach{ y =>
          if (x + y == 2020){
            println(x*y)
            return }
      }
    }
  }


  def part2() : Unit = {
    val fileName = "Day01/inputnaomi.txt"
    val entries = extractEntries(fileName)
    entries.foreach{ x =>
      entries.foreach{ y =>
        entries.foreach { z =>
          if (x + y + z == 2020) {
            println(x * y * z)
            return
          }
        }
      }
    }
  }

}
