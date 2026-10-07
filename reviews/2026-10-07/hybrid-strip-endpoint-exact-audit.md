# 438–441 精确有限代数审计

2026-10-07。运行 scripts/hybrid_strip_endpoint_exact_audit.py，通过。

861 个有理端点参数，165 个 clipped-low 参数，36 个局部 Euler 模型及 5 个抽象正谱模型；全部使用 Fraction。端点恒等式、候选余量和闭式模型分别核对。

另有1000个retained反射dyad模型，其中276个empty-slot模型，核Td/H恒等式与row loss。

nominal endpoint margin = 307/11016000；candidate boundary = 69999/80000。

这些是有限模型检查。连续域有理下界的证明见439，Euler无限乘积见440；实际AF/Lamzouri算子分析见438及独立报告。没有重跑外部Lean，也没有证明新比例或新无零区。

机器数据及正文绑定哈希见 output/hybrid-strip-endpoint-exact-audit.json。
