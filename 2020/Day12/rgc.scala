import scala.io.Source
import scala.collection.mutable.ArrayBuffer

object rgc {
    var heading= 90
    var waypoint= List(1,10)
    def main(args: Array[String]) : Unit = {
        var file="rgcinput.txt"
        if (args.size > 0)
            file=args(0)
        val strings= Source.fromFile(file).mkString.split("\n")
        val loc= strings.map(heading(_)).reduce((x,y) => List(x(0)+y(0),x(1)+y(1)))
        println("Part 1",loc,Math.abs(loc(0))+Math.abs(loc(1)))
        val loc2= strings.map(headingWaypoint(_)).reduce((x,y) => List(x(0)+y(0),x(1)+y(1)))
        println("Part 2",loc2,Math.abs(loc2(0))+Math.abs(loc2(1)))
    }
    
  
    
    def heading(dirn : String) : List[Int] = {
        val num= dirn.substring(1).toInt
        dirn.charAt(0) match {
            case 'N' => List(num,0)
            case 'E' => List(0,num)
            case 'S' => List(-num,0)
            case 'W' => List(0,-num)
            case 'R' => heading= (heading+num)%360; List(0,0)
            case 'L' => heading= (heading-num+360)%360; List(0,0)
            case 'F' => heading  match {
                    case 0 => List(num,0)
                    case 90 => List(0,num)
                    case 180 => List(-num,0)
                    case 270 => List(0,-num)
                    case _ => println ("Heading error "+heading); List(0,0)
                }
            case _ => println("Error"+dirn); List(0,0)
        }
    }
    
    
    def headingWaypoint(dirn : String) : List[Int] = {
        val num= dirn.substring(1).toInt
        dirn.charAt(0) match {
            case 'N' => waypoint= List(waypoint(0)+ num,waypoint(1)); List(0,0)
            case 'E' => waypoint= List(waypoint(0),waypoint(1)+num);  List(0,0)
            case 'S' => waypoint= List(waypoint(0)-num,waypoint(1));  List(0,0)
            case 'W' => waypoint= List(waypoint(0),waypoint(1)-num);  List(0,0)
            case 'R' => num match {
                case 90 => waypoint= List(-waypoint(1),waypoint(0));  List(0,0)
                case 180 => waypoint= List(-waypoint(1),-waypoint(0));  List(0,0)
                case 270 => waypoint= List(waypoint(1),-waypoint(0));  List(0,0)
                case _ => println("Rotation error "+dirn); List(0,0)
            }
            case 'L' => num match {
                case 270 => waypoint= List(-waypoint(1),waypoint(0));  List(0,0)
                case 180 => waypoint= List(-waypoint(1),-waypoint(0));  List(0,0)
                case 90 => waypoint= List(waypoint(1),-waypoint(0));  List(0,0)
                case _ => println("Rotation error "+dirn); List(0,0)
            }
            case 'F' => List(waypoint(0)*num,waypoint(1)*num)
            case _ => println("Error"+dirn); List(0,0)
        }
    }
}



