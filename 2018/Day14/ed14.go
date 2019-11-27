package main

import (
    "fmt"
    "strconv"
    "strings"
)

var input int = 236021

func part1(input int)  {
    scores := make([]int, 2)
    var elf1, elf2 int
    elf1 = 0
    elf2 = 1
    scores[elf1] = 3
    scores[elf2] = 7
    for len(scores) < input + 10 {
        total := scores[elf1] + scores[elf2]
        if total >= 10 {
            div := total / 10
            mod := total % 10
            scores = append(scores, div)
            scores = append(scores, mod)
        } else {
            scores = append(scores, total)
        }
        elf1 = (scores[elf1] + elf1 + 1) % len(scores)
        elf2 = (scores[elf2] + elf2 + 1) % len(scores)
    }
    for _, v := range scores[input:input+10] {
        fmt.Print(v)
    }
    fmt.Println()
}

func array_to_string(arr []int) string {
    str := ""
    for _,v := range arr {
        str += strconv.Itoa(v)
    }
    return str
}

func part2(input int) {
    scores := make([]int, 2)
    var elf1, elf2 int
    elf1 = 0
    elf2 = 1
    scores[elf1] = 3
    scores[elf2] = 7
    strinput := strconv.Itoa(input)
    seq := "37"
    seq2 := "3"
    for strings.Compare(seq, strinput) != 0 && 
        strings.Compare(seq2, strinput) != 0 {

        total := scores[elf1] + scores[elf2]
        if total >= 10 {
            div := total / 10
            mod := total % 10
            scores = append(scores, div)
            scores = append(scores, mod)
        } else {
            scores = append(scores, total)
        }

        elf1 = (scores[elf1] + elf1 + 1) % len(scores)
        elf2 = (scores[elf2] + elf2 + 1) % len(scores)
        if len(scores) > len(strinput) {
            seq = array_to_string(scores[len(scores)-len(strinput):])
            seq2 = array_to_string(scores[len(scores)-len(strinput)-1:len(scores)-1])
        }

    }

    if strings.Compare(seq, strinput) == 0 {
        fmt.Println( len(scores) - len(strinput) )
    } else {
        fmt.Println(len(scores) - len(strinput) - 1) 
    }
}

func main() {
    part1(input)
    part2(input)
}
