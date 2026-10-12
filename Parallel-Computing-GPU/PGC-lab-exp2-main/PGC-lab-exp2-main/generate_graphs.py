import matplotlib.pyplot as plt

# Actual measured results from the experiment
threads = [1, 2, 4, 6, 16]

sequential_time = 2.829201

pthread_time = [
    3.143891,
    1.195939,
    0.591231,
    0.642620,
    0.676475
]

openmp_time = [
    2.907441,
    1.851130,
    0.895781,
    1.002151,
    0.834775
]

# ---------------------------------------------------------
# Calculate speedup
# Speedup = Sequential Time / Parallel Time
# ---------------------------------------------------------

pthread_speedup = [
    sequential_time / t for t in pthread_time
]

openmp_speedup = [
    sequential_time / t for t in openmp_time
]

# ---------------------------------------------------------
# Calculate efficiency
# Efficiency = Speedup / Number of Threads × 100
# ---------------------------------------------------------

pthread_efficiency = [
    (s / n) * 100
    for s, n in zip(pthread_speedup, threads)
]

openmp_efficiency = [
    (s / n) * 100
    for s, n in zip(openmp_speedup, threads)
]


# ---------------------------------------------------------
# FIGURE 1: Execution Time vs Number of Threads
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    threads,
    pthread_time,
    marker='o',
    linewidth=2.5,
    markersize=8,
    label='Pthreads'
)

plt.plot(
    threads,
    openmp_time,
    marker='s',
    linewidth=2.5,
    markersize=8,
    label='OpenMP'
)

plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title(
    'Figure 1 — Execution Time vs Number of Threads',
    fontsize=14,
    fontweight='bold'
)

plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig(
    'graphs/execution_time.png',
    dpi=300,
    bbox_inches='tight'
)

plt.close()


# ---------------------------------------------------------
# FIGURE 2: Speedup vs Number of Threads
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    threads,
    pthread_speedup,
    marker='o',
    linewidth=2.5,
    markersize=8,
    label='Pthreads'
)

plt.plot(
    threads,
    openmp_speedup,
    marker='s',
    linewidth=2.5,
    markersize=8,
    label='OpenMP'
)

plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Speedup (×)', fontsize=12)
plt.title(
    'Figure 2 — Speedup vs Number of Threads',
    fontsize=14,
    fontweight='bold'
)

plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig(
    'graphs/speedup.png',
    dpi=300,
    bbox_inches='tight'
)

plt.close()


# ---------------------------------------------------------
# FIGURE 3: Efficiency vs Number of Threads
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    threads,
    pthread_efficiency,
    marker='o',
    linewidth=2.5,
    markersize=8,
    label='Pthreads'
)

plt.plot(
    threads,
    openmp_efficiency,
    marker='s',
    linewidth=2.5,
    markersize=8,
    label='OpenMP'
)

plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Efficiency (%)', fontsize=12)
plt.title(
    'Figure 3 — Efficiency vs Number of Threads',
    fontsize=14,
    fontweight='bold'
)

plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=11)
plt.tight_layout()

plt.savefig(
    'graphs/efficiency.png',
    dpi=300,
    bbox_inches='tight'
)

plt.close()

# ---------------------------------------------------------
# FIGURE 4: Pthreads vs OpenMP Execution Time Comparison
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    threads,
    pthread_time,
    marker='o',
    linewidth=2.5,
    markersize=8,
    label='Pthreads'
)

plt.plot(
    threads,
    openmp_time,
    marker='s',
    linewidth=2.5,
    markersize=8,
    label='OpenMP'
)

plt.xlabel('Number of Threads', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)

plt.title(
    'Pthreads vs OpenMP Execution Time Comparison',
    fontsize=14,
    fontweight='bold'
)

plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=11)

plt.tight_layout()

plt.savefig(
    'graphs/pthread_vs_openmp.png',
    dpi=300,
    bbox_inches='tight'
)

plt.close()
# ---------------------------------------------------------
# Print calculated values
# ---------------------------------------------------------

print("\nPERFORMANCE ANALYSIS")
print("=" * 70)

print("\nThreads | Pthreads Time | OpenMP Time")
print("-" * 45)

for i in range(len(threads)):
    print(
        f"{threads[i]:7} | "
        f"{pthread_time[i]:13.6f} | "
        f"{openmp_time[i]:11.6f}"
    )

print("\nSpeedup")
print("-" * 45)

for i in range(len(threads)):
    print(
        f"{threads[i]:2} threads | "
        f"Pthreads = {pthread_speedup[i]:.3f}x | "
        f"OpenMP = {openmp_speedup[i]:.3f}x"
    )

print("\nEfficiency")
print("-" * 45)

for i in range(len(threads)):
    print(
        f"{threads[i]:2} threads | "
        f"Pthreads = {pthread_efficiency[i]:.2f}% | "
        f"OpenMP = {openmp_efficiency[i]:.2f}%"
    )

print("\nGraphs generated successfully:")
print("graphs/execution_time.png")
print("graphs/speedup.png")
print("graphs/efficiency.png")
print("graphs/pthread_vs_openmp.png")
