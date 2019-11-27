package main

import (
    "fmt"
    "strconv"
    "math"
)

var serial int = 1133


func cell_power(serial, x, y int) int {
    rackid := x + 10
    initpower := (rackid * y + serial) * rackid
    strp := strconv.Itoa(initpower)
    digit := 0
    if len(strp) > 2 {
        digit, _ = strconv.Atoi(string(strp[len(strp)-3]))
    }
    return digit - 5
}


// A simple function to find sum of all sub-squares of size k x k 
// in a given square matrix of size n x n 
func maxsum(grid [300][300]int, k, n int) (int, int, int) { 
  
   max := -math.MaxInt32
   row := 0
   col := 0
   // row number of first cell in current sub-square of size k x k 
   for i := 0; i < n-k+1; i++ { 
        // column of first cell in current sub-square of size k x k 
        for j := 0; j< n-k+1; j++ { 
            // Calculate and print sum of current sub-square 
            sum := 0;
            for p := i; p < k + i; p++ {
                // Calculate and print sum of current sub-square
                for q := j; q < k + j; q++ {
                    sum += grid[p][q];
                }
            }
            if sum > max {
                max = sum
                row = i
                col = j
            }
        } 
   } 
   return max, row+1, col+1
} 

func main () {
    var grid [300][300]int
    for i:= 0; i < 300; i++ {
        for j := 0; j < 300; j++ {
            grid[i][j] = cell_power(serial, i+1, j+1)
        }  
    }
    max, row, col := maxsum(grid, 3, 300)
    fmt.Printf("%d,%d\n", row, col)
    /* Brute force...because... */
    max = -math.MaxInt32
    idx := 1
    for i:= 1; i <=300; i++ {
        v, r, c :=  maxsum(grid, i, 300)
        if v < 0 {
            break
        }
        if v > max {
            max = v
            row = r
            col = c
            idx = i
        }
    }
    fmt.Printf("%d,%d,%d\n", row, col, idx)
}
