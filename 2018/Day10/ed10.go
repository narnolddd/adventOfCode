package main

import (
    "bufio"
    "fmt"
    "os"
    "regexp"
    "strconv"
    "math"
)

var re = regexp.MustCompile(`^position=< ?(?P<x>-?\d+),  ?(?P<y>-?\d+)> velocity=< ?(?P<sx>-?\d+),  ?(?P<sy>-?\d+)>`)

func change_grid(posx, posy, speedx, speedy []float64, op bool) ([]float64, []float64){
    if op == true {
        for i, _ := range posx {
            posx[i] += speedx[i]
            posy[i] += speedy[i]
        }
    } else {
        for i, _ := range posx {
            posx[i] -= speedx[i]
            posy[i] -= speedy[i]
        }
    }
    return posx, posy
}

func calc_area(posx, posy []float64) float64{
    top := make([]float64, 2)
    bottom  := make([]float64, 2)
    for i, _ := range posx {
        if posx[i] + posy[i] < top[0] + top[1] {
            top[0] = posx[i]
            top[1] = posy[i] 
        }
        if posx[i] + posy[i] > bottom[0] + bottom[1] {
            bottom[0] = posx[i]
            bottom[1] = posy[i] 
        }
    }
    return (bottom[0]-top[0])*(bottom[1]-top[1])
}

func min_max_float64_arr(arr []float64) (float64, float64){
    min := math.MaxFloat64
    max := -math.MaxFloat64
    for _, v := range arr {
        if v < min {
            min = v
        } else if v > max {
            max = v
        }
    }
    return min, max
}

func make_grid(posx, posy, speedx, speedy []float64) int {
    min := math.MaxFloat64
    n := 0
    for {
        s := calc_area(posx, posy)
        if s < min {
            min = s
        } else if s > min {
            posx, posy = change_grid(posx, posy, speedx, speedy, false)
            n -= 1
            break
        }
        posx, posy = change_grid(posx, posy, speedx, speedy, true)
        n += 1
    }
    
    minx, maxx := min_max_float64_arr(posx)
    miny, maxy := min_max_float64_arr(posy)
    cols := int(maxx - minx) + 1
    rows := int(maxy - miny) + 1
    grid := make([][]string, rows)
    for i:= 0; i < rows; i ++ {
        grid[i] = make([]string, cols)
        for j:=0; j < cols; j++ {
            grid[i][j] = " "
        } 
    }

    for i, _ := range posx {
        x := int(posy[i]-miny)
        y := int(posx[i]-minx)
        grid[x][y] = "#"
    }
    for i:= 0; i < rows; i ++ {
        for j:=0; j < cols; j++ {
            fmt.Print(grid[i][j])
        }
        fmt.Println()
    } 
    return n
}

func main() {
    input := bufio.NewScanner(os.Stdin)
    posx := make([]float64, 0)
    posy := make([]float64, 0)
    speedy := make([]float64, 0)
    speedx := make([]float64, 0)
    for input.Scan() {
        line := input.Text() 
        if match := re.FindStringSubmatch(line); match != nil {
            px,_ := strconv.ParseFloat(match[1], 64)
            py,_ := strconv.ParseFloat(match[2], 64) 
            sx,_ := strconv.ParseFloat(match[3], 64)
            sy,_ := strconv.ParseFloat(match[4], 64)
            posx = append(posx, px)
            posy = append(posy, py)
            speedx = append(speedx, sx)
            speedy = append(speedy, sy)
        }
    }
    
    fmt.Println(make_grid(posx, posy, speedx, speedy))
    
}