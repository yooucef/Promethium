# Benchmarking

Methodology for evaluating reconstruction quality and performance.

## Datasets

### Synthetic Benchmark
We generate synthetic gathers using Ricker wavelets and convolution with reflectivity series derived from well logs.
- **Scenario A**: Randomly missing traces (10% to 50%).
- **Scenario B**: Large gap (10 consecutive traces).

### Real Data
Public datasets (e.g., Stratton 3D, Viking Graben) are used for qualitative assessment.

## Metrics

### Quantitative
- **SNR (Signal-to-Noise Ratio)**: Measured in dB. Higher is better.
- **MSE (Mean Squared Error)**: L2 norm difference. Lower is better.
- **Correlation**: Pearson correlation coefficient between reconstructed and ground truth traces.

### Performance
- **Throughput**: Traces processed per second.
- **Latency**: Time to result availability after job submission.

## Reproducibility

To run benchmarks (requires local dev environment):

```bash
python -m promethium.benchmark --dataset synthetic --scenario A
```

(Note: Benchmarking script is part of the roadmap for v0.2.0)
