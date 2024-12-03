package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
    "sort"
)

func main() {
    f, err := os.ReadFile("3.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    data := string(f)
    
    re_mul := regexp.MustCompile(`mul\([0-9]+,[0-9]+\)`)
    re_do := regexp.MustCompile(`do\(\)`)
    re_dont := regexp.MustCompile(`don't\(\)`)
    muls := re_mul.FindAllString(data, -1)
    mulPos := re_mul.FindAllStringIndex(data, -1)
    var mps []map[string]int
    for i := range mulPos {
        mps = append(mps, map[string]int{"m": mulPos[i][1]})
    }
    var dps []map[string]int
    doPos := re_do.FindAllStringIndex(data, -1)
    for i := range doPos {
        dps = append(dps, map[string]int{"d": doPos[i][1]})
    }
    var dnps []map[string]int
    dontPos := re_dont.FindAllStringIndex(data, -1)
    for i := range dontPos {
        dnps = append(dnps, map[string]int{"dn": dontPos[i][1]})
    }
    aps := append(mps, dps...)
    aps = append(aps, dnps...)
    sort.Slice(aps, func(i, j int) bool {
        var val1 int
        var val2 int
        for _, v := range aps[i] {
            val1 = v
        }
        for _, v := range aps[j] {
            val2 = v
        }
        return val1 < val2
    })

    var result int = 0
    var matches int = 0
    var mulmap = make(map[int]int)
    for i := range muls {
        matches++
        curr := muls[i]
        re := regexp.MustCompile(`[0-9]+`)
        nums := re.FindAllString(curr, -1)
        num1, _ := strconv.Atoi(nums[0])
        num2, _ := strconv.Atoi(nums[1])
        prod := (num1*num2)
        result += prod
        mulmap[mulPos[i][1]] = prod 
    }
    fmt.Println("Part-1:", result)

    var disabled bool = false
    var newResult int = 0
    for i := range aps {
        _, d := aps[i]["d"]
        if d {
            disabled = false
        }
        _, dn := aps[i]["dn"]
        if dn {
            disabled = true
        }
        if disabled {
            continue
        }

        val, _ := aps[i]["m"]
        newResult += mulmap[val]

    }
    fmt.Println("Part-2:", newResult)
}

