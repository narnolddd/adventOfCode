import scala.io.Source
import scala.collection.mutable.ListBuffer

object Command extends Enumeration {
    type Command = Value
    val Nop = Value("nop")
    val Acc = Value("acc")
    val Jmp = Value("jmp")
}
import Command._

class Instruction(val inst: Command, val value: Int) {
    override def toString: String= s"($inst,$value)"
}

class machine (val prog : Array[Instruction], var acc: Int = 0, var sp: Int = 0, 
    var visited : ListBuffer[Int] = ListBuffer[Int]() ) {
    def iterate () : Boolean = {
        if (sp == prog.size)
            return true
        if (visited.contains(sp))
            return true
        visited += sp
        
        prog(sp).inst match {
            case Nop => sp= sp+1
            case Acc => acc=acc+prog(sp).value; sp= sp+1
            case Jmp => sp= sp+prog(sp).value
        }
        
        return false
    }
    override def toString: String= s"($sp,$acc)"
}


object rgc {
    def main(args: Array[String]) : Unit = {
        val data= Source.fromFile("rgcinput.txt").mkString
        val prog= data.split("\n").map(parseLine(_))
        var m= new machine(prog)
        while (!m.iterate()) {
         //   println(m.sp,m.acc)
        }
        println("Part 1",m.acc)
    }
    
    def parseLine(line: String) : Instruction = {
        val parts=line.split(" ")
        return new Instruction(Command.withName(parts(0)),parts(1).toInt)
    }
}




