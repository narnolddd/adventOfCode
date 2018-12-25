package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type cell int

const (
	unknown cell = iota
	wall
	room
	doorh
	doorv
	marker
)

type point struct {
	x int
	y int
}

var world [][]cell
var roomDist map[point]int

func (c cell) String() string {
	switch c {
	case unknown:
		return "?"
	case wall:
		return "#"
	case room:
		return "."
	case doorh:
		return "-"
	case doorv:
		return "|"
	case marker:
		return "X"
	default:
		panic("")
	}
}

func printWorld() {
	for y := 0; y < len(world[0]); y++ {
		for x := 0; x < len(world); x++ {
			fmt.Print(world[x][y])
		}
		fmt.Println()
	}
	fmt.Println()
}

func dfs(x, y, dist int) {
	if _, ok := roomDist[point{x, y}]; ok {
		return
	}
	roomDist[point{x, y}] = dist
	if world[x][y+1] == doorh {
		dfs(x, y+2, dist+1)
	}
	if world[x][y-1] == doorh {
		dfs(x, y-2, dist+1)
	}
	if world[x-1][y] == doorv {
		dfs(x-2, y, dist+1)
	}
	if world[x+1][y] == doorv {
		dfs(x+2, y, dist+1)
	}
}

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Print(err)
	}

	input := []rune(strings.TrimSpace(string(b)))

	world = make([][]cell, 250)
	for i := 0; i < len(world); i++ {
		world[i] = make([]cell, 250)
	}

	world[125][125] = marker
	pos := point{125, 125}
	//printWorld()

	if input[0] == '^' {
		input = input[1:]
	} else {
		panic("")
	}

	stack := make([]point, 0)
	for _, r := range input {
		switch r {
		case 'N':
			world[pos.x][pos.y-1] = doorh
			world[pos.x][pos.y-2] = room
			pos.y -= 2
		case 'E':
			world[pos.x+1][pos.y] = doorv
			world[pos.x+2][pos.y] = room
			pos.x += 2
		case 'S':
			world[pos.x][pos.y+1] = doorh
			world[pos.x][pos.y+2] = room
			pos.y += 2
		case 'W':
			world[pos.x-1][pos.y] = doorv
			world[pos.x-2][pos.y] = room
			pos.x -= 2
		case '(':
			stack = append(stack, pos)
		case ')':
			pos = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		case '|':
			pos = stack[len(stack)-1]
		case '$':
		default:
			panic("")
		}
	}

	for i := 0; i < len(world); i++ {
		for j := 0; j < len(world[i]); j++ {
			if world[i][j] == unknown {
				world[i][j] = wall
			}
		}
	}

	//printWorld()
	roomDist = make(map[point]int)
	dfs(125, 125, 0)

	maxValue := -1
	for _, v := range roomDist {
		if v > maxValue {
			maxValue = v
		}
	}
	fmt.Println(maxValue)

	count := 0
	for _, v := range roomDist {
		if v >= 1000 {
			count++
		}
	}
	fmt.Println(count)
}
