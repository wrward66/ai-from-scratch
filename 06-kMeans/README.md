## K-Means from Scratch
A pure Python implementation of the K-Means clustering algorithm built from scratch using only NumPy. This implementation demonstrates unsupervised learning with centroid-based clustering.

## Overview
This project implements K-Means clustering entirely from first principles, covering:

Centroid initialization (random selection)

Distance calculations (Euclidean)

Iterative clustering with centroid updates

Convergence detection

No pre-built ML libraries for the core algorithm.

## Implementation Structure
The implementation is organized into the following components:

# KMeans Class
Main clustering algorithm with complete functionality:

Random centroid initialization

Iterative assignment and update steps

Convergence checking

# Example Implementation
Ready-to-run demo with synthetic data showing the algorithm in action.

## Key Features
Pure from-scratch implementation - No scikit-learn or other ML libraries for the core algorithm

Euclidean distance calculations for cluster assignments

Configurable K - Choose number of clusters

Visualization-ready - Easy to plot clusters and centroids

Educational focus - Clean, commented code that explains each step

## Algorithm Explanation
K-Means is an unsupervised learning algorithm that partitions data into K clusters by:

Initializing K centroids randomly

Assigning each point to nearest centroid

Updating centroids to mean of assigned points

Repeating until convergence

## Usage
The implementation demonstrates the complete workflow including:

Synthetic dataset generation with clear clusters

Model training with iterative improvements

Cluster visualization with centroid movement

Convergence tracking