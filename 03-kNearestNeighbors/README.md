## k-Nearest Neighbors from Scratch
A pure Python implementation of the k-Nearest Neighbors algorithm built from scratch using only NumPy. This notebook demonstrates the complete implementation and visualization of the k-NN classifier.

## Overview
This project implements k-NN classification entirely from first principles, covering:

Euclidean and Manhattan distance metrics

Configurable k values (number of neighbors)

Decision boundary visualization

Model performance analysis

No pre-built ML libraries for the core algorithm

## Notebook Structure
The notebook is organized into the following sections:

Implementation - Complete k-NN class with distance calculations and prediction logic

Demo Data - Synthetic dataset generation for testing and visualization

Model Testing - Evaluation with different k values and distance metrics

Visualization - Decision boundary plots showing how the algorithm classifies regions

Performance Analysis - Accuracy metrics and model behavior insights

## Key Features
Pure from-scratch implementation - No scikit-learn or other ML libraries for the core algorithm

Multiple distance metrics - Compare Euclidean vs Manhattan distance performance

Interactive visualization - See how different k values affect decision boundaries

Educational focus - Clean, commented code that explains each step of the algorithm

Real-time results - Immediate feedback on model accuracy and behavior

## Algorithm Explanation
k-Nearest Neighbors is a simple instance-based learning algorithm that classifies data points based on the majority class of their k closest neighbors in the feature space. The implementation includes:

Distance calculation between points

Neighbor selection and sorting

Majority voting for classification

Model evaluation and scoring

## Usage
Simply run the notebook cells sequentially to see the algorithm in action. The demo includes synthetic data generation, model training, prediction, and visualization of results.
