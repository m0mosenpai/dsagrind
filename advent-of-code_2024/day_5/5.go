package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var adjlist = make(map[int][]int, 0)
var order = make([]int, 0)
var correct_total int = 0
var incorrect_total int = 0

func updateTotal(updates []string, invalid bool) {
    mid := int(len(updates) / 2)
    num, _ := strconv.Atoi(updates[mid])
    if invalid {
        incorrect_total += num
    } else {
        correct_total += num
    }
}

func correctOrder(nums []string) {
    indices := make([]int, 0)
    for i := range nums {
        num, _ := strconv.Atoi(nums[i])
        idx := getIndex(order, num)
        indices = append(indices, idx)
    }
    sort.Ints(indices)
    for i := range indices {
        nums[i] = strconv.Itoa(order[indices[i]])
    }
}

func getIndex (array []int, num int) int {
    for i := range(array) {
        if array[i] == num {
            return i
        }
    }
    return -1
}

func dfs(root int, adjlist map[int][]int, visited map[int]int) {
    if (visited[root] == 1) {
        return
    }

    visited[root] = 1
    neighbors := adjlist[root]
    for i := range neighbors {
        n := neighbors[i]
        dfs(n, adjlist, visited)
    }
    order = append(order, root)
}

func topologicalSort(adjlist map[int][]int) {
    visited := make(map[int]int)
    for k := range adjlist {
        dfs(k, adjlist, visited)
    }
    for i, j := 0, len(order)-1; i < j; i, j = i+1, j-1 {
        order[i], order[j] = order[j], order[i]
    }
}

func main() {
    f, err := os.ReadFile("5.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    data := string(f)
    parsedData := strings.Split(data, "\n")

    var i int = 0
    for i = range parsedData {
        if parsedData[i] == "" {
            break
        }
        rule := strings.Split(parsedData[i], "|")
        num1, _ := strconv.Atoi(rule[0])
        num2, _ := strconv.Atoi(rule[1])
        _, ok := adjlist[num1]
        if !ok {
            adjlist[num1] = make([]int, 0)
        }
        adjlist[num1] = append(adjlist[num1], num2)
    }

    for i < len(parsedData) {
        updates := strings.Split(parsedData[i], ",")
        if len(updates) > 1 {
            // get ordering for only nums in updates
                sec_adjlist := make(map[int][]int)
                for n := range updates {
                    update, _ := strconv.Atoi(updates[n])
                    for k, v := range adjlist {
                        if update == k {
                            sec_adjlist[k] = v
                            break
                        }
                    }
                }
            topologicalSort(sec_adjlist)

            maxIdx := -1
            var invalid bool = false
            for j := range(updates) {
                num, _ := strconv.Atoi(updates[j])
                // check precedence order
                idx := getIndex(order, num)
                if idx == -1 {
                    continue
                }

                if idx >= maxIdx {
                    maxIdx = idx
                } else {
                    invalid = true
                    break
                }
            }
            if invalid {
                correctOrder(updates)
            }
            updateTotal(updates, invalid)
        }
        i++;
    }

    fmt.Println("Part-1:", correct_total)
    fmt.Println("Part-2:", incorrect_total)
}
