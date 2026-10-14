# 547 §4 canonical joint 准备恒等式短审

2026-10-14；`/root/c017_gamma_cross`，只核准备，不作新研究，不编辑 STATE/cadence/Git。
依 AGENTS 恢复 README/STATE/check/show、当前 Goal/frontier/C018/D20261014S。
现场 HEAD 3cebe129e1785eeaaff8f76b82152e1cbe334264；root 的组织/547稿处于工作树修改态。
子 get_goal=null 不代替 root active 运行态。
所读 [547](../../../notes/547-integer-core-entry-and-canonical-joint-response-gate.md) raw SHA256：
`f2679ead99d0b4bfc32627a3876562ffbb88d84388fb2ebe72b373036ebdc109`。

## 精确向量式及内积

采用内积第一变量线性，rank-one 算子 `|a〉〈b|` 作用为 f↦〈f,b〉a。
全部量是原 du=dx/x Hilbert space，N≥4 integer、M=N−1，
P 为完整 integer cells 的 weighted 均值正交投影，R=I−P。
令 a=N^−1/4 sqrt x、b=N^1/4/sqrt x、p=Pa、
U=N^1/2||Ra||²，V=N^−1/2||Rb||²、κ=〈Ra,Rb〉。
canonical a、b、p 都为实源，所以 D=〈Pa,Pb〉=log N−κ 为实数；不需换内积或共轭系数。
完整 pole operator 是 |a〉〈b|+|b〉〈a|，因而

    R Pole p = D Ra + ||p||² Rb，
    ||p||²=N^−1/2(M−U)。

对全部 strict q<N proper primepowers，T_qF(x)=F(qx) 原区间外为零。
已核 R T_q*P=0，所以 B_N=Σw_q(T_q+T_q*) 给 RB_Np=RD_N^+p。
而 T_qa=sqrt q·a·1_(x<N/q)，w_q=Λ(q)/sqrt q，故 a.e. 精确为

    D_N^+a=a ψ_<(N/x)，ψ_<(y)=Σ_(q<y)Λ(q)，
    RD_N^+p=R[a ψ_<(N/x)]−R[D_N^+Ra]。

由于 x>1，N/x<N，ψ_<(N/x) 的 q cutoff 与原 strict q<N 完全一致。
有限边界 x=N/q 仅零测集，不添加/遗漏 atom；proper powers 全保。
令 E_<(y)=ψ_<(y)−y，且 a·N/x=sqrt N·b，则

    RQp = RΓp−R[a E_<(N/x)]+R[D_N^+Ra]
          +D Ra−N^−1/2(1+U)Rb。                     (1)

最后系数正是 ||p||²−sqrt N=N^−1/2(M−U−N)，无符号或缺一常数。
Γ 仍为 actual2θ′ 的原零延拓/压到 I_L 的算子，不是 half multiplier。
fixed-N 的 p 是有限 BV step，hat p=O_N(1/|t|)，log² Fourier weight 可积；
故 p 在完整 Γ operator domain，(1) 在原 H_N 是合法向量式，也可对任意 r∈R∩Dlog 配对读作 mixed form。

## 完整 carry 与 norm

若 x=n+v、0<v<1，j=floor(qv)、w=qv−j，则 qx=qn+j+w。
每个 q 保 j=0,…,q−1 且 qn+j≤M 的全部 target cells。
任何相关积分都使用

    dv/(n+v)=dw/(qn+j+w)。

这是原 dx/x Jacobian，无额外 q、sqrt q 或 arithmetic norm 修正。
原 normalized basis e_n=1_(n,n+1)/sqrt ell_n，ell_n=log(1+1/n)，
因此 〈T_qe_m,e_n〉=sqrt(ell_m/ell_n) 当
qn≤m≤min(q(n+1)−1,M)，其余为 0；不是 thincomb 的 only-divisor matrix。
(1) 中 R[D_N^+Ra] 恰保留这些实际 carry，不能删除或改成纯整除。

已审 U≤1/8、V≤1/12、|κ|≤sqrt(UV)，S_N=Σw_q≤K sqrt N 为旧 Chebyshev 输入。
T_q contraction、R orthogonal projection，给

    ||R D_N^+Ra||/||p||≤S_N sqrt[U/(M−U)]=O(1)，
    ||D Ra||/||p||=|D|sqrt[U/(M−U)]=O(logN/sqrt N)=o(1)，
    N^−1/2(1+U)||Rb||/||p||
       =(1+U)sqrt[V/(M−U)]=O(1/sqrt N)=o(1)。

这些均有 absolute 常数及所有 N≥4 的非空 domain。
carry 只付 O(1)，没有得到 o(1)；p 的 Γ 费用仍没有 uniform-N 结论。
不把 pole 分量原 sqrt N 下界当作完整 RQP 下界，因为 (1) 保留真实算术同源抵消。

## 范围裁定

547 §4 的 exact identity、strict cutoff、basis/carry/Jacobian 和三项归一化修正通过。
没有证明 projected E 的 critical/polylog 响应或 Γp uniform bound，也没有 Γ-relative/detail 全源输入。
这是接口准备和旧工具消费，零研究轮；最新数学结算仍546。
后续 C019 须先审 critical bound 是否已含旧521–525的 RH 强度，不能将其作为新独立来源。
本短审不证明 whole Q、成长惯性改进、Ξ识别或宏观 Goal 完成。
