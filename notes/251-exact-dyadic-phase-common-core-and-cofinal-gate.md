# 251. Exact dyadic phase common core 与 cofinal gate

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1i normalized common core / finite physical
prime--continuum overlap

状态：`Y=8,16` 两个 intended finite configurations 在同一 phase-normalized
rational core上的 whole-cell geometry、双尺度 response-energy lower与共同 Schur
gain为 [T]；由此向任意 dyadic尺度外推为 [O]。本笔记只更新 Markdown，不更新 PDF，
不声称 RH/GRH、零点比例改进或渐近 Weil 正性。

## 1. 归一化不需要超越数 enclosure

令 `h=1/200`。笔记 249、250 分别产生 verified positive-frequency parent cells

\[
 I_i=[ih,(i+1)h],\quad i\in\mathcal I_8,
\qquad
 I_j=[jh,(j+1)h],\quad j\in\mathcal I_{16}.
\tag{1}
\]

预注册相位坐标为

\[
 \theta=\xi\log Y.
\tag{2}
\]

由于 `8=2^3,16=2^4`，再置

\[
 t=\frac{\theta}{\log2},
\tag{3}
\]

则两个尺度上的映射精确为

\[
 t=3\xi\quad(Y=8),\qquad t=4\xi\quad(Y=16).
\tag{4}
\]

因此共同 core 的构造只涉及整数网格，不需要近似 `log 2`，也没有 floating endpoint
comparison。

## 2. Exact common-core geometry

对每个整数 `k` 定义 normalized base cell

\[
 K_k=[kh,(k+1)h].
\tag{5}
\]

定义

\[
 \mathcal K=
 \{k:\lfloor k/3\rfloor\in\mathcal I_8,
       \ \lfloor k/4\rfloor\in\mathcal I_{16}\}.
\tag{6}
\]

等价地，`K_k/3` 位于一个 scale-8 verified parent cell内，且 `K_k/4` 位于一个
scale-16 verified parent cell内。

### 定理 251-A（exact dyadic normalized common core）[T]

集合 `mathcal K` 恰有 5,931 个 base cells，并分解成下列 18 个 closed connected
components（相邻 cell endpoints合并）：

\[
\begin{aligned}
 &[732/200,1239/200],&&[29368/200,29560/200],\\
 &[39090/200,39540/200],&&[41048/200,41271/200],\\
 &[57468/200,57738/200],&&[62316/200,62368/200],\\
 &[64480/200,64548/200],&&[83064/200,83406/200],\\
 &[92196/200,92520/200],&&[101208/200,101997/200],\\
 &[110841/200,111184/200],&&[113264/200,113760/200],\\
 &[121797/200,122032/200],&&[135168/200,135252/200],\\
 &[136852/200,137199/200],&&[148074/200,148912/200],\\
 &[151857/200,151892/200],&&[152500/200,152836/200].
\end{aligned}
\tag{7}
\]

其总 normalized `t`-width为

\[
 |K|=\frac{5931}{200}=29.655,
\tag{8}
\]

最长 component为

\[
 [148074/200,148912/200],
 \qquad\text{width}=838/200=4.19.
\tag{9}
\]

#### 证明

scale 8 parent `I_i` 在 `t` 轴恰覆盖三个 cells
`K_(3i),K_(3i+1),K_(3i+2)`；scale 16 parent `I_j` 恰覆盖四个 cells
`K_(4j),...,K_(4j+3)`。对笔记 249、250 已冻结且重新计算通过的 parent index
sets作整数集合交，随后合并连续整数。脚本逐项断言式 (7) 的完整 range tuple、式
(8) 的 count、式 (9) 的 longest tuple及下列 index hash：

`80f057bb217ce9ae7f2dd12515c7ccac0f407387ab41bb7380f1632e95873703`。

range tuple本身已显式列出，所以 hash只用于回归，不承担存在性证明。`square`

## 3. Parent lower 向 normalized subcells 的严格传递

令 `b_i^(8)` 与 `b_j^(16)` 是笔记 249、250 stored fixed-point lower
contributions。其构造给出 parent cell上的一个常数 pointwise density lower
`L_i^(Y)`，且

