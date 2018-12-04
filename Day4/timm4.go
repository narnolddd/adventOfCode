package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
)

var reGuard = regexp.MustCompile(`\[\d{4}-\d{2}-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] Guard #(?P<guard_id>\d+) begins shift`)
var reSleep = regexp.MustCompile(`\[\d{4}-\d{2}-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] falls asleep`)
var reAwake = regexp.MustCompile(`\[\d{4}-\d{2}-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] wakes up`)

func main() {
	f, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(f)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	sort.Strings(lines)

	var currentGuard int
	var sleepMinute int
	var sleepMinutes = make(map[int]int)
	for _, line := range lines {
		if match := reGuard.FindStringSubmatch(line); match != nil {
			g, _ := strconv.Atoi(match[4])
			currentGuard = g
		} else if match := reSleep.FindStringSubmatch(line); match != nil {
			s, _ := strconv.Atoi(match[3])
			sleepMinute = s
		} else if match := reAwake.FindStringSubmatch(line); match != nil {
			wakeMinute, _ := strconv.Atoi(match[3])
			fmt.Printf("Guard %d slept for %d minutes\n", currentGuard, wakeMinute-sleepMinute)
			sleepMinutes[currentGuard] += wakeMinute - sleepMinute
		} else {
			fmt.Println("FUCK")
		}
	}

	var maxGuard, maxSleep = -1, 0
	for guard, sleep := range sleepMinutes {
		if sleep > maxSleep {
			maxGuard = guard
			maxSleep = sleep
		}
	}
	fmt.Println(maxGuard, maxSleep)

	sleepMinutes = make(map[int]int)
	for _, line := range lines {
		if match := reGuard.FindStringSubmatch(line); match != nil {
			g, _ := strconv.Atoi(match[4])
			currentGuard = g
		} else if match := reSleep.FindStringSubmatch(line); match != nil {
			s, _ := strconv.Atoi(match[3])
			sleepMinute = s
		} else if match := reAwake.FindStringSubmatch(line); match != nil {
			wakeMinute, _ := strconv.Atoi(match[3])
			if currentGuard == maxGuard {
				for i := sleepMinute; i < wakeMinute; i++ {
					sleepMinutes[i] += 1
				}
			}
		} else {
			fmt.Println("FUCK")
		}
	}

	var maxMinute = 0
	maxSleep = 0
	for minute, sleep := range sleepMinutes {
		if sleep > maxSleep {
			maxMinute = minute
			maxSleep = sleep
		}
	}
	fmt.Println(maxMinute)

	var sleepGuardsMinutes = make(map[int]map[int]int)
	for _, line := range lines {
		if match := reGuard.FindStringSubmatch(line); match != nil {
			g, _ := strconv.Atoi(match[4])
			currentGuard = g
		} else if match := reSleep.FindStringSubmatch(line); match != nil {
			s, _ := strconv.Atoi(match[3])
			sleepMinute = s
		} else if match := reAwake.FindStringSubmatch(line); match != nil {
			wakeMinute, _ := strconv.Atoi(match[3])
			if sleepGuardsMinutes[currentGuard] == nil {
				sleepGuardsMinutes[currentGuard] = make(map[int]int)
			}
			for i := sleepMinute; i < wakeMinute; i++ {
				sleepGuardsMinutes[currentGuard][i] += 1
			}
		} else {
			fmt.Println("FUCK")
		}
	}

	maxGuard, maxSleep, maxMinute = -1, -1, -1
	for guard, sleepMinutes := range sleepGuardsMinutes {
		for minute, count := range sleepMinutes {
			if count > maxSleep {
				maxGuard = guard
				maxMinute = minute
				maxSleep = count
			}
		}
	}
	fmt.Println(maxGuard, maxMinute)
}
