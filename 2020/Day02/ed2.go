package main 

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func strToInt(str string) int{
	i, err := strconv.Atoi(str)
	if err != nil{
		fmt.Println("Input error. Exiting...")
        os.Exit(0)
    }
    return i
}

func solve(password string, chr byte, lbound, ubound int) (rule1, rule2 int) {
	count := strings.Count(password, string(chr))
	rule1 = 0
	rule2 = 0
	if count >= lbound && count <= ubound {
		rule1 = 1
	}

	if (password[lbound-1] == chr && password[ubound-1] != chr) || 
	   (password[lbound-1] != chr && password[ubound-1] == chr){
		rule2 += 1
	}

	return rule1, rule2
}


func main() {
 
	input := bufio.NewScanner(os.Stdin) 
	rule1 := 0
	rule2 := 0
	for input.Scan() {
        parts := strings.Split(input.Text(), " ")
        bounds := strings.Split(parts[0], "-")
        lower_bound := strToInt(string(bounds[0]))
        upper_bound := strToInt(string(bounds[1]))
        chr := parts[1][0]
        word := parts[2]
        r1, r2 := solve(word, chr, lower_bound, upper_bound)
        rule1 += r1
        rule2 += r2
    }
    
    fmt.Println(rule1, rule2)
}