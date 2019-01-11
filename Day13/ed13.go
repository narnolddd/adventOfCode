package main

import (
    "bufio"
    "os"
    "fmt"
    "sort"
    "math"
)

const (
 LEFT = 0
 RIGHT = 1
 UP = 2
 DOWN = 3
)

const (INTERL = 0
    INTERS = 1
    INTERR = 2
)
type Cart struct {
    x int
    y int
    direction int
    runetype rune
    inter_direction int
}

type Carts []*Cart

func (carts Carts) Len() int {
    return len(carts)
}
func (carts Carts) Less(i, j int) bool {
    if carts[i].x == carts[j].x {
        return carts[i].y < carts[j].y
    }
    return carts[i].x < carts[j].x
}
func (carts Carts) Swap(i, j int) {
    carts[i], carts[j] = carts[j], carts[i]
}

func print_grid(grid [][]rune){
    for i:=0; i < len(grid); i++ {
        for j:=0; j < len(grid[i]); j++ {
            fmt.Print(string(grid[i][j]))
        }
        fmt.Println()
    }
}

func collided(b rune) bool {
    if b == '<' || b == '>' ||
       b == 'v' || b == '^' {
        return true
    }
    return false
}

func refill_cart(grid [][]rune, cart *Cart) {
    var icon rune
    switch cart.direction {
        case LEFT:
            icon = '<'
        case RIGHT:
            icon = '>'
        case UP:
            icon = '^'
        case DOWN:
            icon = 'v'
    }
    grid[cart.x][cart.y] = icon
}

func print_carts(carts Carts) {
    for _, v := range carts {
        fmt.Println(v)
    }
}

func remove_collided(grid [][]rune, carts Carts, cart *Cart, pos int) (int,int, Carts){
    var c2 *Cart
    var c2pos int
    for i,v := range carts {
        if i == pos {
            continue
        }
        if cart.x == v.x && cart.y == v.y {
            c2pos = i
            c2 = v
            break
        }
    }
    grid[c2.x][c2.y] = c2.runetype
    fmt.Println("Crash at ", c2.y, c2.x)
    carts = append(carts[:c2pos], carts[c2pos+1:]...)
    if pos > c2pos {
        pos -= 1
    }
    carts = append(carts[:pos], carts[pos+1:]...)

    return pos, c2pos, carts
}

/* Move and remove in case of collision*/
func move_cart(grid [][]rune, carts Carts, cart *Cart, pos int) (int,int, Carts) {
    /* Update map */
    grid[cart.x][cart.y] = cart.runetype
    
    /* Update position */
    switch cart.direction {
        case LEFT:
            cart.y -= 1
        case RIGHT:
            cart.y += 1
        case UP:
            cart.x -= 1
        case DOWN:
            cart.x += 1
    }
    
    next_rune := grid[cart.x][cart.y]
    /* check colision */

    if collided(next_rune){
        return remove_collided(grid, carts, cart, pos)        
    }
    /* Update map */
    cart.runetype = next_rune

    /* Update direction */
    if next_rune == '/'{
        switch cart.direction {
            case DOWN:
                cart.direction = LEFT
            case UP:
                cart.direction = RIGHT
            case LEFT:
                cart.direction = DOWN
            case RIGHT:
                cart.direction = UP
        }
    } else if next_rune == '\\' {
        switch cart.direction {
            case DOWN:
                cart.direction = RIGHT
            case UP:
                cart.direction = LEFT
            case LEFT:
                cart.direction = UP
            case RIGHT:
                cart.direction = DOWN
        }
    } else if next_rune == '+' {
        /* Current is left */
        if cart.inter_direction == INTERL {
            switch cart.direction {
                case LEFT: 
                    cart.direction = DOWN
                case RIGHT: 
                    cart.direction = UP
                case DOWN:
                    cart.direction = RIGHT
                case UP:
                    cart.direction = LEFT
            }
            cart.inter_direction = INTERS
         /* Current is Right */
        } else if cart.inter_direction == INTERR {
            switch cart.direction {
                case LEFT: 
                    cart.direction = UP
                case RIGHT: 
                    cart.direction = DOWN
                case DOWN:
                    cart.direction = LEFT
                case UP:
                    cart.direction = RIGHT
            }
            cart.inter_direction = INTERL
        /* Current is straight */
        } else if cart.inter_direction == INTERS {
            cart.inter_direction = INTERR
        }
    }
    /* Update map */
    refill_cart(grid, cart)
    return -1, -1, carts
}

func tick_order(carts map[int]*Cart) Carts {
    var c Carts 
    for _,v := range carts {
        c = append(c, v)
    }
    sort.Sort(c)
    return c
}

func main () {
    input := bufio.NewScanner(os.Stdin)
    grid := make([][]rune, 0)
    var carts Carts
    i := 0
    cnum := 0
    for input.Scan() {
        grid = append(grid, make([]rune, 0))
        line := input.Text()
        for idx, c := range line {
            grid[i] = append(grid[i], rune(c))
            direction := -1
            var runetype rune
            switch string(c) {
                case ">":
                    direction = RIGHT
                    runetype = '-'
                case "<":
                    direction = LEFT
                    runetype = '-'
                case "^":
                    direction = UP
                    runetype = '|'
                case "v":
                    direction = DOWN
                    runetype = '|'
            }
            /* Cart in the position */
            if direction > -1 {
                carts = append(carts, &Cart{x:i, y:idx, direction:direction, runetype:runetype}) 
                cnum++
            }
            
        }
        i += 1
    }
    sort.Sort(carts)
    var a, b int
    for {
        until := len(carts)
        for i := 0; i < until; i++ {
            a, b, carts = move_cart(grid, carts, carts[i], i)
            if a > -1 {
                    /* Removed before */
                if b < i {
                    i -= 2
                } else {
                    /* Removed after */
                    i -= 1
                }
                until -= 2
            }
        }
        if len(carts) == 1 {
            break
        }
        sort.Sort(carts)
    }
    cart := *carts[0]
    fmt.Println(cart.y, cart.x)
}
