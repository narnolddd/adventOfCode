package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "sort"
    "math"
)

func alphabet() map[rune]int {
    m := make(map[rune]int)
    for i := 1; i <= 26; i++  {
        c := 'A' + byte(i-1)
        m[rune(c)] = 60 + i 
    }
    return m
}

type nodes map[int][]int

func find_next(node string, nodes map[string][]string, visited map[string]bool) []string {
    next := []string{}
    iter := func (n string) bool { _, ok := visited[n]; return !ok }
    for _, n := range nodes[node] {
        if iter(n) {
            next = append(next, n)
        }
    }
    return next
}

func search_array(arr []string, k string) bool {
    for _, v := range arr {
        if v == k {
            return true
        }
    }
    return false
}

func remove_deps(node string, graph, deps map[string][]string) {
    nodes := graph[node]
    for _,v := range nodes {
        dep_nodes,_ := deps[v]
        for j, n := range dep_nodes {
            if n == node {
                deps[v] = append(deps[v][:j], deps[v][j+1:]...)
            }
        }
    }
}

func part1(last string, nodes, deps map[string][]string) {
    next := make([]string, 0)
    visited := map[string]bool{}
    vord := make([]string, len(nodes))
    pos := 0

    /* Find initial nodes */
    for k, _ := range nodes {
        _, ok := deps[k]
        if !ok {
            next = append(next, k)
        }
    }

    sort.Strings(next)
    
    for  len(visited) != len(nodes)  {
        node := next[pos]
        // fmt.Println(vord)
        for len(deps[node]) != 0 {
            pos += 1
            node = next[pos]
        }

        visited[node] = true
        vord = append(vord, node)
        remove_deps(node, nodes, deps)
        for _, n := range find_next(node, nodes, visited) {
            if n != last && search_array(next, n) == false {
                next = append(next, n)
            }
        }
        next = append(next[:pos], next[pos+1:]...)
        sort.Strings(next)
        pos = 0

    }
    for _,v := range vord {
        fmt.Print(v)
    }
    fmt.Println(last)
}

/* Find a free worker */
func get_free_worker(workers map[int]int) int {
    for i := 0; i < 5; i++ {
        if workers[i] == 0{
            return i
        }
    }
    return -1
}

/* Find a free worker */
func all_free(workers map[int]int) bool {
    for i := 0; i < 5; i++ {
        if workers[i] != 0{
            return false
        }
    }
    return true
}

/* Find a free worker */
func find_min_working(workers map[int]int) int {
    min := math.MaxInt32
    for i := 0; i < 5; i++ {
        if workers[i] > 0 && workers[i] < min{
            min = workers[i]
        }
    }
    return min
}

func array_delete(arr []string, s string ) []string{
    for idx, v := range arr {
        if v == s{
            arr = append(arr[:idx], arr[idx+1:]...)
            return arr
        }
    }
    return arr
}

func part2(last string, nodes, deps map[string][]string) {
    next := make([]string, 0)
    visited := map[string]bool{}
    vord := make([]string, len(nodes))
    time := 0
    times := alphabet()

    /* Find initial nodes */
    for k, _ := range nodes {
        _, ok := deps[k]
        if !ok {
            next = append(next, k)
        }
    }

    sort.Strings(next)
    wchar := make([]string, 5)
    workers := make(map[int]int)
    for i:=0; i < 5; i++{
        workers[i] = 0
        wchar[i] = "."
    }
    added := 0
    for {
        /* Are there nodes available? */
        enabled := make([]string, 0)
        for _, n := range next  {
            if len(deps[n]) == 0 {
                enabled  = append(enabled, n)
            }
        }
        sort.Strings(enabled)
        /* Worker is available and node is enabled*/
        for _, node := range enabled {
            worker := get_free_worker(workers)
            if worker > -1 {
                workers[worker] += times[rune(node[0])] 
                visited[node] = true
                wchar[worker] = node
                for _, n := range find_next(node, nodes, visited) {
                    if n != last && search_array(next, n) == false {
                        next = append(next, n)
                    }
                }
                next = array_delete(next, node) 
            } else {
                /* There are no more workers available */
                break
            }
        }
        min := find_min_working(workers)
        time += min
        /* Reduce */
        for k, _ := range workers {
            if workers[k] > 0 {
                workers[k]-=min
            }
            if workers[k] == 0 && wchar[k] != "." { 
                vord = append(vord, wchar[k])
                remove_deps(wchar[k], nodes, deps)
                wchar[k] = "."
                added += 1
            }
        }
        /* Added all nodes and no more work to do */
        if added == len(nodes) && all_free(workers) == true{
            break
        }
    }
    for _,v := range vord {
        fmt.Print(v)
    }
    fmt.Println(last)
    fmt.Println(time + times[rune(last[0])])
}


func main() {
    input := bufio.NewScanner(os.Stdin)
    graph := make(map[string][]string)
    dep_graph := make(map[string][]string)
    var last *string
    last = nil
    for input.Scan() {
        line := strings.Split(input.Text(), " ")
        a, b := line[1], line[7]
        _, found := graph[a]
        if found == false {
            graph[a] = make([]string, 0)
        }
        graph[a] = append(graph[a], b)
        if _, found := graph[b]; !found{
            if last == nil {
                last = new(string)
            }
            *last = b
        }
        if _, found := dep_graph[b]; found == false {
            dep_graph[b] = make([]string, 0)
        }
        dep_graph[b] = append(dep_graph[b], a)

    }
    /* Too lazy to make a copy of the map and use in part1 */
    // part1(*last, graph, dep_graph)
    part2(*last, graph, dep_graph)
}