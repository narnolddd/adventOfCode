package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "time"
    "strings"
    "strconv"
)

type kv struct {
    Key   string
    Rec *guard_record
}

type shift struct {
    date time.Time
    action string
}

type sleep_schedule struct{
    start time.Time
    end time.Time
} 

type guard_record struct {
    minutes float64
    schedule []sleep_schedule
}

type timeSlice []shift

func (p timeSlice) Len() int {
    return len(p)
}

func (p timeSlice) Less(i, j int) bool {
    return p[i].date.Before(p[j].date)
}

func (p timeSlice) Swap(i, j int) {
    p[i], p[j] = p[j], p[i]
}


func main() {
    //Creating a Scanner that will read the input from the console
    input := bufio.NewScanner(os.Stdin) 
    sorted_shifts := make(timeSlice, 0)
    sleep := make(map[string]*guard_record)
    /* Parse */
    for input.Scan() {
        t := string(input.Text()[1:17])
        act := string(input.Text()[18:])
        dt,_ := time.Parse("2006-01-02 15:04", t)
        sh := shift{date:dt, action:act}
        sorted_shifts = append(sorted_shifts, sh)
    }
    /* Sort by chronological order */
    sort.Sort(sorted_shifts)
    /* Calculate minutes and store sleep and wake times */
    for i:= 0; i < len(sorted_shifts); i++ {
        s := sorted_shifts[i]
        if strings.Contains(s.action, "Guard") {
            parts := strings.Split(s.action, " ")
            guard := string(parts[2])
            if _, found := sleep[guard]; found == false {
                sleep[guard] = &guard_record{minutes: 0, 
                            schedule:make([]sleep_schedule, 0)}
            }
            // j := i
            for strings.Contains(sorted_shifts[i+1].action, "asleep"){
                dt := sorted_shifts[i+2].date.Sub(sorted_shifts[i+1].date)
                sleep[guard].minutes += dt.Minutes()
                sch := sleep_schedule{end:sorted_shifts[i+2].date, 
                                    start:sorted_shifts[i+1].date }
                sleep[guard].schedule = append(sleep[guard].schedule, sch)
                i += 2
                if (i == len(sorted_shifts)-1){
                    break
                }
            }
        }        
    }

    var ss []kv
    for k, v := range sleep {
        ss = append(ss, kv{k, v})
    }

    sort.Slice(ss, func(i, j int) bool {
        return ss[i].Rec.minutes > ss[j].Rec.minutes
    })

    guard := ss[0]
    var min []int
    min = make([]int, 60)
    max := -1
    id := -1
    var rec kv 
    /* Part 1 */
    for _,sch  := range guard.Rec.schedule {
        start := sch.start.Format("2006-01-02 15:04")
        end := sch.end.Format("2006-01-02 15:04")
        ms,_ := strconv.Atoi(start[14:16])
        me,_ := strconv.Atoi(end[14:16])
        for i:= ms; i < me; i++{
            min[i] += 1
        }
    }
    for idx, v:= range min{
        if v > max {
                max = v
                id = idx
                rec = guard
        }
    }
    g, _ := strconv.Atoi(string(rec.Key[1:]))
    fmt.Println(rec.Key[1:], id, max, g * id)
    
    /* Part 2 */
    max = -1
    id = -1
    for _, guard := range ss {
        var min []int
        min = make([]int, 60)
        for _,sch  := range guard.Rec.schedule {
            start := sch.start.Format("2006-01-02 15:04")
            end := sch.end.Format("2006-01-02 15:04")
            ms,_ := strconv.Atoi(start[14:16])
            me,_ := strconv.Atoi(end[14:16])
            for i:= ms; i < me; i++{
                min[i] += 1
            }
        }
        for idx, v:= range min{
            if v > max {
                max = v
                id = idx
                rec = guard
            }
        }
    }
    g, _ = strconv.Atoi(string(rec.Key[1:]))
    fmt.Println(rec.Key[1:], id, max, g * id)
}