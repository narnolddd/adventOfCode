import scala.io.Source

//part 1
new ((Int,Array[Int]) => Array[Int]){def apply(pos:Int,machine:Array[Int]):Array[Int] =
 if(machine(pos)==99) return machine
 else if(machine(pos)==1) apply(pos+4,machine.updated(machine(pos+3),(machine(machine(pos+1)) + machine(machine(pos+2)))))
 else apply(pos+4,machine.updated(machine(pos+3),(machine(machine(pos+1)) * machine(machine(pos+2)))))
 }.apply(0,Source.fromURL("https://pastebin.com/raw/NCwzm5xf").mkString.split(",").map(x=>x.toInt).updated(1,12).updated(2,2))

//part2

0.to(99).foreach(noun=> 0.to(99).foreach(verb =>
if(new ((Int,Array[Int]) => Array[Int]){
  def apply(pos:Int,machine:Array[Int]):Array[Int] =
    if(machine(pos)==99) return machine
    else if(machine(pos)==1) apply(pos+4,machine.updated(machine(pos+3),(machine(machine(pos+1)) + machine(machine(pos+2)))))
    else apply(pos+4,machine.updated(machine(pos+3),(machine(machine(pos+1)) * machine(machine(pos+2)))))
  }.apply(0,Source.fromURL("https://pastebin.com/raw/NCwzm5xf").mkString.split(",").map(x=>x.toInt).updated(1,noun).updated(2,verb))(0) == 19690720)
  print("SUCCESS"+noun.toString+verb.toString)
))
