package main

import (
    "bufio"
    "fmt"
    "os"
    "math"
    "strconv"
    "strings"
    "sort"
)

func max(arr []float64 ) float64{
    m := -math.MaxFloat64
    for _, v := range arr {
        if v > m{
            m = v
        }
    }
    return m
}

func dist(x1, y1, x2, y2 float64) float64 {
    return math.Abs(x1 - x2) + math.Abs(y1 - y2)   
}

/* Returns the id of the coordinate with minimum distance to a point 
   If there there is more than one minimum, the returned id is -1, signalizing a tie.
*/  
func min_dist(x, y int, xs, ys []float64) (int, float64){
    min := math.MaxFloat64
    idx := 0
    eq := false
    for id := range xs {
        dist := dist(float64(x), float64(y), xs[id], ys[id])
        if dist < min {
            min = dist
            idx =  id
            eq = false
          /* If there is an equidistant point, ignore it */ 
        } else if dist == min {
            idx = -1
        }
    }
    if eq {
        return idx, float64(-1)
    }
    return idx, min
}

func sum_dist(x, y int, xs, ys []float64) float64 {
    var sum float64 
    for id := range xs {
        sum += dist(float64(x), float64(y), xs[id], ys[id])
    }
    return sum
}

func solve(xs, ys []float64 )  {

    // max := -math.MaxFloat64
    xmax := int(max(xs))
    ymax := int(max(ys))
    units := make([]int, len(xs))
    within := 0
    for i:= 0; i <= xmax ; i++ {
        for j:= 0; j <= ymax; j++ {
            /* Task 1: Maximum safe units near a coordinate */
            idx, min := min_dist(i, j, xs, ys)
            if idx > -1 {
                /* Eliminate the borders */
                if i == 0 || i == xmax || j == 0 || j == ymax {
                    units[idx] = -1
                } else if min != math.MaxFloat64 && units[idx] > -1{
                    units[idx] += 1
                }  
            }

            /* Task 2: Sum of distances below 1000 */
            if sum_dist(i, j, xs, ys) < 10000 {
                within += 1
            }
        }
    }

    sort.Sort(sort.Reverse(sort.IntSlice(units)))
    fmt.Println(units[0])
    fmt.Println(within)
}

func main() {
    input := bufio.NewScanner(os.Stdin)
    xs := make([]float64, 0)
    ys := make([]float64, 0)
    for input.Scan() {
        xy := strings.Split(input.Text(), ",")
        x, _ := strconv.ParseFloat(string(xy[0]), 64)
        y, _:= strconv.ParseFloat(string(xy[1][1:]), 64) 
        xs = append(xs, x)
        ys = append(ys, y)
    }
    solve(xs, ys)
}