import scala.io.Source
import collection.mutable.Map
import scala.util.matching.Regex

object Command extends Enumeration {
    type Command = Value
    val Nop = Value("nop")
    val Acc = Value("acc")
    val Jmp = Value("jmp")
}
import Command._

class Instruction(var name: Command, var value: Int) {
    override def toString: String= s"($name,$value)"
}




object rgc {
    def main(args: Array[String]) : Unit = {
        val data= Source.fromFile("rgcinput.txt").mkString
        val prog= data.split("\n").map(parseLine(_))
        for (p <- prog)
            println(p)
    }
    
    def parseLine(line: String) : Instruction = {
        val parts=line.split(" ")
        return new Instruction(Command.withName(parts(0)),parts(1).toInt)
    }
}




