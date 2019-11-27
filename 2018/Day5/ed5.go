package main

import (
    "bufio"
    "fmt"
    "os"
    "unicode"
    "strings"
)

type stack []rune

func (s stack) Push(v rune) stack {
    return append(s, v)
}

func (s stack) Pop() (stack, rune) {
    // FIXME: What do we do if the stack is empty, though?

    l := len(s)
    return  s[:l-1], s[l-1]
}

func (s stack) Peek() (rune) {
    // FIXME: What do we do if the stack is empty, though?

    l := len(s)
    return  s[l-1]
}

func (s stack) Empty() bool {
    return len(s) == 0
}

func react(chain string) int {
    st :=  make(stack, 0)
    for _, v := range chain {
        if st.Empty(){
            st = st.Push(rune(v))
        } else {
            ch := st.Peek()
            if unicode.IsLower(ch){
                if unicode.IsUpper(rune(v)) && unicode.ToLower(v) == ch{
                    st, _ = st.Pop()
                } else {
                    st = st.Push(rune(v))
                } 
            } else {
                if unicode.IsLower(rune(v)) && unicode.ToUpper(v) == ch{
                    st, _ = st.Pop()
                } else {
                    st = st.Push(rune(v))
                } 
            }
        }
    }
    return len(st)
}

func alphabet() string {
    p := make([]byte, 26)
    for i := range p {
        p[i] = 'a' + byte(i)
    }
    return string(p)
}

func main() {
    //Creating a Scanner that will read the input from the console
    input := bufio.NewScanner(os.Stdin) 
    /* Does go has any kind of dynamic arrays? */
    var chain string
    for input.Scan() {
        chain = input.Text()
    }

    /* Task 1 */
    fmt.Println(react(chain))

    /* Task 2 */
    min := 100000
    for _, c := range alphabet(){
        mod_chain := chain
        mod_chain = strings.Replace(mod_chain, string(c), "", -1)
        mod_chain = strings.Replace(mod_chain, string(unicode.ToUpper(rune(c))), "", -1)
        tmp_min := react(mod_chain)
        if tmp_min < min {
            min = tmp_min
        }
    }
    fmt.Println(min)
}