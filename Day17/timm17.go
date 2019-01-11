package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type Square int

const (
	Sand Square = iota
	Clay
	Spring
	Water
	WetSand
)

var re = regexp.MustCompile(`^(.)=(\d+), (.)=(\d+)\.\.(\d+)$`)
var world = make([][]Square, 0)
var xOffset int
var yMin int

func SquareToRune(s Square) rune {
	switch s {
	case Sand:
		return '.'
	case Clay:
		return '#'
	case Spring:
		return '+'
	case Water:
		return '~'
	case WetSand:
		return '|'
	default:
		panic("")
	}
}

func printWorld() {
	for i := 0; i < len(world[0]); i++ {
		for _, row := range world {

			fmt.Print(string(SquareToRune(row[i])))
		}
		fmt.Println()
	}
}

func parseInput() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	yMin = 99999
	yMax := 0
	xMin := 99999
	xMax := -1

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		match := re.FindStringSubmatch(scanner.Text())
		if match == nil {
			panic("parsing error")
		}
		v1, _ := strconv.Atoi(match[2])
		v2, _ := strconv.Atoi(match[4])
		v3, _ := strconv.Atoi(match[5])

		var _xMin, _xMax, _yMin, _yMax int
		if match[1] == "x" && match[3] == "y" {
			_xMin = v1
			_xMax = v1
			_yMin = v2
			_yMax = v3
		} else if match[1] == "y" && match[3] == "x" {
			_yMin = v1
			_yMax = v1
			_xMin = v2
			_xMax = v3
		} else {
			panic("parsing error")
		}

		if _xMin < xMin {
			xMin = _xMin
		}

		if _yMin < yMin {
			yMin = _yMin
		}

		if _xMax > xMax {
			xMax = _xMax
		}

		if yMax < _yMax {
			for i := 0; i < len(world); i++ {
				world[i] = append(world[i], make([]Square, _yMax-yMax)...)
			}
			yMax = _yMax
		}
		for len(world) <= _xMax+1 {
			world = append(world, make([]Square, yMax+1))
		}
		for i := _xMin; i <= _xMax; i++ {
			for j := _yMin; j <= _yMax; j++ {
				world[i][j] = Clay
			}
		}
	}
	world[500][0] = Spring
	world = world[xMin-1:]
	xOffset = xMin - 1
}

func CheckSettleWater(x, y int) bool {
	leftStopFound := false
	for i := x; i >= 0; i-- {
		FillWaterDown(i, y+1)
		if world[i][y+1] != Water && world[i][y+1] != Clay {
			break
		}
		if world[i][y] == Clay || world[i][y] == Water {
			leftStopFound = true
			break
		}
	}

	rightStopFound := false
	for i := x; i < len(world); i++ {
		FillWaterDown(i, y+1)
		if world[i][y+1] != Water && world[i][y+1] != Clay {
			break
		}
		if world[i][y] == Clay || world[i][y] == Water {
			rightStopFound = true
			break
		}
	}
	return leftStopFound && rightStopFound
}

func FillWater(x, y int) {
	fmt.Println("FillWater", x, y)
	if y >= len(world[0])-1 {
		return
	}

	if world[x][y] == Clay || world[x][y] == Water || world[x][y] == WetSand {
		return
	}

	if world[x][y] == Sand {
		world[x][y] = WetSand
	}

	printWorld()

	FillWater(x, y+1)
	if CheckSettleWater(x, y) {
		world[x][y] = Water
	}
	if y < len(world[0])-1 {
		FillWater(x-1, y)
		FillWater(x+1, y)
	}
}

func FillWaterDown(x, y int) {
	if world[x][y] != Sand {
		//fmt.Println("No sand... Cannot flow")
		return
	}

	world[x][y] = WetSand

	if y >= len(world[0])-1 {
		//fmt.Println("Reached bottom")
		return
	}

	FillWaterDown(x, y+1)

	if CheckSettleWater(x, y) {
		world[x][y] = Water
	}

	if world[x][y+1] == Clay || world[x][y+1] == Water {
		FillWaterLeft(x-1, y)
		FillWaterRight(x+1, y)
	}
}

func FillWaterLeft(x, y int) {
	if x < 0 {
		return
	}

	if world[x][y] != Sand {
		// fmt.Println("No sand... Cannot flow")
		return
	}
	world[x][y] = WetSand

	FillWaterDown(x, y+1)
	if world[x][y+1] == Clay || world[x][y+1] == Water {
		FillWaterLeft(x-1, y)
	}

	if CheckSettleWater(x, y) {
		world[x][y] = Water
	}
}

func FillWaterRight(x, y int) {
	if x >= len(world) {
		return
	}

	if world[x][y] != Sand {
		// fmt.Println("No sand... Cannot flow")
		return
	}
	world[x][y] = WetSand

	FillWaterDown(x, y+1)
	if world[x][y+1] == Clay || world[x][y+1] == Water {
		FillWaterRight(x+1, y)
	}

	if CheckSettleWater(x, y) {
		world[x][y] = Water
	}
}

func main() {
	parseInput()

	FillWaterDown(500-xOffset, 1)
	printWorld()

	count := 0
	for _, col := range world {
		for i := yMin; i < len(col); i++ {
			if col[i] == Water || col[i] == WetSand {
				count++
			}
		}
	}
	fmt.Println(count)

	count = 0
	for _, col := range world {
		for i := yMin; i < len(col); i++ {
			if col[i] == Water {
				count++
			}
		}
	}
	fmt.Println(count)
}
