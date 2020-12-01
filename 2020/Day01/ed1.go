package main 

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type void struct{}
var member void

type numbers struct {
    n1 int
    n2 int
}

func main() {
	// values map[int]void
	set := make(map[int]int)
	// subtracted := []int{}
 
	input := bufio.NewScanner(os.Stdin) 
	for input.Scan() {
        if i, err := strconv.Atoi(input.Text()); err == nil{
            set[i] = 2020 - i
        }
    }

    for k, v := range set {
    	_, exists := set[v]
		if exists {
			fmt.Println(k, v, k*v)
			break
		}
    }

    // Part 2
    second_set := make(map[numbers]int)
    for k1, _ := range set {
    	for k2, _ := range set {
    		if k1 == k2 || k1 + k2 > 2020 {
    			continue
    		}
    		v := k1 + k2
    		key := numbers{k1, k2}
    		second_set[key] = 2020 - v
    	}
    }

    for k, v := range second_set {
    	_, exists := set[v]
		if exists {
			fmt.Println(k.n1, k.n2, v, k.n1 * k.n2 *v)
			break
		}
    }
}