package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
)

var re = regexp.MustCompile(`^Step (.+) must be finished before step (.) can begin.$`)

func part1(steps map[string][]string) {
	stepsDone := make(map[string]bool)
	stepsReady := []string{}
	nSteps := len(steps)

	for i := 0; i < nSteps; i++ {
	Loop:
		for step, prereqs := range steps {
			for _, prereq := range prereqs {
				if stepsDone[prereq] != true {
					continue Loop
				}
			}
			stepsReady = append(stepsReady, step)
			delete(steps, step)
		}
		sort.Strings(stepsReady)
		nextStep := stepsReady[0]
		fmt.Print(nextStep)
		stepsDone[nextStep] = true
		stepsReady = stepsReady[1:]
	}
	fmt.Println()
}

func part2(steps map[string][]string) {
	stepsDone := make(map[string]bool)
	stepsReady := []string{}
	nSteps := len(steps)

	workersJob := [5]string{".", "."}
	workersDuration := [5]int{-1, -1}

	jobDuration := make(map[string]int)
	for i := 0; i < 26; i++ {
		jobDuration[string('A'+i)] = i + 1 + 60
	}

	for i := 0; len(stepsDone) < nSteps; i++ {

		for w := 0; w < len(workersJob); w++ {
			if workersDuration[w] >= 0 {
				workersDuration[w] -= 1
			}

			if workersDuration[w] == 0 {
				stepsDone[workersJob[w]] = true
				workersJob[w] = "."
			}
		}

	Loop:
		for step, prereqs := range steps {
			for _, prereq := range prereqs {
				if stepsDone[prereq] != true {
					continue Loop
				}
			}
			stepsReady = append(stepsReady, step)
			delete(steps, step)
		}
		sort.Strings(stepsReady)

		for len(stepsReady) > 0 {
			s := stepsReady[0]
			for w, Duration := range workersDuration {
				if Duration <= 0 {
					workersJob[w] = s
					workersDuration[w] = jobDuration[s]
					stepsReady = stepsReady[1:]
					s = ""
					break
				}
			}
			if s != "" {
				break
			}
		}
		fmt.Println(i, workersJob, workersDuration)
	}
}

func main() {
	f, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(f)

	steps := make(map[string][]string)
	for scanner.Scan() {
		line := scanner.Text()
		if match := re.FindStringSubmatch(line); match != nil {
			steps[match[2]] = append(steps[match[2]], match[1])
			if steps[match[1]] == nil {
				steps[match[1]] = []string{}
			}
		}
	}

	stepsCopy := make(map[string][]string)
	for k, v := range steps {
		stepsCopy[k] = v
	}
	part1(stepsCopy)

	fmt.Println()

	part2(steps)
}
