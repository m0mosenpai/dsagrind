package main

import (
	"fmt"
	"os"
    "strings"
)

var x, y int
var maze = make([]string, 0)
var curr_dir dir
var positions int = 0

type dir struct {
    x int
    y int
}

var dir_map = map[dir]dir{
    {x: -1, y: 0}: {x: 0, y: 1},
    {x: 0, y: 1}: {x: 1, y: 0},
    {x: 1, y: 0}: {x: 0, y: -1},
    {x: 0, y: -1}: {x: -1, y: 0},
}

func move(i *int, j *int) {
    *i += curr_dir.x
    *j += curr_dir.y
}

func turnRight() {
    curr_dir.x = dir_map[curr_dir].x
    curr_dir.y = dir_map[curr_dir].y
}

func checkObstacle(i int, j int) bool {
    next_i, next_j := i + curr_dir.x, j + curr_dir.y
    if ((next_i < x && next_i >= 0) &&
        (next_j < y && next_j >= 0) &&
        string(maze[next_i][next_j]) == "#") {
        return true
    }
    return false
}


func main() {
    f, err := os.ReadFile("6.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    data := string(f)
    maze = strings.Split(data, "\n")

    x, y = len(maze) - 1, len(maze[0])
    visited := make([][]int, x)
    for i := range visited {
        visited[i] = make([]int, y)
    }

    // facing up in the start
    curr_dir.x = -1
    curr_dir.y = 0

    // get start position
    var g_x, g_y int
    for i := range maze {
        for j := range maze[i] {
            if string(maze[i][j]) == "^" {
                g_x = i
                g_y = j
                visited[i][j] = 1
                positions++
                break
            }
        }
    }

    // traverse
    var i, j int = g_x, g_y
    for i > 0 && i < x && j > 0 && j < y {
        // mark current pos as visited
        if visited[i][j] != 1 {
            positions++
        }
        visited[i][j] = 1

        // check for obstacles
        if checkObstacle(i, j) {
            turnRight()
            fmt.Println("Turned Right!")
        }

        // step ahead
        move(&i, &j)
        fmt.Printf("Moved to i: %d, j: %d\n", i, j)
    }
    fmt.Println("Part-1:", positions)
}
