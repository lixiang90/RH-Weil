# Meyer径向源与谱实现：限定来源核读

2026-10-11。服务于本仓库[518](../../notes/518-f1-quantitative-mellin-division-and-mobius-source.md)、
[519](../../notes/519-f1-closed-source-image-and-degree-moments.md)、
[520](../../notes/520-f1-source-quotient-spectrum-and-centered-growth.md)。
这是定义、闭像及谱接口核对，不是该文全部证明或世界新颖性认证。

## 固定原件和阅读范围

Ralf Meyer，*A spectral interpretation for the zeros of the Riemann zeta function*，
[arXiv math/0412277v3原始PDF](https://arxiv.org/pdf/math/0412277v3)，
[本地原件](../f1/meyer-zeta-spectrum-math-0412277v3.pdf)。
15页，248788字节，SHA256：
`60be6001f5eb1e37a5d0bcb85431930b52929e90fc0d78e792ad26db9e3f2d40`。
原样保存；页码指PDF顺序页码。核读第2–8页的空间与算子定义，
重点为第5页Möbius逆及Poisson公式、第6页Theorem 3.3及证明、
第7页Theorem 4.1及证明、第8页Corollary 4.2及证明。
后续核迹、summability及几何字符计算未纳入本次数学审计。

## 原模型对应和范围

原文的偶Schwartz源具有零原点值和零积分；其ζ算子Z为正整数求和。
本项目405的源条件相同，E=2Z。原文所有实指数权的对数Schwartz交空间
与405的超指数衰减空间拓扑相同：增加一个指数权吸收任意多项式对数权，
反向由带权Schwartz上确界控制。

Theorem 3.3提供闭像及源拓扑同构；Theorem 4.1给Mellin商刻画；
Corollary 4.2识别**对偶**谱与零点代数重数。因此本轮不声称首次构造ζ谱。
518给本仓库的全重数消失后定量除法和实际Möbius重建；519核准双次数的源积分；
520在原商上明确构造连续双侧预解及Jordan函数，并限定所用谱定义。
原文的完成ζ约定与本项目整ξ约定不同，不能直接照搬其极点记号。

这一来源接口不提供正定Hilbert自伴实现、独立中心化双向增长、RH、
几何主除子或全局HH链。尤其520保留完整Jordan信息；忠实正定酉化还会迫使简单零点。

## ζ固定条带上界的另一直接原始来源

独立核读[NIST DLMF 25.2.10](https://dlmf.nist.gov/25.2#E10)的有限阶
Euler–Maclaurin公式。对任意固定条带，选择n使其最左实部大于−2n。
周期Bernoulli函数有界，余项积分绝对收敛；其系数为固定次数的s多项式。
在高处避开极点1，即给518所需的固定条带多项式上界。
只使用这条经典公式，不消费RH、新无零区域或零点间距下界。
该页面在线核读；未归档整个DLMF，也未重放其全部公式推导。

三份内部全文审查分别见
[分析](../../reviews/2026-10-11/f1-mellin-source-analysis-review.md)、
[源重建](../../reviews/2026-10-11/f1-mellin-source-source-review.md)、
[谱](../../reviews/2026-10-11/f1-mellin-source-spectrum-review.md)。
它们是内部独立审查，不是外部同行评议、Lean或区间证书。
