package main

import (
	"fmt"
	"os"
    "strings"
    // "time"
)

var x, y int
var maze = make([]string, 0)
var maze_map = make(map[dir]string)
var curr_dir dir
var positions int = 0
var player string = "^"

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

var player_map = map[string]string{
    "^" : ">",
    ">" : "v",
    "v" : "<",
    "<" : "^",
}

func move(i *int, j *int) {
    maze_map[dir{x: *i, y: *j}] = "X"
    *i += curr_dir.x
    *j += curr_dir.y
    maze_map[dir{x: *i, y: *j}] = player
}

func turnRight() {
    curr_dir = dir_map[curr_dir]
    player = player_map[player]
}

func checkObstacle(i int, j int) bool {
    if ((i < x && i >= 0) && (j < y && j >= 0) && maze_map[dir{x: i, y: j}] == "#") {
        return true
    }
    return false
}

func createMazeMap(x int, y int) {
    for i := range x {
        for j := range y {
            maze_map[dir{x: i, y: j}] = string(maze[i][j])
        }
    }
}

func renderMaze() {
    for i := range x {
        for j := range y {
            fmt.Printf("%s", maze_map[dir{x: i, y: j}])
        }
        fmt.Println()
    }
    fmt.Printf("Positions: %d\n\n", positions)
    // time.Sleep(500 * time.Millisecond)
    // fmt.Print("\033[H\033[2J")
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
    var visited = make(map[dir]int)
    createMazeMap(x, y)

    // facing up in the start
    curr_dir.x = -1
    curr_dir.y = 0

    // get start position
    var start dir
    for c, v := range(maze_map) {
        if v == "^" {
            start.x = c.x
            start.y = c.y
            visited[c] = 1
            positions++
            break
        }
    }
    fmt.Printf("Starting Position: (%d, %d)\n", start.x, start.y)

    // traverse
    var i, j int = start.x, start.y
    for i >= 0 && i < x && j >= 0 && j < y {
        // display maze
        // renderMaze()

        // mark current pos as visited
        if visited[dir{x: i, y: j}] != 1 {
            positions++
        }
        visited[dir{x: i, y: j}] = 1

        // check for obstacles
        if checkObstacle(i + curr_dir.x, j + curr_dir.y) {
            turnRight()
        } else {
            // step ahead
            move(&i, &j)
        }

    }
    renderMaze()
    fmt.Println("Part-1:", positions)
}
