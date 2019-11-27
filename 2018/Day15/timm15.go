package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type CellType int

const (
	Wall CellType = iota
	Cavern
	Goblin
	Elf
)

type Unit struct {
	X        int
	Y        int
	UnitType CellType
	HP       int
}

type Tuple struct {
	X int
	Y int
}

func runeToWorldCell(r rune) CellType {
	switch r {
	case '#':
		return Wall
	case '.':
		return Cavern
	case 'G':
		return Goblin
	case 'E':
		return Elf
	default:
		panic("")
	}
}

func WorldCellToRune(c CellType) rune {
	switch c {
	case Wall:
		return '#'
	case Cavern:
		return '.'
	case Goblin:
		return 'G'
	case Elf:
		return 'E'
	default:
		panic("")
	}
}

func printWorld() {
	sort.Slice(units, func(i, j int) bool {
		if units[i].Y != units[j].Y {
			return units[i].Y < units[j].Y
		} else {
			return units[i].X < units[j].X
		}
	})
	for y, worldLine := range world {
		for _, cell := range worldLine {
			fmt.Print(string(WorldCellToRune(cell)))
		}
		fmt.Print("  ")
		for _, unit := range units {
			if unit.Y == y {
				fmt.Printf("%d(%d) ", unit.UnitType, unit.HP)
			}
		}
		fmt.Println()
	}
}

func shortestPathLength(x1, y1, x2, y2 int) int {
	if world[y2][x2] != Cavern {
		return -1
	}
	return bfs([]Tuple{Tuple{x1, y1}}, make(map[Tuple]bool), x2, y2)
}

func bfs(queue []Tuple, visited map[Tuple]bool, xDst int, yDst int) int {
	pathLength := 0
	for len(queue) > 0 {
		queueNew := make([]Tuple, 0)
		for len(queue) > 0 {
			x := queue[0].X
			y := queue[0].Y
			queue = queue[1:]

			if x == xDst && y == yDst {
				return pathLength
			}

			if world[y][x] != Cavern && pathLength > 0 {
				continue
			}

			if _, ok := visited[Tuple{x - 1, y}]; !ok && x-1 >= 0 {
				queueNew = append(queueNew, Tuple{x - 1, y})
				visited[Tuple{x - 1, y}] = true
			}
			if _, ok := visited[Tuple{x + 1, y}]; !ok && x+1 < len(world[0])-1 {
				queueNew = append(queueNew, Tuple{x + 1, y})
				visited[Tuple{x + 1, y}] = true
			}
			if _, ok := visited[Tuple{x, y - 1}]; !ok && y-1 >= 0 {
				queueNew = append(queueNew, Tuple{x, y - 1})
				visited[Tuple{x, y - 1}] = true
			}
			if _, ok := visited[Tuple{x, y + 1}]; !ok && y+1 < len(world)-1 {
				queueNew = append(queueNew, Tuple{x, y + 1})
				visited[Tuple{x, y + 1}] = true
			}
		}
		queue = queueNew
		pathLength++
	}

	return -1
}

func parseInput() {
	world = make([][]CellType, 0)
	units = make([]Unit, 0)

	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for y := 0; scanner.Scan(); y++ {
		line := scanner.Text()
		worldLine := make([]CellType, 0)
		for x, r := range line {
			if r == ' ' {
				break
			}
			worldLine = append(worldLine, runeToWorldCell(r))
			switch runeToWorldCell(r) {
			case Elf:
				units = append(units, Unit{x, y, Elf, 200})
			case Goblin:
				units = append(units, Unit{x, y, Goblin, 200})
			}
		}
		world = append(world, worldLine)
	}
}

