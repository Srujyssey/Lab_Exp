import matplotlib.pyplot as plt

dataset_size = [100000, 100000, 200000, 200000, 300000, 400000]
threads = [6, 8, 10, 12, 14, 16]
execution_time = [0.001176, 0.004268, 0.007784, 0.014891, 0.012609, 0.006312]

speedup = [0.2066, 0.0569, 0.0528, 0.0276, 0.0638, 0.1340]
efficiency = [3.44, 0.71, 0.53, 0.23, 0.46, 0.84]


# Graph 1: Execution Time vs Threads
plt.figure(figsize=(8, 5))
plt.plot(threads, execution_time, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs Threads")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/execution_time_vs_threads.png", dpi=300)
plt.close()


# Graph 2: Execution Time vs Dataset Size
plt.figure(figsize=(8, 5))
plt.plot(dataset_size, execution_time, marker='o')
plt.xlabel("Dataset Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs Dataset Size")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/execution_time_vs_dataset_size.png", dpi=300)
plt.close()


# Graph 3: Threads vs Dataset Size
plt.figure(figsize=(8, 5))
plt.plot(dataset_size, threads, marker='o')
plt.xlabel("Dataset Size")
plt.ylabel("Number of Threads")
plt.title("Threads vs Dataset Size")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/threads_vs_dataset_size.png", dpi=300)
plt.close()


# Graph 4: Speedup vs Threads
plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Threads")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/speedup_vs_threads.png", dpi=300)
plt.close()


# Graph 5: Efficiency vs Threads
plt.figure(figsize=(8, 5))
plt.plot(threads, efficiency, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Efficiency (%)")
plt.title("Efficiency vs Threads")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/efficiency_vs_threads.png", dpi=300)
plt.close()


print("All graphs generated successfully!")
