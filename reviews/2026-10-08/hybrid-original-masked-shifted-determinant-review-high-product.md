# 完整次弧的移位行列式归约：不同作者全文审查

2026-10-08，high_product_joint。研究轮6。限定数学 PASS。
只新增本peer，不改作者源、冻结输入、Git、index或cadence。
结论是准确全移位归约和raw远尾负幂付款；没有新的near或whole费用。

## 1. FULL READ 与冻结身份

FULL READ [496作者源](../../notes/496-original-masked-shifted-determinant-core.md)
全部118行，5792 canonical UTF-8 LF bytes，SHA256：

87f25bb46864759e154597e732500c44fec9da351b377eee9b5ffb73a8808c2b

本轮另全文读489和491；425、337、188、228与128此前均已FULL READ，
本轮回核实际所用合同及下列全部身份。LF只转CRLF/lone CR，不trim。

| 输入 | 行数 | canonical LF SHA256 |
| --- | --- | --- |
| [actual425](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [337完整mask](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 337 | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [原ν188](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 188 | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |
| [mixed228](hybrid-original-mixed-prime-continuous-legs-research-checkpoint-audit.md) | 228 | 7716f0b9452914f24e321fe9bd4d76e1e63d1cae0b31a01e18b761a5f58f8a87 |
| [carry128](hybrid-original-prime-target-carry-and-character-contract-research-high-product.md) | 128 | 14dc75b6fcae08270d18e5377a6c74bb13a1a84c63041ab4903271d5e9659d37 |
| [489](../../notes/489-original-high-product-rational-minor-slice.md) | 85 | c39081acaf5d1bd22685df4a918d42b1bffa635bb15a09b41b66794654ecdddd |
| [491](../../notes/491-original-period-edges-and-signed-core-statistics.md) | 136 | 28ff712f977b3a378a7d3df52d4335bb1a603d1105c2134f51e83e741c784149 |

## 2. 完整对象及归一化

425(9)、(26)中ν主分量为 \(F_A^{(\nu)}(n)/q^2=(2\pi s/q)\nu(2\pi sn/q)e_q(ns)\)。
其余 \(\mathcal V_{\rm corr}\) 保持原完整正付款；不把本归约称作未分解 \(F_A\) 的身份。
所以作者 \(h=pr-qs\) 的相位准确为 \(e_{q^2}(-nh)\)，没有1/n。
228的1/n来自continuous腿IBP的 \(q^2/(2\pi i nN_L)\)；
乘原prefactor后为 \(s^2(N_LX^2)^{-1}V(y)/y\)。这另一核不能套概率Ψ。

489的两套有理删弧均允许全部整数平移，因此剩余0/1 mask模q周期，
与individual s无关。原ν先恢复后的零支撑把全部整数n限制在
\(\mathcal I_{q,s}\subset J_q\subset(0,q^2)\)；全整数扩展准确。
它保留原floor、共同窗的两个端period以及真实ν参数，
没有分离后重新保留individual(s,n)频带。

491在 \(Z<qs\le Z_2\) 另删共同窗端period，故其mask额外非周期。
496明确回到489的完整对象作为充分接口，差是独立已付edge union
\(X^{993/1400}L^C\)，没有从signed总界截取子族。
更高产品域保留原全部n；原chirp、graph、nn及physical桥未被扩大。

## 3. Fourier、Poisson 与所有aliases

作 \(\theta=(2\pi s/q)x\)，准确有
\[
 \int (2\pi s/q)\nu(2\pi sx/q)e(-\xi x)\,dx
 =\int\nu(\theta)e^{-i\xi q\theta/s}\,d\theta
 =\Psi(-\xi q/s).
\]
mask反演为 \(\Omega(n)=\sum_b\widehat\Omega(b)e_q(bn)\)；
Poisson取 \(\xi=(h-qb)/q^2+\ell\)，得到作者(2)的号及全部q² aliases。
没有额外Jacobian，也没有只取b=0或删除unit减项。
ν光滑紧支撑与原Γ衰减保证aliases绝对收敛。

## 4. 远尾正付款的完整消费

相邻alias参数距 \(q/s\ge1\)。因 \(\Delta<1/2\)、\(s<q\)，
严格near \(|h-qb+\ell q^2|<qs\Delta\) 每b至多一个；等号属far。
最近branch若far，其参数模长至少Δ，而
\[
 \sqrt{s_T\Delta}/16=\sqrt{8\pi}\,L,
 \qquad |\Psi(u)|\le|\Gamma(s_Tu)|.
\]
故其界恰为 \(X^{-\sqrt{8\pi}}\)。
其余branch距离至少 \((m-1/2)q/s\)，\(m\ge1\)；
求和 \(\sum_{m\ge1}\exp(-c\sqrt{Xm}/L^{1/4})\)
为 \(O(\exp(-c'\sqrt X/L^{1/4}))\)，可吸收至同一固定负幂。
最近branch并列只增加固定常数，不漏分支。

Parseval给 \(\sum_b|\widehat\Omega(b)|^2=q^{-1}\sum_a\Omega(a)\le1\)，
Cauchy给L1至多√q，故完整far核为 \(O(\sqrt q X^{-\sqrt{8\pi}})\)。
所有profiles/g有界，同u外正质量有界；
四素数正权总质量不超过 \((\sum_{p\le X}b_p)^4\ll X^2L^C\)。
最大性、方面比、产品cap和实际s删除都只缩小该正上界，
恢复全部最大位置仅添固定因子。因此作者(3)确为完整union负幂付款。

## 5. 限定结论

剩余必须保留全部 \(pr-q(s+b)+\ell q^2=v\)、\(|v|<qs\Delta\)
及其相位、Ωhat权、真实prime masks；移位商没有自动prime性。
这份near是signed统计，不能逐移位免费截取正上界。
原ν已在恢复层完整保留，不是零Mellin-twist或漏端period的结果。
一级充分输入仍需 \(r>u+w-12/7\)，balanced顶端需 \(r>2/7\)，尚未证明。
限定 PASS；无实质缺口，不需修源。没有新增box、whole、中心常数、比例或无零边界。
