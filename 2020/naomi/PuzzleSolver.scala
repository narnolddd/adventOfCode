package naomi

trait PuzzleSolver {

  def execute() : Unit = {
    part1()
    part2()
  }

  def part1() : Unit
  def part2() : Unit

}
