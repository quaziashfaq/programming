package main

import (
	"fmt"
)

// my Node class
type Node struct {
	data int
	left *Node
	right *Node
}

// Node Contstructor
func NewNode(aData int) *Node {
	return &Node {
		data: aData,
		left: nil,
		right: nil,
	}
}

// A member function for Node. It just prints
func (n *Node) Print() {
	if n != nil {
		fmt.Println(n.data)
	} else {
		fmt.Println ("nil")
	}
}


// A member function for Node. It just prints with Depth
func (n *Node) PrintDepth() {
	n.Print()
	if n != nil {
		fmt.Print("Going to left : ")
		n.left.PrintDepth()
		fmt.Print("Going to right : ")
		n.right.PrintDepth()
	}
}

type BST struct {
	root *Node
}

func NewBST() *BST {
	return &BST {
		root: nil,
	}
}

func (bst *BST) Insert(data int) {
	if bst.root == nil {
		bst.root = NewNode(data)
	} else {
		var temp **Node
		temp = &bst.root
		for *temp != nil {
			if data <= (*temp).data {
				temp = & ((*temp).left)
			} else {
				temp = & ((*temp).right)
			}
		}
		*temp = NewNode(data)
	}
}

func (bst *BST) PrintDepth() {
	bst.root.PrintDepth()
}


func main() {
	numbers := []int {18, 21, 10, 20, 30}
	bst := NewBST()
	for _, value := range numbers {
		bst.Insert(value)
	}
	bst.PrintDepth()
}
