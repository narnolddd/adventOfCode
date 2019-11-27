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
	//opcode  func(int, int, int, *[6]int)
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
		//opcode := funcs[match[1]]
		opcode := match[1]
		A, _ := strconv.Atoi(match[2])
		B, _ := strconv.Atoi(match[3])
		C, _ := strconv.Atoi(match[4])
		program = append(program, instruction{opcode, A, B, C})
	}

	return ipRegister, program
}

func runProgramUntilHalt(registers [6]int, ipRegister int, program []instruction, debug bool) {
	ip := 0
	for {
		if ip >= len(program) {
			fmt.Println("Trying to load instruction outside of program... Halting...")
			fmt.Println(registers)
			break
		}
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
		ip++
	}
}

func runProgramForTime(registers *[6]int, ipRegister int, program []instruction, debug bool, loops int) {
	ip := 0
	for i := 0; i < loops; i++ {
		instr := program[ip]
		registers[ipRegister] = ip
		if debug {
			fmt.Printf("ip=%d %v %s %d %d %d ", ip, registers, instr.opcode, instr.A, instr.B, instr.C)
		}
		funcs[instr.opcode](instr.A, instr.B, instr.C, registers)
		ip = registers[ipRegister]
		if debug {
			fmt.Printf("%v\n", registers)
		}
		ip++
	}
}

func main() {
	ipRegister, program := parseProgram()

	// Part 1
	registers := [6]int{0, 0, 0, 0, 0, 0}
	runProgramUntilHalt(registers, ipRegister, program, false)

	// Part 2
	registers = [6]int{1, 0, 0, 0, 0, 0}
	runProgramForTime(&registers, ipRegister, program, false, 100)
	targetNumber := registers[5]

	sum := 0
	for i := 1; i <= targetNumber; i++ {
		if targetNumber%i == 0 {
			sum += i
		}
	}
	fmt.Println(sum)
}
