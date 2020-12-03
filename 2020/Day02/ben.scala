object day2 extends App {
  case class PasswordPolicy(min:Int,max:Int,letter:Char){
    def checkPasswordDownTheStreet(password: String):Boolean = min to max contains password.count (_ == letter)
    def checkPasswordTobogganCorporate(password:String):Boolean = password.charAt(min-1) == letter ^ password.charAt(max-1) == letter
  }
  case class CorruptPassword(policy: PasswordPolicy,password:String)

  println(scala.io.Source.fromFile("day2.text")
    .getLines
    .map(line => {
      val components = line.split(" ")
      val counts = components(0).split("-").map(_.toInt)
      CorruptPassword(PasswordPolicy(counts(0), counts(1), components(1).charAt(0)), components(2))
    })
    .count(toCheck =>
      toCheck.policy checkPasswordDownTheStreet toCheck.password)
    )

  println(scala.io.Source.fromFile("day2.text")
    .getLines
    .map(line => {
      val components = line.split(" ")
      val counts = components(0).split("-").map(_.toInt)
      CorruptPassword(PasswordPolicy(counts(0), counts(1), components(1).charAt(0)), components(2))
    })
    .count(toCheck =>
      toCheck.policy checkPasswordTobogganCorporate toCheck.password)
    )


}
