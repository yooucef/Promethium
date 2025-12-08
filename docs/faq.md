# Frequently Asked Questions

## General

**Q: What formats does Promethium support?**
A: Promethium natively supports SEG-Y. Support for SEG-2, SAC, and miniSEED is experimental.

**Q: Can I run Promethium without a GPU?**
A: Yes, but training deep learning models will be extremely slow. Inference can run on CPU/RAM, but GPU is recommended for production throughput.

## Technical

**Q: How does Zarr improve performance?**
A: SEG-Y is designed for tape drives (sequential access). Zarr enables efficient, parallel random access to multidimensional chunks, which matches the access pattern of patch-based ML training.

**Q: Is the Physics-Informed loss fully rigorous?**
A: The current implementation enforces the Acoustic Wave Equation via finite-difference kernels. It assumes constant density and ignores elastic effects (shear waves), which is a common simplification in seismic processing.

## Licensing

**Q: Can I use Promethium for commercial projects?**
A: Provide the current project license is proprietary, you must obtain a commercial license. Please contact the maintainers.
