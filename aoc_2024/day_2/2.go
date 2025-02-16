package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
    "strings"
    "math"
)

func checkSafety(l1 int, l2 int, dir *int) bool {
    diff := float64(l2 - l1)
    if math.Abs(diff) < 1 || math.Abs(diff) > 3 {
        return false
    }
    if *dir == 0 {
        if diff < 0 {
            *dir = -1
        } else {
            *dir = 1
        }
    }
    if *dir > 0 && diff < 0 || *dir < 0 && diff > 0 {
        return false
    }
    return true
}

func main() {
    f, err := os.Open("2.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    r := bufio.NewReader(f)
    var safe int = 0
    for {
        line, err := r.ReadString('\n')
        if err != nil {
            break
        }
        levels := strings.Fields(line)
        var i int = 0
        var dir int = 0
        var isSafe bool = true
        var fixed int = 0
        fmt.Println("Levels:", levels)
        for i = 0; i < len(levels) - 1; i++ {
            curr, _ := strconv.Atoi(levels[i])
            next, _ := strconv.Atoi(levels[i+1])
            if !checkSafety(curr, next, &dir) {
                if (fixed == 1) {
                    fmt.Println("Can only fix 1!")
                    isSafe = false
                    break
                }
                if i > 0 && i < len(levels) - 2 {
                    new_curr, _ := strconv.Atoi(levels[i-1])
                    new_next, _ := strconv.Atoi(levels[i+2])
                    // remove first element & check
                    if i == 1 {
                        tmp := dir
                        dir = 0
                        if checkSafety(curr, next, &dir) {
                            fmt.Println("Safe by removing:", new_curr)
                            fixed++
                            continue
                        }
                        dir = tmp
                    }// else {
                    //     // remove prev element & check
                    //     new_prev, _ := strconv.Atoi(levels[i-2])
                    //     if checkSafety(new_prev, curr, &dir) {
                    //         fmt.Println("Safe by removing:", curr)
                    //         fixed++
                    //         continue
                    //     }
                    // }

                    // remove curr element & check
                    if checkSafety(new_curr, next, &dir) {
                        fmt.Println("Safe by removing:", curr)
                        fixed++
                        continue
                    }


                    // remove next element & check
                    if checkSafety(curr, new_next, &dir) {
                        fmt.Println("Safe by removing:", next)
                        fixed++
                        i++
                        continue
                    }
                    isSafe = false
                    break
                }
                fixed++
                if i == len(levels) - 2 {
                    fmt.Println("Safe by removing:", next)
                }
            }
        }
        if isSafe && i > 0 {
            safe++
            fmt.Println("Safe:", safe)
        } else {
            fmt.Println("Unsafe")
        }
    }
    // fmt.Printf("Part 1: %d\n", safe)
    fmt.Printf("Part 2: %d\n", safe)
    defer f.Close()
}

