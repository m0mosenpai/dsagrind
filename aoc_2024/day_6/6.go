package main

import (
	"fmt"
	"os"
    "strings"
    // "time"
)

var x, y int
var maze_map = make(map[dir]string)
var curr_dir dir
var positions int = 0
var player string = "^"
var path = make([]dir, 0)

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

func setStartPosition(pos *dir) {
    // facing up at the start
    curr_dir.x = -1
    curr_dir.y = 0

    for c, v := range(maze_map) {
        if v == "^" {
            pos.x = c.x
            pos.y = c.y
            positions++
            return
        }
    }
}

func move(pos *dir) {
    pos.x += curr_dir.x
    pos.y += curr_dir.y
}

func turnRight() {
    curr_dir = dir_map[curr_dir]
    player = player_map[player]
}

func checkObstacle(pos dir) bool {
    var i, j int = pos.x, pos.y
    if ((i < x && i >= 0) && (j < y && j >= 0) && maze_map[dir{x: i, y: j}] == "#") {
        return true
    }
    return false
}

func canCreateLoop(pos dir, visited map[dir][]dir) bool {
    for !checkObstacle(pos) {
        dirs := visited[pos]
        fmt.Println(dirs)
        // for d := range dirs {
        // }
        move(&pos)
    }
    return false
}

func createMazeMap(maze []string) {
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
    f, err := os.ReadFile("6.ex")
    if err != nil {
        fmt.Println(err)
        return
    }
    data := string(f)

    var maze = make([]string, 0)
    maze = strings.Split(data, "\n")

    x, y = len(maze) - 1, len(maze[0])
    var visited = make(map[dir][]dir)
    createMazeMap(maze)

    // set start position
    var pos dir
    setStartPosition(&pos)
    visited[pos] = append(visited[pos], curr_dir)
    fmt.Printf("Starting Position: (%d, %d)\n", pos.x, pos.y)

    // traverse
    for pos.x >= 0 && pos.x < x && pos.y >= 0 && pos.y < y {

        // visit cell
        _, haveVisited := visited[pos]
        if !haveVisited {
            positions++
        }
        visited[pos] = append(visited[pos], curr_dir)

        // canCreateLoop(pos, visited)

        // check for obstacles
        if checkObstacle(dir{x: pos.x + curr_dir.x, y: pos.y + curr_dir.y}) {
            turnRight()
        } else {
            // step ahead and log path
            path = append(path, pos)
            maze_map[pos] = "X"
            move(&pos)
            maze_map[pos] = player
        }

    }
    renderMaze()
    fmt.Println("Visited:", visited)
    fmt.Println("Part-1:", positions)
}
