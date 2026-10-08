# 原素数前缀的直接正投影与准确 minor 剩余

2026-10-08，perron_reviewer；复盘后第1轮，基线 b763892e95a17bbb19f940b1dc4d37b0c2d9536d。
只新增本源，不改冻结稿、Git或检查器；定稿供根作者及不同作者全文独审。
本稿不从 signed 总上界限制子掩码：先证明逐 packet 正包络稳定，再作完整项相减。

## 1. 同一实际对象及全文读取输入

保持 \(X=T/(2\pi),L=\log X,N_L=a_LL,d=\lfloor XL\rfloor,\eta=2\pi/L\)，
原 \(\chi,\nu,\phi\in C^2,I_+,\Delta,\delta_{\rm near}=64\Delta\)、全部最大标签位置与共同空间变量。
仍为425(36)的四全异 unit **主带**，记 \(\mathfrak L\)；不是 canonical scalar 子集。
所有 genuine primes 在 \((\sqrt X,X]\)，最大为 \(q\)，\(s,p,r<q\)，原 \(p,r\ne s\) 保留。
\(p=r\) 的原 graph 比较仍按425整体桥处理，不能在新频率掩码中免费删除。
空间变量记 \(w\)，以区别指数 \(u\)。固定
\[
W=X^{1/10},\quad B=X^{1/5},\quad C_0=X^{1193/700},\quad C_2=X^{2393/1400}.
\]
以下输入本轮均全文读回；canonical LF 仅统一行尾，不 trim。

| 输入／实际消费 | SHA256 |
|---|---|
| [actual425](hybrid-whole-fourth-unit-unit-actual-research-whole.md)：参数、主带、完整误差 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [major378](hybrid-original-unit-band-joint-cancellation-research-whole.md)：低产品及完整 \(n\) 分区 | 7c95bd2e700c16e0b0e836063f7545e8222a4de4b03d60c3271965252ec744b4 |
| [cap464](hybrid-original-unit-band-minor-lift-research-pc8.md)：Poisson、点排除 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [major340](hybrid-original-unit-band-joint-rational-large-sieve-research-high-product.md)：联合有理正包络 | 92989568fd5ffbe25a8f6f47997c9ced10acd96b8d3732c740d2cb8a7563ee7e |
| [shell337](hybrid-original-high-product-minor-rational-slice-research-high-product.md)：两套 residual、最大区间 | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [edge285](hybrid-original-high-product-minor-edge-and-coherent-period-research-checkpoint-audit.md)：共同端周期 | 85bd0985a63b56941be5a216111a53f95ec0494fbd08a29cbdf8ac8f20ed93e0 |
| [cutoff175](hybrid-original-prime-cutoff-fourth-and-max-label-research-perron.md)：完整最大标签主带 | d7aaee914be30cfee19b4aa62b3efcb36adaa0f058155cc05d2e82e1c8740062 |
| [mixed160](hybrid-original-low-label-mixed-union-research-high-product.md)：完整至少一小标签主带 | 55d632dd6565b1c4ed3a1abfd8a7785b3e253c0ddd3e36c52d8cdde48941b0cf |
| [cutoff peer91](hybrid-original-prime-cutoff-fourth-and-max-label-review-high-product.md)：不同作者限定审查 | fb707a9a2b2c879542c5f85c830192294a5cc18f48e6fedcbad016145091218f |
| [485](../../notes/485-original-minor-product-cap-and-point-repairs.md) | 4fd6db48a93dcc5ff18840c3f663341096988f3c6b624ee761c90f85108f6eed |
| [487](../../notes/487-original-joint-rational-major-payment.md) | 1768ac94f1d72b1934fa6b8c7290e78717bd2082214e562fde5586c2d788de7d |
| [489](../../notes/489-original-high-product-rational-minor-slice.md) | c39081acaf5d1bd22685df4a918d42b1bffa635bb15a09b41b66794654ecdddd |
| [491](../../notes/491-original-period-edges-and-signed-core-statistics.md) | 28ff712f977b3a378a7d3df52d4335bb1a603d1105c2134f51e83e741c784149 |

## 2. 允许的矩形、准确掩码与完整 \(n\) 桥

