# 小活跃 radical 付款的公开复现

本页补充[完整研究证明](active-radical-mixed-cross-research.md)的第7节。
原第7节指向研究作者保存的临时快照；公开运行改用下面的程序。
证明正文未改变。实际源核对、有限有理计算和无限理想计数分别记录。

[公开程序](../../scripts/hybrid_active_radical_mixed_cross_budget.py)和
[默认有限收据](../../output/hybrid-active-radical-mixed-cross-budget.json)自包含运行：

```powershell
python scripts/hybrid_active_radical_mixed_cross_budget.py --check
```

默认不读取仓库外源文件，也不写文件。1349项有限检查包括局部指数差、自然零、
实际系数的分解数和完整有理参数盒预算，`source_matched=false`。
实际原文需额外传入固定 TeX：

```powershell
python scripts/hybrid_active_radical_mixed_cross_budget.py --check --source <frozen-paper.tex>
```

这时另外检查源哈希和两个精确片段，共1352项，`source_matched=true`。
`--certificate` 指定被比较的有限收据；`--audit-output` 可另写新收据，
不会隐式覆盖被检查的公开输出。`-O` 明确拒绝。
本轮[实际源复验](active-radical-mixed-cross-source-check.json)由根代理重新执行，
不是把暂存作者的 PASS 字段复制为当前运行记录。

局部有限计算不证明无限理想对计数。后者依赖研究证明第4节和明列的固定数域
线性理想计数输入。完整 signed cross、count 节省、新无零边界、Lean 移植及
网站验收均未由这些检查完成。
