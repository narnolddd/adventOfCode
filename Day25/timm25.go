package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type point struct {
	x0, x1, x2, x3 int
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func (p point) distance(p2 point) int {
	return abs(p.x0-p2.x0) + abs(p.x1-p2.x1) + abs(p.x2-p2.x2) + abs(p.x3-p2.x3)
}

func dfs(p point, neighbours map[point][]point, visited map[point]struct{}) {
	if _, ok := visited[p]; ok {
		return
	}
	visited[p] = struct{}{}
	
	for _, n := range neighbours[p] {
		dfs(n, neighbours, visited)
	}
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	points := make([]point, 0)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		split := strings.Split(scanner.Text(), ",")
		x0, _ := strconv.Atoi(split[0])
		x1, _ := strconv.Atoi(split[1])
		x2, _ := strconv.Atoi(split[2])
		x3, _ := strconv.Atoi(split[3])
		points = append(points, point{x0, x1, x2, x3})
	}

	neighbours := make(map[point][]point)
	for i := 0; i < len(points); i++ {
		for j := 0; j < len(points); j++ {
			if points[i].distance(points[j]) <= 3 {
				neighbours[points[i]] = append(neighbours[points[i]], points[j])
			}
		}
	}

	visited := make(map[point]struct{})
	constellationCount := 0
	for _, p := range points {
		if _, ok := visited[p]; ok {
			continue
		}
		dfs(p, neighbours, visited)
		constellationCount++
	}
	fmt.Println(constellationCount)
}
