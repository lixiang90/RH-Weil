# 496. 原完整次弧核的移位行列式核心

2026-10-08。基线 main 5f85dada6754d9493d3e7b9d34595b731fe940cb。
复盘后第6轮，继续[495](495-original-carry-covariance-and-sparse-spectrum-barrier.md)。
本轮应完成[周期复盘](../goals/reviews/2026-10-08-original-route-review-cycle-2.md)。
本稿给完整周期mask的准确短差归约及全部移位远尾付款；
仍未支付近相关，没有新的whole幂、实际中心常数、比例或无零边界。

## 1. 冻结输入与原完整对象

本轮全文读425、原ν188、494 mixed228、491及495；
337与128 carry源在连续研究中全文读，本轮重核实际mask合同。
canonical LF只转换CRLF/lone CR，不trim。

| 输入 | SHA256 |
| --- | --- |
| [原raw unit载体425](../reviews/2026-10-08/hybrid-whole-fourth-unit-unit-actual-research-whole.md) | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [完整周期mask337](../reviews/2026-10-08/hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [原ν及阈值188](../reviews/2026-10-08/hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |
| [mixed228](../reviews/2026-10-08/hybrid-original-mixed-prime-continuous-legs-research-checkpoint-audit.md) | 7716f0b9452914f24e321fe9bd4d76e1e63d1cae0b31a01e18b761a5f58f8a87 |
| [128 carry源](../reviews/2026-10-08/hybrid-original-prime-target-carry-and-character-contract-research-high-product.md) | 14dc75b6fcae08270d18e5377a6c74bb13a1a84c63041ab4903271d5e9659d37 |

回到[489](489-original-high-product-rational-minor-slice.md)的完整高产品minor，
其中 \(\Omega_{q,S}(n\bmod q)\in\{0,1\}\) 保留unit与两套有理删弧，
与individual s无关。保留真实q/s/p/r、\(q\)最大、全部s排除、same-u、
原profiles、g、产品cap和所有n周期。
425已整体支付chirp correction；以下原ν主分量的raw核准确为
\[
 A_{q,s}(n)=\frac{2\pi s}{q}\nu(2\pi sn/q),\qquad h=pr-qs,
 \quad {\cal K}_{q,s}(h)=
 \sum_{n\in\mathbb Z}\Omega_{q,S}(n)A_{q,s}(n)e_{q^2}(-nh).
 \tag{1}
\]
这里原ν先恢复，零支撑自动给 \(n\in{\cal I}_{q,s}\subset J_q\subset(0,q^2)\)，
故全整数扩展准确，包含floor及两个端period；不是分离后保留私有频率窗。
raw核没有1/n。mixed228的1/n是连续腿IBP后来产生，若研究该核必须
使用V/y的Fourier核，不能把下面的原概率Ψ直接搬过去。

[491](491-original-period-edges-and-signed-core-statistics.md)在低产品带删去端period
后的优化余项具有额外非周期截断，本稿不对那个子mask免费用Poisson。
可由完整差恢复489的更强充分接口；两者差是491已付的
\(O(X^{993/1400}\log^C X)\) 原edge union。
原chirp、graph、nn和physical的完整桥继续按原范围消费。

## 2. 全部移位及q² aliases的准确身份

令
\[
 \widehat\Omega(b)=q^{-1}\sum_{a=0}^{q-1}\Omega(a)e_q(-ab),
 \qquad \Psi(u)=\int_{\mathbb R}\nu(t)e^{itu}dt.
\]
有限Fourier反演及平滑Poisson准确给
\[
 \boxed{{\cal K}_{q,s}(h)=
 \sum_{b=0}^{q-1}\widehat\Omega(b)
 \sum_{\ell\in\mathbb Z}
 \Psi\!\left(-\frac{h-qb+\ell q^2}{qs}\right).}
 \tag{2}
\]
证明：\(\Omega(n)=\sum_b\widehat\Omega(b)e_q(bn)\)，
而 \(A_{q,s}\) 的实Fourier变换为
\(\int A_{q,s}(x)e(-\xi x)dx=\Psi(-\xi q/s)\)；
取 \(\xi=(h-qb)/q^2+\ell\) 即得(2)，没有额外Jacobian因子。
原ν光滑且紧支撑；其Fourier衰减保证aliases绝对收敛。
该身份在恢复层直接保留全部ν参数，不是零Mellin-twist的替代。

## 3. 移位远尾的完整付款

取原
\[
 X=T/(2\pi),\ L=\log X,\quad
 \Delta=1024L^{5/2}/X,\quad \kappa=\sqrt{8\pi}>5,\quad H_{q,s}=qs\Delta.
\]
定义(2)的near为 \(|h-qb+\ell q^2|<H_{q,s}\)；
等号及其余项全属far。大X时 \(\Delta<1/2\)、\(s<q\)，
每个b至多一个near alias。
固定b的最近alias如果是far，原188的衰减给 \(|\Psi|\le X^{-\kappa}\)。
其余aliases的参数模长按 \(q/s\ge1\) 递增，
首个至少 \(q/(2s)\ge1/2\)，故由
\(|\Psi(u)|\le|\Gamma(s_Tu)|\) 得整个余尾为
\[
 O\!\left(\exp(-c\sqrt X/L^{1/4})\right)=O(X^{-\kappa}).
\]
最近点并列只增加固定常数。
原有限mask的Parseval给
\[
 \sum_b|\widehat\Omega(b)|^2=q^{-1}\sum_a\Omega(a)\le1,\qquad
 \sum_b|\widehat\Omega(b)|\le\sqrt q.
\]
所以完整far核点界为 \(O(\sqrt q X^{-\kappa})\)。
所有原profiles/g有界，原same-u外积分质量有界；
真实四素数的正权质量至多 \((\sum_{p\le X}b_p)^4\ll X^2\log^C X\)。
限制最大性、方面比、产品cap和s排除只缩小这个正上界。
全部q/s/p/r及最大标签位置恢复后，准确付款为
\[
 \boxed{|K_{\rm far}|\ll X^{5/2-\sqrt{8\pi}}\log^C X.}
 \tag{3}
\]
这是本完整mask原raw主项的移位远尾；未给near任何省幂。

## 4. 下一算术输入必须覆盖哪些项

准确剩余为(2)的全部near：
\[
 pr-q(s+b)+\ell q^2=v,\qquad |v|<qs\Delta,
\]
带同一 \(\widehat\Omega(b)\)、Ψ及真实四prime权。
外素数依然是s；\(s+b-\ell q\)没有自动prime性。
因此只估 \(b=0,\ell=0\) 的 \(pr-qs\) 短差不控制原minor；
近相关也不是正项，不能逐移位免费截出上界。
这补齐了495 carry对象在原ν恢复层的具体算术表述。

完整带F一级统计的充分节省门槛仍是
\(\int W|{\cal T}|\ll Q^2X^{-r}\log^C X\)、
\(r>u+w-12/7\)；balanced顶端为 \(r>2/7\)。
本稿没有证明此前件，不能把(3)或平滑近零模型当作完整whole付款。
不同作者全文审查见[独审](../reviews/2026-10-08/hybrid-original-masked-shifted-determinant-review-high-product.md)。
原目标继续保留；第6轮复盘据此判断下一周期的投入。
