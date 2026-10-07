# 439. 素数槽几何与一个有严格余量的条件边界候选

2026-10-07。通用指数的代数推导和有理余量为 [T/R]；
改变实际补偿探测器后的完整估计仍为 [C/O]。本稿没有证明新的无零半平面。
外部来源固定为 [OpenAI/math September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。

## 1. 固定探测器为何停在 7/8

原 proof 的 Part II 用

\[
 b=1/8,\quad \ell=1/6,\quad
 l_x=17/48,\quad l_y=23/48,\quad h=13/16.
\]

low 为 Z^{l_x/2+b/12+epsilon}=Z^{3/16+epsilon}。
主信号的 Mellin 指数是 C(s)=s−11/16；因此 C(7/8)=3/16。
只改善 high 行计数、或只减少 high 误差，不能使这个固定 low 指数下降。
AF 的固定角色高度比例也不是 Hecke 角色行数的幂节省：即使每一行只有一个孤立离线对，
它的在线比例仍可趋于 1，而每一行都需要被 detector 处理。

## 2. 可变槽长度的 low 账本

暂保持原范数、ray group、补偿算子及 zero-on-nonunit masks，提出形式几何

\[
 M=1-\ell,\quad l_x=(1-\ell-b)/2,\quad
 l_y=(1-\ell+b)/2,\quad h=(1+3\ell+b)/2.
 \tag{1}
\]

M+ell=1、h=1−l_x+ell。主留数始终在 z=1/6，故

\[
 C_b(s)=s+l_x/2-1+h/6=s-2/3-b/6.
 \tag{2}
\]

若补偿 low 的相同行范数和 Gram 估计能覆盖 (1)，取 rescaled subset 总长度 d，
则 M′=M−2d、ell′=ell−d，源式中的反射能量分子变成

\[
 1+3\ell'-2M'=5\ell-1+d.
\]

原 tuple 的额外指数 −d 加上反射损失 (5ell−1+d)_+/8。
在 0<=d<=ell 上，最大值准确为 (5ell−1)_+/8，取于 d=0。
因此该相同账本的候选 low 指数及交点为

\[
 L_{\ell,b}=(1-\ell)/4-b/6+(5\ell-1)_+/8,
\quad
 \boxed{\sigma(\ell)=11/12-\ell/4+(5\ell-1)_+/8.}
 \tag{3}
\]

b 从交点中消失。对 ell<=1/5，增加槽总长度能改善交点；
ell>1/5 后反射损失反而使交点上升。
形式 minimum 在 ell=1/5 为 13/15；这没有支付 high，不能解释为可实现边界。
源 `prop:probe-low` 的定理只声明固定 ell=1/6；(3) 的实际 low 前件仍须扩域证明。

## 3. high 指数必须保留固定的主留数

源 `eq:stage-high-exponent` 对保留行 u、Nu~Z^d、a=(1+delta)/2 给

\[
 E_\sigma(d;R,g)=a-\sigma+h(z_0-1/6)-a l_y-\ell/2+g
       +d(R+\delta/2-z_0),\quad z_0=17/50.
 \tag{4}
\]

若主要标记项 g=q ell，0<=q<=delta/2，在 d=h、ell<=1/5 和
sigma=11/12−ell/4 处，代入 (1) 得

\[
 \boxed{E(h)=K+(1/2+\ell)\delta+\ell q-h(1-R),\quad
 K=-1/4+5\ell/4+b/6.} \tag{5}
\]

z 留数是固定 1/6，不是可变 ell。
把式 (4) 的 h(z_0−1/6)误换成 h(z_0−ell)，会出现错误的二次 K；
本稿和独立推导均使用 (5)。

任何真正的 R→R−eta 幂节省都使 (4) 降低 d eta。
常数比例 c·(Z^d)^R 仍只有同一个 R，因此 AF 的平均比例没有直接的指数收益。

## 4. 在原 nominal capacity 上的精确小扰动

用原证书的 alpha=5/6，x=q/delta in [0,1/2]，定义

\[
 D_x=3-17x/9,\quad P_x=2-26x/9+8x^2/9,
\quad J=(\alpha-\delta)D_x+\delta P_x,
\]
\[
 R_*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2J}.
 \tag{6}
\]

J>0；源 `lem:balanced-endpoint` 在整个 0<=delta<=5/6 上有

