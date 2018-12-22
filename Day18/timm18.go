package main

import (
	"bufio"
	"fmt"
	"os"
)

type forest int

const (
	open forest = iota
	tree
	lumberyard
)

func runeToForest(r rune) forest {
	switch r {
	case '.':
		return open
	case '|':
		return tree
	case '#':
		return lumberyard
	default:
		panic("")
	}
}

func forestToRune(f forest) rune {
	switch f {
	case open:
		return '.'
	case tree:
		return '|'
	case lumberyard:
		return '#'
	default:
		panic("")
	}
}

func printWorld() {
	for i := 0; i < len(world[0]); i++ {
		for _, row := range world {
			fmt.Print(string(forestToRune(row[i])))
		}
		fmt.Println()
	}
}

var world [][]forest

func parseInput() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if world == nil {
			for i := 0; i < len(line); i++ {
				world = append(world, make([]forest, 0))
			}
		}

		for i, r := range line {
			world[i] = append(world[i], runeToForest(r))
		}
	}
}

func CountNeighbours(x, y int, f forest) int {
	count := 0
	if y > 0 {
		if x > 0 && world[x-1][y-1] == f {
			count++
		}
		if world[x][y-1] == f {
			count++
		}
		if x < len(world)-1 && world[x+1][y-1] == f {
			count++
		}
	}

	if x > 0 && world[x-1][y] == f {
		count++
	}
	if x < len(world)-1 && world[x+1][y] == f {
		count++
	}

	if y < len(world[0])-1 {
		if x > 0 && world[x-1][y+1] == f {
			count++
		}
		if world[x][y+1] == f {
			count++
		}
		if x < len(world)-1 && world[x+1][y+1] == f {
			count++
		}
	}
	return count
}

func main() {
	parseInput()

	newWorld := make([][]forest, len(world))
	for i := 0; i < len(newWorld); i++ {
		newWorld[i] = make([]forest, len(world[0]))
	}
	
	valueLastSeen := make(map[int]int)
	valueCounter := make(map[int]int)
	
	for t := 1; t <= 1000000000; t++ {
		for i := 0; i < len(world); i++ {
			for j := 0; j < len(world[i]); j++ {
				switch world[i][j] {
				case open:
					if CountNeighbours(i, j, tree) >= 3 {
						newWorld[i][j] = tree
					} else {
						newWorld[i][j] = open
					}
				case tree:
					if CountNeighbours(i, j, lumberyard) >= 3 {
						newWorld[i][j] = lumberyard
					} else {
						newWorld[i][j] = tree
					}

				case lumberyard:
					if CountNeighbours(i, j, lumberyard) >= 1 && CountNeighbours(i, j, tree) >= 1 {
						newWorld[i][j] = lumberyard
					} else {
						newWorld[i][j] = open
					}
				default:
					panic("")
				}
			}
		}

		world, newWorld = newWorld, world
		
		countWood := 0
		countLumberyard := 0
		for _, col := range world {
			for _, cell := range col {
				if cell == tree {
					countWood++
				} else if cell == lumberyard {
					countLumberyard++
				}
			}
		}
		forestValue := countWood*countLumberyard
		if t == 10 {
			fmt.Println("Part 1", forestValue)
		}
	
		valueCounter[forestValue]++
		if valueCounter[forestValue] >= 10 {
			period := t-valueLastSeen[forestValue]
			fmt.Printf("Seen first value for more than ten times, assume stable series now...\n")
			fmt.Printf("Current iteration %d\n", t)
			fmt.Printf("Saw value %d last time in iteration %d, which is %d iterations ago...\n", forestValue, valueLastSeen[forestValue], period)

			targetIteration := t - (period - ((1000000000 - t) % period))
			fmt.Printf("Correct value is value of iteration %d\n", targetIteration)
			for k, v := range valueLastSeen {
				if v == targetIteration{
					fmt.Println("Part 2", k)
				}
			}
			break
		}
		valueLastSeen[forestValue] = t
	}
}
