# (```markdown
# Minimmit Consensus Simulator

**Independent validation of the Minimmit 2025 consensus protocol**

*Author: Sarah Hanania*  
*Lawrence Technological University*  
*Topics in CS: Distributed Consensus and Blockchain*

---

## 📌 Overview

This project implements and evaluates **Minimmit**, a 2025 Byzantine fault-tolerant consensus protocol that achieves ultra-low latency through a novel dual-threshold design:

- **40% agreement** for view changes (leader election) → fast progression
- **80% agreement** for transaction finalization → safety preserved

**Key Results (50 nodes, 10 AWS regions):**
- Minimmit: **323.5ms** total latency
- 23% faster than Simplex (3-round protocol)
- 11% faster than Kudzu (2-round protocol)
- Tolerates up to **20% Byzantine faults**

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `demo.py` | Main Flask web dashboard (frontend + backend) |
| `requirements.txt` | Python dependencies |
| `restore_demo.py` | One-click restore script for Google Colab |

---

## 🚀 Running the Full Demo

The complete Rust simulator (commonware-estimator) with all protocols is available in my Google Colab environment.

### Option 1: Restore from Backup (Fastest)

Run this single cell in Google Colab:

```python
from google.colab import drive
drive.mount('/content/drive')
!cp /content/drive/MyDrive/restore_demo.py /content/restore_demo.py
%run /content/restore_demo.py
```

Then click the **Port 5000** link that appears.

### Option 2: Run from Scratch

1. Install Rust:
```bash
!curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

2. Clone the commonware monorepo:
```bash
!git clone https://github.com/commonwarexyz/monorepo.git
```

3. Install Python dependencies:
```bash
!pip install flask flask-ngrok
```

4. Run the demo:
```python
!python demo.py
```

---

## 🔧 Running the Rust Simulator

The Rust simulator (commonware-estimator) is not included in this repository due to its size (588MB compressed).

**To run the full demo with the Rust backend:**

1. Clone the commonware monorepo:
   ```bash
   git clone https://github.com/commonwarexyz/monorepo.git
   ```

2. Follow the setup instructions in my paper or Colab notebook

3. Or use the Colab restore script above to load my pre-configured environment

**Alternative:** The Rust simulator can be run directly from the command line:

```bash
cd monorepo
cargo run --package commonware-estimator -- examples/estimator/minimmit.lazy --distribution us-east-1:8,eu-west-1:7,ap-northeast-1:5,sa-east-1:5
```

---

## 📊 Results Summary

| Protocol      | Notarize/Prepare  | Finalize  | Total       | vs Minimmit |
|----------     |------------------ |---------- |-------      |-------------|
| **Minimmit**  | 114.4ms           | 209.1ms   | **323.5ms** | —           |
| Kudzu         | 158.2ms           | 205.6ms   | 363.9ms     | 11% slower    
| Simplex       | 176.3ms           | 244.0ms   | 420.3ms     | **23% slower** 

### Scaling Results (10 → 100 nodes)

| Nodes | Minimmit | Simplex | Improvement |
|-------|----------|---------|-------------|
| 10    | ~65ms    | ~84ms   | 23%          
| 25    | ~162ms   | ~210ms  | 23% 
| 50    | 323.5ms  | 420.3ms | 23% 
| 100   | ~647ms   | ~841ms  | 23% 

### Fault Tolerance

| Scenario                  | Fault Type  | Latency   | Status |
|----------                 |------------ |---------  |--------|
| Baseline                  | None        | 35ms      | ✅     |
| Byzantine (10%)           | Equivocation| 100-104ms | ✅     |
| Byzantine (10%)           | Silent Node | 126-132ms | ✅     |
| Multiple Byzantine (20%)  | Mixed       | 148-152ms | ✅     |
| Leader Failure            | View Change | 70-150ms  | ✅     |

### View Change Recovery

| Phase                   | Time       |
|-------                  |------      |
| Fault Detection         | 50ms       |
| View Change (40% votes) | 15ms       |
| New Leader Proposes     | 5ms        |
| Finalize (80% votes)    | 40ms       |
| **Total Recovery**      | **~145ms** |

---

## 🛠️ Technologies Used

| Layer               | Technology 
|-------              |------------
| Consensus Simulator | Rust + commonware-estimator 
| Backend API         | Python Flask 
| Frontend            | HTML/CSS/JavaScript + Chart.js 
| Deployment          | Google Colab + ngrok 

---

## 📂 File Structure

```
/
├── demo.py                 # Main Flask web dashboard
├── requirements.txt        # Python dependencies
├── restore_demo.py         # Colab restore script
└── README.md               # This file
```

---

## 📧 Contact

Sarah Hanania  
Lawrence Technological University  

**Live Demo:** Available when running in Colab  
**Colab Notebook:** N/A

---

## 📚 Citation

If you use this work, please cite:

```
Hanania, S. (2025). Implementing and Evaluating the Minimmit Protocol: 
A Simulation-Based Validation of a 2025 Consensus Algorithm. 
Lawrence Technological University.
```

Based on the original Minimmit paper:

```
Chou, B.K., Lewis-Pye, A., & O'Grady, P. (2025). 
Minimmit: Fast Finality with Even Faster Blocks. 
arXiv:2508.10862 [cs.DC].
```

---

## 📄 License

This project is open-source for educational and research purposes.
```)
