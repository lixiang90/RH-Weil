# 真正高产品次弧的六腿 shifted covariance：准确 joint 接口

2026-10-08，high_product_joint。研究基线 main
`3afd19318bf9c6fd6b3a1472929d13b4484698d3`，俯瞰复盘后第1轮。
只新增本源，不改旧冻结文件、输出、检查器或 Git。

本稿把489之后真正剩余 \(\mathfrak K_{W,B,>Z}\) 的 \(F\)-权联合能量
准确化为真实 prime 与 prime-product 的 shifted covariance。
新接口把可以直接支付的系数对角与必须控制的六腿交叉项分开。
它没有证明交叉项的省幂，没有宣布新实际频率子族已付，也没有扩大 \(B\)。
这里完成的是一个有完整量词的核心新输入及其严格消费证明。

具体得到：系数对角能量为 \(O(Q^2X/S)\)，对应 joint Cauchy 的
\(O(\sqrt Q)\) 费用；真实交叉项若取得上界 \(Q^3X^{-j}\)，
则其 box 费用为 \(Q\sqrt{S/X}X^{-j/2}\)。
跨过 \(5/7\) 的准确门槛仍是 \(j>2u+w-17/7\)。
合并 \(h=qs-pr\) 的 prime 因子唯一性本身不证明这个新输入。

## 1. 全文重读的准确对象与同一参数

本轮 FULL READ [489](../../notes/489-original-high-product-rational-minor-slice.md)、
[337行新增 rational-slice 源](hybrid-original-high-product-minor-rational-slice-research-high-product.md)、
[actual425](hybrid-whole-fourth-unit-unit-actual-research-whole.md)，
以及[真正 prime F 腿源](hybrid-original-high-product-minor-prime-leg-research-checkpoint-audit.md)。
另重读原 [minor464](hybrid-original-unit-band-minor-lift-research-pc8.md) 的§7。
保持各源的真实最大标签、同一 \(u\)、\(C^2\) profile、时间 floor、
正 carrier、carry、\(g\) 以及原 sharp prime endpoints。

canonical LF 身份只把 CRLF/lone CR 转 LF，不 trim：

| 输入 | 行数／字节 | SHA256 |
| --- | --- | --- |
| 489 | 85／4231 | c39081acaf5d1bd22685df4a918d42b1bffa635bb15a09b41b66794654ecdddd |
| rational-slice 源 | 337／14790 | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| actual425 | 425／16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| prime F 源 | 246／10811 | 1790bc3878900e88c89d2ba3b51ba0cf06e85583e353879df0e9a514bfd79b0f |
| minor464（本轮重读§7） | 464／17560 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |

仍取 \(X=T/(2\pi)\)、\(L=\log X\)、
\(b_p=\log p/(a_LL\sqrt p)\)、\(a_L\ge c_\phi>0\)，
全部 genuine primes 在 \((\sqrt X,X]\)。当前已付的两个分母范围为
\[
 W=X^{1/10},\qquad B=X^{1/5},\qquad Z=X^{1193/700}.
\tag{1}
\]
固定真实 dyadic \(Q,S,P,R\)，保留 \(PR\asymp QS\)、\(P,R\ll Q\)。
\(q\) 是实际最大 prime，\(s,p,r<q\)；\(qs>Z\)、interior 与 dyadic
端点组成原真实 \(q\)-相关 \(s\) interval \(\mathcal S_q\)。

对固定 \(q,S\)，定义 \(\mathcal A_{q,S}\subset\{1,\ldots,q-1\}\)：
\(a\) 必须同时排除所有 reduced rational 所给的两套邻域，
\[
 \left\|a/q-b/d\right\|>W/(dS)\quad(1\le d\le W),
 \qquad
 \left\|a/q-b/d\right\|>1/S\quad(W<d\le B).
\tag{2}
\]
这里 \(\|\cdot\|\) 是距最近整数的距离，\((b,d)=1\)，
每个 \(d\) 的 reduced residues 全部保留。
这两条件都以 \(S\) 为 scale，不以 individual \(s\) 为 scale。
它们在 \(n/q\) 下对整数平移不变，故真正剩余 mask 周期为 \(q\)。
令 \(J_q\) 是337源利用 \(\nu\) 的零支撑得到的准确共同频窗，置
\[
 \mathcal N_q=\{n\in J_q:n\bmod q\in\mathcal A_{q,S}\},
 \quad |J_q|\ll qX/S,\quad J_q\subset(0,q^2).
\tag{3}
\]
这严格保留489的 \(\mathfrak K\)；不把新半径改成 \(B/(dS)\)。

