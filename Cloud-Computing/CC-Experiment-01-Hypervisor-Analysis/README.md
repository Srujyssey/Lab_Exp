# EXP-01 — Hypervisor Performance Analysis

> **Type-1 vs Type-2 Hypervisor Performance Analysis using Proxmox VE and VMware Workstation**

[![Proxmox VE](https://img.shields.io/badge/Type--1-Proxmox%20VE-orange)](https://www.proxmox.com/en/proxmox-virtual-environment)
[![VMware Workstation](https://img.shields.io/badge/Type--2-VMware%20Workstation-blue)](https://www.vmware.com/products/desktop-hypervisor/workstation-pro.html)
[![Ubuntu](https://img.shields.io/badge/Guest%20OS-Ubuntu-E95420)](https://ubuntu.com/)
[![Sysbench](https://img.shields.io/badge/Benchmark-Sysbench-green)](https://github.com/akopytov/sysbench)
[![Virtualization](https://img.shields.io/badge/Topic-Virtualization-purple)](#problem-statement)
[![VM Configuration](https://img.shields.io/badge/VM-2%20vCPU%20%7C%202GB%20RAM%20%7C%2020GB%20Disk-red)](#configuration)

---

## Problem Statement

This experiment analyzes the CPU performance of virtual machines running on two different hypervisor architectures:

- **Type-1 Hypervisor — Proxmox VE**
- **Type-2 Hypervisor — VMware Workstation**

Ubuntu is used as the guest operating system in both environments. Both virtual machines use an equivalent basic hardware configuration, and the same Sysbench CPU benchmark is used to provide a consistent basis for performance analysis.

---

## Objective

1. Understand the difference between Type-1 and Type-2 hypervisors.
2. Create and configure an Ubuntu virtual machine using Proxmox VE.
3. Create and configure an Ubuntu virtual machine using VMware Workstation.
4. Execute the same CPU benchmark in both environments and record the results.
5. Compare the measured performance using execution time, throughput, and latency.

---

# PART A — TYPE-1 HYPERVISOR: PROXMOX VE

## Configuration

| Parameter | Value |
|---|---|
| Hypervisor | Proxmox VE |
| Hypervisor Type | Type-1 |
| Guest OS | Ubuntu |
| CPU | `2 vCPU` |
| Memory | `2 GB RAM` |
| Disk | `20 GB` |
| Benchmark | Sysbench CPU |

---

## Architecture

Proxmox VE is used as the **Type-1 hypervisor**.

A Type-1 hypervisor operates directly on the physical infrastructure and provides virtualized hardware resources to the guest virtual machine.

    Physical Hardware
           |
           v
       Proxmox VE
        Type-1
           |
           v
       Ubuntu VM
           |
           v
        Sysbench
           |
           v
     Benchmark Results

---

## Execution Steps

### Step 1 — Open Proxmox VE

Open the Proxmox VE interface and access the virtualization environment.

### Step 2 — Create the Ubuntu Virtual Machine

Create a new Ubuntu virtual machine in Proxmox VE.

### Step 3 — Configure the Virtual Machine

Configure the VM with:

- `2 vCPU`
- `2 GB RAM`
- `20 GB Disk`

### Step 4 — Start the Virtual Machine

Start the Ubuntu VM and open the guest operating system console.

### Step 5 — Verify CPU Configuration

Check the processor configuration:

    lscpu

### Step 6 — Verify Memory Configuration

Check the available memory:

    free -h

### Step 7 — Run the Sysbench Benchmark

Execute the CPU benchmark:

    sysbench cpu --cpu-max-prime=20000 run

### Step 8 — Monitor Resource Utilization

Monitor the virtual machine resources during execution:

    top

Observe the CPU and memory utilization while the benchmark is running.

### Step 9 — Record the Benchmark Output

Record the following values:

- Total execution time
- Total events
- Events per second
- Minimum latency
- Average latency
- Maximum latency
- 95th percentile latency
- Latency sum

### Step 10 — Capture Experimental Evidence

Capture screenshots showing:

- Proxmox dashboard
- VM configuration
- VM running state
- Ubuntu console
- System configuration
- Sysbench output
- Resource monitoring

---

## Results

The recorded Proxmox VE Sysbench results are:

| Metric | Proxmox VE |
|---|---:|
| Sysbench Version | `1.0.20` |
| Number of Threads | `1` |
| Prime Number Limit | `20,000` |
| Total Execution Time | `10.0004 s` |
| Total Events | `17,257` |
| Events per Second | `1,725.49` |
| Minimum Latency | `0.57 ms` |
| Average Latency | `0.58 ms` |
| Maximum Latency | `1.68 ms` |
| 95th Percentile Latency | `0.62 ms` |
| Latency Sum | `9997.48 ms` |

### Proxmox Result Summary

    Sysbench Version       : 1.0.20
    Threads                : 1
    Prime Number Limit     : 20000
    Total Execution Time   : 10.0004 s
    Total Events           : 17257
    Events per Second      : 1725.49
    Minimum Latency        : 0.57 ms
    Average Latency        : 0.58 ms
    Maximum Latency        : 1.68 ms
    95th Percentile        : 0.62 ms
    Latency Sum            : 9997.48 ms

---

## Proxmox Evidence

| Screenshot | Evidence |
|---|---|
| ![Proxmox Dashboard](screenshots/type1-proxmox/01-proxmox-dashboard.png) | Proxmox VE Dashboard |
| ![Proxmox VM Configuration](screenshots/type1-proxmox/02-proxmox-vm-configuration.png) | VM Configuration |
| ![Proxmox VM Running](screenshots/type1-proxmox/03-proxmox-vm-running.png) | Running VM |
| ![Ubuntu Console](screenshots/type1-proxmox/04-proxmox-ubuntu-console.png) | Ubuntu Console |
| ![System Configuration](screenshots/type1-proxmox/05-proxmox-sys-configuration%281%29.png) | System Configuration |
| ![Sysbench Result](screenshots/type1-proxmox/06-proxmox-sys-configuration%282%29.png) | Sysbench Result |
| ![Resource Monitoring](screenshots/type1-proxmox/07-proxmox-resource-monitoring.png) | Resource Monitoring |

---

# PART B — TYPE-2 HYPERVISOR: VMWARE WORKSTATION

## Configuration

| Parameter | Value |
|---|---|
| Hypervisor | VMware Workstation |
| Hypervisor Type | Type-2 |
| Guest OS | Ubuntu |
| CPU | `2 vCPU` |
| Memory | `2 GB RAM` |
| Disk | `20 GB` |
| Network | NAT |
| Benchmark | Sysbench CPU |

---

## Architecture

VMware Workstation is used as the **Type-2 hypervisor**.

A Type-2 hypervisor operates on top of a host operating system and provides virtualization services to the guest virtual machine.

    Physical Hardware
           |
           v
    Host Operating System
           |
           v
    VMware Workstation
          Type-2
           |
           v
       Ubuntu VM
           |
           v
        Sysbench
           |
           v
     Benchmark Results

---

## Execution Steps

### Step 1 — Open VMware Workstation

Open VMware Workstation on the host system.

### Step 2 — Create the Ubuntu Virtual Machine

Create a new Ubuntu virtual machine in VMware Workstation.

### Step 3 — Configure the Virtual Machine

Configure the VM with:

- `2 vCPU`
- `2 GB RAM`
- `20 GB Disk`
- `NAT` Network

### Step 4 — Start the Virtual Machine

Start the Ubuntu VM and open the guest operating system terminal.

### Step 5 — Verify CPU Configuration

Check the processor configuration:

    lscpu

### Step 6 — Verify Memory Configuration

Check the available memory:

    free -h

### Step 7 — Run the Sysbench Benchmark

Execute the same CPU benchmark:

    sysbench cpu --cpu-max-prime=20000 run

### Step 8 — Monitor Resource Utilization

Monitor the virtual machine resources during execution:

    top

Observe the CPU and memory utilization while the benchmark is running.

### Step 9 — Record the Benchmark Output

Record the following values:

- Total execution time
- Total events
- Events per second
- Minimum latency
- Average latency
- Maximum latency
- 95th percentile latency
- Latency sum

### Step 10 — Capture Experimental Evidence

Capture screenshots showing:

- VM configuration
- VM running state
- System configuration
- Sysbench benchmark output

---

## Results

The recorded VMware Workstation Sysbench results are:

| Metric | VMware Workstation |
|---|---:|
| Sysbench Version | `1.0.20` |
| Number of Threads | `1` |
| Prime Number Limit | `20,000` |
| Total Execution Time | `10.0006 s` |
| Total Events | `24,366` |
| Events per Second | `2,436.05` |
| Minimum Latency | `0.40 ms` |
| Average Latency | `0.41 ms` |
| Maximum Latency | `4.39 ms` |
| 95th Percentile Latency | `0.42 ms` |
| Latency Sum | `9992.75 ms` |

### VMware Result Summary

    Sysbench Version       : 1.0.20
    Threads                : 1
    Prime Number Limit     : 20000
    Total Execution Time   : 10.0006 s
    Total Events           : 24366
    Events per Second      : 2436.05
    Minimum Latency        : 0.40 ms
    Average Latency        : 0.41 ms
    Maximum Latency        : 4.39 ms
    95th Percentile        : 0.42 ms
    Latency Sum            : 9992.75 ms

---

## VMware Evidence

| Screenshot | Evidence |
|---|---|
| ![VMware VM Configuration](screenshots/type2-vmware/01-vmware-vm-configuration.png) | VM Configuration |
| ![VMware VM Running](screenshots/type2-vmware/02-vmware-vm-running.png) | Running VM |
| ![VMware System Configuration](screenshots/type2-vmware/03-vmware-system-configuration.png) | System Configuration |
| ![VMware Sysbench Result](screenshots/type2-vmware/04-vmware-sysbench-result.png) | Sysbench Result |

---

# PERFORMANCE COMPARISON

The same benchmark workload is executed in both environments:

    sysbench cpu --cpu-max-prime=20000 run

## Performance Comparison Table

| Performance Metric | Proxmox VE — Type-1 | VMware Workstation — Type-2 |
|---|---:|---:|
| Guest OS | Ubuntu | Ubuntu |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 2 GB |
| Disk | 20 GB | 20 GB |
| Sysbench Version | `1.0.20` | `1.0.20` |
| Number of Threads | `1` | `1` |
| Prime Number Limit | `20,000` | `20,000` |
| Total Execution Time | `10.0004 s` | `10.0006 s` |
| Total Events | `17,257` | `24,366` |
| Events per Second | `1,725.49` | `2,436.05` |
| Minimum Latency | `0.57 ms` | `0.40 ms` |
| Average Latency | `0.58 ms` | `0.41 ms` |
| Maximum Latency | `1.68 ms` | `4.39 ms` |
| 95th Percentile Latency | `0.62 ms` | `0.42 ms` |
| Latency Sum | `9997.48 ms` | `9992.75 ms` |

---

## Performance Observation

### Throughput

| Hypervisor | Events per Second |
|---|---:|
| Proxmox VE — Type-1 | `1,725.49` |
| VMware Workstation — Type-2 | `2,436.05` |

### Average Latency

| Hypervisor | Average Latency |
|---|---:|
| Proxmox VE — Type-1 | `0.58 ms` |
| VMware Workstation — Type-2 | `0.41 ms` |

### Execution Time

| Hypervisor | Execution Time |
|---|---:|
| Proxmox VE — Type-1 | `10.0004 s` |
| VMware Workstation — Type-2 | `10.0006 s` |

The measured execution times are very close in this benchmark run. The recorded throughput and latency values are used as the measured basis for the performance comparison.

---

# PERFORMANCE GRAPH

## Sysbench CPU Throughput Comparison


![Sysbench CPU Throughput Comparison](https://raw.githubusercontent.com/Srujyssey/Lab_Exp/main/Cloud-Computing/CC-Experiment-01-Hypervisor-Analysis/results/performance-analysis-throughput.png)

The graph represents the recorded **events per second** from the Sysbench CPU benchmark.

---

# EXPERIMENT WORKFLOW

    Hypervisor Performance Analysis
                 |
        +--------+--------+
        |                 |
        v                 v
    Proxmox VE      VMware Workstation
      Type-1              Type-2
        |                   |
        v                   v
     Ubuntu VM           Ubuntu VM
        |                   |
        v                   v
  Configure VM        Configure VM
        |                   |
        v                   v
  Verify System       Verify System
        |                   |
        v                   v
     Sysbench            Sysbench
        |                   |
        v                   v
 Monitor Resources   Monitor Resources
        |                   |
        +--------+----------+
                 |
                 v
       Record Benchmark Data
                 |
                 v
        Performance Analysis
                 |
                 v
             Comparison

---

# CONCLUSION

This experiment demonstrates the practical performance analysis of virtual machines running on **Proxmox VE (Type-1)** and **VMware Workstation (Type-2)**.

Equivalent Ubuntu virtual machines were configured with the intended same CPU, memory, and disk resources. The same Sysbench CPU workload was executed in both environments, and the resulting execution time, throughput, and latency values were recorded.

## Conclusion Table

| Metric | Proxmox VE — Type-1 | VMware Workstation — Type-2 |
|---|---:|---:|
| Hypervisor Type | Type-1 | Type-2 |
| Guest OS | Ubuntu | Ubuntu |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 2 GB |
| Disk | 20 GB | 20 GB |
| Execution Time | `10.0004 s` | `10.0006 s` |
| Total Events | `17,257` | `24,366` |
| Events per Second | `1,725.49` | `2,436.05` |
| Average Latency | `0.58 ms` | `0.41 ms` |
| Maximum Latency | `1.68 ms` | `4.39 ms` |
| 95th Percentile Latency | `0.62 ms` | `0.42 ms` |

The recorded benchmark values provide the practical basis for comparing CPU performance across the two virtualization environments.

---

# TOOLS & TECHNOLOGIES

| Category | Technology |
|---|---|
| Type-1 Hypervisor | Proxmox VE |
| Type-2 Hypervisor | VMware Workstation |
| Guest Operating System | Ubuntu |
| Benchmark Tool | Sysbench |
| CPU Analysis | `lscpu` |
| Memory Analysis | `free -h` |
| Resource Monitoring | `top` |
| Version Control | Git |
| Repository | GitHub |

---

# REPOSITORY STRUCTURE

    CC-Experiment-01-Hypervisor-Analysis/
    │
    ├── README.md
    │
    ├── results/
    │   ├── performance-analysis.md
    │   └── performance-analysis-throughput.png
    │
    └── screenshots/
        │
        ├── type1-proxmox/
        │   ├── 01-proxmox-dashboard.png
        │   ├── 02-proxmox-vm-configuration.png
        │   ├── 03-proxmox-vm-running.png
        │   ├── 04-proxmox-ubuntu-console.png
        │   ├── 05-proxmox-sys-configuration(1).png
        │   ├── 06-proxmox-sys-configuration(2).png
        │   └── 07-proxmox-resource-monitoring.png
        │
        └── type2-vmware/
            ├── 01-vmware-vm-configuration.png
            ├── 02-vmware-vm-running.png
            ├── 03-vmware-system-configuration.png
            └── 04-vmware-sysbench-result.png

---

**AUTHOR**

# Srujana Patil
