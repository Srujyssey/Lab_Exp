# Parallel Maximum/Minimum Search using OpenMP

## Problem Statement

Find the maximum and minimum values in a large dataset using parallel processing with OpenMP threads.

## Objective

1. Define the problem and sequential approach.
2. Implement maximum and minimum search using OpenMP.
3. Execute the program with different dataset sizes and thread counts.
4. Measure execution time, speedup, and efficiency.
5. Analyze the performance of the parallel implementation.

## Parallel Model

**OpenMP**

OpenMP is used to parallelize the search for the maximum and minimum values using multiple threads.

## Project Structure

```text
parallel_max_min/
├── README.md
├── generate_data.c
├── generate_graphs.py
├── src/
│   ├── max_min_openmp.c
│   └── max_min_sequential.c
├── data/
│   └── data.txt
├── results/
│   ├── results.txt
│   └── results.csv
└── graphs/
    ├── execution_time_vs_threads.png
    ├── execution_time_vs_dataset_size.png
    ├── threads_vs_dataset_size.png
    ├── speedup_vs_threads.png
    └── efficiency_vs_threads.png
Implementation
OpenMP Program

The OpenMP program reads the dataset and uses an OpenMP parallel loop with reduction operations to find the maximum and minimum values.

Sequential Program

A sequential version is included to provide a baseline for calculating speedup and efficiency.

Performance Analysis
Test	Dataset Size	Threads	Sequential Time (s)	Parallel Time (s)	Speedup	Efficiency
1	100,000	6	0.000243	0.001176	0.2066×	3.44%
2	100,000	8	0.000243	0.004268	0.0569×	0.71%
3	200,000	10	0.000411	0.007784	0.0528×	0.53%
4	200,000	12	0.000411	0.014891	0.0276×	0.23%
5	300,000	14	0.000804	0.012609	0.0638×	0.46%
6	400,000	16	0.000846	0.006312	0.1340×	0.84%
Performance Analysis Graphs
Execution Time vs Threads

Execution Time vs Dataset Size

Threads vs Dataset Size

Speedup vs Threads

Efficiency vs Threads

Analysis

The sequential program achieved lower execution time for all tested dataset sizes.

The OpenMP version introduced thread-management and synchronization overhead, which dominated the computation for these relatively small workloads. Consequently, the measured speedup was below 1 and efficiency remained low.

Conclusion

The experiment demonstrates the use of OpenMP threads for parallel maximum and minimum search. The results show that parallel execution does not always provide better performance for small or simple workloads because parallelization introduces additional overhead.
