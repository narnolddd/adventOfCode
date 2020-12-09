object tsu_day09 extends App {
  //TODO: This here ...pretends to be Scala! Don't be fooled! needs reworking...
  val fn = System.getenv().getOrDefault("FILE_PATH", "/home/tsunade/input-tsu-d9.txt").trim
  var data = scala.io.Source.fromFile(fn).getLines().map(_.trim.toLong).toArray
  val pream = 25

  val i = 0
  val invalid = data(Range(i, data.length - pream - 1).find { i =>
    val slice = data.slice(i, i + pream)
    val k = data(i + pream)
    !search(slice, k)
  }.get + pream)
  println("Uno: " + invalid)

  //+=+=+=+=+=+=+=+=+

  var mylist = List(0L)
  while (mylist.sum != invalid) {
    mylist = mylist.init
    val y = data.takeWhile { x =>
      mylist = x :: mylist //<---TODO: me not gusta
      mylist.sum <= invalid
    }
    data = data.drop(y.length)
    mylist = mylist.tail
  }
  println("Dos: " + (mylist.min + mylist.max))

  //+=+=+=+=+=+=+=+=+
  def search(slice: Array[Long], k: Long): Boolean = {
    var sorts = slice.sorted
    while (sorts.head < sorts.last) {
      val sum = sorts.head + sorts.last
      if (sum == k)
        return true
      else if (sum < k)
        sorts = sorts.tail
      else
        sorts = sorts.init
    }
    false
  }
}