func orderUnitsInReadingOrder(units *[]Unit) {
	sort.Slice(*units, func(i, j int) bool {
		if (*units)[i].Y != (*units)[j].Y {
			return (*units)[i].Y < (*units)[j].Y
		} else {
			return (*units)[i].X < (*units)[j].X
		}
	})
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func CalcAttackableNeighbours(activeUnit Unit) (int, bool) {
	attNeighbourIdx := -1
	attNeighbourHP := 999
	for j := 0; j < len(units); j++ {
		if abs(activeUnit.X-units[j].X)+abs(activeUnit.Y-units[j].Y) == 1 && activeUnit.UnitType != units[j].UnitType {
			if units[j].HP < attNeighbourHP {
				attNeighbourIdx = j
				attNeighbourHP = units[j].HP
			} else if units[j].HP == attNeighbourHP && (units[j].Y < units[attNeighbourIdx].Y ||
				(units[j].Y == units[attNeighbourIdx].Y && units[j].X < units[attNeighbourIdx].X)) {
				attNeighbourIdx = j
			}
		}
	}

	return attNeighbourIdx, attNeighbourIdx != -1
}

func CalcSquaresInRange(TargetUnitType CellType) []Tuple {
	SquaresInRange := make([]Tuple, 0)
	for j := 0; j < len(units); j++ {
		if units[j].UnitType == TargetUnitType {
			unitX := units[j].X
			unitY := units[j].Y
			if unitX-1 >= 0 {
				SquaresInRange = append(SquaresInRange, Tuple{unitX - 1, unitY})
			}
			if unitX+1 < len(world[0])-1 {
				SquaresInRange = append(SquaresInRange, Tuple{unitX + 1, unitY})
			}
			if unitY-1 >= 0 {
				SquaresInRange = append(SquaresInRange, Tuple{unitX, unitY - 1})
			}
			if unitY+1 >= 0 {
				SquaresInRange = append(SquaresInRange, Tuple{unitX, unitY + 1})
			}
		}
	}
	return SquaresInRange
}

func FindNearestSquare(activeUnit Unit, Squares []Tuple) (Tuple, bool) {
	var minSquare Tuple
	pathFound := false
	minDist := 999999
	for _, t := range Squares {
		if dist := shortestPathLength(activeUnit.X, activeUnit.Y, t.X, t.Y); dist != -1 && dist < minDist {
			minDist = dist
			minSquare = t
			pathFound = true
		} else if minDist == dist {
			if t.Y < minSquare.Y || (t.Y == minSquare.Y && t.X < minSquare.X) {
				minSquare = t
			}
		}
	}
	return minSquare, pathFound
}

func FindSquareToMoveTo(activeUnit Unit, Target Tuple) Tuple {
	var minSquare Tuple
	minDist := 99999
	if activeUnit.Y-1 >= 0 && world[activeUnit.Y-1][activeUnit.X] == Cavern {
		if dist := shortestPathLength(activeUnit.X, activeUnit.Y-1, Target.X, Target.Y); dist != -1 && dist < minDist {
			minDist = dist
			minSquare = Tuple{activeUnit.X, activeUnit.Y - 1}
		}
	}
	if activeUnit.X-1 >= 0 && world[activeUnit.Y][activeUnit.X-1] == Cavern {
		if dist := shortestPathLength(activeUnit.X-1, activeUnit.Y, Target.X, Target.Y); dist != -1 && dist < minDist {
			minDist = dist
			minSquare = Tuple{activeUnit.X - 1, activeUnit.Y}
		}
	}
	if activeUnit.X+1 < len(world[0]) && world[activeUnit.Y][activeUnit.X+1] == Cavern {
		if dist := shortestPathLength(activeUnit.X+1, activeUnit.Y, Target.X, Target.Y); dist != -1 && dist < minDist {
			minDist = dist
			minSquare = Tuple{activeUnit.X + 1, activeUnit.Y}
		}
	}
	if activeUnit.Y+1 < len(world) && world[activeUnit.Y+1][activeUnit.X] == Cavern {
		if dist := shortestPathLength(activeUnit.X, activeUnit.Y+1, Target.X, Target.Y); dist != -1 && dist < minDist {
			minDist = dist
			minSquare = Tuple{activeUnit.X, activeUnit.Y + 1}
		}
	}
	return minSquare
}

func SimulateCombat(ElfAttackPower int, PrintCombat bool) bool {
	parseInput()

	if PrintCombat {
		printWorld()
	}

	LostElf := false
	for t := 1; ; t++ {
		if PrintCombat {
			fmt.Println(t)
		}
		orderUnitsInReadingOrder(&units)

		for i := 0; i < len(units); i++ {
			activeUnit := &units[i]
			desiredType := Elf
			if (*activeUnit).UnitType == Elf {
				desiredType = Goblin
			}

			// Check whether not in range for attack, so move
			AttackNeighbourIdx, attackOk := CalcAttackableNeighbours(*activeUnit)
			if !attackOk {

				SquaresInRange := CalcSquaresInRange(desiredType)
				// No more enemies left
				if len(SquaresInRange) == 0 {
					if PrintCombat {
						printWorld()
					}
					remainingHP := 0
					for _, unit := range units {
						remainingHP += unit.HP
					}
					fmt.Printf("Combat ends after %d rounds with %d HP remaining\n", t-1, remainingHP)
					fmt.Println((t - 1) * remainingHP)
					return LostElf
				}
				chosenSquare, ok := FindNearestSquare(*activeUnit, SquaresInRange)

				// if not ok, no path found, cannot move
				if ok {
					minSquare := FindSquareToMoveTo(*activeUnit, chosenSquare)
					world[activeUnit.Y][activeUnit.X] = Cavern
					activeUnit.X = minSquare.X
					activeUnit.Y = minSquare.Y
					world[activeUnit.Y][activeUnit.X] = activeUnit.UnitType
				}
				AttackNeighbourIdx, attackOk = CalcAttackableNeighbours(*activeUnit)
			}
			// Moving done, now attack?
			if attackOk {
				if activeUnit.UnitType == Elf {
					units[AttackNeighbourIdx].HP -= ElfAttackPower
				} else {
					units[AttackNeighbourIdx].HP -= 3
				}
				// unit dead, remove from world
				if units[AttackNeighbourIdx].HP <= 0 {
					if units[AttackNeighbourIdx].UnitType == Elf {
						LostElf = true
					}
					world[units[AttackNeighbourIdx].Y][units[AttackNeighbourIdx].X] = Cavern
					units = append(units[:AttackNeighbourIdx], units[AttackNeighbourIdx+1:]...)
					// update index if deleting 'left in slice' of currently active unit
					if AttackNeighbourIdx < i {
						i--
					}
				}
			}
		}
		if PrintCombat {
			printWorld()
		}
	}
}

var world [][]CellType
var units []Unit

func main() {
	// Part 1
	SimulateCombat(3, true)

	// Part 2
	for ElfCombatPower := 4; SimulateCombat(ElfCombatPower, false); ElfCombatPower++ {
	}
}
