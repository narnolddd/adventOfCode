package main

import (
	"bufio"
	"fmt"
	"os"
)

func part1() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var twos, threes int64 = 0, 0
	for scanner.Scan() {
		line := scanner.Text()
		char_freqs := make(map[rune]int)
		for _, runeValue := range line {
			if count, found := char_freqs[runeValue]; found {
				char_freqs[runeValue] = count + 1
			} else {
				char_freqs[runeValue] = 1
			}
		}

		var count_two, count_three bool = false, false
		for _, count := range char_freqs {
			if count == 2 {
				count_two = true
			} else if count == 3 {
				count_three = true
			}
		}

		if count_two {
			twos += 1
		}
		if count_three {
			threes += 1
		}
	}
	fmt.Println(twos * threes)
}

func part2() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
Loop:
	for _, line1 := range lines {
		for _, line2 := range lines {
			diff_counter := 0
			for i := 0; i < len(line1); i++ {
				rune1 := line1[i]
				rune2 := line2[i]
				if rune1 != rune2 {
					diff_counter += 1
				}
			}
			if diff_counter == 1 {
				fmt.Println(line1)
				fmt.Println(line2)
				break Loop
			}
		}
	}
}

func main() {
	part1()
	part2()
}
