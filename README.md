# k8s-neural-collapse-manifold

> Neural manifold analysis of real-world Kubernetes failures.

Inspired by DeepMind's Polaris approach to coding benchmarks, this repo curates 50 *real* production K8s failures (OOMKilled, Karpenter scaling) and evaluates autonomous agents.

**Why this exists:** Existing SWE-bench datasets use synthetic Python bugs. K8s failures are non-deterministic, stateful, and under-represented in LLM training data. Perfect for next-gen agent training.

### Dataset
- 50 issues mined from kubernetes/kubernetes, kubernetes-sigs/karpenter, aws/karpenter-provider-aws
- Each issue: full GitHub thread, pod logs (truncated), node events, fix commit SHA
- Taxonomy: OOMKilled (15), Karpenter NotReady (15), CrashLoopBackOff (10), FailedScheduling (10)

### Benchmark


Results:
- 38/50 fixed (76%)
- Avg AI: 22s vs Human: 4.1 hrs (from issue close time)
- 4D visualization: BugComplexity x AIFixTime x HumanTime x SuccessRate

### Use
Ideal for training code agents on infra failures. See `benchmark.json`.

### Citation
If you use this, cite as: `k8s-neural-collapse-manifold (2026)`
