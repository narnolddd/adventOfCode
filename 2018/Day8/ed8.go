package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
)

func solve(info []string) (int, []string, int){

    metadata := 0
    children,_ := strconv.Atoi(info[0])
    meta_num, _ := strconv.Atoi(info[1])
    chvalues := make(map[int]int)
    /* Recurse until all children are done */
    tmp := children
    i := 1
    for tmp != 0 {
        meta, inf, value := solve(info[2:])
        chvalues[i] = value
        info = append([]string{}, append(info[:2], inf...)...)
        metadata += meta
        tmp -= 1
        i += 1
    }
    /* Calculate metadata */
    idxs := make([]int, 0)
    for j := 2; j < 2 + meta_num; j++ {
        meta,_ := strconv.Atoi(info[j])
        if meta != 0 {
            idxs = append(idxs, meta)
        }
        metadata += meta
    }
    
    value := 0
    /* End node */
    if children == 0 {
        value = metadata
    } else {
        /* Add value from from children referenced by metadata indexes  */
        for _, v :=  range idxs {
            chv, ok := chvalues[v]
            if ok {
                value += chv
            }
        }
    }
    return metadata, info[2+meta_num:], value
}

func main() {
    input := bufio.NewScanner(os.Stdin)
    for input.Scan() {
        line := strings.Split(input.Text(), " ")
        meta, inf, value := solve(line)
        fmt.Println(meta, inf, value)
    }
}