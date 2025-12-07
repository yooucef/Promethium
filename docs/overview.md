# Promethium Overview

## The Challenge

Seismic data acquisition is inherently constrained by logistics, economics, and environmental factors. This often results in datasets that are:
- **Incomplete**: Missing traces due to dead channels or acquisition gaps involved in obstacle avoidance.
- **Noisy**: Contaminated by ground roll, ambient noise, and acquisition artifacts.
- **Irregular**: Sampled on non-Cartesian grids, complicating wavefield analysis.

Traditional processing workflows rely heavily on manual parameter tuning and linear theory. While effective, they often struggle with highly complex noise patterns or large gaps in spatial sampling.

## The Promethium Solution

**Promethium** bridges the gap between rigourous classical geophysics and the generative power of modern Deep Learning.

### Design Philosophy

1.  **Scientific Integrity**: We prioritize physics-consistent reconstruction. Neural networks are not "black boxes" but tools constrained by the wave equation (via PINNs) or guided by domain knowledge.
2.  **Scalability**: The system is designed for terabyte-scale surveys, utilizing asynchronous task queues and efficient memory mapping.
3.  **Usability**: Advanced algorithms are accessible through a modern web interface, democratizing access to high-end recovery techniques.

## Core Capabilities

-   **Hybrid Recovery**: Users can choose between fast, classical Matrix Completion methods for simple gaps, or deep U-Net architectures for complex diffraction reconstruction.
-   **Automated Quality Control**: Every processing job generates quantitative metrics (SNR, Frequency correlation) to validate results.
-   **Production Ready**: Built on standard industry formats (SEG-Y) and modern software stacks (Docker, FastAPI, React), Promethium fits into existing infrastructure seamlessly.
