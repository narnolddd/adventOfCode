package main

import (
	"bufio"
	"container/ring"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

var re = regexp.MustCompile(`^(\d+) players; last marble is worth (\d+) points$`)

func solveMarblesSlice(nPlayers int, nMarbles int) {
	marbles := make([]int, 1, nMarbles)
	currentMarbleIdx := 0
	currentPlayer := 0
	playerPoints := make([]int, nPlayers)

	for marble := 1; marble <= nMarbles; marble++ {
		if marble%23 == 0 {
			playerPoints[currentPlayer] += marble
			removeMarbleIdx := (currentMarbleIdx - 7) % (len(marbles))
			if removeMarbleIdx < 0 {
				removeMarbleIdx += len(marbles)
			}
			removeMarbleValue := marbles[removeMarbleIdx]
			playerPoints[currentPlayer] += removeMarbleValue

			copy(marbles[removeMarbleIdx:], marbles[removeMarbleIdx+1:])
			marbles = marbles[:len(marbles)-1]
			currentMarbleIdx = removeMarbleIdx
		} else {
			nextMarbleIdx := (currentMarbleIdx + 1) % (len(marbles))
			nextMarbleIdx++

			marbles = append(marbles, 0)
			copy(marbles[nextMarbleIdx+1:], marbles[nextMarbleIdx:])
			marbles[nextMarbleIdx] = marble

			currentMarbleIdx = nextMarbleIdx
		}
		currentPlayer = (currentPlayer + 1) % nPlayers
	}

	maxPoints := 0
	for _, points := range playerPoints {
		if points > maxPoints {
			maxPoints = points
		}
	}

	fmt.Println(maxPoints)
}

func solveMarblesRing(nPlayers int, nMarbles int) {
	marbles := ring.New(1)
	marbles.Value = 0

	currentMarble := marbles
	currentPlayer := 0
	playerPoints := make([]int, nPlayers)

	for marble := 1; marble <= nMarbles; marble++ {
		if marble%23 == 0 {
			playerPoints[currentPlayer] += marble

			for i := 0; i < 7; i++ {
				currentMarble = currentMarble.Prev()
			}
			playerPoints[currentPlayer] += currentMarble.Value.(int)

			currentMarble = currentMarble.Prev()
			currentMarble.Unlink(1)
			currentMarble = currentMarble.Next()
		} else {
			newRing := ring.New(1)
			newRing.Value = marble

			currentMarble = currentMarble.Next()
			currentMarble.Link(newRing)
			currentMarble = currentMarble.Next()
		}
		currentPlayer = (currentPlayer + 1) % nPlayers

		/*marbles.Do(func(x interface{}) {
			fmt.Printf("%d ", x.(int))
		})
		fmt.Println()*/
	}

	maxPoints := 0
	for _, points := range playerPoints {
		if points > maxPoints {
			maxPoints = points
		}
	}

	fmt.Println(maxPoints)
}

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	line := scanner.Text()
	match := re.FindStringSubmatch(line)
	nPlayers, _ := strconv.Atoi(match[1])
	nMarbles, _ := strconv.Atoi(match[2])

	solveMarblesSlice(nPlayers, nMarbles)
	solveMarblesRing(nPlayers, nMarbles)
	solveMarblesRing(nPlayers, nMarbles*100)
}
