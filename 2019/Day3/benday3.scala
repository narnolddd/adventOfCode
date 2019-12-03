import scala.io.Source
import scala.collection.mutable.ArrayBuffer

//part 1
Source.fromURL("https://pastebin.com/raw/iWXHmv4B").mkString.split("\n").map(line=>line.trim.replaceAll("\"",""))
  .map(line => line.split(",").map(mov=>(mov.head,mov.tail.toInt)))
  .map(data=> new ((Array[(Char,Int)],ArrayBuffer[(Int,Int)],(Int,Int)) => ArrayBuffer[(Int,Int)]){
     def apply(mvmnts:Array[(Char,Int)],visited:ArrayBuffer[(Int,Int)],pos:(Int,Int)):ArrayBuffer[(Int,Int)] =
       if(mvmnts.isEmpty)  visited
       else if (mvmnts.head._1 == 'U') apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1,pos._2+inc)),(pos._1,pos._2+mvmnts.head._2))
       else if (mvmnts.head._1 == 'D') apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1,pos._2-inc)),(pos._1,pos._2-mvmnts.head._2))
       else if (mvmnts.head._1 == 'L') apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1-inc,pos._2)),(pos._1-mvmnts.head._2,pos._2))
       else  apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1+inc,pos._2)),(pos._1+mvmnts.head._2,pos._2))
      }.apply(data,ArrayBuffer[(Int,Int)](),(0,0))).reduce(_.intersect(_)).map(x=> x._1.abs+x._2.abs).min

//part2
Source.fromURL(  "https://pastebin.com/raw/iWXHmv4B").mkString.split("\n").map(line=>line.trim.replaceAll("\"",""))
  .map(line => line.split(",").map(mov=>(mov.head,mov.tail.toInt)))
  .map(data=> new ((Array[(Char,Int)],ArrayBuffer[(Int,Int,Int)],(Int,Int,Int)) => ArrayBuffer[(Int,Int,Int)]){
    def apply(mvmnts:Array[(Char,Int)],visited:ArrayBuffer[(Int,Int,Int)],pos:(Int,Int,Int)):ArrayBuffer[(Int,Int,Int)] =
      if(mvmnts.isEmpty)  visited
      else if (mvmnts.head._1 == 'U') apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1,pos._2+inc,pos._3+inc)),(pos._1,pos._2+mvmnts.head._2,pos._3+mvmnts.head._2))
      else if (mvmnts.head._1 == 'D') apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1,pos._2-inc,pos._3+inc)),(pos._1,pos._2-mvmnts.head._2,pos._3+mvmnts.head._2))
      else if (mvmnts.head._1 == 'L') apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1-inc,pos._2,pos._3+inc)),(pos._1-mvmnts.head._2,pos._2,pos._3+mvmnts.head._2))
      else  apply(mvmnts.tail,visited ++= 1.to(mvmnts.head._2).map(inc => (pos._1+inc,pos._2,pos._3+inc)),(pos._1+mvmnts.head._2,pos._2,pos._3+mvmnts.head._2))
  }.apply(data,ArrayBuffer[(Int,Int,Int)](),(0,0,0)).groupBy(x=>(x._1,x._2)).map(x=> (x._1._1,x._1._2,x._2.map(y=>y._3).min)))
  .reduce(_ ++ _).groupBy(x=>(x._1,x._2)).filter(x=>x._2.size>1).map(x=>x._2.map(y=>y._3).sum).min  //.map(x=>x._2)
