package main

import (
	"fmt"
)

func main() {
	p := twoSum([]int{1, 2, 3, 4}, 3)
	fmt.Println(p)
}

func twoSum(nums []int, target int) []int {
	var diff int = 0
	var DifferenceTable = make(map[int]int)

	for i := 0; i < len(nums); i++ {
		diff = target - nums[i]
		value, found := DifferenceTable[diff]
		if found == true {
			return []int{value, i}
		}
		DifferenceTable[nums[i]] = i
	}
	return []int{}
}
