package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
)

type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
    return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
    return len(s)
}

func SortString(s string) string {
    r := []rune(s)
    sort.Sort(sortRunes(r))
    return string(r)
}

/* Check if a strings repeats a character 2 or 3 times */
func check_letters(b string) (x, y bool){
    m := make(map[rune]int)
    x = false 
    y = false
    for _, c := range b{
        if _, found := m[c]; found {
            m[c] += 1
        } else {
            m[c] = 1
        }
    }

    for _, v := range m {
        if v == 2 {
            x = true
        }
        if v == 3 {
            y = true
        }
    }

    return x, y
}

func MinIntSlice(v []int) int {
  sort.Ints(v)
  return v[0]
}

/* Calculates the difference between the two string using 
    https://en.wikipedia.org/wiki/Levenshtein_distance
*/
func LevenshteinDistance(s, t string, n, m int) int{

    v0 := make([]int, n+1)
    v1 := make([]int, n+1)

    for i:=0; i <= n; i++ {
        v0[i] = i
    }

    for i:=0; i < m; i++ {
        v1[0] = i + 1

        for j := 0; j < n; j++ {
            deletionCost := v0[j + 1] + 1
            insertionCost := v1[j] + 1
            substitutionCost := 0
            if s[i] == t[j]{
                substitutionCost = v0[j]
            } else {
                substitutionCost = v0[j] + 1
            }
            costs := []int{deletionCost, insertionCost, substitutionCost}
            v1[j + 1] = MinIntSlice(costs)
        }

        for j:= 0; j <= n; j++ {
            v0[j], v1[j] = v1[j], v0[j]
        }
    }
    return v0[n]
}

/* Remove the common character from the strings */
func Difference(a, b string, n int) string {
    r := make([]byte, n)
    for i := 0; i < n; i++ {
        if a[i] == b[i] {
            r[i] = a[i]
        }
    }
    return string(r[:n])
}

func main() {
    //Creating a Scanner that will read the input from the console
    input := bufio.NewScanner(os.Stdin) 
    two_letters := 0
    three_letters := 0
    var arr [250]string
    i := 0
    for input.Scan() {
        b := input.Text()
        x, y := check_letters(b)
        if x {
            two_letters += 1
        }
        if y {
            three_letters += 1
        }
        // fmt.Println(SortString(b))
        arr[i] = b
        i += 1
    }
    var a,b string
    for i := 0; i < 250; i++ {
        done := false
        for j:= 0; j < 250; j++{
            if i == j{
                continue
            }
            dist := LevenshteinDistance(arr[i], arr[j], 26, 26)
            if dist == 1{
                a = arr[i]
                b = arr[j]
                done = true
                break
            }
        }
        if done {
            break
        }
    }

    fmt.Println(two_letters * three_letters)
    fmt.Println(Difference(a, b, 26))
}