\[
 -E_0(h_0;R_*)\ge c_*:=49/440640.
 \tag{7}
\]

这是有完成平方恒等式支撑的严格下界，不是网格采样结论。
3P_x<=2D_x，因为 2D_x−3P_x=(44x−24x²)/9>=0。
从 (6) 得 R_*<=1−2delta/3，闭端点 delta=alpha 同样成立。
保持 b=1/8，令 ell=1/6+t。对 (5) 的相同 nominal R_*，

\[
 E_t(h_t;R_*)-E_0(h_0;R_*)
 =t\{-1/4+\delta+q+3R_*/2\}
 \le (5/3)t.
 \tag{8}
\]

取 t=1/20000，得到

\[
 \ell_1=1/6+1/20000,\quad
 \sigma_1=7/8-1/80000=0.8749875,
\]
\[
 \boxed{-E_1(h_1;R_*)\ge
 49/440640-1/12000=307/11016000>0.} \tag{9}
\]

若把已给的全 Hecke 7/8 结论作为 bootstrap，则 beta_*<=7/8、delta<=3/4。
plain moment 可固定 kappa=3/4，因为其前件 beta_*<=(1+kappa)/2 成立。
不能把新的 beta_*−sigma_1 代入旧 proof 专为第一轮 11/12→7/8 设置的 Delta 容量，
也不能为 delta<=3/4 以外的行重新选择另一套 beta_*。
(9) 在更大的 5/6 代数范围成立，但不自动把 (6) 变成新几何下已证行数。

## 5. 其他原账本的局部余量

floor delta_0=1/50、R=1、q<=delta_0/2 的 formal high 上界为

\[
 E_{\rm floor}\le-7/1200+(32/25)t<0.
 \tag{10}
\]

对固定 d 的 (4)，不跟随 h 移动，保持同一个 R 时导数为

\[
 \partial_\ell E(d)=13/50+\delta/4+q\le177/200.
\]

因此原 d_min<=d<=1/2 区间若保留其 49/14400 余量，扣除最多
177/4000000 后仍为正。这里没有把 R 的几何依赖设成零；
这只是检验在保留原容量前件时，对显式 outside powers 的变化。
更小物理行 d<d_min 使用原文独立 small-row 估计，仍在下节的完整轮廓待付项内。

低侧的充分长度条件 M−2d>0、l_x−ell>0、l_y−ell−11b/6>0
在整个 0<=d<=ell_1 上保持严格，最后一个等价于 9ell_1+8b<3。
另外 ell_1<1/5、3ell_1+b<1。
供槽比 ell/h 对 ell 的导数为 (1+b)/(2h²)>0；
原在 d=h 的 ell/h=8/39>7/37 供给余量没有缩小。
这些都是可核验的参数事实，不能代替 moments 的共同 masks、系数和高度统一性。

## 6. 已付项与完整定理的待付项

[440](440-principal-euler-correction-below-seven-eighths.md)直接从准确 Euler 因子证明
主校正在 Re s>2/3 全纯；对主留数轮廓的箱域 x_r>401/600 正常收敛。
因此它覆盖 sigma_1；这项接口可以实际支付。

新无零定理仍需要在同一实际 physical probe 上完成：

1. 可变槽补偿、row norm、reflected energy 与 additive Gram 的完整 low 证明，
   包含每一个 subset、原零延拓和有界 annular ratios。
2. 重新证明 detector counts 的 adaptive cutoff、饱和、反射与 mark capacity
   在 ell_1 几何上的统一性；(6) 目前只是 nominal 比较函数。
3. 共享 contour accounting 的 sigma_0>=7/8 限制如何逐条向 sigma_1 扩展，
   包括 principal/bounded/outer rows、非主项、局部误差及全部高度尾。
4. 在固定 excluded set、target-independent 正节省和同一个 Mellin signal 下闭合 continuation criterion。

本稿筛出有严格余量且没有本地主信号障碍的参数；没有把上述四个前件标成已完成。
AF 比例并未用于 (9) 的节省，这也是接口研究的实际结果：
现在可见的边界候选来自改变原 low/high 几何，比例法真正可共用的误差接口另见 [438](438-seven-eighths-and-zero-proportion-interfaces.md)。

完整独立推导见本轮 `hybrid-detector-endpoint-derivation.md`；
精确有理核验只检查显示的代数和模型，不认证整个 OpenAI 证明或新的边界。
