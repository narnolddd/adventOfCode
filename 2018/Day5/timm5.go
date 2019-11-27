package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func reduce_polymer(polymer string) (string, int) {
	p := []rune(polymer)

	for i, j := 0, 1; i < len(p)-1 && j < len(p); {
		if unicode.ToLower(p[i]) == unicode.ToLower(p[j]) && p[i] != p[j] {
			p[i] = '_'
			p[j] = '_'

			for i > 0 && p[i] == '_' {
				i -= 1
			}
		} else {
			i++
			for i < len(p)-1 && p[i] == '_' {
				i += 1
			}
		}
		j++
	}

	count := 0
	for _, r := range p {
		if r != '_' {
			count += 1
		}
	}

	return string(p), count
}

func part1(polymer string) {
	_, count := reduce_polymer(polymer)
	fmt.Println(count)
}

func part2(polymer string) {
	set := make(map[rune]bool)
	for _, r := range polymer {
		set[unicode.ToLower(r)] = true
	}

	min := len(polymer)
	for r, _ := range set {
		small_polymer := strings.Replace(polymer, string(r), "", -1)
		small_polymer = strings.Replace(small_polymer, string(unicode.ToUpper(r)), "", -1)
		_, count := reduce_polymer(small_polymer)
		if count < min {
			min = count
		}
	}
	fmt.Println(min)
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Scan()
	line := scanner.Text()

	part1(line)
	part2(line)
}
