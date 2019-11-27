package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var re = regexp.MustCompile(`^Before: \[(\d+), (\d+), (\d+), (\d+)\](\d+) (\d+) (\d+) (\d+)After:  \[(\d+), (\d+), (\d+), (\d+)\]$`)

func addr(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] + registers[B]
}

func addi(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] + B
}

func mulr(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] * registers[B]
}

func muli(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] * B
}

func banr(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] & registers[B]
}

func bani(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] & B
}

func borr(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] | registers[B]
}

func bori(A, B, C int, registers *[4]int) {
	registers[C] = registers[A] | B
}

func setr(A, _, C int, registers *[4]int) {
	registers[C] = registers[A]
}

func seti(A, _, C int, registers *[4]int) {
	registers[C] = A
}

func gtir(A, B, C int, registers *[4]int) {
	if A > registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func gtri(A, B, C int, registers *[4]int) {
	if registers[A] > B {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func gtrr(A, B, C int, registers *[4]int) {
	if registers[A] > registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func eqir(A, B, C int, registers *[4]int) {
	if A == registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func eqri(A, B, C int, registers *[4]int) {
	if registers[A] == B {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

func eqrr(A, B, C int, registers *[4]int) {
	if registers[A] == registers[B] {
		registers[C] = 1
	} else {
		registers[C] = 0
	}
}

var funcs = map[string]func(int, int, int, *[4]int){
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

func CountMatchingOpcodes(registersBefore, registersAfter [4]int, A, B, C int) (int, []string) {
	counter := 0
	opcodes := make([]string, 0)
	for name, f := range funcs {
		registers := registersBefore
		f(A, B, C, &registers)
		if registers == registersAfter {
			counter++
			opcodes = append(opcodes, name)
		}
	}
	return counter, opcodes
}

func cloneCandidatesMap(m map[int]map[string]struct{}) map[int]map[string]struct{} {
	cloneMap := make(map[int]map[string]struct{})
	for k1, v1 := range m {
		cloneMap[k1] = make(map[string]struct{})
		for k2, v2 := range v1 {
			cloneMap[k1][k2] = v2
		}
	}
	return cloneMap
}

// untested, recursion apparently unneccesary in my input file...
func deriveOpcodeMap(opcodeCandidates map[int]map[string]struct{}) map[int]string {
	// recursion stopper, could assign all opcodes
	if len(opcodeCandidates) == 0 {
		return make(map[int]string)
	}

	minOpcode := -1
	minCount := 999
	for opcode, candidates := range opcodeCandidates {
		if count := len(candidates); count < minCount {
			minOpcode = opcode
			minCount = count
		}
	}

	// there is an opcode with no candidate left, return nil
	if minCount < 1 {
		return nil
	}

	for opcode := range opcodeCandidates[minOpcode] {
		// Try to set opcode, remove set opcode from clone
		opcodeCandidatesClone := cloneCandidatesMap(opcodeCandidates)
		for k, v := range opcodeCandidatesClone {
			delete(v, opcode)
			if len(v) == 0 {
				delete(opcodeCandidatesClone, k)
			}
		}
		//fmt.Println(opcodeCandidatesClone)
		opcodeMap := deriveOpcodeMap(opcodeCandidatesClone)
		if opcodeMap != nil {
			opcodeMap[minOpcode] = opcode
			return opcodeMap
		}
	}

	panic("")
}

func main() {
	f, _ := os.Open("input.txt")
	defer f.Close()

	var buffer string
	scanner := bufio.NewScanner(f)
	var samples [][12]int
	var program [][4]int
	phaseOne := true
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 {
			if len(buffer) == 0 {
				phaseOne = false
				// skip empty lines
				scanner.Text()
				scanner.Text()
				continue
			}
			match := re.FindStringSubmatch(buffer)
			register11, _ := strconv.Atoi(match[1])
			register12, _ := strconv.Atoi(match[2])
			register13, _ := strconv.Atoi(match[3])
			register14, _ := strconv.Atoi(match[4])
			opcode, _ := strconv.Atoi(match[5])
			A, _ := strconv.Atoi(match[6])
			B, _ := strconv.Atoi(match[7])
			C, _ := strconv.Atoi(match[8])
			register21, _ := strconv.Atoi(match[9])
			register22, _ := strconv.Atoi(match[10])
			register23, _ := strconv.Atoi(match[11])
			register24, _ := strconv.Atoi(match[12])
			samples = append(samples, [...]int{
				register11, register12, register13, register14,
				opcode, A, B, C,
				register21, register22, register23, register24,
			})
			buffer = ""
		} else if phaseOne {
			buffer += line
		} else {
			split := strings.Split(line, " ")
			opcode, _ := strconv.Atoi(split[0])
			A, _ := strconv.Atoi(split[1])
			B, _ := strconv.Atoi(split[2])
			C, _ := strconv.Atoi(split[3])
			program = append(program, [4]int{opcode, A, B, C})
		}
	}

	// Part 1
	countThreePossibilities := 0
	for _, sample := range samples {
		if count, _ := CountMatchingOpcodes(
			[4]int{sample[0], sample[1], sample[2], sample[3]},
			[4]int{sample[8], sample[9], sample[10], sample[11]},
			sample[5], sample[6], sample[7],
		); count >= 3 {
			countThreePossibilities++
		}
	}
	fmt.Println(countThreePossibilities)

	// Part 2
	opcodeCandidatesMap := make(map[int]map[string]struct{})
	for _, sample := range samples {
		_, matchingOpCodes := CountMatchingOpcodes(
			[4]int{sample[0], sample[1], sample[2], sample[3]},
			[4]int{sample[8], sample[9], sample[10], sample[11]},
			sample[5], sample[6], sample[7],
		)
		for _, matchingOpCode := range matchingOpCodes {
			if _, ok := opcodeCandidatesMap[sample[4]]; !ok {
				opcodeCandidatesMap[sample[4]] = make(map[string]struct{})
			}
			opcodeCandidatesMap[sample[4]][matchingOpCode] = struct{}{}
		}
	}

	opcodeMap := deriveOpcodeMap(opcodeCandidatesMap)

	registers := [4]int{0, 0, 0, 0}
	for _, line := range program {
		funcs[opcodeMap[line[0]]](line[1], line[2], line[3], &registers)
	}
	fmt.Println(registers)
}
