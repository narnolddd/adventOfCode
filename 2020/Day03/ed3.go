package main 

import (
	"bufio"
	"fmt"
	"os"
)

type direction struct {
	down int
	right int
	x_pos int 
}


func check_hit(line string, step, x_pos int, hits *int) int{
	if line[x_pos] == '#'{
		*hits += 1
	}
	return (x_pos + step) % len(line)
}

func main () {
	input := bufio.NewScanner(os.Stdin) 
	directions := [5]direction{ direction{1,1, 1}, direction{1, 3, 3}, direction{1, 5, 5}, 
				direction{1, 7, 7}, direction{2, 1, 1} }
	hits := [5]int{0, 0, 0, 0, 0}
	
	// Ignore the first line. 
	// This would not work if the problem 
	// wanted to check every traversed tree
	y := 1
	_ = input.Scan()
	for input.Scan() {
		line := input.Text()
		for i := 0; i < 5; i++ {
			if (y % directions[i].down == 0) {
				directions[i].x_pos = check_hit(line, directions[i].right, directions[i].x_pos, &hits[i]) 	
			}  			
		}
		y += 1

	}
	fmt.Println(hits[1])
	hit_mult := 1
	for i := 0; i < 5; i++ {
		hit_mult *= hits[i]
	}
	fmt.Println(hit_mult)
}