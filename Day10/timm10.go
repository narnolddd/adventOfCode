package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type tuple struct {
	x int
	y int
}

type star struct {
	position tuple
	velocity tuple
}

var re = regexp.MustCompile(`^position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>$`)

func printStars(stars []star) (string, int) {
	starMap := make(map[int]map[int]bool)

	minX := 99999
	maxX := -99999
	minY := 99999
	maxY := -99999
	for _, star := range stars {
		if starMap[star.position.x] == nil {
			starMap[star.position.x] = make(map[int]bool)
		}
		starMap[star.position.x][star.position.y] = true

		if star.position.x < minX {
			minX = star.position.x
		}

		if star.position.x > maxX {
			maxX = star.position.x
		}

		if star.position.y < minY {
			minY = star.position.y
		}

		if star.position.y > maxY {
			maxY = star.position.y
		}
	}

	width := maxX - minX
	if width > 250 {
		return "", width
	}

	var b strings.Builder
	for y := minY - 1; y <= maxY+1; y++ {
		for x := minX - 1; x <= maxX+1; x++ {
			if starMap[x][y] == true {
				b.WriteString("#")
			} else {
				b.WriteString(".")
			}
		}
		b.WriteString("\n")
	}

	return b.String(), width
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	stars := []star{}
	for scanner.Scan() {
		match := re.FindStringSubmatch(scanner.Text())
		posX, _ := strconv.Atoi(match[1])
		posY, _ := strconv.Atoi(match[2])
		velX, _ := strconv.Atoi(match[3])
		velY, _ := strconv.Atoi(match[4])
		stars = append(stars, star{tuple{posX, posY}, tuple{velX, velY}})
	}

	minWidth := 99999
	var minFirmament string
	var minLoopIndex int

	for i := 0; i < 25000; i++ {
		firmament, width := printStars(stars)
		if width < minWidth {
			minWidth = width
			minFirmament = firmament
			minLoopIndex = i
		}

		for i, star := range stars {
			stars[i].position.x += star.velocity.x
			stars[i].position.y += star.velocity.y
		}
	}
	fmt.Println(minLoopIndex)
	fmt.Print(minFirmament)
}
