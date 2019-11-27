package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func part1() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var sum int64 = 0
	for scanner.Scan() {
		val, _ := strconv.ParseInt(scanner.Text(), 10, 64)
		sum += val
	}
	fmt.Println(sum)
}

func part2() {
	frequencies_seen := make(map[int64]bool)
	frequencies_seen[0] = true

	var sum int64 = 0
Loop:
	for {
		file, _ := os.Open("input.txt")
		defer file.Close()

		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			val, _ := strconv.ParseInt(scanner.Text(), 10, 64)
			sum += val
			_, found := frequencies_seen[sum]
			if found {
				fmt.Println(sum)
				break Loop
			} else {
				frequencies_seen[sum] = true
			}
		}
	}
}

func main() {
	part1()
	part2()
}
