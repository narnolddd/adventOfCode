package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
    "container/ring" 
)

func print_ring(r *ring.Ring) {
    fmt.Printf("(%d)",  r.Value)
    for j := 0; j < r.Len()-1; j++ {
        r = r.Next()
        fmt.Printf(" %d", r.Value)
    }
    fmt.Println()
}

func max_int_map(m map[int]int) int{
    max := -1
    for _, v := range m {
        if v > max {
            max = v
        }
    }
    return max
}

func solve(players, last int) int {
    circle := ring.New(1)
    values := make(map[int]int)
    circle.Value = 0
    for i:= 1; i < last + 1; i++ {
        if i % 23 == 0 {
            circle = circle.Move(7)
            v := circle.Value.(int)
            values[i % players] += i + v
            /* Unlink removes next, so return to prev */
            circle = circle.Prev() 
            circle.Unlink(1)
        } else {
            circle = circle.Move(-1)
            add := ring.New(1)
            add.Value =  i
            circle = add.Link(circle)
        }
    }
    return max_int_map(values)
}

func main() {
    input := bufio.NewScanner(os.Stdin)
    circle := make([]int, 0)
    circle = append(circle, 0)
    for input.Scan() {
        line := strings.Split(input.Text(), " ")
        players, _ := strconv.Atoi(line[0])
        last, _ := strconv.Atoi(line[6])
        fmt.Println(solve(players, last))
        fmt.Println(solve(players, last*100))
    }

}