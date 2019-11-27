package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type node struct {
	children []node
	metadata []int
}

func part1(input *[]int) int {
	nChildren := (*input)[0]
	nMetadata := (*input)[1]
	*input = (*input)[2:]

	nodeValue := 0
	for i := 0; i < nChildren; i++ {
		nodeValue += part1(input)
	}

	for i := 0; i < nMetadata; i++ {
		nodeValue += (*input)[i]
	}
	*input = (*input)[nMetadata:]

	return nodeValue
}

func part2(input *[]int) int {
	nChildren := (*input)[0]
	nMetadata := (*input)[1]
	*input = (*input)[2:]

	childrenValue := []int{}
	for i := 0; i < nChildren; i++ {
		childrenValue = append(childrenValue, part2(input))
	}

	nodeValue := 0
	if nChildren == 0 {
		for i := 0; i < nMetadata; i++ {
			nodeValue += (*input)[i]
		}
	} else {
		for i := 0; i < nMetadata; i++ {
			if metaData := (*input)[i]; metaData > 0 && metaData <= nChildren {
				nodeValue += childrenValue[metaData-1]
			}
		}
	}
	*input = (*input)[nMetadata:]

	return nodeValue
}

func main() {
	f, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)
	input := make([]int, 0)
	for scanner.Scan() {
		inputInt, _ := strconv.Atoi(scanner.Text())
		input = append(input, inputInt)
	}
	inputOne := input[:]
	fmt.Println(part1(&inputOne))

	inputTwo := input[:]
	fmt.Println(part2(&inputTwo))
}
