package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

type group struct {
	units        int
	hp           int
	weak         []string
	immune       []string
	attackDamage int
	attackType   string
	initiative   int
	side         int
}

var re = regexp.MustCompile(`^(\d+) units each with (\d+) hit points(?: \((.+)\)|) with an attack that does (\d+) (\S+) damage at initiative (\d+)$`)

func parseInput() []group {
	f, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(f)
	side := 0
	groups := make([]group, 0)
	for scanner.Scan() {
		line := scanner.Text()
		switch line {
		case "":
		case "Immune System:":
		case "Infection:":
			side = 1
		default:
			match := re.FindStringSubmatch(line)
			if match == nil {
				panic("")
			}
			var weak, immune []string
			if len(match[3]) > 0 {
				split1 := strings.Split(match[3], "; ")
				for _, sub := range split1 {
					if strings.HasPrefix(sub, "weak to") {
						weak = strings.Split(sub[8:], ", ")
					} else if strings.HasPrefix(sub, "immune to") {
						immune = strings.Split(sub[10:], ", ")
					} else {
						panic("")
					}
				}
			}
			units, _ := strconv.Atoi(match[1])
			hp, _ := strconv.Atoi(match[2])
			attackDamage, _ := strconv.Atoi(match[4])
			initiative, _ := strconv.Atoi(match[6])
			groups = append(groups, group{units, hp, weak, immune, attackDamage, match[5], initiative, side})
		}
	}

	return groups
}

func attackDamage(a, b group) int {
	// standard damage
	damage := a.units * a.attackDamage

	// check weak
	for _, weak := range b.weak {
		if weak == a.attackType {
			damage *= 2
			break
		}
	}

	// check immune - somewhat inefficient
	for _, immune := range b.immune {
		if immune == a.attackType {
			damage = 0
			break
		}
	}

	return damage
}

func simulateCombat(groups []group, boost int) (int, int) {
	for i := 0; i < len(groups); i++ {
		if groups[i].side == 0 {
			groups[i].attackDamage += boost
		}
	}
	for combatEnd := false; !combatEnd; {
		// instead of sorting the array, keep pointers and sort slice of pointers
		p := make([]*group, 0)
		for i := 0; i < len(groups); i++ {
			p = append(p, &groups[i])
		}

		// sort by effective power
		sort.Slice(p, func(i, j int) bool {
			if ep1, ep2 := p[i].units*p[i].attackDamage, p[j].units*p[j].attackDamage; ep1 != ep2 {
				return ep1 > ep2
			} else {
				return p[i].initiative > p[j].initiative
			}
		})

		// determine attack targets
		attackedBy := make(map[*group]*group)
		for i := 0; i < len(p); i++ {
			maxDamage := -1
			targetIdx := -1
			for j := 0; j < len(p); j++ {
				// same side (supercase of same group)
				if p[i].side == p[j].side {
					continue
				}

				// target already chosen
				if _, ok := attackedBy[p[j]]; ok {
					continue
				}

				// check whether to prefer new target
				damage := attackDamage(*p[i], *p[j])
				if damage > maxDamage {
					maxDamage = damage
					targetIdx = j
				} else if damage == maxDamage {
					if p[j].units*p[j].attackDamage > p[targetIdx].units*p[targetIdx].attackDamage {
						targetIdx = j
					} else if p[j].units*p[j].attackDamage == p[targetIdx].units*p[targetIdx].attackDamage &&
						p[j].initiative > p[targetIdx].initiative {
						targetIdx = j
					}
				}
			}
			if targetIdx != -1 && maxDamage > 0 {
				attackedBy[p[targetIdx]] = p[i]
			}
		}

		// invert mapping to attacker - target
		attackTargets := make(map[*group]*group)
		for k, v := range attackedBy {
			attackTargets[v] = k
		}

		// sort by initiative
		sort.Slice(p, func(i, j int) bool {
			return p[i].initiative > p[j].initiative
		})

		// attack
		attacked := false
		for i := 0; i < len(p); i++ {
			if p[i].units <= 0 {
				continue
			}
			if _, ok := attackTargets[p[i]]; !ok {
				continue
			}
			target := attackTargets[p[i]]
			damage := attackDamage(*p[i], *target)
			loss := damage / target.hp
			target.units -= loss
			if loss > 0{
			attacked = true
			}
		}

		if !attacked{
			return -1, -1
		}

		for i := len(groups) - 1; i >= 0; i-- {
			if groups[i].units <= 0 {
				groups = append(groups[:i], groups[i+1:]...)
			}
		}

		side0 := groups[0].side
		unitCount := 0
		combatEnd = true
		for _, group := range groups {
			if group.side != side0 {
				combatEnd = false
				break
			}
			unitCount += group.units
		}
		
		if combatEnd {
			return side0, unitCount
		}
	}

	return -1, -1
}

func cloneGroups(groups []group) []group {
	groupsNew := make([]group, 0)
	for _, g := range groups {
		weak := make([]string, len(g.weak))
		copy(weak, g.weak)
		immune := make([]string, len(g.immune))
		copy(immune, g.immune)
		newStruct := group{g.units, g.hp, weak, immune, g.attackDamage, g.attackType, g.initiative, g.side}
		groupsNew = append(groupsNew, newStruct)
	}
	return groupsNew
}

func main() {
	groups := parseInput()

	groupsNew := cloneGroups(groups)
	fmt.Println(simulateCombat(groupsNew, 0))

	for boost := 1; ; boost++ {
		groupsNew := cloneGroups(groups)
		side, units := simulateCombat(groupsNew, boost)
		fmt.Println(side, units)
		if side == 0{
			break
		}
	}
}
