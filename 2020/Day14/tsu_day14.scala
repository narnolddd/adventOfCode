import java.lang.Long.parseLong

object tsu_day14 extends App {
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d14.txt").trim
  var data = scala.io.Source.fromFile(fn).getLines().toArray
  var dataMem = scala.collection.mutable.Map[Long, String]()
  var addrMem = scala.collection.mutable.Map[Long, Long]()
  val REG_SIZE = 36
  var mask = "X" * REG_SIZE

  data.foreach { line =>
    if (line.startsWith("mask")) {
      mask = line.split("=").last.trim
    } else {
      val List(mem, value) = """\d+""".r.findAllIn(line).toList.map(_.toLong)
      val binv = ("0" * REG_SIZE + value.toBinaryString takeRight REG_SIZE grouped 1).toArray
      mask.zipWithIndex.filter(_._1 != 'X').foreach(x => binv(x._2) = mask(x._2).toString)
      if (!dataMem.keySet.contains(mem))
        dataMem ++= Map(mem -> "0" * REG_SIZE)
      dataMem(mem) = binv.mkString

      val binmem = ("0" * REG_SIZE + mem.toBinaryString takeRight REG_SIZE grouped 1).toArray
      mask.zipWithIndex.filter(_._1 != '0').foreach(x => binmem(x._2) = mask(x._2).toString)
      possBins(binmem.mkString).foreach { addr =>
        if (!addrMem.keySet.contains(addr))
          addrMem ++= Map(mem -> 0)
        addrMem(addr) = value
      }
    }
  }

  println("パート 1: " + dataMem.values.map(parseLong(_, 2)).sum) // パート 1: 9615006043476
  println("パート 2: " + addrMem.values.sum)                            //  パート 2: 4275496544925

  def possBins(bin: String): Array[Long] = {
    val idx = bin.indexWhere(_ == 'X')
    val tmp = Array('0', '1').map(bin.take(idx) + _ + bin.drop(idx + 1))
    if (tmp.mkString.contains('X'))   tmp.flatMap(possBins)    else  tmp.map(parseLong(_, 2))
  }
}