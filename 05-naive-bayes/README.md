## Naive Bayes from Scratch
A pure Python implementation of a Naive Bayes classifier built from scratch using only NumPy. This implementation demonstrates the complete Naive Bayes algorithm with Gaussian probability distributions and Bayesian inference.

## Overview
This project implements Naive Bayes classification entirely from first principles, covering:

Gaussian probability density functions

Bayes theorem for classification

Feature independence assumption

Maximum a posteriori decision making

No pre-built ML libraries for the core algorithm.

## Implementation Structure
The implementation is organized into the following components:

# NaiveBayes Class
Main classifier with complete functionality:

Probability distribution estimation

Bayesian inference for predictions

Gaussian PDF calculations

# Example Implementation
Ready-to-run demo with synthetic data showing the algorithm in action.

## Key Features
Pure from-scratch implementation - No scikit-learn or other ML libraries for the core algorithm

Gaussian Naive Bayes - Assumes continuous features follow normal distributions

Probabilistic foundation - Uses Bayes theorem for classification decisions

Educational focus - Clean, commented code that explains each step of the algorithm

Fast training - No iterative optimization required

## Algorithm Explanation
Naive Bayes applies Bayes theorem with the "naive" assumption that features are conditionally independent given the class. The implementation:

Trains by calculating mean and variance for each feature per class

Predicts by computing posterior probabilities using Gaussian PDF

Classifies by selecting the class with highest posterior probability

## Usage
The implementation demonstrates the complete workflow from data preparation to model evaluation, including:

Synthetic dataset generation

Model training with probability estimation

Prediction on test data using Bayesian inference

Accuracy scoring and performance analysis