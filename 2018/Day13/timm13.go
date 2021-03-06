package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type cart struct {
	x                    int
	y                    int
	direction            int
	nextIntersectionTurn int
}

func intToTrack(c int) string {
	switch c {
	case 0:
		return " "
	case 1:
		return "|"
	case 2:
		return "-"
	case 3:
		return "/"
	case 4:
		return "\\"
	case 5:
		return "+"
	default:
		panic("Unknown track type")
	}
}

func intToCart(c int) string {
	switch c {
	case 1:
		return "^"
	case 2:
		return ">"
	case 3:
		return "v"
	case 4:
		return "<"
	default:
		panic("Unknown cart type")
	}
}

func printTrack(track [][]int, carts []cart) {
	for i, row := range track {
	Loop:
		for j, cell := range row {
			cartCount := 0
			var cartDirection int
			for _, cart := range carts {
				if cart.direction != -1 && cart.x == i && cart.y == j {
					cartCount++
					cartDirection = cart.direction
				}
			}
			if cartCount == 1 {
				fmt.Print(intToCart(cartDirection))
				continue Loop
			} else if cartCount == 2 {
				fmt.Print("X")
				continue Loop
			}

			fmt.Print(intToTrack(cell))
		}
		fmt.Println()
	}
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	trackWidth := 0
	trackHeight := 0
	scanner := bufio.NewScanner(f)
	lines := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
		if lineLen := len([]rune(line)); lineLen > trackWidth {
			trackWidth = lineLen
		}
		trackHeight++
	}

	track := make([][]int, 0)
	carts := make([]cart, 0)
	for i, line := range lines {
		row := make([]int, trackWidth)
		for j, c := range line {
			switch c {
			case ' ':
				row[j] = 0
			case '|':
				row[j] = 1
			case '-':
				row[j] = 2
			case '/':
				row[j] = 3
			case '\\':
				row[j] = 4
			case '+':
				row[j] = 5

			case '^':
				row[j] = 1
				carts = append(carts, cart{i, j, 1, 0})
			case 'v':
				row[j] = 1
				carts = append(carts, cart{i, j, 3, 0})

			case '<':
				row[j] = 2
				carts = append(carts, cart{i, j, 4, 0})
			case '>':
				row[j] = 2
				carts = append(carts, cart{i, j, 2, 0})

			default:
				panic("Unknown input type")
			}
		}
		track = append(track, row)
	}
	nCarts := len(carts)

Loop:
	for t := 0; t < 25000; t++ {
		// sort carts into turn order
		sort.Slice(carts, func(i, j int) bool {
			if carts[i].y != carts[j].y {
				return carts[i].y < carts[j].y
			} else {
				return carts[i].x < carts[j].x
			}
		})
		// move carts
		for i := range carts {
			cart := &carts[i]
			switch cart.direction {
			case -1:
				continue
			case 1:
				cart.x -= 1
				switch track[cart.x][cart.y] {
				case 1:
				case 2:
					break
				case 3:
					cart.direction = 2
				case 4:
					cart.direction = 4
				case 5:
					switch cart.nextIntersectionTurn {
					case 0:
						cart.direction = 4
					case 1:
					case 2:
						cart.direction = 2
					default:
						panic("")
					}
					cart.nextIntersectionTurn = (cart.nextIntersectionTurn + 1) % 3
				default:
					panic("")
				}
			case 2:
				cart.y += 1
				switch track[cart.x][cart.y] {
				case 1:
				case 2:
					break
				case 3:
					cart.direction = 1
				case 4:
					cart.direction = 3
				case 5:
					switch cart.nextIntersectionTurn {
					case 0:
						cart.direction = 1
					case 1:
					case 2:
						cart.direction = 3
					default:
						panic("")
					}
					cart.nextIntersectionTurn = (cart.nextIntersectionTurn + 1) % 3
				default:
					panic("")
				}
			case 3:
				cart.x += 1
				switch track[cart.x][cart.y] {
				case 1:
				case 2:
				case 3:
					cart.direction = 4
				case 4:
					cart.direction = 2
				case 5:
					switch cart.nextIntersectionTurn {
					case 0:
						cart.direction = 2
					case 1:
					case 2:
						cart.direction = 4
					default:
						panic("")
					}
					cart.nextIntersectionTurn = (cart.nextIntersectionTurn + 1) % 3
				default:
					panic("")
				}
			case 4:
				cart.y -= 1
				switch track[cart.x][cart.y] {
				case 1:
				case 2:
				case 3:
					cart.direction = 3
				case 4:
					cart.direction = 1
				case 5:
					switch cart.nextIntersectionTurn {
					case 0:
						cart.direction = 3
					case 1:
					case 2:
						cart.direction = 1
					default:
						panic("")
					}
					cart.nextIntersectionTurn = (cart.nextIntersectionTurn + 1) % 3
				default:
					panic("")
				}
			default:
				panic("Unknown movement direction")
			}
			for j := 0; j < len(carts); j++ {
				if i == j {
					continue
				}
				if carts[i].direction != -1 && carts[j].direction != -1 && carts[i].x == carts[j].x && carts[i].y == carts[j].y {
					fmt.Printf("Crash at %d,%d. Removing Carts...\n", carts[i].y, carts[i].x)
					carts[i].direction = -1
					carts[j].direction = -1
					nCarts -= 2
				}
			}
		}
		if nCarts == 1 {
			for _, cart := range carts {
				if cart.direction != -1 {
					fmt.Printf("Last cart at %d,%d\n", cart.y, cart.x)
					break Loop
				}
			}
		}
		//fmt.Printf("%d:\n", t)
		//printTrack(track, carts)
	}
}
