package main

import (
	"fmt"
	"os"
    "strings"
)

var x, y int
var mazeMap = make(map[dir]string)
var currDir dir
var start dir
var positions int = 0
var player string = "^"
var path = NewSet()
var pathDirMap = make(map[dir][]dir)
var obstacles int = 0;

// ************** Set Implementation in Go ****************
type Set struct {
	list map[dir]struct{} //empty structs occupy 0 memory
}

func (s *Set) Has(v dir) bool {
	_, ok := s.list[v]
	return ok
}

func (s *Set) Add(v dir) {
	s.list[v] = struct{}{}
}

func (s *Set) Remove(v dir) {
	delete(s.list, v)
}

func (s *Set) Clear() {
	s.list = make(map[dir]struct{})
}

func (s *Set) Size() int {
	return len(s.list)
}

func NewSet() *Set {
	s := &Set{}
	s.list = make(map[dir]struct{})
	return s
}
// ************** End of Set Implementation ****************

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

func setStartPosition() {
    // facing up at the start
    currDir.x = -1
    currDir.y = 0

    for c, v := range(mazeMap) {
        if v == "^" {
            start = c
            return
        }
    }
}

func move(pos *dir) {
    pos.x += currDir.x
    pos.y += currDir.y
}

func turnRight() {
    currDir = dir_map[currDir]
    player = player_map[player]
}

func checkObstacle(pos dir) bool {
    var i, j int = pos.x, pos.y
    if ((i < x && i >= 0) && (j < y && j >= 0) && mazeMap[dir{x: i, y: j}] == "#") {
        return true
    }
    return false
}

func createMazeMap(maze []string) {
    x, y = len(maze) - 1, len(maze[0])
    for i := range x {
        for j := range y {
            mazeMap[dir{x: i, y: j}] = string(maze[i][j])
        }
    }
}

func traverseMaze(visited map[dir][]dir, part2 bool) {
    var prev dir
    pos := start
    for pos.x >= 0 && pos.x < x && pos.y >= 0 && pos.y < y {

        // visit cell
        dirs, haveVisited := visited[pos]
        if !part2 && !haveVisited {
            positions++
        }

        // HACK: handle edge case for when the player turns right and the next
        // iteration of the loop has the pos visited already, but in a different
        // direction. This causes it to be incorrectly classified as "being caught in
        // a loop" when it has only just turned to the right and not stepped ahead.
        if pos != prev {
            if part2 && haveVisited {
                for _, d := range dirs {
                    if currDir == d {
                        obstacles++
                        return
                    }
                }
            }
            visited[pos] = append(visited[pos], currDir)
            prev = pos
        }

        // turn right if an obstacle was found
        if checkObstacle(dir{x: pos.x + currDir.x, y: pos.y + currDir.y}) {
            turnRight()
        } else {
            // step ahead and log path
            // HACK: crossing a previously visited pos at a later point in time
            // causes the path to have duplicates, which if not resolved, lead to
            // duplicate obstacle calculations
            if !part2 && pos != start {
                path.Add(pos)
            }
            move(&pos)
        }
    }
}

func renderMaze() {
    for i := range x {
        for j := range y {
            fmt.Printf("%s", mazeMap[dir{x: i, y: j}])
        }
        fmt.Println()
    }
    fmt.Println()
}


func main() {
    var maze = make([]string, 0)
    var visited = make(map[dir][]dir)

    f, err := os.ReadFile("6.in")
    if err != nil {
        fmt.Println(err)
        return
    }
    data := string(f)
    maze = strings.Split(data, "\n")
    createMazeMap(maze)

    setStartPosition()
    traverseMaze(visited, false)
    fmt.Println("Part-1:", positions)

    for p := range path.list {
        mazeMap[p] = "#"
        setStartPosition()
        visited = make(map[dir][]dir)
        traverseMaze(visited, true)
        mazeMap[p] = "."
    }
    fmt.Println("Part-2:", obstacles)
}
