package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    //Creating a Scanner that will read the input from the console
    input := bufio.NewScanner(os.Stdin) 
    var grid[1000][1000]map[string]string
    overlap := 0
    non_overlaps := make(map[string]bool)
    for input.Scan() {
       parts := strings.Split(input.Text(), " ")
       positions := strings.Split(strings.Trim(parts[2], ":"), ",")
       sizes := strings.Split(parts[3], "x")
       posx,_ := strconv.Atoi(positions[0])
       posy,_ := strconv.Atoi(positions[1])
       lenx,_ := strconv.Atoi(sizes[0])
       leny,_ := strconv.Atoi(sizes[1])
       non_overlaps[parts[0]] = true
       /* Populate the grid with claims in each position */
       for i:= posx; i < posx+lenx; i++ {
            for j:= posy; j < posy+leny; j++ {
                if len(grid[i][j]) == 0 {
                    grid[i][j] = make(map[string]string)
                }
                grid[i][j][parts[0]] = input.Text()
            } 
       }
    }

    /* loop through the grid finding overlapping positions*/
    for i:= 0; i < 1000; i++ {
        for j:= 0; j < 1000; j++ {
            if len(grid[i][j]) > 1 {
                overlap += 1
                /* If overlaps, remove from non overlapping */
                for k, _ := range grid[i][j] {
                    _, found := non_overlaps[k]
                    if found {
                        delete(non_overlaps, k)
                    }
                }
            } 
        } 
    }
    fmt.Println(overlap)
    fmt.Println(non_overlaps)
}