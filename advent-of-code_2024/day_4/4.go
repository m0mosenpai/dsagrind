package main

import (
	"bufio"
	"fmt"
	"os"
)

var xmas string = "XMAS"
var mas string = "MAS"
var wordsearch = make([]string, 0)

func checkUp(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) {
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        i--
    }
    return 0
}

func checkUpLeft(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        i--
        j--
    }
    return 0
}

func checkUpRight(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        i--
        j++
    }
    return 0
}

func checkDown(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        i++
    }
    return 0
}

func checkDownLeft(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        i++
        j--
    }
    return 0
}

func checkDownRight(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        i++
        j++
    }
    return 0
}

func checkLeft(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        j--
    }
    return 0
}

func checkRight(i int, j int, target string) int {
    word := ""
    for i >= 0 && i < len(wordsearch) && j >= 0 && j < len(wordsearch[i]){
        word += string(wordsearch[i][j])
        if (len(word) == len(target)) {
            if (word == target) {
                return 1
            } else {
                break
            }
        }
        j++
    }
    return 0
}

func main() {
    f, err := os.Open("4.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        row := scanner.Text()
        wordsearch = append(wordsearch, row)
    }
    defer f.Close()

    total := 0
    for i := range wordsearch {
        for j := range wordsearch[i] {
            if (string(wordsearch[i][j]) == "X") {
                total += checkUp(i, j, xmas)
                total += checkUpLeft(i, j, xmas)
                total += checkUpRight(i, j, xmas)
                total += checkDown(i, j, xmas)
                total += checkDownLeft(i, j, xmas)
                total += checkDownRight(i, j, xmas)
                total += checkLeft(i, j, xmas)
                total += checkRight(i, j, xmas)
            }
        }
    }
    fmt.Println("Part-1:", total)

    total = 0
    for i := range wordsearch {
        for j := range wordsearch[i] {
            if (string(wordsearch[i][j]) == "A") {
                if (checkDownRight(i-1, j-1, mas) != 0 && checkDownLeft(i-1, j+1, mas) != 0) {
                    total++
                    continue
                }
                if (checkDownLeft(i-1, j+1, mas) != 0 && checkUpLeft(i+1, j+1, mas) != 0) {
                    total++
                    continue
                }
                if (checkUpLeft(i+1, j+1, mas) != 0 && checkUpRight(i+1, j-1, mas) != 0) {
                    total++
                    continue
                }
                if (checkUpRight(i+1, j-1, mas) != 0 && checkDownRight(i-1, j-1, mas) != 0) {
                    total++
                    continue
                }
            }
        }
    }
    fmt.Println("Part-2:", total)
}
