package main

import (
	"bufio"
	"fmt"
	"os"
)

var minPlantIdx, maxPlantIdx int

func encodePlant(r rune) int {
	if r == '.' {
		return 0
	} else if r == '#' {
		return 1
	} else {
		panic("unknown input encoding")
	}
}

func decodePlant(i int) rune {
	if i == 0 {
		return '.'
	} else if i == 1 {
		return '#'
	} else {
		panic("unknown input encoding")
	}
}

func printPlants(pots map[int]int, generation int) {
	fmt.Printf("%2d: ", generation)

	for i := minPlantIdx; i <= maxPlantIdx; i++ {
		fmt.Print(string(decodePlant(pots[i])))
	}
	fmt.Println()
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Scan()
	line := scanner.Text()
	line = line[15:]
	fmt.Println(line)

	pots := make(map[int]int)

	for i, r := range line {
		pots[i] = encodePlant(r)
	}
	minPlantIdx = 0
	maxPlantIdx = len(line) - 1

	scanner.Scan()
	rules := make(map[[5]int]int)
	for scanner.Scan() {
		line := []rune(scanner.Text())
		var rule [5]int
		for i, r := range line[:5] {
			rule[i] = encodePlant(r)
		}
		rules[rule] = encodePlant(line[9])
	}

	printPlants(pots, 0)
	var i int
	for i = 0; i < 20; i++ {
		potsNew := make(map[int]int)
		for j := minPlantIdx - 2; j <= maxPlantIdx+2; j++ {
			plantConfig := [5]int{pots[j-2], pots[j-1], pots[j], pots[j+1], pots[j+2]}
			potsNew[j] = rules[plantConfig]
		}
		minPlantIdx -= 2
		maxPlantIdx += 2
		pots = potsNew
		printPlants(pots, i+1)
	}

	potsSum := 0
	for k, v := range pots {
		if v == 1 {
			potsSum += k
		}
	}
	fmt.Println(potsSum)

	/*
	 Number of plants stabilises at some point.
	 Then it is only a matter of shifting them.
	 So run until stable.
	*/
	lastPotsSum := potsSum
	lastDiff := -1
	for ; ; i++ {
		potsNew := make(map[int]int)
		for j := minPlantIdx - 2; j <= maxPlantIdx+2; j++ {
			plantConfig := [5]int{pots[j-2], pots[j-1], pots[j], pots[j+1], pots[j+2]}
			potsNew[j] = rules[plantConfig]
		}
		minPlantIdx -= 2
		maxPlantIdx += 2
		pots = potsNew

		potsSum := 0
		for k, v := range pots {
			if v == 1 {
				potsSum += k
			}
		}

		if diff := potsSum - lastPotsSum; diff == lastDiff {
			fmt.Println((50000000000-i-1)*diff + potsSum)
			break
		} else {
			lastDiff = diff
			lastPotsSum = potsSum
		}
	}
}
