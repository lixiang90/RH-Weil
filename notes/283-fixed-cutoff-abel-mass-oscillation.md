# 283. 固定 cutoff 的 Abel 质量双向振荡

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T] 不完全 Gamma 乘子的无零域、Mellin 极点幅值引理；
[T/R] 实际 von Mangoldt 源在固定比例 \(N=Y\) 上的无条件双向大质量。
证明使用已核验的 Littlewood 外部振荡定理及标准显式公式；
RH 只用于一个穷尽性分支，不是最终结论的假设。
本篇没有证明中频四阶预算、RH/GRH 或零点比例改进，也未声称文献新颖性。

## 1. 对象、主结论和准确量词

固定 \(0<\sigma<1/2\)，置
\[
 d=\frac12-\sigma>0,\qquad
 \ell(Y)=\max(1,\log\log\log Y)
 \quad\text{（只在充分大的 \(Y\) 使用）}.
 \tag{1}
\]
令 \(R(x)=\psi(x)-x\)，其中 \(\psi\) 右连续，所有整数原子取完整权。
对实数 \(Y\ge1\)，定义匹配的固定 cutoff 质量
\[
 A_\sigma(Y)=M(Y,Y)
 =\sum_{2\le n\le Y}\Lambda(n)n^{-\sigma}e^{-n/Y}
       -\int_1^Yx^{-\sigma}e^{-x/Y}\,dx .
 \tag{2}
\]
连续积分的右端是实际的实数 \(Y\)，不是先取整后的端点。

### 定理283-A [T/R]

无条件有
\[
 \boxed{\quad A_\sigma(Y)
       =\Omega_\pm\!\left(Y^d\ell(Y)\right).\quad}
 \tag{3}
\]
而且(3)可以把 \(Y\) 限制为正整数，此时两个 cutoff 精确满足 \(N=Y\)。
亦即存在常数 \(c_\sigma>0\) 和两列趋于无穷的整数 \(n_j^+,n_j^-\)，使
\[
 A_\sigma(n_j^+)\ge c_\sigma(n_j^+)^d\ell(n_j^+),\qquad
 A_\sigma(n_j^-)\le-c_\sigma(n_j^-)^d\ell(n_j^-).
 \tag{4}
\]
因 \(\ell(Y)\to\infty\)，这特别给出两种符号的共尾整数点，满足
\[
 |M(Y,Y)|>Y^d\sqrt{\ell(Y)}.
 \tag{5}
\]
这里没有断言这些整数是 \(2^m\)，也没有证明
\(P_\beta(Y)Y^{\beta-\sigma}<C_{\sigma,\beta}|M(Y,Y)|\)。
因此(5)只达到275的质量门槛，不能替换275的两条件认证序列。

## 2. Mellin 恒等式及所有有限下端项 [T]