先作原共同 Fourier/Mellin 分离。对每组固定且共同的参数 \(\lambda\)，
实际双腿是
\[
 F_{q,n}=\sum_{s\in\mathcal S_q}A_{\lambda,s}e(ns/q),
 \qquad A_{\lambda,s}=b_s(s/S)s^{it_s},
\]
\[
 G_{q,n}=\sum_k C_{\lambda,q,k}e(-nk/q^2),\qquad
 C_{\lambda,q,k}=\sum_{\substack{pr=k\\p,r\ {\rm actual},\ p,r<q}}
                    b_pb_rp^{it_p}r^{it_r}.
\tag{4}
\]
所有 twists 来自同一组公共参数；原 \(g\) 单独 Mellin，\(\nu\) 先用
零支撑恢复(3)再 Mellin。不存在私下随 \(q,n\) 改变的系数。
\(\sum_s|A_s|^2\ll1\)、\(\sum_k|C_{q,k}|^2\ll1\)，常数对 twists 一致。
后式直接用每个 prime-product 至多两个有序 pairs，并包括 \(p=r\)。
原 \(p=s,r=s\) 修正按337源§7在本准确 \((q,n,S)\) mask上重用正 Parseval，
全族费用 \(O(\sqrt X L^C)\)；不从 signed 全次弧界推该子mask。

## 2. 合并整数 h 与不能删除的 alias

定义 \(H_q(n)=F_{q,n}G_{q,n}\)。准确合并为
\[
 H_q(n)=\sum_h D_{q,h}e(nh/q^2),\qquad
 D_{q,h}=\sum_{s\in\mathcal S_q}A_sC_{q,qs-h}.
\tag{5}
\]
这里相位整数是 \(h=qs-pr\)，不再乘一个 \(s\)。
真实 \(qs,pr\in(0,q^2)\)，所以 \(-q^2<h<q^2\)。
\(p,r<q\) 为 primes，故 \(q\nmid pr\)，从而
\[
 q\nmid h,\qquad h=0\text{ 不可能}.
\tag{6}
\]
但同一个非零 \(h\) 可以有多个 \((s,p,r)\)。prime-product 至多两个
factor pairs，并不使 \(h\) 至多两对一；每个 \(s\) 都给一个新产品 \(qs-h\)。

