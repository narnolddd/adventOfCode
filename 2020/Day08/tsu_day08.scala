object tsu_day08 extends App {
  //TODO: test the toroise/hare algorithm to detect loop
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d8.txt").trim
  val data = scala.io.Source.fromFile(fn).getLines().map(_.split(' ')).map(x=>(x.head, x.last.toInt)).toArray
  var track = List(0)
  var line = data.head
  var acc = 0

  run(data)
  println("Uno: " + acc)

  //+=+=+=+=+=+=+=+=+

  val loop = track.filter { x => List("jmp", "nop").contains(data(x)._1) }

  val culptit = loop.find { ptx =>
    val dtc = data.clone()
    dtc(ptx) = if (dtc(ptx)._1=="jmp") ("nop", dtc(ptx)._2) else ("jmp", dtc(ptx)._2)
    run(dtc)
  }.get
  println("Dos: " + acc+ " at line " + culptit)


  //+=+=+=+=+=+=+=+=+

  def run(code: Array[(String, Int)]): Boolean = {
    var line = code.head
    acc = 0
    track = List(0)
    while (!track.tail.contains(track.head)) {
      line = code(track.head)
      val opcode = line._1
      val value = line._2
      opcode match {
        case "acc" => {
          acc += value
          track = track.head + 1 :: track
        }
        case "jmp" =>   track = track.head + value :: track
        case _ => track = track.head + 1 :: track
      }
      if (track.head >= data.length) {
        return true
      }
    }
    false
  }
}