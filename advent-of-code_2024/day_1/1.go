package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
    "strings"
    "sort"
    "math"
)

func main() {
    f, err := os.Open("1.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    r := bufio.NewReader(f)
    nums1 := make([]int, 0)
    nums2 := make([]int, 0)
    for {
        line, err := r.ReadString('\n')
        if err != nil {
            break
        }
        nums := strings.Fields(line)
        num1, err1 := strconv.Atoi(nums[0])
        num2, err2 := strconv.Atoi(nums[1])
        if err1 != nil || err2 != nil {
            break
        }
        nums1 = append(nums1, num1)
        nums2 = append(nums2, num2)
    }
    defer f.Close()

    sort.Ints(nums1)
    sort.Ints(nums2)
    var sum float64 = 0
    for i := range nums1 {
        diff := float64(nums1[i] - nums2[i])
        sum += math.Abs(diff)
    }
    fmt.Printf("Part 1: %d\n", int(sum))

    smap := make(map[int]int)
    for i := range nums2 {
        n := nums2[i]
        _, ok := smap[n]
        if !ok {
            smap[n] = 1
        } else {
            smap[n]++
        }
    }

    var ssum int = 0
    for i := range nums1 {
        n := nums1[i]
        _, ok := smap[n]
        if ok {
            ssum += n*smap[n]
        }
    }
    fmt.Printf("Part 2: %d\n", ssum)
}
