package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type claim struct {
	id     int
	x      int
	y      int
	width  int
	height int
}

var re = regexp.MustCompile(`^#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<width>\d+)x(?P<height>\d+)$`)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	claims := make([]claim, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		match := re.FindStringSubmatch(line)
		id, _ := strconv.Atoi(match[1])
		x, _ := strconv.Atoi(match[2])
		y, _ := strconv.Atoi(match[3])
		width, _ := strconv.Atoi(match[4])
		height, _ := strconv.Atoi(match[5])
		claims = append(claims, claim{id, x, y, width, height})

	}

	fabric := [1000][1000]int{}
	for _, claim := range claims {
		for i := claim.x; i < claim.x+claim.width; i++ {
			for j := claim.y; j < claim.y+claim.height; j++ {
				fabric[i][j] += 1
			}
		}
	}

	double_count := 0
	for _, col := range fabric {
		for _, cell := range col {
			if cell > 1 {
				double_count += 1
			}
		}
	}
	fmt.Println(double_count)

Loop:
	for _, claim := range claims {
		for i := claim.x; i < claim.x+claim.width; i++ {
			for j := claim.y; j < claim.y+claim.height; j++ {
				if fabric[i][j] > 1 {
					continue Loop
				}
			}
		}
		fmt.Println(claim)
		break
	}
}
