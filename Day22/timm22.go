package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type point struct {
	x, y int
	tool tool
}

type state struct {
	x, y, dist int
	tool       tool
}

type tool int

const (
	neither tool = iota
	torch
	climbing
)

func checkMove(typeFrom, typeTo int, tool tool) (int, tool) {
	if typeFrom == typeTo {
		return 0, tool
	}

	switch typeFrom {
	case 0:
		switch typeTo {
		case 1:
			if tool == torch {
				return 7, climbing
			}
			return 0, climbing
		case 2:
			if tool == climbing {
				return 7, torch
			}
			return 0, torch
		}
	case 1:
		switch typeTo {
		case 0:
			if tool == neither {
				return 7, climbing
			}
			return 0, climbing
		case 2:
			if tool == climbing {
				return 7, neither
			}
			return 0, neither
		}
	case 2:
		switch typeTo {
		case 0:
			if tool == neither {
				return 7, torch
			}
			return 0, torch
		case 1:
			if tool == torch {
				return 7, neither
			}
			return 0, neither
		}
	}
	panic("")
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Scan()
	depth, _ := strconv.Atoi(scanner.Text()[7:])
	scanner.Scan()
	s := strings.Split(scanner.Text()[8:], ",")
	targetX, _ := strconv.Atoi(s[0])
	targetY, _ := strconv.Atoi(s[1])

	cave := make([][]int, 2*targetX+1)
	for i := 0; i <= 2*targetX; i++ {
		cave[i] = make([]int, 2*targetY+1)
	}

	cave[0][0] = 0

	for x := 1; x <= 2*targetX; x++ {
		cave[x][0] = 16807 * x
	}

	for y := 1; y <= 2*targetY; y++ {
		cave[0][y] = 48271 * y
	}

	minCoordinate := targetX
	if targetY < minCoordinate {
		minCoordinate = targetY
	}

	for x := 1; x <= 2*targetX; x++ {
		for y := 1; y <= 2*targetY; y++ {
			cave[x][y] = (cave[x-1][y] + depth) % 20183 * ((cave[x][y-1] + depth) % 20183)
		}
		cave[targetX][targetY] = 0
	}

	for x := 0; x < len(cave); x++ {
		for y := 0; y < len(cave[x]); y++ {
			erosionLevel := ((cave[x][y] + depth) % 20183) % 3
			cave[x][y] = erosionLevel
		}
	}

	// part 1
	risk := 0
	for x := 0; x <= targetX; x++ {
		for y := 0; y <= targetY; y++ {
			risk += cave[x][y]
		}
	}
	fmt.Println(risk)

	// part 2
	visited := make(map[point]struct{})
	queue := []state{state{0, 0, 0, torch}}

	for len(queue) > 0 {
		// get state with shortest momentarily path
		var minIndex int
		minDist := 99999
		for idx, _ := range queue {
			if dist := queue[idx].dist; dist < minDist {
				minDist = dist
				minIndex = idx
			}
		}
		minState := queue[minIndex]
		queue = append(queue[:minIndex], queue[minIndex+1:]...)

		if minState.x == targetX && minState.y == targetY {
			if minState.tool == torch {
				fmt.Println(minDist)
				break
			} else {
				queue = append(queue, state{minState.x, minState.y, minState.dist + 7, torch})
				continue
			}

		}

		if _, ok := visited[point{minState.x, minState.y, minState.tool}]; ok {
			continue
		}
		visited[point{minState.x, minState.y, minState.tool}] = struct{}{}

		if minState.x > 0 {
			duration, newTool := checkMove(cave[minState.x][minState.y], cave[minState.x-1][minState.y], minState.tool)
			queue = append(queue, state{minState.x - 1, minState.y, minState.dist + duration + 1, newTool})
		}
		if minState.x < len(cave)-1 {
			duration, newTool := checkMove(cave[minState.x][minState.y], cave[minState.x+1][minState.y], minState.tool)
			queue = append(queue, state{minState.x + 1, minState.y, minState.dist + duration + 1, newTool})
		}
		if minState.y > 0 {
			duration, newTool := checkMove(cave[minState.x][minState.y], cave[minState.x][minState.y-1], minState.tool)
			queue = append(queue, state{minState.x, minState.y - 1, minState.dist + duration + 1, newTool})
		}
		if minState.y < len(cave[0])-1 {
			duration, newTool := checkMove(cave[minState.x][minState.y], cave[minState.x][minState.y+1], minState.tool)
			queue = append(queue, state{minState.x, minState.y + 1, minState.dist + duration + 1, newTool})
		}
	}
}
