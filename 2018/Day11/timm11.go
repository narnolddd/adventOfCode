package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func calcPowerLevel(x, y, gridSerial int) int {
	rackID := x + 10
	powerLevel := rackID * y
	powerLevel += gridSerial
	powerLevel *= rackID
	powerLevel /= 100
	powerLevel %= 10
	powerLevel -= 5
	return powerLevel
}

func sumPowerLevel(x, y, size int, fuelGrid [][]int) int {
	if x > (300-size) || y > (300-size) {
		panic("FUCK")
	}
	sum := 0
	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			sum += fuelGrid[x+i][y+j]
		}
	}
	return sum
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()
	scanner := bufio.NewScanner(f)
	scanner.Scan()
	gridSerial, _ := strconv.Atoi(scanner.Text())

	fuelGridLen := 300
	fuelGrid := make([][]int, fuelGridLen)
	for i := 0; i < fuelGridLen; i++ {
		fuelGrid[i] = make([]int, fuelGridLen)
	}

	for i := 0; i < fuelGridLen; i++ {
		for j := 0; j < fuelGridLen; j++ {
			fuelGrid[i][j] = calcPowerLevel(i+1, j+1, gridSerial)
		}
	}

	var maxX, maxY int
	maxPower := -1
	for i := 0; i < fuelGridLen-2; i++ {
		for j := 0; j < fuelGridLen-2; j++ {
			if power := sumPowerLevel(i, j, 3, fuelGrid); power > maxPower {
				maxPower = power
				maxX = i
				maxY = j
			}
		}
	}
	fmt.Printf("%d,%d\n", maxX+1, maxY+1)

	maxPower = -1
	maxSize := -1
	for s := 1; s <= fuelGridLen; s++ {
		for i := 0; i <= fuelGridLen-s; i++ {
			for j := 0; j <= fuelGridLen-s; j++ {
				if power := sumPowerLevel(i, j, s, fuelGrid); power > maxPower {
					maxPower = power
					maxX = i
					maxY = j
					maxSize = s
				}
			}
		}
	}
	fmt.Printf("%d,%d,%d\n", maxX+1, maxY+1, maxSize)
}
