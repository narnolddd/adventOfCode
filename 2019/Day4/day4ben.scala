  import scala.util.matching.Regex

  def incrementing(x:String):Boolean = if(x.isEmpty) true else if(x.size==1) true else if(x.head <= x.tail.head) incrementing(x.tail) else false
  def secondCheck(x:String,count:Int,lastChar:Char) :Boolean =
    if (count==2) {
      if (x.isEmpty || (x.head != lastChar)) {
        true
      }
      else secondCheck(x.tail, count+1, x.head)
    }
    else {
      if (x.isEmpty) false
      else if (x.head == lastChar) secondCheck(x.tail, count + 1, x.head)
      else secondCheck(x.tail, 1, x.head)
    }
  231832.to(767346)
    .map(num => num.toString )
    .filter(x=> "00+|11+|22+|33+|44+|55+|66+|77+|88+|99+".r.findFirstIn(x)match{case Some(e) => true case None => false})
    .count(x => incrementing(x))
  
  231832.to(767346)
    .map(num => num.toString )
    .filter(x => incrementing(x))
    .count(x=> secondCheck(x,1,'s'))
