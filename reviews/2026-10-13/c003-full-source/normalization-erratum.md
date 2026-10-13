# 完整 Weil 无穷位 multiplier 的因子2纠正

2026-10-13。核对对象为实际 `w_real`、原论文v1 (3.8)、(3.19)、(4.4)，
及旧016/017/023和`qw_matrix.py`的scalar helper；不是全部历史成果重审。
[一级来源](https://arxiv.org/html/2511.22755v1#S3)的完整型使用 `2θ′(t)`。
换成单位Fourier变换，仍是同一个 `2θ′`，不能因dt/(2π)消失而少一因子。

## 精确区别

令 `θ(t)=−(t/2)logπ+Im logΓ(1/4+it/2)`。
旧023式(29)及代码 `dirichlet_archimedean_multiplier(t,0,1)` 是

    K_half(t)=θ′(t)=0.5 Re ψ(1/4+it/2)−0.5 logπ.

其函数不等式、最低点t=0的digamma证明本身正确。
但实际原核 `−w_real` 的全线multiplier是

    K_actual(t)=2θ′(t)=Re ψ(1/4+it/2)−logπ,
    m_actual=−γ−π/2−3log2−logπ=2m_half.

也可不依赖原文multiplier命名，从实际正核
`ρ(a)=Σexp(−(2j+1/2)a)` 得

    K_actual(t)−K_actual(0)
      =2∫_0^∞ρ(a)(1−cos(ta))da
      =2Σ_j t²/[t_j(t_j²+t²)].

与digamma差分直接相等。旧half函数的差只有右边的一半。
高频首项实际是log|t|，不是0.5log|t|。
旧023的quadratic constant `ζ(3,1/4)/8` 是half函数；实际constant为 `/4`。

## 哪些不受影响，哪些须重新支付

- 原冻结C001调用的`q_nm,w02,w_real,w_primes,qw_entry`与原文实空间一致，
  没有使用half scalar helper。527/528及本轮连续交叉核按实际ρ推导，因而不需改算。
- `build_polarization_defect_matrices`用actual `−w_real`但默认shift为`m_half`。
  `Q=P−V`的代数消去仍成立；然而“arch−shift是已知非负块”的来源理由错误。
  `m_half`不再是actual全线的谱底，不能免费消费该块或其相对completion为正。
  尚未重新审每个固定有限matrix在加入graph/pole后的最终惯性，不能反过来声称它们全部负。
- 016/017符号恒等式在使用actual K和actual m时仍成立；
  016的degree范数线性损失不依赖这个因子，指定no-go仍保留。
  023的abstract minmax及所证half digamma命题保留其范围，
  把它们消费到完整actual form须改正shift/threshold/constants并另作预算审查。
- 本轮不重写旧数值报告、不冒称已重跑所有下游或给新的RH结论。
  原冻结shared source文件及函数字节保持，避免无声消耗旧哈希。
  此helper当前只可按half约定解释；未来实际预算入口必须显式使用actual归一化。

## 恢复与消费规则

当前C003精确半群边界使用实空间实际ρ和极点，不使用这些half helpers。
旧Hodge正块若重新进入主合同，先冻结一个明确的actual入口、保留旧版本，
以actual m重建来源，并审其全域非负性及新旧费用；不能单改数字便宣告历史预算通过。
本纠错不缩小完整Weil正性的数学瓶颈，但降低了错误消费既有“正输入”的风险。
