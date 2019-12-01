import scala.io.Source
Source.fromURL("https://pastebin.com/raw/Hmh1GDNa").mkString.split("\n").map(x=> new ((Int) => Int){def apply(x:Int):Int = if((x/3)-2<=0) 0 else ((x/3)-2) + apply((x/3)-2)}.apply(x.trim.replaceAll("\"","").toInt)).sum