先固定任意实数 \(c>0\)，对 \(Y\ge1/c\) 定义
\[
 A_{\sigma,c}(Y)
 =\sum_{2\le n\le cY}\Lambda(n)n^{-\sigma}e^{-n/Y}
       -\int_1^{cY}x^{-\sigma}e^{-x/Y}\,dx .
 \tag{6}
\]
取这个下界保证连续区间不反向；在 \(Y=1/c\) 两项均为零。
对 \(\Re s>0\)，定义下不完全 Gamma 函数
\[
 \gamma(s,c)=\int_0^c t^{s-1}e^{-t}\,dt,
 \qquad t^{s-1}=\exp((s-1)\log t).
 \tag{7}
\]
当 \(\Re s>1-\sigma\) 时，所有下列交换由绝对收敛支持，且
\[
 \boxed{\quad
 \int_{1/c}^\infty A_{\sigma,c}(Y)Y^{-s-1}\,dY
 =\gamma(s,c)
 \left\{-\frac{\zeta'(s+\sigma)}{\zeta(s+\sigma)}
                     -\frac1{s+\sigma-1}\right\}.
 \quad}
 \tag{8}
\]

证明。原子 \(n\) 出现的条件是 \(Y\ge n/c\)，故代换 \(t=n/Y\) 给
\[
 \int_{n/c}^\infty e^{-n/Y}Y^{-s-1}\,dY
     =n^{-s}\gamma(s,c).
 \tag{9}
\]
于是原子项是 \(\gamma(s,c)\sum_{n\ge2}\Lambda(n)n^{-s-\sigma}\)。
对连续项用同一代换和 Fubini，得到
\[
 \int_1^\infty x^{-\sigma}
       \int_{x/c}^\infty e^{-x/Y}Y^{-s-1}\,dY\,dx
   =\gamma(s,c)\int_1^\infty x^{-s-\sigma}\,dx
   =\frac{\gamma(s,c)}{s+\sigma-1}.
 \tag{10}
\]
这证明(8)。在参数域 \(\Re s>1-\sigma\)，相应绝对值积分分别由
\(\sum\Lambda(n)n^{-\Re s-\sigma}\) 和
\(\int_1^\infty x^{-\Re s-\sigma}\,dx\) 控制。
位于单个整数 cutoff 的完整/半权选择不影响 \(Y\) 的 Lebesgue 积分，
但(6)以及后面的 Abel 恒等式始终采用完整权。\(\square\)

如果另选任意固定下界 \(Y_0\ge1/c\)，则(8)右侧还须减去
\(\int_{1/c}^{Y_0}A_{\sigma,c}(Y)Y^{-s-1}\,dY\)。
这是整函数，不可在精确恒等式中漏掉，但它不改变任何有限位置的极点。
特别，主定理 \(c=1\) 的自然下界就是1，不需要额外的有限校正。

## 3. 不完全 Gamma 的显式无零域 [T]

### 引理283-B

对 \(c>0\)，在
\[
 \Re s>0,\qquad \Re s\ge c-1
 \tag{11}
\]
内有 \(\gamma(s,c)\ne0\)。因此对每个固定 \(0<c\le1\)，
\(\gamma(s,c)\) 在整个 \(\Re s>0\) 内无零。

证明。记 \(s=a+ib\)、\(a>0\)。分部积分及 \(t=ce^{-u}\) 给
\[
 s\gamma(s,c)=c^se^{-c}+\gamma(s+1,c),
\]
\[
 s c^{-s}\gamma(s,c)
   =e^{-c}+c\int_0^\infty
           e^{-(s+1)u-ce^{-u}}\,du.
 \tag{12}
\]
令 \(h(u)=e^{-(a+1)u-ce^{-u}}\)。在 \(a+1\ge c\) 下，
\[
 h'(u)=\bigl(-(a+1)+ce^{-u}\bigr)h(u)<0
       \quad(u>0),
 \tag{13}
\]
且 \(h\) 严格为正、可积。对 \(b>0\)，其正弦变换严格为正；一个完整证明为
\[
 \int_0^\infty h(u)\sin(bu)\,du
 =\frac1b\sum_{k\ge0}\int_0^\pi
 \left\{h\!\left(\frac{2k\pi+t}{b}\right)
       -h\!\left(\frac{(2k+1)\pi+t}{b}\right)\right\}\sin t\,dt>0.
 \tag{14}
\]
重组由 \(h\in L^1\) 允许；每一项非负，且第一项严格正。
所以(12)右侧的虚部严格负，不可能为零。\(b<0\) 用共轭，
\(b=0\) 则直接由(7)的实正性得到结论。\(\square\)

必须先按(12)除以 \(c^s\) 再判断虚部；对任意 \(c\ne1\)，
\(\gamma(s+1,c)\) 本身带有额外复相位。
本证明不是“正核的复 Mellin 变换自动无零”，也不声称所有 \(c>1\)
在整个右半平面无零。特别，\(c=1\) 时每个
\(\rho\) 满足 \(\Re\rho>\sigma\) 的实际非平凡零点都满足
\[
 \gamma(\rho-\sigma,1)\ne0.
 \tag{15}
\]

## 4. 非实 Mellin 极点的定量双向幅值 [T]

本节重建所需的 Landau 论证，不把“存在极点”直接跳写为带幅值的振荡结论。

### 引理283-C

设实值、局部可积函数 \(A(Y)\) 定义于 \([1,\infty)\)，有多项式增长。
其 Mellin 变换 \(F(s)=\int_1^\infty A(Y)Y^{-s-1}\,dY\) 最初在某个
右半平面绝对收敛，并有亚纯延拓到 \(\Re s>0\)。设：

- 某个 \(a>0\) 满足 \(F\) 在每个实数 \(s\ge a\) 处全纯；
- 某个 \(b\ne0\) 使 \(F\) 在 \(a+ib\) 有简单极点，留数为 \(r\ne0\)。

则
\[
 \limsup_{Y\to\infty}\frac{A(Y)}{Y^a}\ge|r|,
 \qquad
 \liminf_{Y\to\infty}\frac{A(Y)}{Y^a}\le-|r|.
 \tag{16}
\]
不要求 \(a\) 是全部非实极点的最大实部，也不要求存在最右极点。

证明。先证明下面使用的非负 Mellin 性质：非负函数 \(B\) 的 Mellin
积分若有有限收敛横坐标 \(\lambda\)，则其和函数不能在实数 \(\lambda\)
处全纯。否则，选 \(s_1>\lambda\) 足够接近 \(\lambda\)，可使和函数
在以 \(s_1\) 为中心、半径 \(r_1>s_1-\lambda\) 的圆盘内全纯。
这里圆盘由原来的右半平面与 \(\lambda\) 的一个全纯邻域共同覆盖。
稍减 \(r_1\)，Taylor 展开和非负性给
\[
 \sum_{k\ge0}\frac{r_1^k}{k!}
       \int_{Y_0}^\infty B(Y)Y^{-s_1-1}(\log Y)^k\,dY<\infty
 \quad(Y_0\ge1).
\]
各项非负，Tonelli 将其变成
\(\int_{Y_0}^\infty B(Y)Y^{-(s_1-r_1)-1}\,dY<\infty\)，
与 \(s_1-r_1<\lambda\) 矛盾。这也给出了本处 Landau 性质的证明。

现在若(16)的第二式不成立，可选 \(0\le c<|r|\) 及 \(Y_0\ge1\)，使
\(B(Y)=A(Y)+cY^a\ge0\) 对所有 \(Y\ge Y_0\) 成立（几乎处处已足够）。
其 Mellin 和函数在最初收敛域等于
\[
 F_B(s)=F(s)-\int_1^{Y_0}A(Y)Y^{-s-1}\,dY
                  +\frac{cY_0^{a-s}}{s-a}.
 \tag{17}
\]
右侧在每个实数 \(s>a\) 全纯。由刚证的非负 Mellin 性质，
\(B\) 的收敛横坐标至多为 \(a\)；否则会在一个实数 \(\lambda>a\)
产生奇点。多项式增长保证该横坐标有有限上界；若它为 \(-\infty\)，
下面同样成立。因此对 \(\varepsilon>0\)，积分确实收敛且
\[
 |F_B(a+\varepsilon+ib)|\le F_B(a+\varepsilon).
 \tag{18}
\]
两侧乘 \(\varepsilon\) 后令 \(\varepsilon\downarrow0\)。
左侧趋于 \(|r|\)：(17)的有限前缀为整函数，最后一项在 \(a+ib\)
全纯。右侧趋于 \(c\)：\(F\) 在实数 \(a\) 全纯。
于是 \(|r|\le c\)，矛盾。对 \(-A\) 重复即得第一式。\(\square\)

对(8)，括号内函数在每个实数 \(s>0\) 处全纯：
在 \(s=1-\sigma\)，\(-\zeta'/\zeta\) 的留数为1，恰被所减项消去；
其他正实数处没有 zeta 零点。后一点可直接由 \(\zeta(x)>0\)（\(x>1\)）
及交错级数
\(\eta(x)=(1-2^{1-x})\zeta(x)>0\)（\(0<x<1\)）核验。
因此 \(F(s)\) 在右半平面正实轴上没有被遗漏的极点。

如果某个实际零点 \(\rho=\alpha+i\gamma\) 满足 \(\alpha>\sigma\)，
其重数为 \(m_\rho\)，则对 \(c=1\)，(8)在 \(s=\rho-\sigma\) 有留数
\[
 r_\rho=-m_\rho\gamma(\rho-\sigma,1)\ne0.
 \tag{19}
\]
引理283-C于是严格给出
\[
 \limsup_{Y\to\infty}\frac{A_\sigma(Y)}{Y^{\alpha-\sigma}}
     \ge m_\rho|\gamma(\rho-\sigma,1)|,
 \qquad
 \liminf_{Y\to\infty}\frac{A_\sigma(Y)}{Y^{\alpha-\sigma}}
     \le-m_\rho|\gamma(\rho-\sigma,1)|.
 \tag{20}
\]
这是对每一个满足条件的实际零点的单独结论；没有假设这些零点位于中心线。

## 5. RH 分支的端点保留平滑余项 [C]

### 引理283-D

若 RH 成立，则对实数 \(Y\to\infty\)，包括整数 \(Y\)，有
\[
 \boxed{\quad
 A_\sigma(Y)=e^{-1}Y^{-\sigma}R(Y)+O_\sigma(Y^d).
 \quad}
 \tag{21}
\]
这里 \(R(Y)\) 是完整右连续端点，未换成半权端点。

证明。令 \(w_Y(x)=x^{-\sigma}e^{-x/Y}\)。精确 Stieltjes 分部积分为
\[
 A_\sigma(Y)=w_Y(Y)R(Y)+w_Y(1)
                    +\int_1^Y R(x)(-w_Y'(x))\,dx .
 \tag{22}
\]
\(w_Y(1)\) 来自 \(R(1)=-1\)；原子 \(Y\)（若存在）完整留在第一项。
需证普通积分为 \(O_\sigma(Y^d)\)。区间 \([1,2]\) 为 \(O_\sigma(1)\)。
在 \([2,Y]\) 使用282-(12)--(15)的半权截断显式公式，只在此普通积分中
以 \(R_0=R\) 几乎处处替换。先固定 \(Y\)，再令截断高度 \(V\to\infty\)；
截断误差被固定区间可积函数支配，其积分趋于零。常数项和平凡零点项
为 \(O_\sigma(1)\)，因为 \(-w_Y'\ge0\)、\(\int_2^Y(-w_Y')\le w_Y(2)\)，
且 \(-\tfrac12\log(1-x^{-2})\) 在 \(x\ge2\) 有界。

对 RH 下 \(\rho=1/2+i\gamma\)，单个非平凡零点的积分满足
\[
 \frac1\rho\int_2^Yx^\rho(-w_Y'(x))\,dx
 =\frac1\rho\int_{\log2}^{\log Y}
   (\sigma+e^u/Y)e^{du-e^u/Y}e^{i\gamma u}\,du .
 \tag{23}
\]
282-B 的 \(L^1\)/BV 界（包含零延拓的两个端点跳跃）给
\[
 \left|\frac1\rho\int_2^Yx^\rho(-w_Y')\,dx\right|
        \ll_\sigma\frac{Y^d}{(1+|\gamma|)^2}.
 \tag{24}
\]
标准单位高度计数 \(O(\log(2+|\gamma|))\) 使(24)按零点重数绝对可和。
因此积分后的高度极限等于该绝对收敛和，且为 \(O_\sigma(Y^d)\)。
代回(22)即得(21)。没有在端点对 \(\sum Y^\rho/\rho\) 取绝对值，
也没有让 \(V\) 与 \(Y\) 同时趋于无穷。\(\square\)

本节只是条件性余项引理，不能在无条件分析中直接使用(21)。
其作用是下一节穷尽性论证中的 RH 分支。

## 6. 穷尽两种分支及整数化：证明283-A [T/R]

独立外部输入为 Littlewood 的无条件定理
\[
 R(x)=\Omega_\pm(\sqrt x\,\ell(x)).
 \tag{25}
\]
沿用271、275核验的 Hardy--Littlewood 原论文 §5.1 与 Theorem5.8；
见[作者原论文扫描件](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1916.Hardy.pdf)。
该定理本身无条件：原论文的 RH 分支展开不能误读为给整个(25)添加 RH 假设。

若 RH 成立，(21)、(25)及 \(\ell(Y)\to\infty\) 直接给
\(A_\sigma(Y)=\Omega_\pm(Y^d\ell(Y))\)：系数 \(e^{-1}\) 为正，
而 \(O(Y^d)\) 平滑余项不足以消去两侧的大端点振荡。

若 RH 不成立，由函数方程对称性存在实际零点
\(\rho_0=\alpha_0+i\gamma_0\) 满足 \(\alpha_0>1/2\)。
引理283-B保证其 Mellin 乘子不为零，(20)给
\[
 A_\sigma(Y)=\Omega_\pm(Y^{\alpha_0-\sigma}),
 \qquad \alpha_0-\sigma>d.
 \tag{26}
\]
因为 \(Y^{\alpha_0-1/2}/\ell(Y)\to\infty\)，这比(3)更强。
两种分支穷尽所有可能，故(3)是无条件结论，并不需要判断哪个分支实际成立。

最后核验整数化。若 \(n=\lfloor Y\rfloor\ge2\)，则 \(Y\in[n,n+1)\)
内的原子集合保持不变，且原子 \(n\) 从整个区间的左端起即取完整权。
在该开区间逐项求导得
\[
 A_\sigma'(Y)=\frac1{Y^2}
 \left\{\sum_{k\le n}\Lambda(k)k^{1-\sigma}e^{-k/Y}
             -\int_1^Yx^{1-\sigma}e^{-x/Y}\,dx\right\}
                  -e^{-1}Y^{-\sigma}.
 \tag{27}
\]
仅用 \(\Lambda(k)\le\log k\) 就得
\[
 |A_\sigma(Y)-A_\sigma(\lfloor Y\rfloor)|
       \ll_\sigma Y^{-\sigma}\log Y .
 \tag{28}
\]
\(Y\) 为整数时左侧为零；取左侧整数不会跨越尚未计入的下一个原子。
此误差为 \(o(Y^d)\)，当然也是 \(o(Y^{\alpha_0-\sigma})\)。
两侧振荡序列取整后仍趋于无穷，且幂次与 \(\ell\) 的比值趋于1，
所以得到(4)，进而得到(5)。\(\square\)

## 7. 最小输入、275接口与止损边界

| 输入 | 本篇的确切作用 | 不得到的结论 |
|---|---|---|
| 匹配的实 cutoff 与下界 \(Y\ge1/c\) | (8)的精确 Gamma 乘子和有限前缀账本 | 不允许随意删连续下端或变成不匹配 cutoff |
| 283-B 的复无零证明 | 非 RH 分支不丢失 \(\rho_0-\sigma\) 的实际极点 | 不是仅由正核宣称复域无零 |
| 实轴解析性与非负 Mellin 奇点性质 | (16)、(20)的双向定量幅值 | 单个零点本身只给固定幂次幅值，不凭空产生 \(\ell\) |
| RH 分支的 \(1/\rho\) 与积分后 BV 衰减 | (21)保留端点并把平滑余项降到 \(Y^d\) | 不在无条件论证中偷用全部零点实部为 \(1/2\) |
| 独立 Littlewood 振荡 [R] | RH 分支保留 \(\ell\) 增益 | 选择或紧性本身不产生算术振荡 |
| 同一整数单元的精确求导 | (28)把连续尺度结论转为 \(N=Y\in\mathbb N\) | 不把整数尺度误写成 dyadic 尺度 |

相较于只用一个固定零点的 Mellin 极点，本篇补上了固定 \(N=Y\) 的
\(\ell\) 强度，因此实际源的单独大质量条件不再必须依靠窗口内移动 cutoff。
但275的联合条件还有整个历史的 \(P_\beta\) guard，且其认证搜索使用 dyadic \(Y\)。
本篇没有证明这两个附加性质在同一固定-cutoff 振荡点成立；不能仅从(3)声称
275全部选择自由度已被消除。相应最小后续问题是能否在同一整数点同时控制历史
与质量，而不是重复证明已有的单点振荡。

同样，本篇的零点使用是证明已明确给出的实际质量振荡；没有得到
279的真实尾部中频四阶预算。281已排除的纯包络/正源推理不会因质量更大
而自动复活。完整 Gamma gluing、统一算术正性与上同调桥梁仍开放。

附注：283-B与(8)也适用于每个固定 \(0<c\le1\)，因此相同的两分支证明
可给一般固定比例的质量振荡；此处主定理只以 \(c=1\) 表述，避免将
\(c<1\) 的 cutoff 自动放入原 \([Y,2Y]\) 配置。更广的 \(c\) 只具有
(11)所列的已证无零域，本文不声称复域无零条件可以任意放宽。

## 8. 独立有限复算 [E]

主代理全文读并独立运行
`python -B scripts/fixed_cutoff_abel_mass_probe.py`（默认 \(\sigma=1/4\)）。
脚本用18/24阶 Taylor 展开及归一化前缀矩在 \(O(24N_{\max})\) 内
扫描所有整数 \(2\le Y=N\le2^{18}\)，不以有限网格代替实尺度定理。
本机 NumPy2.5.2、SciPy1.18.1、mpmath1.3.0，实际 longdouble 尾数为52位。

- 在诊断容差 \(10^{-7}\) 外，正样本75,494个、负样本186,649个，
  相邻整数反号2,736对；首对为 \(198,199\)。函数有素数幂跳跃，
  所以反号对不是连续零点证书。
- 采样最小值 \(A(175620)\simeq-5.39546512162\)，
  最大值 \(A(230393)\simeq3.96646898859\)。
  九个选定点用独立直接 `fsum` 与MP50连续积分重算，
  与前缀算法的最大绝对差为 \(5.20\cdot10^{-11}\)。
- 18/24阶结果最大差 \(1.82\cdot10^{-12}\)；
  24阶解析截断余项上界 \(9.96\cdot10^{-22}\) **不包含浮点舍入**。
  前述容差与交叉复算均不是严格区间认证。

另对 \(X=16,32\) 独立检查精确的有限恒等式
\[
 \begin{aligned}
 \int_1^X A_\sigma(Y)Y^{-s-1}\,dY
 &=\sum_{n\le X}\Lambda(n)n^{-s-\sigma}
       \{\gamma(s,1)-\gamma(s,n/X)\}\\
 &\quad-\int_1^X x^{-s-\sigma}
       \{\gamma(s,1)-\gamma(s,x/X)\}\,dx .
 \end{aligned}
 \tag{29}
\]
其证明是在有限三角区域上重复(9)--(10)，无需任何无限和或高度极限。
左端在每个整数 \(Y\) 单元分别高斯积分，右端独立换成 \(\log x\) 积分；
MP50下最大恒等式差 \(3.65\cdot10^{-42}\)，20/32阶积分差不超过
\(3.76\cdot10^{-24}\)。这些数值是有限一致性检查，不是误差认证。

以 `mpmath.zetazero(1)` 的虚部作为数值模板，
\(\lvert\gamma(1/4+i\gamma_1,1)\rvert\simeq0.02612187232\)，
而完整 Gamma 模仅约 \(2.94\cdot10^{-10}\)，不能把两种核混用。
递推式的MP50残差小于 \(7\cdot10^{-52}\)。
脚本还单独评价解析下界
\[
 |\gamma(s,1)|\ge
 \frac{e^{-1}(1-2/|\Im s|)}{|s|}
 \quad(\Re s>0,\ |\Im s|>2).
 \tag{30}
\]
证明是(12)在 \(c=1\) 时的递减密度具有初值 \(e^{-1}\)、总变差
\(e^{-1}\)，故 \(|\gamma(s+1,1)|\le2e^{-1}/|\Im s|\)，再用递推与三角不等式。
零点模板的近似值不参与此解析证明。任何有限实验都不参与(3)、(16)、(21)，
不认证无界振荡、dyadic 限制、284记录高度或中频预算。

## 9. 依赖与审计状态

无条件外部算术输入：(25)及 zeta 的标准解析延拓、函数方程、单位高度计数
与截断显式公式。显式公式和单位计数沿用282已核验的
[Kedlaya 第9章](https://kskedlaya.org/ant/chap-von-mangoldt.html)。
本篇自行证明 Mellin 恒等式、乘子无零域、所需非负 Mellin 奇点性质和定量幅值，
并逐段保留原子/连续端点。

本轮主代理及 carrier_audit 已独立完成全文逆向审计；
重点复核不完全 Gamma 相位、Landau 幅值而非仅指数、固定 \(Y\) 后的高度极限、
完整端点和不跨原子的整数化。主代理还再次逐页视觉核验外部原论文
印刷页184的第5.1节和194的Theorem5.8，确认(25)为无条件双向振荡。
gap_exception_audit 完成写作及自审；上述内部审计不等于外部同行评审、
新颖性证明或完整 Goal 的阶段验收。

同轮后续：[284](284-causal-abel-inverse-and-diagonal-record-selection.md)
以单独证明的稳定因果逆核，在本篇强振荡基础上构造**另一列**
整数对角记录，同时控制质量与历史；它不是声称本篇任意振荡点都有 guard。
