package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type nanobot struct {
	x, y, z, r int
}

type bbox struct {
	x0, x1 int
	y0, y1 int
	z0, z1 int
	count  int
}

var re = regexp.MustCompile(`^pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)$`)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func distance(n1, n2 nanobot) int {
	return abs(n1.x-n2.x) + abs(n1.y-n2.y) + abs(n1.z-n2.z)
}

func distance3(n nanobot, box bbox) int {
	dist := 0
	if d := box.x0 - n.x; d > 0 {
		dist += d
	}
	if d := n.x - box.x1; d > 0 {
		dist += d
	}
	if d := box.y0 - n.y; d > 0 {
		dist += d
	}
	if d := n.y - box.y1; d > 0 {
		dist += d
	}
	if d := box.z0 - n.z; d > 0 {
		dist += d
	}
	if d := n.z - box.z1; d > 0 {
		dist += d
	}
	return dist
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	nanobots := make([]nanobot, 0)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		match := re.FindStringSubmatch(scanner.Text())
		if match == nil {
			panic(scanner.Text())
		}
		x, _ := strconv.Atoi(match[1])
		y, _ := strconv.Atoi(match[2])
		z, _ := strconv.Atoi(match[3])
		r, _ := strconv.Atoi(match[4])
		nanobots = append(nanobots, nanobot{x, y, z, r})
	}

	// part 1
	maxNanobot := nanobots[0]
	for _, nanobot := range nanobots {
		if nanobot.r > maxNanobot.r {
			maxNanobot = nanobot
		}
	}

	count := 0
	for _, nanobot := range nanobots {
		if distance(nanobot, maxNanobot) <= maxNanobot.r {
			count += 1
		}
	}
	fmt.Println(count)

	// part 2
	var box bbox
	for count, bound := 0, 1; count < len(nanobots); bound *= 2 {
		box = bbox{-(bound - 1), bound, -(bound - 1), bound, -(bound - 1), bound, 0}
		count = 0
		for _, nanobot := range nanobots {
			if distance3(nanobot, box) == 0 {
				count++
			}
		}
		box.count = count

	}

	boxes := []bbox{box}
	for {
		maxCount := -1
		maxIdx := -1
		for idx, box := range boxes {
			if box.count > maxCount {
				maxCount = box.count
				maxIdx = idx
			}
		}

		maxBox := boxes[maxIdx]
		if maxBox.x0 == maxBox.x1 && maxBox.y0 == maxBox.y1 && maxBox.z0 == maxBox.z1 {
			fmt.Println(abs(maxBox.x0) + abs(maxBox.y0) + abs(maxBox.z0))
			break
		}
		boxes = append(boxes[:maxIdx], boxes[maxIdx+1:]...)

		newBoxes := []bbox{
			bbox{maxBox.x0, (maxBox.x0 + maxBox.x1) / 2, maxBox.y0, (maxBox.y0 + maxBox.y1) / 2, maxBox.z0, (maxBox.z0 + maxBox.z1) / 2, -1},
			bbox{(maxBox.x0+maxBox.x1)/2 + 1, maxBox.x1, maxBox.y0, (maxBox.y0 + maxBox.y1) / 2, maxBox.z0, (maxBox.z0 + maxBox.z1) / 2, -1},
			bbox{maxBox.x0, (maxBox.x0 + maxBox.x1) / 2, (maxBox.y0+maxBox.y1)/2 + 1, maxBox.y1, maxBox.z0, (maxBox.z0 + maxBox.z1) / 2, -1},
			bbox{(maxBox.x0+maxBox.x1)/2 + 1, maxBox.x1, (maxBox.y0+maxBox.y1)/2 + 1, maxBox.y1, maxBox.z0, (maxBox.z0 + maxBox.z1) / 2, -1},
			bbox{maxBox.x0, (maxBox.x0 + maxBox.x1) / 2, maxBox.y0, (maxBox.y0 + maxBox.y1) / 2, (maxBox.z0+maxBox.z1)/2 + 1, maxBox.z1, -1},
			bbox{(maxBox.x0+maxBox.x1)/2 + 1, maxBox.x1, maxBox.y0, (maxBox.y0 + maxBox.y1) / 2, (maxBox.z0+maxBox.z1)/2 + 1, maxBox.z1, -1},
			bbox{maxBox.x0, (maxBox.x0 + maxBox.x1) / 2, (maxBox.y0+maxBox.y1)/2 + 1, maxBox.y1, (maxBox.z0+maxBox.z1)/2 + 1, maxBox.z1, -1},
			bbox{(maxBox.x0+maxBox.x1)/2 + 1, maxBox.x1, (maxBox.y0+maxBox.y1)/2 + 1, maxBox.y1, (maxBox.z0+maxBox.z1)/2 + 1, maxBox.z1, -1},
		}
		for i, box := range newBoxes {
			count := 0
			for _, nanobot := range nanobots {
				if dist := distance3(nanobot, box); dist <= nanobot.r {
					count++
				}
			}
			newBoxes[i].count = count
		}
		boxes = append(boxes, newBoxes...)
	}
}
