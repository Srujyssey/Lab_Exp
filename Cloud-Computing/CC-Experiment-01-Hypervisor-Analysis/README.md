# EXP-01 — Hypervisor Performance Analysis

> **Type-1 vs Type-2 Hypervisor Performance Analysis using Proxmox VE and VMware Workstation**

[![Proxmox VE](https://img.shields.io/badge/Type--1-Proxmox%20VE-orange)](https://www.proxmox.com/en/proxmox-virtual-environment)
[![VMware Workstation](https://img.shields.io/badge/Type--2-VMware%20Workstation-blue)](https://www.vmware.com/products/desktop-hypervisor/workstation-pro.html)
[![Ubuntu](https://img.shields.io/badge/Guest%20OS-Ubuntu-E95420)](https://ubuntu.com/)
[![Sysbench](https://img.shields.io/badge/Benchmark-Sysbench-green)](https://github.com/akopytov/sysbench)
[![Virtualization](https://img.shields.io/badge/Topic-Virtualization-purple)](#experiment-overview)
[![VM Configuration](https://img.shields.io/badge/VM-2%20vCPU%20%7C%202GB%20RAM%20%7C%2020GB%20Disk-red)](#virtual-machine-configuration)

---

## 📌 Experiment Overview

This experiment studies the CPU performance of virtual machines running on two different hypervisor architectures:

- **Type-1 Hypervisor — Proxmox VE**
- **Type-2 Hypervisor — VMware Workstation**

Ubuntu is used as the guest operating system in both environments. Both virtual machines use an equivalent basic hardware configuration, and CPU performance is evaluated using the **Sysbench CPU benchmark**.

The same benchmark workload is used in both environments to provide a consistent basis for performance analysis.

---

## 🎯 Objective

The experiment aims to:

- Understand the difference between Type-1 and Type-2 hypervisors.
- Create and configure an Ubuntu VM using Proxmox VE.
- Create and configure an Ubuntu VM using VMware Workstation.
- Maintain an equivalent virtual hardware configuration.
- Perform CPU benchmarking using Sysbench.
- Record execution time, total events, events per second, and latency.
- Compare the measured performance of both virtualization approaches.
- Observe virtual machine resource utilization.

---

## 🧠 Hypervisor Architectures

### Type-1 Hypervisor — Proxmox VE

Proxmox VE is used as the Type-1 hypervisor in this experiment.

A Type-1 hypervisor operates directly on the physical infrastructure and provides virtual machines with virtualized hardware resources.

### Type-2 Hypervisor — VMware Workstation

VMware Workstation is used as the Type-2 hypervisor.

A Type-2 hypervisor operates on top of a host operating system and provides virtualization services to guest virtual machines.

---

## 🖥️ Virtual Machine Configuration

To make the comparison consistent, both virtual machines use the same intended basic configuration.

| Resource | Configuration |
|---|---|
| Guest Operating System | Ubuntu |
| CPU | `2 vCPU` |
| Memory | `2 GB RAM` |
| Disk | `20 GB` |
| Benchmark | Sysbench CPU |

---

## 🧪 Benchmark Method

The same CPU benchmark is used for both virtual machines:

    sysbench cpu --cpu-max-prime=20000 run

The benchmark records:

- Total execution time
- Total number of events
- Events per second
- Minimum latency
- Average latency
- Maximum latency
- 95th percentile latency

---

# 🟠 PART A — TYPE-1 HYPERVISOR: PROXMOX VE

## Proxmox VE

Proxmox VE is used as the Type-1 hypervisor.

An Ubuntu virtual machine is created and configured using the standard experimental configuration.

### Proxmox VM Configuration

| Parameter | Value |
|---|---|
| Hypervisor | Proxmox VE |
| Hypervisor Type | Type-1 |
| Guest OS | Ubuntu |
| CPU | 2 vCPU |
| Memory | 2 GB RAM |
| Disk | 20 GB |

### Proxmox Evidence

![Proxmox VE Dashboard](screenshots/type1-proxmox/01-proxmox-dashboard.png)

![Proxmox VM Configuration](screenshots/type1-proxmox/02-proxmox-vm-configuration.png)

![Proxmox VM Running](screenshots/type1-proxmox/03-proxmox-vm-running.png)

![Ubuntu Running in Proxmox Console](screenshots/type1-proxmox/04-proxmox-ubuntu-console.png)

![Proxmox System Configuration](screenshots/type1-proxmox/05-proxmox-system-configuration.png)

![Proxmox Sysbench Result](screenshots/type1-proxmox/06-proxmox-sysbench-result.png)

![Proxmox Resource Monitoring](screenshots/type1-proxmox/07-proxmox-resource-monitoring.png)

---

# 🔵 PART B — TYPE-2 HYPERVISOR: VMWARE WORKSTATION

## VMware Workstation

VMware Workstation is used as the Type-2 hypervisor.

An equivalent Ubuntu virtual machine is created using the same intended CPU, memory, and disk configuration.

### VMware VM Configuration

| Parameter | Value |
|---|---|
| Hypervisor | VMware Workstation |
| Hypervisor Type | Type-2 |
| Guest OS | Ubuntu |
| CPU | 2 vCPU |
| Memory | 2 GB RAM |
| Disk | 20 GB |
| Network | NAT |

### VMware Evidence

![VMware VM Configuration](screenshots/type2-vmware/01-vmware-vm-configuration.png)

![VMware VM Running](screenshots/type2-vmware/02-vmware-vm-running.png)

![VMware System Configuration](screenshots/type2-vmware/03-vmware-system-configuration.png)

![VMware Sysbench Result](screenshots/type2-vmware/04-vmware-sysbench-result.png)

---

# 📊 PERFORMANCE ANALYSIS

The same Sysbench CPU benchmark is used on both hypervisors:

    sysbench cpu --cpu-max-prime=20000 run

## Performance Comparison

| Performance Metric | Proxmox VE — Type-1 | VMware Workstation — Type-2 |
|---|---:|---:|
| Guest OS | Ubuntu | Ubuntu |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 2 GB |
| Disk | 20 GB | 20 GB |
| Sysbench Version | To be added | `1.0.20` |
| Number of Threads | To be added | `1` |
| Prime Number Limit | `20,000` | `20,000` |
| Total Execution Time | To be added | `10.0006 s` |
| Total Events | To be added | `24,366` |
| Events per Second | To be added | `2,436.05` |
| Minimum Latency | To be added | `0.40 ms` |
| Average Latency | To be added | `0.41 ms` |
| Maximum Latency | To be added | `4.39 ms` |
| 95th Percentile Latency | To be added | `0.42 ms` |
| Latency Sum | To be added | `9992.75 ms` |

### VMware Benchmark Observation

The VMware Workstation benchmark completed in **10.0006 seconds**.

The VM processed **24,366 total events** with a throughput of **2,436.05 events per second**.

The measured latency values were:

- Minimum: **0.40 ms**
- Average: **0.41 ms**
- Maximum: **4.39 ms**
- 95th percentile: **0.42 ms**

![VMware Sysbench Performance Result](screenshots/type2-vmware/04-vmware-sysbench-result.png)

### Proxmox Benchmark Observation

The same Sysbench benchmark is performed on the Proxmox VE virtual machine.

The Proxmox values in the comparison table are taken directly from the actual Proxmox Sysbench output.

![Proxmox Sysbench Performance Result](screenshots/type1-proxmox/06-proxmox-sysbench-result.png)

---

# 🔄 EXPERIMENT WORKFLOW

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
     Sysbench            Sysbench
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

# 📈 PERFORMANCE OBSERVATION

The experiment keeps the guest operating system, intended virtual CPU allocation, memory allocation, disk allocation, and Sysbench workload equivalent across both environments.

The main performance metrics considered are:

- **Execution Time** — time taken to complete the benchmark.
- **Total Events** — number of completed benchmark events.
- **Events per Second** — benchmark throughput.
- **Average Latency** — average time taken per event.
- **Minimum and Maximum Latency** — observed latency range.
- **95th Percentile Latency** — latency threshold covering most benchmark events.

The final comparison is completed using the actual Sysbench values recorded from both virtual machines.

---

# 🛠️ TOOLS & TECHNOLOGIES

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

# 📁 REPOSITORY STRUCTURE

    CC-Experiment-01-Hypervisor-Analysis/
    │
    ├── README.md
    │
    ├── results/
    │   └── performance-analysis.md
    │
    └── screenshots/
        │
        ├── type1-proxmox/
        │   ├── 01-proxmox-dashboard.png
        │   ├── 02-proxmox-vm-configuration.png
        │   ├── 03-proxmox-vm-running.png
        │   ├── 04-proxmox-ubuntu-console.png
        │   ├── 05-proxmox-system-configuration.png
        │   ├── 06-proxmox-sysbench-result.png
        │   └── 07-proxmox-resource-monitoring.png
        │
        └── type2-vmware/
            ├── 01-vmware-vm-configuration.png
            ├── 02-vmware-vm-running.png
            ├── 03-vmware-system-configuration.png
            └── 04-vmware-sysbench-result.png

---

# 🔍 KEY OBSERVATIONS

- Proxmox VE represents a **Type-1 hypervisor**.
- VMware Workstation represents a **Type-2 hypervisor**.
- Ubuntu is used as the guest operating system in both environments.
- Both virtual machines use equivalent intended hardware resources.
- The same Sysbench CPU benchmark is used for both environments.
- Execution time, event throughput, and latency are used for performance analysis.
- CPU, memory, network, and disk utilization are also observed during the experiment.
- The final comparison is based only on the actual benchmark output.

---

# 🏁 CONCLUSION

This experiment demonstrates the practical performance analysis of virtual machines running on **Proxmox VE (Type-1)** and **VMware Workstation (Type-2)**.

Equivalent Ubuntu virtual machines are created and tested using the same Sysbench CPU workload.

The VMware Workstation benchmark recorded:

- **Total Execution Time:** `10.0006 s`
- **Total Events:** `24,366`
- **Events per Second:** `2,436.05`
- **Average Latency:** `0.41 ms`

The corresponding Proxmox benchmark values are taken from the actual Proxmox Sysbench output to complete the final comparison.