\[
 b_i^{(Y)}\le hL_i^{(Y)}.
\tag{10}
\]

### 引理 251-B（subcell splitting）[T]

若 `K_k/3 subset I_i`，则 scale-8 response energy在 `K_k/3` 上至少为
`b_i^(8)/3`；若 `K_k/4 subset I_j`，则 scale-16 response energy在 `K_k/4`
上至少为 `b_j^(16)/4`。

#### 证明

pullback intervals的 `xi`-width分别为 `h/3,h/4`。式 (10) 的同一个 pointwise
lower在整个 parent cell成立，故子区间积分至少为 `hL_i/3` 或 `hL_j/4`；而
`b_i/3<=hL_i/3`、`b_j/4<=hL_j/4`。这里除法在 exact rationals中进行，不把
fixed-point整数再次舍入。`square`

## 4. Common core 携带双尺度正能量

令 `K` 是式 (7) 的 union，并分别以 `xi=t/3`、`xi=t/4` pull back。由引理
251-B逐 `k in mathcal K` 求和：

### 定理 251-C（two-scale common-core capture）[T]

scale 8 的 common-core numerator满足

\[
 \mathcal N_{8,K}
 \ge0.000039220662642190066268978048,
\tag{11}
\]

从而结合笔记 248 的 intended denominator upper，

\[
 \frac{\mathcal N_{8,K}}{D_8}
 >0.053294357127071656>\frac1{20}.
\tag{12}
\]

scale 16相应地满足

\[
 \mathcal N_{16,K}
 \ge0.000116177723841047733338034809,
\tag{13}
\]

以及

\[
 \frac{\mathcal N_{16,K}}{D_{16}}
 >0.113275592614188418>\frac1{20}.
\tag{14}
\]

共同 `(k,parent-bound-8,parent-bound-16)` ledger 的 SHA-256为

`2e89fecb2f7c56905d73ba5efcc89e462d0c7a48f7191c1c608f0865373d86a3`。

#### 证明

式 (11)、(13)分别是

\[
 \sum_{k\in\mathcal K}
 \frac{b^{(8)}_{\lfloor k/3\rfloor}}3,
 \qquad
 \sum_{k\in\mathcal K}
 \frac{b^{(16)}_{\lfloor k/4\rfloor}}4.
\tag{15}
\]

引理 251-B证明每项是一侧 lower，且不同 `K_k` interiors互不相交。再除以笔记
248、250的完整 intended denominator uppers。所有运算使用 exact `Fraction`；显示值
向下舍入。`square`

## 5. 一个真正共享但仍有限的 physical Schur 常数

每个 common parent cell都满足 `1/4<=W_p/W_c<=4`，故

\[
 \frac{W_pW_c}{W_p^2+W_c^2}\ge\frac4{17}.
\tag{16}
\]

此外笔记 244 证明全部频率上的 `W_p,W_c>=0`，所以 common core之外的 cross
integrand也不会抵消式 (16) 的贡献。

### 推论 251-D（shared two-scale physical gain）[T]

对 `Y in {8,16}` 的相应 finite physical responses同时有

\[
 -z_Y>\frac4{17}\frac1{20}D_Y=\frac1{85}D_Y,
\tag{17}
\]

因而

\[
 \|u_{p,Y}+u_{c,Y}\|^2
 =D_Y+2z_Y<\frac{83}{85}D_Y,
\tag{18}
\]

\[
 \boxed{
 \frac{D_Y}{\|u_{p,Y}+u_{c,Y}\|^2}>
 \frac{85}{83}=1.0240963855\ldots .}
\tag{19}
\]

与笔记 249、250各自使用全部 verified arcs所得常数相比，式 (19)较弱；它的新内容
是两个尺度使用同一个 normalized geometric core与同一个 rational lower。

## 6. 最小公理与每条作用

本定理的最小输入为：

1. `[T]` 两个父证书的完整 verified index及 fixed lower ledgers；作用是提供
   pointwise whole-parent lower，而非 midpoint evidence；
