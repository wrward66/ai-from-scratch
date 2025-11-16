## Decision Tree from Scratch 🌳
A pure Python implementation of a Decision Tree classifier built from scratch using only NumPy. This implementation demonstrates the complete decision tree algorithm with entropy-based splitting and recursive tree building.

## Overview
This project implements Decision Tree classification entirely from first principles, covering:

Entropy and information gain calculations

Recursive binary splitting with configurable depth

Multiple stopping criteria to prevent overfitting

Tree traversal for predictions

Visualization-ready structure

No pre-built ML libraries for the core algorithm.

## Implementation Structure
The implementation is organized into the following components:

# Node Class
The fundamental building block of the decision tree, representing both internal decision nodes and leaf prediction nodes.

# DecisionTree Class
Main classifier with complete functionality:

Tree construction using information gain

Configurable depth and splitting parameters

Prediction methods for new data

# Example Implementation
Ready-to-run demo with synthetic data showing the algorithm in action.

## Key Features
Pure from-scratch implementation - No scikit-learn or other ML libraries for the core algorithm

Entropy-based splitting - Uses information gain to find optimal splits

Configurable parameters - Control tree depth, minimum samples, and feature selection

Educational focus - Clean, commented code that explains each step of the algorithm

Real-time results - Immediate feedback on model accuracy and performance

## Algorithm Explanation
Decision Trees work by recursively splitting the data based on feature values that maximize information gain, creating a tree-like model where:

Internal nodes test feature conditions

Branches represent decision outcomes

Leaf nodes provide final predictions

The implementation uses entropy to measure node impurity and information gain to select the most informative splits.

## Usage
The notebook demonstrates the complete workflow from data preparation to model evaluation, including:

Synthetic dataset generation

Model training with different parameters

Prediction on test data

Accuracy scoring and performance analysis