令 \(\widetilde D_{q,\gamma}=\sum_{h\equiv\gamma\ (q^2)}D_{q,h}\)。
上述整数支撑使每个 \(\gamma\) 最多有两个 \(h\)；不能免费只取一个符号。
完整能量的 collision 条件是
\[
 q(s-s')-(k-k')=j q^2,\qquad j\in\{-1,0,1\}.
\tag{7}
\]
这是新的六腿 Fourier 能量折叠。它不同于actual425已经付款的原 physical
\(a\)-lattice tails；后者的付款不能用来删除本式的正负 \(h\) aliases。
\(h=0\) 不可能，也不能删除 \(h=h'\) 的自身能量对角。

完整 \(q^2\) Parseval 及去 \(q\mid n\) 的准确身份为
\[
 \sum_{n\bmod q^2}|H_q(n)|^2
            =q^2\sum_\gamma|\widetilde D_{q,\gamma}|^2,
\]
\[
 \sum_{\substack{n\bmod q^2\\q\nmid n}}|H_q(n)|^2
 =q^2\sum_\gamma|\widetilde D_{q,\gamma}|^2
   -q\left|\sum_s A_s\right|^2
                 \sum_{v\bmod q}\left|\sum_{k\equiv v\ (q)}C_{q,k}\right|^2.
\tag{8}
\]
第二项是完整 \(n=qj\) 的实际正能量，不因 \(q\nmid h\) 而消失。
对于真正(3)必须直接使用该 mask，不能从一个 signed 差免费删出子域。

## 3. Prime 结构给出的 collision 界仍没有省幂

逐个 \(h\) 用 \(O(S)\) 个可能的 \(s\) 做 Cauchy，再完整求和，给
\(\sum_h|D_{q,h}|^2\ll S\)。折叠最多二层，故
\[
 \sum_\gamma|\widetilde D_{q,\gamma}|^2\ll S,\qquad
 \sum_q\sum_{n\bmod q^2}|H_q(n)|^2\ll Q^3SL^C.
\tag{9}
\]
这个 bound 保留实际 prime weights，所有 twists 与真实 \(q\)-prefix统一。

也可跨 \(q\) 消费 genuine-prime 因子结构而得到同一尺度。
置 \(A_q(\ell)=\sum_{s-s'=\ell}A_s\overline{A_{s'}}\)，则
\(|A_q(\ell)|\le\sum_s|A_s|^2\ll1\)。以所有真实 \(p,r\) dyad 的
正系数 \(c_k^+=\sum_{pr=k}b_pb_r\) 作共同 envelope，
\(|C_{q,k}|\le c_k^+\)，\(\sum_k(c_k^+)^2\ll1\)，
\((\sum_kc_k^+)^2\ll PRL^C\)。