2. `[T]` `8=2^3,16=2^4`；作用是把 transcendental normalization化成 exact
   `3:4` integer subdivision；
3. `[T]` parent lower的 pointwise来源；作用是允许引理 251-B，单纯 parent integral
   lower不能任意分给子区间；
4. `[T]` intended denominator uppers；作用是把 common numerator转成相对 capture；
5. `[T]` symmetric sign theorem `W_p,W_c>=0`；作用是 common core外的 cross不能抵消；
6. `[T]` ratio inequality (16)；作用是把 diagonal capture转成 physical cross gain。

结论不是公理改写：两个父集合完全可能在 normalized coordinate上不相交；即使相交，
它们也可能只落在 response density任意小的位置。式 (7) 与式 (11)--(14)均是可失败的
finite arithmetic outputs。

## 7. 删除、反例与失效位置

- 删除 power-of-two commensurability：`log Y_1/log Y_2`一般为无理数，需新的 directed
  endpoint enclosure；当前整数证明不能引用；
- 删除 complete parent index ledgers而只保留 count/width：两个同宽集合可完全错开，
  common core无从推出；
- 删除 pointwise parent lower而只保留 parent integral：能量可集中在 common subcell
  的补集，引理 251-B失效；
- 删除 denominator upper：共同几何宽度不能推出 relative capture；
- 删除 global sign：core外的正 cross可能被负 cross抵消，式 (17)失效；
- 删除 ratio margin：`W_pW_c/(W_p^2+W_c^2)`可趋零；
- 把 `{8,16}` 换成所有 dyadic `Y`：没有第三尺度或 transfer theorem，属于量词偷换。

## 8. 循环性与模型范围

循环性审计：未使用 zeros、RH/GRH、Weil positivity、谱酉性、PNT error、Mertens
平方根界、bounded negative index或紧性。新增步骤只使用两个已独立认证的 finite
prime/continuum ledgers及整数网格交。

模型范围：

- Riemann-zeta 的两个 finite Abel configurations：定理直接适用；
- 任意两个 `Y=2^m,2^n` 的 positive-coefficient finite models：若分别给出同型 parent
  ledgers，可在 `t=theta/log2` 上用 `m:n` subdivision；
- 一般 algebraic/rationally independent scales：需 separately certified log-ratio
  endpoint geometry；
- complex Dirichlet/automorphic coefficients：`W_p,W_c>=0`失效，几何交本身不能推出
  physical cross；
- 本结果属于显式公式型 Weil response，不提供上同调极化或 Hard Lefschetz bridge。

## 9. Cofinal gate 与下一最小引理 B1j [O]

定理 251-D是共享的 two-scale mechanism，但不是 cofinal theorem。尤其当前
`(Y,N)=(8,10),(16,15)` 没有定义一个增长 schedule；固定 `N/Y=O(1)` 也不能自动使
被截断的 Abel prime tail消失。因此继续计算 `Y=32` 之前，必须先写出 cofinal coupling

\[
 Y_m=2^m,\quad N_m,\quad J_m,\quad h_m,\quad \Xi_m
\tag{20}
\]

以及每个 truncation/quadrature/cell error趋零所需的明确条件。

下一最小引理 B1j 是证明 dyadic normalized-symbol transfer identity：把

\[
 W_{p,2^{m+1}}\!\left(\frac{t}{m+1}\right)
 -W_{p,2^m}\!\left(\frac{t}{m}\right)
\tag{21}
\]

连同 continuum counterpart分解成：

1. 一个显式 Abel kernel作用于 `dpsi-dx` 的 arithmetic discrepancy term；
2. prime cutoff tail；
3. continuum mesh/tail；
4. phase rescaling remainder。

随后证明：若这些四项在某个 fixed normalized core上小于父证书的 strict ratio与
response-density margins，则 common capture从 `m` 传到 `m+1`。这将 uniform B1a 的
缺口缩成具体 smoothed prime discrepancy估计；在该 identity及 cofinal schedule闭合前，
禁止用更多 finite points冒充渐近证据。
