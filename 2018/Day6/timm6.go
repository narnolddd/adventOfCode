package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x  int
	y  int
	id int
}

func abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}

func manhattanDistance(a Point, b Point) int {
	return abs(a.x-b.x) + abs(a.y-b.y)
}

func part1(points []Point, maxX int, maxY int) {
	for j := 0; j < maxY+1; j++ {
		indexLower := -1
		indexUpper := -1
		minDistLower := 999999
		minDistUpper := 999999
		for p, point := range points {
			if dist := manhattanDistance(Point{0, j, -1}, point); dist < minDistLower {
				minDistLower = dist
				indexLower = p
			}
			if dist := manhattanDistance(Point{maxX, j, -1}, point); dist < minDistUpper {
				minDistUpper = dist
				indexUpper = p
			}
		}

		// fmt.Println("Killing Point", points[indexLower])
		points[indexLower].id = -1
		// fmt.Println("Killing Point", points[indexUpper])
		points[indexUpper].id = -1
	}

	for i := 0; i < maxX+1; i++ {
		indexLeft := -1
		indexRight := -1
		minDistLeft := 999999
		minDistRight := 999999
		for p, point := range points {
			if dist := manhattanDistance(Point{i, 0, -1}, point); dist < minDistLeft {
				minDistLeft = dist
				indexLeft = p
			}
			if dist := manhattanDistance(Point{i, maxY, -1}, point); dist < minDistRight {
				minDistRight = dist
				indexRight = p
			}
		}

		// fmt.Println("Killing Point", points[indexLeft])
		points[indexLeft].id = -1
		// fmt.Println("Killing Point", points[indexRight])
		points[indexRight].id = -1
	}

	/*for i, pointA := range points {
		smallerX := false
		smallerY := false
		biggerX := false
		biggerY := false
		for _, pointB := range points {
			if pointB.x < pointA.x {
				smallerX = true
			}
			if pointB.x > pointA.x {
				biggerX = true
			}
			if pointB.y < pointA.y {
				smallerY = true
			}
			if pointB.y > pointA.y {
				biggerY = true
			}
		}
		if !smallerX || !biggerX || !smallerY || !biggerY {
			fmt.Println("Killing Point", pointA)
			points[i].id = -1
		}
	}*/

	/*
		grid := make([][]int, maxX+1)
		for i := range grid {
			grid[i] = make([]int, maxY+1)
		}

		for i := 0; i < len(grid); i++ {
			for j := 0; j < len(grid[i]); j++ {
				minDistance := 999999
				var minPoint Point
				gridPoint := Point{i, j, -1}
				for _, point := range points {
					dist := manhattanDistance(point, gridPoint)
					if dist < minDistance {
						minDistance = dist
						minPoint = point
					} else if dist == minDistance {
						minPoint = Point{0, 0, -1}
					}
				}
				grid[i][j] = minPoint.id
			}
		}


		pointCounts := make(map[int]int)
		for _, col := range grid {
			for _, cell := range col {
				pointCounts[cell] += 1
			}
		}
	*/

	pointCounts := make(map[int]int)
	for i := 0; i < maxX+1; i++ {
		for j := 0; j < maxY+1; j++ {
			minDistance := 999999
			var minPointId int
			gridPoint := Point{i, j, -1}
			for _, point := range points {
				dist := manhattanDistance(point, gridPoint)
				if dist < minDistance {
					minDistance = dist
					minPointId = point.id
				} else if dist == minDistance {
					minPointId = -1
				}
			}
			pointCounts[minPointId] += 1
		}
	}

	MaxCellCount := 0
	for cellNumber, cellCount := range pointCounts {
		if cellNumber != -1 && cellCount > MaxCellCount {
			MaxCellCount = cellCount
		}
	}

	fmt.Println(MaxCellCount)
}

func part2(points []Point, maxX int, maxY int) {
	areaCounter := 0
	for i := 0; i < maxX+1; i++ {
		for j := 0; j < maxY+1; j++ {
			totalDistance := 0
			gridPoint := Point{i, j, -1}
			for _, point := range points {
				totalDistance += manhattanDistance(point, gridPoint)
			}
			if totalDistance <= 10000 {
				areaCounter += 1
			}
		}
	}

	fmt.Println(areaCounter)
}

func main() {
	f, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(f)

	var points []Point
	maxX := 0
	maxY := 0
	id := 1
	for scanner.Scan() {
		p := strings.Split(scanner.Text(), ", ")
		x, _ := strconv.Atoi(p[0])
		y, _ := strconv.Atoi(p[1])
		point := Point{x, y, id}
		points = append(points, point)
		id += 1

		if point.x > maxX {
			maxX = x
		}

		if point.y > maxY {
			maxY = y
		}
	}

	part1(points, maxX, maxY)
	part2(points, maxX, maxY)
}
