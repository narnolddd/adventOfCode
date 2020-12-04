object tsu_day04 extends App{
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d4.txt").trim
  val data = scala.io.Source.fromFile(fn).mkString
  val ps= data.split("\n\n").map(_.split(Array(' ', '\n')).map(_.split(":").map(_.trim)).map(x=>(x.head->x.last)).toMap)

  println("First valid batch: \t"+ ps.count { x => checkpass(x) })
  println("Second valid batch: "+ ps.count{x=> if (checkpass(x)){checkpass2(x)}else false})

  def checkpass(data:Map[String,String]):Boolean={
    (data.keySet.size == 8) | ((data.keySet.size == 7) & (!data.keySet.contains("cid")))
  }
  def checkpass2(data:Map[String,String]):Boolean={
   (data("byr").length==4)&Range(1920,2003).contains(data("byr").toInt)&
    (data("iyr").length==4)&Range(2010,2021).contains(data("iyr").toInt)&
    (data("eyr").length==4)&Range(2020,2031).contains(data("eyr").toInt)&
    ((data("hgt").contains("cm")&Range(150,194).contains(data("hgt").split("\\D+").head.toInt))|
        (data("hgt").contains("in")&Range(59,77).contains(data("hgt").split("\\D+").head.toInt)))&
    data("hcl").startsWith("#")&(data("hcl").tail.length==6)&
    List("amb","blu","brn","gry","grn","hzl","oth").contains(data("ecl"))&
    data("pid").split("\\D+").head.length==9
  }
  }