对每个最大位置，允许外 \(q\) 为前缀／区间，实际 \(s\) 为原 dyadic 区间与
\(s<q\)、interior、产品上下 cap、固定素数区间的交；它仍是一个区间或固定有限个区间。
内 \(p,r\) 各为固定素数区间与原 dyadic 支撑、严格 \(p,r<q\) 的交。
这些条件不依赖 \(n\)；不允许随 \(q\) 私选稀疏素数集合。
记这种矩形为 \(\Pi\)，原 same-\(w\) profiles及精确 \(s\) 排除在其中保持。

先在完整主带加回全部 \(q\mid n\)，再插入原 \(g(pr/(qs))\)。
加回以前，模 \(q\) Fourier 矩形范数为 \(\sqrt q\)，原两腿 \(L^2\) 仍 \(O_\phi(1)\)；
故每个 \((q,s)\) 的完整加回绝对费用 \(\ll q^{-1/2}\)。
外权聚合为 \(O(\sqrt X L^C)\)，若 \(q\le Z=X^u\) 则为 \(O(\sqrt Z L^C)\)。
插入 \(g\) 只在完整 \(n\) 后用 Poisson 与原 \(\chi\) tail：内区 aliases、
gate 外尾的绝对质量受原完整四权正包络控制，额外区间只减少该质量。
不能把此桥改写为 individual \(n\) 的等价。
低产品 boxes \(QS\le64WX\) 用完整逆变换的整数 near 计数支付 \(WX^\epsilon L^C\)；
固定区间不增加真实 factor pairs，不能按这些 boxes 再删频率。

高 boxes 的旧 major 是存在 \(d\le W\) 且
\(|n/q-m-a/d|\le W/(dS)\)；它包含全部 \(q\mid n\)。
旧 minor \(\mathfrak I_W[\Pi]\) 为其完整 complement，**暂不加 \(qs>C_0\)**。
先从旧 minor 保留 \(qs>C_0\)，再删 \(W<d\le B\)、半径 \(1/S\) 的 shell；
其余准确记 \(\mathfrak K_{489}[\Pi]\)。两半径始终不同，均用固定 dyadic \(S\)。

## 3. major 与 shell 的直接正包络

对固定公共 twists、固定 binary 区间，两腿合成 \(C_k=\sum_{pr=k}b_pb_rp^{it_1}r^{it_2}\)。
额外内区间后仍逐式有 \(\sum|C_k|^2\le2\sum b_p^2\sum b_r^2\ll1\)；
不是从原 signed 系数和的范数推出子集范数。任意实际区间可用至多 \(2O(L)\)
个 binary 块精确表示；两端点和严格 \(q\)-prefix 同时恢复，只增日志。

major340的非空频率仍是 reduced \(c/(dq)\)，且唯一恢复 \((q,d,a,m)\)；
投影只能减少这些实际 packets，记其分母族为 \(\mathcal A_H\)。\(H<d\le2H\) 的共同 chirp 包络
绝对积分 \(O(1+W/H)\)，same-\(w\) \(C^2\) profile 包络 \(L^C\)，均无需升级 \(\phi\)。
由 fixed-coefficient 大筛重推
\(\sum F_{q,d,a,m}(w)^2\ll(H+W)^2Q^2L^C\)；
另一正 Cauchy 因子 \(\sum_{\mathcal A_H}b_q^2\ll H^2X/S\)，实际整数数
\(O(QW/(HS)+1)\) 保留 \(+1\)。于是每 box
\[
|\mathfrak A_W[\Pi]|\ll W^2(Q+S)L^C/\sqrt X.                 \tag{1}
\]
额外 \(s\) interval仅减少该处正质量；\(p=s,r=s\) sup 修正仍受原正包络控制。
故全族 \(\ll W^2\sqrt X L^C\)，\(q\le Z\) 时直接重聚合为 \(W^2ZL^C/\sqrt X\)。

shell337先用 \(\nu\) 的零支撑统一到 \(J_q\)，再分别分离 \(g\)、外 residual、
内 residual；它们的共同包络不依赖 \(s\)，不能换回 \(s\)-私有绝对包络。
实际 \(s\) 区间被同一个最大区间 \(R_{d,a}\) 支配；
\(\sum_{d,a}R_{d,a}^2\ll(H^2+S)L^C\ll SL^C\)，额外固定 \(s\) cut 仍为真实区间。
内两腿按上述 binary 恢复，联合能量仍 \(H^2Q^2L^C\)；
外 packet 能量仍 \(XL^C\)，整数数 \(O(Q/S+1)\) 含 \(+1\)。
因此
\[
|\mathfrak J_{W,B,>C_0}[\Pi]|\ll B(Q+S)L^C/\sqrt X          \tag{2}
\]
逐 box 成立；全族 \(B\sqrt X L^C\)，\(q\le Z\) 时为 \(BZL^C/\sqrt X\)。
当前 \(qs>C_0\) 原样保证 \(B^2\ll S, QS>64BX,q>B\)；没有另扩大参数范围。

