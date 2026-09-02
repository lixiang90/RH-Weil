# 230. 中心四迹常数的十二路径独立重建

日期：2026-09-02

分支：MOM-1 / 路线 A1i；接口：paired \(2+2\) diagonal、deterministic mixed diagonal

状态：从原始符号词和配对出发的十二路径分类、背景/素数 mixed cyclic 重数、
平窗常数及 Montgomery--Taylor 常数的独立重算为 [T/E]；没有发现笔记 199、226、
227 的 orientation 或 normalization 错误。未配对素数项的解析闭合不由本笔记
重证，记录级比例仍保持 [C]。本笔记不更新 PDF。

## 1. 结论

笔记 229 通过了两个最强外部算术输入。本轮不调用笔记 199 已写出的

\[
 D_{22}=\frac4{a^4}\iint rs(A_++A_-+B)
\tag{1}
\]

作为起点，而是重新枚举：

1. 四个 prime signs 中恰有两个 \(+\)、两个 \(-\) 的六个 words；
2. 对每个 word，把两个正变量与两个负变量配对的两种 bijections；
3. 每个 pairing 的四个 cumulative path positions。

共得到十二条闭合路径。只用积分平移、窗口偶性和交换两个配对变量，十二条路径
严格分成

\[
 \boxed{4A_+\;\sqcup\;4A_-\;\sqcup\;4B.}
\tag{2}
\]

这独立恢复式 (1) 的系数 \(4\)。

对背景 mixed diagonal，四个 cyclic slots 中选择两个 prime slots 有六种：四种
相邻、两种交替。每种 surviving zero frequency 又有 \((+,-)\)、\((-,+)\)
两种 orientation，故重数精确为

\[
 \boxed{8C_1+4C_2.}
\tag{3}
\]

这独立恢复笔记 226 的 \(D_{\rm mix}\) 系数。

把十二条**原始路径**逐条积分，而不是先合并为 \(A_+,A_-,B\)，得到

\[
 D_{22}(\psi_{\rm MT})
 =0.244589382034\ldots,
\tag{4}
\]

并独立重算

\[
 D_0=0.000078787511\ldots,
 \qquad
 D_{\rm mix}=0.007840799168\ldots.
\tag{5}
\]

因此

\[
 \boxed{
 D_0+D_{\rm mix}+D_{22}
 =0.252508968714\ldots.}
\tag{6}
\]

平窗的十二路径直接积分同时恢复 \(D_{22}=4/15\)。本轮没有发现系数重复、漏掉
cyclic orientation 或 \(a^{-4}\) normalization 错误。

## 2. 十二路径枚举 [T]

固定 signs \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_4)\)，其中两个为
正、两个为负。把两个正 increments 标为

\[
 e_r=(1,0),\qquad e_s=(0,1).
\tag{7}
\]

一个 pairing \(\pi\) 把两个负 increments 指定为 \(-e_{\pi(r)}\)、
\(-e_{\pi(s)}\)。令

\[
 v_0=0,\qquad v_j=\sum_{i\le j}\varepsilon_i e_{\pi(i)}.
\tag{8}
\]

闭合性给 \(v_4=0\)，而四循环窗口读取
\(v_0,v_1,v_2,v_3\)。允许的等价变换是：

1. 给四点加共同平移；
2. 同时取负，来自偶窗口及积分变量反射；
3. 交换 \(r,s\)。

在这些变换下，只有三种 multiset：

\[
 \begin{array}{c|c}
 A_+&\{0,0,e_r,e_s\}\\
 A_-&\{0,0,e_r,-e_s\}\\
 B&\{0,e_r,e_s,e_r+e_s\}.
 \end{array}
\tag{9}
\]

直接枚举六个 sign words 与每个 word 的两个 bijections，三类各出现四次，证明
式 (2)。这里的十二是 \(6\times2\)，不是把三种 pair partitions 与四个
orientations作为未经检查的文字计数。

## 3. Mixed cyclic 重数 [T]

\(\operatorname{tr}(S+P)^4\) 中恰含两个 \(P\) 的六个 placements 在 cyclic
等价下分成：

\[
 \underbrace{SSPP,S P P S,P P S S,P S S P}_{4\text{ adjacent}},
 \qquad
 \underbrace{SPSP,PSPS}_{2\text{ alternating}}.
\tag{10}
\]

写 \(P=Z+Z^*\)。zero frequency 只保留 \(ZZ^*\)、\(Z^*Z\) 两种 orientation。
相邻 placements 的 symbol overlap 是 \(C_1\)，交替 placements 是 \(C_2\)，
所以式 (3) 成立。零 prime word 只有 \(S^4\) 一项，给 \(D_0\)；没有额外 cyclic
factor。

## 4. 独立数值重建 [E]

脚本不调用预合并的式 (1)。对每个 raw path \(\{v_j\}\) 直接计算

\[
 \frac1{a^4}\int_0^1\int_0^1rs
 \int_{\mathbb R}\prod_{j=0}^3
 \psi(u+v_j(r,s))\,du\,dr\,ds.
\tag{11}
\]

外层正方形沿 \(r=s\) 与 \(r+s=1\) 分成四个三角形；这使 compact-support
交点的 max/min 分段在每块内固定，避免把 nonsmooth kink 当作普通 tensor
Gauss 误差。内层积分则直接取四个移动支撑的交集端点。

对 mixed 常数，脚本从六个 placements 自动得到 \(8,4\)，再分别积分相应的
\(C_1,C_2\)。阶数增加时得到式 (4)--(6)，并与既有两个独立脚本的数值一致。

## 5. 删除审计与剩余边界

1. 删除两个 pairing bijections 会把每个 family 的系数减半，错误改变
   \(D_{22}\)。
2. 把 trace words 当作普通交换二项式会看不到相邻/交替的 \(4+2\) 分裂，无法得到
   \(8C_1+4C_2\)。
3. 删除窗口偶性后，全局反射不再是合法等价，十二路径可能分裂成更多函数型；本
   结论只对当前实偶窗类成立。
4. 本轮只重建 surviving diagonals。笔记 221--225 的 unpaired critical shell、
   signed height mean 与 finite crossing bounds 仍须继续内部逆审计；式 (6) 的数值
   一致不能替代这些解析估计。

下一最小引理 A1j [O]：独立重建笔记 218--225 的“local positive energy
\(\to\) whole pure-prime one-sided fourth trace”组合，特别检查 product/ratio
boxes 跨层求和、Fejer cone 聚类和 finite crossing signed means 是否使用同一
原子集合与同一 frozen grid。若通过，再复核 Archimedean \(O(1/L)\) 余项到
zero-side tail 的最终拼接。

## 6. 可复现检查 [E]

`scripts/cyclic_fourth_constant_reconstruction.py` 输出：

```text
raw paired paths: A_plus=4, A_minus=4, B=4
mixed placements: adjacent orientations=8, alternating orientations=4
MT constants: D0=0.000078787511, Dmix=0.007840799168, D22=0.244589382034, total=0.252508968714
cyclic fourth-constant reconstruction: PASS
```

脚本只审计有限组合、窗口积分和正规化，不证明任何素数相关渐近或 RH 结论。
