package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

var re = regexp.MustCompile(`^(.{4}) (\d+) (\d+) (\d+)$`)

type instruction struct {
	opcode  string
	A, B, C int
}

func addr(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] + registers[B]
}

func addi(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] + B
}

func mulr(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] * registers[B]
}

func muli(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] * B
}

func banr(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] & registers[B]
}

func bani(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] & B
}

func borr(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] | registers[B]
}

func bori(A, B, C int, registers *[6]int) {
	registers[C] = registers[A] | B
}

func setr(A, _, C int, registers *[6]int) {
	registers[C] = registers[A]
}

func seti(A, _, C int, registers *[6]int) {
	registers[C] = A
}

func gtir(A, B, C int, registers *[6]int) {
	if A > registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func gtri(A, B, C int, registers *[6]int) {
	if registers[A] > B {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func gtrr(A, B, C int, registers *[6]int) {
	if registers[A] > registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func eqir(A, B, C int, registers *[6]int) {
	if A == registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func eqri(A, B, C int, registers *[6]int) {
	if registers[A] == B {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func eqrr(A, B, C int, registers *[6]int) {
	if registers[A] == registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

var funcs = map[string]func(int, int, int, *[6]int){
	"addr": addr,
	"addi": addi,
	"mulr": mulr,
	"muli": muli,
	"banr": banr,
	"bani": bani,
	"borr": borr,
	"bori": bori,
	"setr": setr,
	"seti": seti,
	"gtir": gtir,
	"gtri": gtri,
	"gtrr": gtrr,
	"eqir": eqir,
	"eqri": eqri,
	"eqrr": eqrr,
}

func parseProgram() (int, []instruction) {
	f, _ := os.Open("input.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Scan()
	ipRegister, _ := strconv.Atoi(scanner.Text()[4:])

	program := make([]instruction, 0)
	for scanner.Scan() {
		line := scanner.Text()
		match := re.FindStringSubmatch(line)
		if match == nil {
			panic("Parsing error")
		}
		opcode := match[1]
		A, _ := strconv.Atoi(match[2])
		B, _ := strconv.Atoi(match[3])
		C, _ := strconv.Atoi(match[4])
		program = append(program, instruction{opcode, A, B, C})
	}

	return ipRegister, program
}

func runProgram(registers [6]int, ipRegister int, program []instruction, debug bool) {
	seenRegisterValues := make(map[int]struct{})
	lastStopValue := -1
	lastIterationChange := -1
	ip := 0
	for t := 0; t-lastIterationChange < 1000; t++ {
		instr := program[ip]
		registers[ipRegister] = ip
		if debug {
			fmt.Printf("ip=%d %v %s %d %d %d ", ip, registers, instr.opcode, instr.A, instr.B, instr.C)
		}
		funcs[instr.opcode](instr.A, instr.B, instr.C, &registers)
		ip = registers[ipRegister]
		if debug {
			fmt.Printf("%v\n", registers)
		}
		//Fast track loop in program code
		if ip == 24 {
			registers[1] = registers[5] / 256
		}

		if ip == 28 {
			if len(seenRegisterValues) == 0 {
				fmt.Println("Earliest stop input", registers[4])
			}
			if _, ok := seenRegisterValues[registers[4]]; !ok {
				lastIterationChange = t
				lastStopValue = registers[4]

			}
			seenRegisterValues[registers[4]] = struct{}{}
		}
		ip++
	}
	fmt.Println("Latest stop input", lastStopValue)
}

func main() {
	ipRegister, program := parseProgram()

	registers := [6]int{-1, 0, 0, 0, 0, 0}
	runProgram(registers, ipRegister, program, false)
}