若 \(k=k'\)，(7)与 \(|s-s'|<q\) 强制 \(s=s',j=0\)，
跨 \(q\) 的费用为 \(O(QL^C)\)。若 \(k\ne k'\)，(7)先强制
\(q\mid k-k'\)。非零整数 \(|k-k'|<X^2\) 至多有三个不同的
prime 因子 \(q>\sqrt X\)。每个 \(q\) 至多三个 \(j\)，并唯一确定 \(\ell\)。
因此所有非trivial collisions的绝对上界为
\(9\sum_{k,k'}c_k^+c_{k'}^+\ll PRL^C\)。严格得到
\[
 \sum_q\sum_\gamma|\widetilde D_{q,\gamma}|^2
                           \ll(Q+PR)L^C\ll QSL^C.
\tag{10}
\]
有限 \(q\)-prefix只减少正 envelope；没有另给每个 \(q\) 自由选择系数。
乘完整 \(q^2\) 后仍是(9)。这是实际 prime collision 的上界，
不能将 \(Q+PR\) 误写成 \(Q\)，也不能把乘 \(q^2\) 的费用漏掉。
用(9)与原前因子直接联合 Cauchy只给 \(QS/\sqrt X\)，
比两独立二能量的 \(Q\sqrt{S/X}\) 多一个 \(\sqrt S\)。

## 4. 真正 minor 核下的准确 shifted covariance

定义这个实际 mask 的有限 Fourier 核
\[
 \mathcal W_q(v)=\sum_{n\in\mathcal N_q}e(nv/q^2).
\tag{11}
\]
它是 \(q^2\)-周期的 Hermitian 核：
\(\mathcal W_q(-v)=\overline{\mathcal W_q(v)}\)，
\(\mathcal W_q(0)=|\mathcal N_q|\)。
它一般不是一个非负整数值函数，也不等于完整周期的 \(q^2\) 倍指示。
实际正联合能量准确为
\[
 \mathcal E_\lambda=
 \sum_q\sum_{n\in\mathcal N_q}|F_{q,n}G_{q,n}|^2
 =\sum_q\sum_{s,s'}\sum_{k,k'}
 A_s\overline{A_{s'}}C_{q,k}\overline{C_{q,k'}}
                 \mathcal W_q(q(s-s')-(k-k')).
\tag{12}
\]
用真实 product-coefficient autocorrelation
\(B_q(t)=\sum_{k-k'=t}C_{q,k}\overline{C_{q,k'}}\)，等价写为
\[
 \mathcal E_\lambda=
             \sum_q\sum_{\ell,t}A_q(\ell)B_q(t)\mathcal W_q(q\ell-t).
\tag{13}
\]
包括 \(\ell=0,t\ne0\) 及 \(\ell\ne0,t=0\)；
真正短 band 下这两类不能按完整 Parseval 免费删掉。

分离唯一的系数对角 \((\ell,t)=(0,0)\)：
\[
 \mathcal D_\lambda=
 \sum_q|\mathcal N_q|\left(\sum_s|A_s|^2\right)
                       \left(\sum_k|C_{q,k}|^2\right)
                        \ll Q^2X/S\,L^C,
\]
\[
 \boxed{\mathcal E_\lambda=\mathcal D_\lambda+\mathcal C_\lambda,\qquad
 \mathcal C_\lambda=
  \sum_q\sum_{(\ell,t)\ne(0,0)}A_q(\ell)B_q(t)\mathcal W_q(q\ell-t).}
\tag{14}
\]
\(\mathcal C_\lambda\) 是实数，可以为负；它不是原 signed 主项的频率子集。
所以本稿直接证明 \(\mathcal D\) 的正能量界，却不由它宣布任何原子族付款。
若将 \(\mathcal C\) 的各项取绝对值，其振荡核与 shifted covariance相消
会被丢弃；(10)也只处理完整周期核的 collisions，不处理本准确核。

写 \(n=a+qj\) 可更具体看到共同相关性。定义实际整数 interval
\(\mathcal J_{q,a}=\{j:a+qj\in J_q\}\)，长度 \(O(X/S+1)\)，则准确有
\[
 \mathcal W_q(q\ell-t)=
 \sum_{a\in\mathcal A_{q,S}}e(a\ell/q-at/q^2)
                          \sum_{j\in\mathcal J_{q,a}}e(-jt/q).
\tag{15}
\]
minor只决定 \(a\)，真实 carrier band又决定 \(\mathcal J_{q,a}\)，
二者不能换成独立矩形。这里没有转为一个 inverse phase或引用
trilinear Kloosterman 定理；若要如此处理，必须另证准确变换及完整 tails。

## 5. 新 joint 输入与严格主项费用门槛

在固定共同参数上，原 box 的外前因子为 \(O(S/(QX))\)。
所有外 Mellin 的 \(q,n\) 相位模为1，\(Q/q\) 有固定上界。
由 \(\sum_qb_q^2\ll1\) 和(3)，直接在本实际 mask 上 Cauchy给
\[
 |\mathfrak K_{\rm box}(\lambda)|^2
 \ll\left(\frac S{QX}\right)^2
          \left(\sum_qb_q^2|\mathcal N_q|\right)\mathcal E_\lambda
 \ll\frac S{QX}\,\mathcal E_\lambda.
\tag{16}
\]
这保留 \(F\) 和 \(G\) 到同一 joint 正能量，未先拆成两条 \(L^2\)。

原共同参数的非负可积正 envelope记为 \(w(\lambda)\)，
\(\int w\ll L^C\)。一次参数 Cauchy/Jensen给
\[
 |\mathfrak K_{\rm box}|^2
               \ll\frac S{QX}L^C\int w(\lambda)\mathcal E_\lambda\,d\lambda.
\tag{17}
\]
对角界对 twists一致，故 \(\int w\mathcal D\ll Q^2X/S\,L^C\)。
新的充分算术输入准确是
\[
 \boxed{\int w(\lambda)\mathcal C_\lambda\,d\lambda
                         \le C_{\phi,j}Q^3X^{-j}L^{C_0}.}
\tag{JSC}
\]
只须上界，不须绝对值界；它不允许每个 \(q,n\) 私选不同参数。
对每组共同参数的统一 covariance上界足以证明本输入，但不是必需条件：
有可积参数费用的证明也可直接消费(17)。不能藏入不可积 twist常数。

若证明 \((\mathrm{JSC})_j\)，(14)、(17)严格给
\[
 |\mathfrak K_{\rm box}|
 \ll\{\sqrt Q+Q\sqrt{S/X}X^{-j/2}\}L^C.
\tag{18}
\]
\(\sqrt Q\) 是已控对角在 joint inequality中的费用，不是独立原频率付款。
在 \(Q=X^u,S=X^w\) 的费用 notation下，(18)的非对角项低于
\(X^{5/7}\) 的准确条件是
\[
 \boxed{j>2u+w-17/7.}
\tag{19}
\]
真实 remaining域有 \(u\ge w\)、\(u+w\ge1193/700-O(1/L)\)。
于是最容易处的 inf 门槛为 \(179/1400-O(1/L)\)，
\(u=w=1\) 的 balanced端点为 \(4/7\)。
一个 \(j\) 超过前者仅支付满足(19)的实际 boxes；不能扩为全部余项。
若按 boxes付款，准确剩余必须保留未满足(19)的 \(Q,S,P,R\) 原tuple族，
并保持两套已排除有理弧、原 \(qs>Z\)、所有 endpoints与同一参数。
本稿尚未证明 \((\mathrm{JSC})_j\)，因此不执行这次删除。

自然的全部近对角尺度 \(\int w\mathcal E\ll Q^2X/S\,L^C\)
会把(17)付到 \(\sqrt Q\)，但它是比(19)更强的充分输入。
原独立 \(G\) 目标 \(Q^2X/S\) 没有被当作唯一门槛；
这里控制的是 genuine-prime \(F\) 加权后的实际六腿 covariance。

## 6. F³/F⁴ Hölder不能独立替代这个输入

在同一实际有限正测度 \(\mu\) 上令 \(N=\mu(\Omega)\)。
对 \(p=3,4\)，若 \(G\) 仍只使用 \(L^2(\mu)\)，Hölder及有限测度嵌入给
\[
 \int|FG|\,d\mu
 \le\|F\|_{p,\mu}\|G\|_{p/(p-1),\mu}
 \le\|F\|_{p,\mu}N^{1/2-1/p}\|G\|_{2,\mu}.
\tag{20}
\]
power mean 又给
\(\|F\|_{p,\mu}N^{1/2-1/p}\ge\|F\|_{2,\mu}\)。
所以只将已知真实 \(F^3\) 或 \(F^4\) 放入本独立 Hölder消费，
其实际范数右端不会优于同一 mask的 \(F^2/G^2\) Cauchy。
对原和可直接取计数测度及 \(\widehat F(q,n)=b_qF(q,n)\)、
\(\widehat G(q,n)=G(q,n)\)，在(20)代入两者即得到原相同mask的比较。
这是比较实际范数；更高矩若进一步证明了较小的 \(F^2\) 上界，
则属于新的二能量输入，未被本论证排除。此结论不要求素数模型或采样。

这不排除高矩辅助证明 minor \(F^2\) 的新省幂，也不排除新的 \(G\) 矩
或实际相关分布输入。它只说明不增加这种算术信息时，指数换位本身
不能供应(\(\mathrm{JSC}\))。参数 envelope须在每个实际共同参数上按原规则
恢复，不能以不同测度或错误的私有系数消去这个费用。

## 7. 本轮结论与准确未付对象

本轮完整证明了(5)—(15)的整数支撑、unit subtraction、aliases、
跨 \(q\) 的 prime collision界以及真正 residual mask的 covariance身份；
也证明(16)—(19)的可积 joint输入和其充分阈值。
它严格识别了尚缺的 actual prime/six-leg shifted covariance估计。
单靠 \(h=0\) 不可能、prime-product唯一分解、较高 \(F\) 范数或
一般频率几何，都没有交付这个实际 covariance省幂。

当前仍准确保留
\(\mathfrak K_{X^{1/10},X^{1/5},>X^{1193/700}}\)，没有新增 paid频率mask。
完整 scalar \(5/7\)、实际中心四阶常数、零点比例及既有无零边界均保持。
本源不含有限采样或新外部解析定理；有限 Fourier身份自证不等于无限省幂。
后续应直接研究(13)、(15)的 genuine-prime covariance或证明其新算术输入，
再按(19)完整消费允许的真实 boxes。
