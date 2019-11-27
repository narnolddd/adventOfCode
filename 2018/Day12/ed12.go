package main

import (
    "bufio"
    "os"
    "fmt"
    "strings"
)

func print_pots(n int, pots []string) {
    fmt.Print(n, " ")
    for _, v := range pots {
        fmt.Print(v)
    }
    fmt.Println()
}

func make_chain(ins [5]string) string {
    ins_chain := ""
    for _, v :=  range ins {
        ins_chain += v
    }
    return ins_chain
}

func match_modify(ins_chain string, insts map[string]string,
                  pots []string, pos int) bool {
    v, found := insts[ins_chain]
    if found {
        pots[pos] = v
        if strings.Compare(v, "#") == 0 {
            return true
        }
    } else {
        pots[pos] = "."
    }
    return false
}

func sum(pots []string, start int) int{
    sum := 0
    for i, v := range pots{
        if strings.Compare(v, "#") == 0 {
            sum += i - start    
        }
    }
    return sum
}

func run (insts map[string]string, pots[]string, gen int) int {
    start := 0
    prev := 0
    prev_sum := 0
    s := 0
    diff := 0
    conv := 0
    for i:= 0; i < gen; i++ {
        cur := make([]string, len(pots))
        copy(cur, pots)
        pos := 0
        for j := 0; j < len(cur); j++ {
            /* Corner cases */
            var ins [5]string
            var ins_chain string
            ins[2] = cur[j]
            if j == 0 {
                ins[0] = "."
                ins[1] = "."
                ins[3] = cur[j+1]
                ins[4] = cur[j+2]
                ins_chain = make_chain(ins)
                f := match_modify(ins_chain, insts, pots, j+pos)
                if f {
                    pots = append([]string{"."}, pots...)
                    pots = append([]string{"."}, pots...)
                    pos += 2
                }
            } else if j == 1 {
                ins[0] = "."
                ins[1] = cur[j-1]
                ins[3] = cur[j+1]
                ins[4] = cur[j+2]
                ins_chain = make_chain(ins)
                f := match_modify(ins_chain, insts, pots, j+pos)
                if f {
                    pots = append([]string{"."}, pots...)
                    pots = append([]string{"."}, pots...)
                    pos += 1
                }
            } else if j == len(cur) - 1 {
                ins[0] = cur[j-2] 
                ins[1] = cur[j-1]
                ins[4] = "."
                ins[3] = "."
                ins_chain = make_chain(ins)
                f := match_modify(ins_chain, insts, pots, j+pos)
                if f {
                    pots = append(pots, ".")
                }
            } else if j == len(cur) - 2 {
                ins[0] = cur[j-2]
                ins[1] = cur[j-1]
                ins[3] = cur[j+1]
                ins[4] = "."
                ins_chain = make_chain(ins)
                f := match_modify(ins_chain, insts, pots, j+pos)
                if f {
                    pots = append(pots, ".")
                }
            } else {
               ins[0] = cur[j-2] 
               ins[1] = cur[j-1]
               ins[3] = cur[j+1]
               ins[4] = cur[j+2] 
               ins_chain = make_chain(ins)
               match_modify(ins_chain, insts, pots, j+pos)
            }
        }
        start += pos
        s = sum(pots, start)
        diff = s - prev_sum
        fmt.Println(conv)
        if diff == prev {
            conv += 1
            if conv > 5 {
                return (gen-(1+i)) * diff + s 
            }
        } else {
            prev_sum = s
            prev = diff
        }
    }
    return s
}

func main () {
    input := bufio.NewScanner(os.Stdin)
    insts := make(map[string]string)
    pots := make([]string, 0)
    for input.Scan() {
        line := strings.Split(input.Text(), " ")
        if strings.Compare(line[0], "initial") == 0 {
            for _,v := range line[2] {
                pots = append(pots, string(v))
            }
        } else if len(line) == 3 {
            insts[line[0]] = line[2]
        }
    }
    pcpy := make([]string, len(pots))
    copy(pcpy, pots)
    fmt.Println(run(insts, pcpy, 20))
    fmt.Println(run(insts, pcpy, 50000000000))
}