## 4. cap、点排除与端周期的直接付款

cap464的完整 \(n\) Poisson 核在 \(|qs-pr|\le\delta_{\rm near}qs\) 外及所有 aliases 有原正 tail。
每个真实整数 \(pr\) 至多两个有序素数因子对，限制内区间仍至多两个；
四权 \(\ll1/(qs)\)，所以每个 \((q,s)\) 正计数上界仍
\(O(\delta_{\rm near}+1/(qs))\)。恢复实际 \(qs\le C_0\)（不以完整 boxes 放大阈值）得
\[
|\mathfrak L_F^g[\Pi;qs\le C_0]|\ll(C_0/X+1)L^C.            \tag{3}
\]
该完整块减去§3直接重付的 region major，才得到 \(\mathfrak I_W[\Pi;qs\le C_0]\)。

原 \(p,r\ne s\) 始终用减两个单点、加双单点精确恢复。
如 \(p=s\)，相位 \(h=s(q-r)\in(0,q^2)\)，固定内 cut 变为 \(s,r\) 的 \(n\) 无关系数。
每个 \(h\le X^2\) 至多三个 prime \(s>\sqrt X\)，各 \(s\) 唯一恢复 \(r\)；
逐 \(h\) Cauchy 给 \(\sum|c_{q,h}|^2\ll1/S\)。
完整 \(q^2\) Parseval 在任何**正平方和**的准确频率 mask 上给 \(Q^3/S\)；
外因子 \(QX/S\) 与原 \(S/(QX)\) 付 \(Q/\sqrt X\)。
双点 \(h=s(q-s)\) 至多二对一；全部修正为 \(\sqrt X L^C\)，前缀时 \(ZL^C/\sqrt X\)。

491优化仍用唯一共同
\[
J_q=[q\theta_-/(4\pi S),q\theta_+/(2\pi S)]\cap\mathbb Z=[l_q,h_q]\cap\mathbb Z.
\]
先用 \(\nu\) 零支撑扩共同窗，后作 Mellin；不残留 individual \((s,n)\) indicator。
完整 periods 是 \(I_j=(jq,(j+1)q]\cap\mathbb Z\)，
\(j_0=\lceil(l_q-1)/q\rceil,j_1=\lfloor h_q/q\rfloor-1\)。
余端 \(E=J_q\setminus\bigcup_{j_0\le j\le j_1}I_j\) 至多两段、每 residue 至多两次，
包括空周期、所有 floors/ceils。限制素数区间后直接得
\(\sum b_q^2\sum_{E\cap K}|F|^2\ll QL^C,\ \sum_q\sum_{E\cap K}|G|^2\ll Q^3L^C\)：
前者用真实 \(s<q\) 的 mod-\(q\) Parseval；后者重新用 factor-pair 正系数能量，
不能引用被截取前的 signed \(G\) 范数。
原前因子给 \(QS/X\)；仅对实际 \(C_0<qs\le C_2\) 聚合得 \(C_2L^C/X\)。
定义 \(\mathfrak K_{491}[\Pi]=\mathfrak K_{489}[\Pi]-\mathfrak E[\Pi]\)；高于 \(C_2\) 的端周期仍在。

## 5. 完整最大标签前缀：三种观察量分开

只消费cutoff175已证的**完整** \(|\mathfrak L[q\le Z]|\ll X^{B(u)+\epsilon}\)，
\(B(u)=3u/2-11/14,\ 17/20\le u\le1\)，条件前件为普通 \([R_{7/8}]\)。
§§2–4逐正包络重推后，完整项的准确减法给下表；全部 logs 吸入 \(\epsilon\)。

