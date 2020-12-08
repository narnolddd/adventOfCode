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
    def terminated () : Boolean = {
        return sp == prog.size
    }
    // Flip the ith nop/Jmp to the other
    def flipOne (flip : Int) : machine = {
        var prog2= prog.clone
        var i= 0
        for(line <- 0 to prog.size) {
            if (prog(line).inst == Nop || prog(line).inst == Jmp) {
                if (i == flip) {
                    if (prog(line).inst == Nop) {
                        prog2(line)= new Instruction(Jmp,prog(line).value)
                    } else {
                        prog2(line)= new Instruction(Nop,prog(line).value)
                    }
                    return new machine(prog2)
                } else {
                    i= i+1
                }
            }
        }
        println("All states now flipped")
        return new machine(prog2)
    }
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
        for (i <- 0 to prog.size) {
            var m2= m.flipOne(i)
            while (!m2.iterate()) {
            }
            if (m2.terminated()) {
                println("Part 2",m2.acc)
                return 
            }
        }
    }
    
    def parseLine(line: String) : Instruction = {
        val parts=line.split(" ")
        return new Instruction(Command.withName(parts(0)),parts(1).toInt)
    }
}




