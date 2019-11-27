package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func equalSlice(sliceA, sliceB []int) bool {
	if len(sliceA) != len(sliceB) {
		panic("slice length")
	}
	for i := 0; i < len(sliceA); i++ {
		if sliceA[i] != sliceB[i] {
			return false
		}
	}
	return true
}

func part1(nRecipes int) {
	scores := []int{3, 7}
	elfIdx1 := 0
	elfIdx2 := 1

	for t := 0; len(scores) < nRecipes+10; t++ {
		nextScore := scores[elfIdx1] + scores[elfIdx2]
		if nextScore >= 10 {
			scores = append(scores, 1)
			scores = append(scores, nextScore-10)
		} else {
			scores = append(scores, nextScore)
		}
		elfIdx1 = (elfIdx1 + scores[elfIdx1] + 1) % len(scores)
		elfIdx2 = (elfIdx2 + scores[elfIdx2] + 1) % len(scores)
	}

	for _, n := range scores[nRecipes : nRecipes+10] {
		fmt.Print(n)
	}
	fmt.Println()
}

func part2(nRecipesStr string) {
	scores := []int{3, 7}
	elfIdx1 := 0
	elfIdx2 := 1

	nRecipes := make([]int, 0)
	for _, n := range nRecipesStr {
		nInt, _ := strconv.Atoi(string(n))
		nRecipes = append(nRecipes, nInt)
	}

	for {
		nextScore := scores[elfIdx1] + scores[elfIdx2]
		if nextScore >= 10 {
			scores = append(scores, 1)
			if len(scores) >= len(nRecipes) {
				if equalSlice(scores[len(scores)-len(nRecipes):], nRecipes) {
					fmt.Println(len(scores) - len(nRecipes))
					break
				}
			}
			scores = append(scores, nextScore-10)
		} else {
			scores = append(scores, nextScore)
		}

		if len(scores) >= len(nRecipes) {
			if equalSlice(scores[len(scores)-len(nRecipes):], nRecipes) {
				fmt.Println(len(scores) - len(nRecipes))
				break
			}
		}

		elfIdx1 = (elfIdx1 + scores[elfIdx1] + 1) % len(scores)
		elfIdx2 = (elfIdx2 + scores[elfIdx2] + 1) % len(scores)
	}
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Scan()
	nRecipesStr := scanner.Text()
	nRecipes, _ := strconv.Atoi(nRecipesStr)

	part1(nRecipes)
	part2(nRecipesStr)
}