| 准确原频率族，均保持 \(q\le X^u\) | 完整费用指数 | \(u=9/10\) |
|---|---|---|
| \(\mathfrak I_W\)：未加产品 cap 的旧完整 minor | \(\max\{B(u),u-3/10\}\) | \(3/5\) |
| \(\mathfrak K_{489}\)：原 cap 外、再删 shell 的准确余额 | \(\max\{B(u),493/700\}\) | \(493/700\) |
| \(\mathfrak K_{491}\)：再删原低产品端周期的准确余额 | \(\max\{B(u),993/1400\}\) | \(993/1400\) |

低产品 \(WX^\epsilon\)、完整 \(q\mid n\) 的 \(X^{u/2}\)、点修正 \(X^{u-1/2}\) 均更低。
第一行不推出第二行；第二行是另减已按(3)付款的完整 cap。
每个固定 \(u<1\) 的完整前缀均低于 \(5/7\)，但未取得 top-\(q\) 总界。

## 6. 至少一小标签的准确消费接口

取 \(Z=X^{9/10}\)。至少一个标签 \(\le Z\) 的全主带逐 tuple 等于以下三不相交矩形之和：
\[
(s\le Z),\qquad(s>Z,\ p\le Z),\qquad(s>Z,\ p>Z,\ r\le Z).     \tag{4}
\]
各自保持真实最大 \(q\)；当 \(q\le Z\)，第一矩形已含其完整族。
内区间均固定，外 \(s\) 每 \(q\) 仍为有限区间；因此§§2–4对各矩形**直接**成立。
消费本轮全文核读的 mixed160(11) 的完整输入
\[
|\mathfrak L_{\rm small}|\ll X^{379/560+\epsilon},             \tag{5}
\]
不能要求或声称(5)对这三个矩形分别成立；本稿仅在先合并全部三矩形后消费它。
由准确全项相减，small 族的 \(\mathfrak I_W,\mathfrak K_{489},\mathfrak K_{491}\)
分别付 \(7/10,493/700,993/1400\)。这也不付款任意小标签 signed 子集。

## 7. 更好的先分完整标签族：只留下四条大素数腿

先写 \(\mathfrak L=\mathfrak L_{\rm small}+\mathfrak L_{\rm large}\)，
large 是单矩形 \(q,s>Z,\ p,r\in(Z,q)\)，原全部 \(s\) 排除和 profiles 保留。
其 \(qs>Z^2=X^{9/5}\) 使原 cap \(C_0\)、低产品 boxes、491已付的 \(qs\le C_2\) 端族全空。
对该单矩形直接用§2完整 \(n\) 桥和§3两个正包络，精确得
\[
\mathfrak L_{\rm large}=\mathfrak K_{489,\rm large}
 +O_\phi(X^{7/10}L^C)+O_\phi(X^{1/2}L^C).
\]
在(5)中先固定 \(0<\epsilon_0<13/560=7/10-379/560\)，把该固定常数吸入隐常数。
因此整个原主带满足日志版本
\[
\boxed{\mathfrak L=\mathfrak K_{489,\rm large}+O_\phi(X^{7/10}L^C).} \tag{6}
\]
此分区在旧全域 cap 相减**以前**完成，所以不继承 \(493/700\)；不是把旧误差截出子项。
原425整体 unit／主带比较已付 \(X^{1/2}L^C\)，可在完整 \(\mathfrak L\) 取得(6)后整体消费。
亦可对 large 矩形直接重证该桥：行列限制不增 Fourier／TT* 范数，
原 chirp 幅 \(X^{-2}L^C\) 与全部外权给 \(\sqrt X L^C\)；boundary、graph、far 与 aliases 用原正包络。
double-nn 的非零加性矩形 \(\sqrt q\) 范数、零频 kernel 高阶展开及 graph 正界亦保持，
核本身不受 inner lowercut 影响；全部费用不超过原 \(\sqrt X L^C\)。
因此保留原完整 unit／physical 观察配置，不投影一个未认证的 signed 桥误差。

这里只删491原低产品 edge cap；\(qs>C_2\) 的共同 \(J_q\) 端频率全部仍在 \(\mathfrak K_{489,\rm large}\)。
剩余所有素数 \(>X^{9/10}\)，\(q/s<X^{1/10}\)，两内腿仍严格 \(<q\)，\(\nu\) 全 Mellin 尾保留。
未付的是这个真实 near-balanced、带原两种 rational complement 的完整 signed 核，
不是更换系数的普适大筛问题；global \(5/7\)、sf 四矩、比例与零点自由边界均未改善。
