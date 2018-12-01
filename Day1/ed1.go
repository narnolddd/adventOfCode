// After feeling like you've been falling for a few minutes, you look at the device's tiny screen. "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock." Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

// For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

//     Current frequency  0, change of +1; resulting frequency  1.
//     Current frequency  1, change of -2; resulting frequency -1.
//     Current frequency -1, change of +3; resulting frequency  2.
//     Current frequency  2, change of +1; resulting frequency  3.

// In this example, the resulting frequency is 3.

// Here are other example situations:

//     +1, +1, +1 results in  3
//     +1, +1, -2 results in  0
//     -1, -2, -3 results in -6

// Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

/* Just sum the whole thing. */
func task1(arr [1000]int) {
    total := 0
    for _, v := range arr {
        total += v
    }
    fmt.Println(total)
}

/* The solution uses a map to store and quick search 
   for the value already seem */ 
func task2(arr [1000]int, j int){
    m := make(map[int]int)
    m[0] = 1
    v := 0
    /* Loops forever until a value is found twice. */
    for {
        found := false
        for z := 0; z < j; z++ {
            v += arr[z]
            if _, ok := m[v]; ok {
                found = true
                break
            }
            m[v] = 1
        }
        if found {
            fmt.Println(v)
            break
        }
    }
}

func main() {
    //Creating a Scanner that will read the input from the console
    input := bufio.NewScanner(os.Stdin) 
    j := 0
    var arr [1000]int
    /* Does go has any kind of dynamic arrays? */
    for input.Scan() {
        if i, err := strconv.Atoi(input.Text()); err == nil{
            arr[j] = i
        }
        j++
    }

    task1(arr)
    task2(arr, j)
}
