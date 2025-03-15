# Causal Ordering Algorithms in Distributed Systems

## Overview
This repository contains Python implementations of three causal ordering algorithms:

1. **BSS Algorithm (Birman-Schiper-Stephenson)** - Uses vector clocks to ensure causal ordering.
2. **SES Algorithm (Schwarz & Mattern)** - Uses interval timestamps to manage dependencies.
3. **Matrix Clock Algorithm** - Uses a matrix of logical clocks to track causal relationships.

Each algorithm enforces causal message ordering in a simulated distributed system.

---
## Installation
Ensure you have Python 3 installed.

```bash
python3 --version
```

Clone this repository:
```bash
git clone https://github.com/your-repo/causal-ordering.git
cd causal-ordering
```

---
## Usage
### 1. Run BSS Algorithm
```bash
python3 bss_causal_order.py
```
**Expected Output:**
```
Process 0 sent message to Process 1 with clock [1, 0, 0]
Process 1 received message from Process 0, updated clock: [1, 1, 0]
Process 1 sent message to Process 2 with clock [1, 2, 0]
Process 2 received message from Process 1, updated clock: [1, 2, 1]
```

### 2. Run SES Algorithm
```bash
python3 ses_causal_order.py
```
**Expected Output:**
```
Process 0 sent message to Process 1 with interval [0,5]
Process 1 received message from Process 0, updated interval: [5,10]
Process 1 sent message to Process 2 with interval [5,10]
```

### 3. Run Matrix Clock Algorithm
```bash
python3 matrix_clock.py
```
**Expected Output:**
```
Process 0 sent message to Process 1 with matrix clock [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
Process 1 received message from Process 0, updated matrix clock: [[1, 0, 0], [1, 1, 0], [0, 0, 0]]
```

---
## Contributors
- **Your Name** (your.email@example.com)

## License
MIT License

