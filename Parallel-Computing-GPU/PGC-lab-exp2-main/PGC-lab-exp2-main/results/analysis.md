# Performance Analysis

## 1. Experimental Setup

The performance experiment compares a sequential implementation with parallel implementations using Pthreads and OpenMP.

The sequential execution time measured during the experiment was:

**Sequential Time = 2.829201 seconds**

Both parallel implementations were executed using 1, 2, 4, 6, and 16 threads.

The same computation was performed in each implementation, and the execution time was recorded for comparison.

---

## 2. Performance Results

| Threads | Pthreads Time (s) | OpenMP Time (s) | Pthreads Speedup | OpenMP Speedup | Pthreads Efficiency | OpenMP Efficiency |
|--------:|------------------:|----------------:|-----------------:|---------------:|--------------------:|------------------:|
| 1 | 3.143891 | 2.907441 | 0.900× | 0.973× | 89.99% | 97.31% |
| 2 | 1.195939 | 1.851130 | 2.366× | 1.528× | 118.28% | 76.42% |
| 4 | 0.591231 | 0.895781 | 4.785× | 3.158× | 119.63% | 78.96% |
| 6 | 0.642620 | 1.002151 | 4.403× | 2.823× | 73.38% | 47.05% |
| 16 | 0.676475 | 0.834775 | 4.182× | 3.389× | 26.14% | 21.18% |

---

## 3. Speedup

Speedup is calculated using:

**Speedup = Sequential Execution Time / Parallel Execution Time**

The measured sequential execution time was **2.829201 seconds**.

### Pthreads

The highest measured Pthreads speedup was **4.785× with 4 threads**.

The speedup increased from 1 thread to 4 threads, but decreased when the number of threads was increased further.

### OpenMP

The highest measured OpenMP speedup was **3.389× with 16 threads**.

OpenMP showed improvement compared with the sequential execution, although the improvement was not proportional to the increase in the number of threads.

---

## 4. Efficiency

Efficiency is calculated using:

**Efficiency = (Speedup / Number of Threads) × 100**

The efficiency decreases at higher thread counts because the additional threads do not provide proportional performance improvement.

For Pthreads, the best measured execution time was obtained using **4 threads**.

For OpenMP, the lowest measured execution time was obtained using **16 threads** among the tested configurations.

The calculated efficiencies above 100% for Pthreads at 2 and 4 threads result from comparing the parallel measurements with the measured sequential baseline. These values reflect the benchmark measurements and should not be interpreted as more than 100% processor efficiency.

---

## 5. Execution Time Analysis

### Pthreads

The measured Pthreads execution times were:

- 1 thread: **3.143891 s**
- 2 threads: **1.195939 s**
- 4 threads: **0.591231 s**
- 6 threads: **0.642620 s**
- 16 threads: **0.676475 s**

The execution time improved significantly up to 4 threads. After 4 threads, increasing the thread count did not improve the execution time. In fact, the execution time increased slightly for 6 and 16 threads.

### OpenMP

The measured OpenMP execution times were:

- 1 thread: **2.907441 s**
- 2 threads: **1.851130 s**
- 4 threads: **0.895781 s**
- 6 threads: **1.002151 s**
- 16 threads: **0.834775 s**

The lowest OpenMP execution time among the tested configurations was obtained with 16 threads.

---

## 6. Pthreads vs OpenMP

For this particular workload and experimental environment, Pthreads produced a lower execution time than OpenMP at all tested thread counts.

| Threads | Faster Implementation |
|--------:|------------------------|
| 1 | OpenMP |
| 2 | Pthreads |
| 4 | Pthreads |
| 6 | Pthreads |
| 16 | Pthreads |

The comparison shows that performance depends on the workload, implementation, number of threads, and execution environment. Therefore, the results should be considered specific to this experiment rather than a universal comparison between Pthreads and OpenMP.

---

## 7. Effect of Increasing Threads

Increasing the number of threads does not always result in proportional performance improvement.

The measured results show that:

- Parallel execution improves performance compared with the sequential implementation.
- Pthreads achieved its best measured execution time at 4 threads.
- OpenMP achieved its best measured execution time at 16 threads.
- Increasing the number of threads beyond the most effective configuration can introduce additional overhead.
- Thread creation and management, scheduling, synchronization, memory access, operating-system activity, and the non-parallel portion of a program can limit the achievable speedup.

Therefore, the optimal number of threads depends on the workload and system.

---

## 8. Overall Observation

The experiment demonstrates the effect of parallelism on execution time and shows that increasing the number of threads does not automatically produce proportional speedup.

For the measured workload:

- **Sequential execution:** 2.829201 s
- **Best Pthreads execution:** 0.591231 s with 4 threads
- **Best OpenMP execution:** 0.834775 s with 16 threads
- **Best measured speedup:** 4.785× using Pthreads with 4 threads

The experiment therefore demonstrates the importance of selecting an appropriate thread count and considering parallelization overhead when evaluating parallel programs.
