# 多点谱包络的固定来源与独立核读

2026-10-08。作者：root。基线 main 5b4c99e561ddec59f1818b8471da508036503745。

本稿是本轮实际比例研究的来源核读与有限数学证明。最初直接推得的 cap m/(m−1) 已被公开更强包络覆盖；不主张新谱机制的优先权。实际 ζ 传递及七点完整执行由不同作者另报；本稿不以读代码代替成功执行。

## 1. 来源、版本及实际阅读范围

Uwe Schwarz [公开研究稿](https://github.com/uwe-schwarz/zeta-simple-zeros-673026/tree/e2453c1cafc1387ef553fe6bee74d1f5223ba801)固定提交 e2453c1cafc1387ef553fe6bee74d1f5223ba801，原始字节和 MIT 许可见[清单](artifacts/hybrid-multipoint-schwarz-e2453c1/source-manifest.json)。

| 原件 | raw SHA256 | 核读范围 |
|---|---|---|
| [paper/riemann.tex](artifacts/hybrid-multipoint-schwarz-e2453c1/paper/riemann.tex) | 6b9796f4cd3b653781cf82de4dc6e22535076514ad62107312280abdbed85a01 | 原行383–501，完整谱包络及实际 Gram 对角归一化；不认证全702行或 Lean 依赖闭包 |
| [docs/proof.md](artifacts/hybrid-multipoint-schwarz-e2453c1/docs/proof.md) | 594ec1cfc0ac0b4717bbe3a211eaa0a458b9ed318c3165bb4b5f5097fe8c0b9d | 全250行提纲；增强证书按作者声明登记 |
| [LICENSE](artifacts/hybrid-multipoint-schwarz-e2453c1/LICENSE) | 5b620cb5c067656c1174c376850723806951c00bf6e4bfccdcc348b86c367d90 | 原样保留 |

另完整读取已归档 ainta 040c5e8 PDF 全7页及本轮复制的 kernel.py、rounding.py、constants.py、verify_seven.py。local pressure 是1/3000，连续七点窗口聚合后的 pressure 是1/500；两层不能混用。公开 teal-sea bridge 仅用于发现舍入核查点，未导入其 Lean 结论或增强目标。

Schwarz 的382623/10^8证书及67.302666%不由本稿认证。本轮首先使用 ainta 原19/5000完整证书。更高公开候选继续按[305审计](../../notes/305-post-6725-literature-baseline-audit.md)的范围比较。

## 2. 原 trace cap 的独立证明 [T]

定义 Ψ(t)=(t−1)^2（0≤t≤2），Ψ(t)=2t−3（t≥2）。若 m≥2、G≥0、trG≤m，某特征值 λ=2+δ>2，则 λ≤m，剩余 m−1 个特征值平均≤(m−2−δ)/(m−1)<1。Ψ在[0,1]递减，标量 Jensen 给

\[
 \operatorname{tr}\Psi(G)
 \ge1+2\delta+(1+\delta)^2/(m-1)\ge m/(m-1).
\]

若全部特征值≤2，则 trΨ(G)=||G−I||_F²≥2Σ_{i<j}|G_ij|²。因此得到 min{m/(m−1),2Σ|G_ij|²} 下界。它要求 trG≤m；原 m-column 范数≤1 Gram 满足此条件，一般 PSD 不自动满足。

该 cap 允许原七点目标的 m270，A=627/625≤270/269，候选比例0.67300871234691693116…；下节已知完整包络给更强数值。初始 cap 不是独立新纪录。

## 3. 已知谱包络的独立数学复核 [T/R]

单位对角 m×m correlation matrix 满足 E=||G−I||_F²=Σ_{i≠j}|G_ij|²∈[0,m(m−1)]。令 J=trΨ(G)。来源的包络为

\[
 g_m(E)=
 \begin{cases}
 E,&E\le m/(m-1),\\
 E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
 \end{cases}
\]

独立检验多大特征值分支：写 λ_i=1+y_i，Σy_i=0。若全部 y_i≤1，则 J=E。否则 H={i:y_i>1}、h=|H|<m，H上写 y_i=1+u_i，q=Σu_i≥r=(Σu_i²)^(1/2)。剩余偏差和为−h−q。Cauchy 给

\[
 E\ge h+2r+r^2+\frac{(h+r)^2}{m-h}
 =\frac{m(1+r)^2}{m-1}
  +\frac{(h-1)(m+r)^2}{(m-h)(m-1)}.
\]

又 E−J=r²，因此 J≥g_m(E)，且该分支只能在 E>m/(m−1)发生。第二分支导数1/m+sqrt((m−1)/(mE))∈(0,1]；拼接连续，故 g_m递增且1-Lipschitz。矩阵 (1−a/(m−1))I+a11*/(m−1)，a=sqrt((m−1)E/m)，在第二分支取等号，证明它确为精确包络。

若 E+x≥A、x≥0，单调性和1-Lipschitz给 J+x≥g_m(A)。这处理 Gram 谱余项，不是把原四矩 T^(5/7+ε)充当常数预算。包络的先行工作归上述 Schwarz 稿。

## 4. 实际原对象的合法比较

有限 Gabor 原列范数≤1，而保留中心零点的对角为1+o(1)。固定 m 下置 D=diag(G_ii^(-1/2))、R=DGD。R单位对角，Cauchy给 Gram entries有界，从而 ||R−G||_F=o(1)。Ψ全局2-Lipschitz及 Hoffman–Wielandt给 |trΨ(R)−trΨ(G)|≤2sqrt(m)||R−G||_F=o(1)，离对角能量亦改变o(1)。原稿行460–490完整给出了此步骤。

[304直接 Hilbert 接口](../../notes/304-mt-triple-geometry-and-second-moment-stability.md)则对固定光滑 ηδ直接产生 unit vectors，Gram 对角精确1。kδ一致趋于MT核k0；固定 m、bounded span下的有限能量差为O_m(sup|kδ−k0|)。必须先固定δ、再T→∞、最后δ→0。完整复零点相关中的非正项由真实 selfadjoint operator及惯性账本保留，不删成仅critical zeros的正和。

两条接口仍须另行保留 zero count、tail、trace和惯性输入。不同点计数不能只用一般不成立的 D≥(N+s)/2；必须从原完整 HS 预算及实际 multiplicity/inertia 关系推出。

## 5. 原七点代码的独立执行前审查

原 GRID4000、pressure denominator3000、target19/5000、cutoff45600 满足精确45600/(4000·3000)=19/5000。sum of low cell indices≥45600的整数剪枝因此正确，不依赖浮点相等。任一 gap≥45600/4000的域外也已由压力支付。

kernel.py以精确 fmpq 中心和半径构造 closed cells，并明确除以K(0)。连续 span个closed cells覆盖的 inclusive range是[sum low,sum high+span−1]，代码一致。超表长时用0作为k0²下界，或−∞作为二导数下界，均保守。

one-body删除用向下下界及向上目标比较。带符号 Hessian 对负下界选向上系数，对正下界选向下系数，再nextafter向下。浮点LDL只启发筛选，必须以精确binary64有理项重建Arb矩阵再证positive pivots，才可用tangent下界剪枝。未解决 terminal cell 抛异常；完整stack清空才生成 verified=true。

本稿代码阅读不代替真实完整运行；新报告须给实际source/table hashes及完整覆盖结果，原文件和旧证书不被覆盖。
