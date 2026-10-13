# C001 不同组织方式逆审

2026-10-13。基线 `3a72930e9f9f554b03b41d17d8c8002f1813ca82`。
审查对象为 `weil_source_decomposition.py`、冻结登记、12组来源结果、
`signed-source-audit.md` 与必要的004/016原件；未修改 STATE、cadence 或主脚本。
已恢复 AGENTS→README/STATE→check/show→Goal/C001/最新决策。
实际 `Get-Process python` 未列出 Python 进程；CIM 命令行读取不可用，
所以不将进程名检查说成所有运行任务的全面认证。本审查未留后台进程。

## 审查结论与范围

没有发现来源符号、完整交叉或固定/移动向量记账的代数错误。
无穷位 H 的正 Gram 和真实 p=2 移位导数不定证明正确，
新混合界的 alpha 及 pole 对应常数正确。
随后新增的纯有理H负向量证书也通过解析公式、区间运算与尾界逆审，见第6节。
这些支付的是指定正指标反向辅助核的结构；没有支付完整 Weil 正性、
连续最低态排序、全补空间或增长支集的统一估计。
因此本轮可保存限定引理和有限负对照，但不能晋级为宏观 Goal 完成或大规模方法类边界。

## 1. 数字按显式奇偶坐标独立复算

主脚本使用 B/H/d 块，本审查改用完整保存矩阵 W 与显式等距嵌入
`E_n=(e_n+e_-n)/sqrt(2)`、`F_n=(e_n-e_-n)/sqrt(2)`。
在110位普通 mpmath中直接形成 `O=F^T W F` 并重求最低向量。
固定向量用归档原核 v0；移动向量按内积与 v0 对齐符号。
对每个向量 v，直接求

\[
C=\begin{pmatrix}
e_0^TWe_0-o &e_0^TWEv\\
(Ev)^TWe_0 &(Ev)^TW(Ev)-o
\end{pmatrix},\quad o=(Fv)^TW(Fv),\quad D=\det C.
\]

再逐源投影并使用**所有有序源对**求和

\[
D=\sum_{s,t}(2A_sh_t-\beta_s\beta_t).
\]

这与主脚本按自项/无序交叉组织不同；beta平方所有交叉及 A/h交叉均保留。
perturbed prime:2 从保存 W_delta−W_0 加到保存原位置来源，不调用主脚本 qprime、blocks 或 source_scalars。
这里独立的是代数组织和保存数字的复算；不是对全部积分的独立重建。

12组均完成；证据为 `reverse-audit.json`，其绑定来源结果 LF SHA256。
最大绝对偏差约 `2.19443e-40`，来自50位、N6、delta=0的移动来源标量。
该点奇gap约 `5.6854e-12`，保存矩阵末位与50位对角化误差可被特征向量响应放大；
同点 D 的偏差仅约 `1.54932e-47`。未作 directed rounding，不能由这些误差认证谱符号。

冻结向量和移动向量的差别是实质的。以下列70位保存数字的直接复算（其余精度一致）：

| N | delta | fixed D | moving D | abs(v0·vdelta) |
|---:|---:|---:|---:|---:|
|4|+1/1000|−2.21915846e−6|−9.26028643e−6|0.39407034|
|4|−1/1000|2.08114903e−6|5.91413093e−5|0.84584171|
|6|+1/1000|1.90318006e−6|7.31830382e−6|0.50052467|
|6|−1/1000|−1.83184206e−6|8.97540834e−5|0.06543520|

最后一行说明 fixed D<0 不能被消费为扰动后全偶底低于全奇底：
固定 v0 此时是奇 Rayleigh试探向量，已经接近与真正奇底正交。
主脚本固定原点 D导数只适用于固定 v0；不包含移动向量 h、beta 的 v' 项。
所有12组 moving h 都为正，故本批来源排序不能被叙述为负 h 的强制机制。
原点 moving D 在N4约2.48674e−8、N6约1.12955e−8均为正；
D正也不否定实际有限偶底更低，因为此二维试探压缩只有充分入口。

## 2. 无穷位 Gram 证明复核

令 `c=2/L`、`omega_n=2pi n/L`、`t_j=2j+1/2`、`b_j=1-exp(-t_jL)>0`。
代码中 n,-m 及 n,0 都是 off-diagonal，常数/subtraction项消失。
几何级数 rho(x)=sum exp(-t_jx) 及周期正弦积分给

\[
H_\infty(n,m)=c\sum_j b_j
\frac{t_j^2+\omega_n\omega_m}
{(t_j^2+\omega_n^2)(t_j^2+\omega_m^2)},\quad
d_\infty(n)=c\sum_j\frac{b_j}{t_j^2+\omega_n^2}.
\]

对任意有限复系数向量也有（实系数为主合同对象）

\[
h_\infty=c\sum_j b_j\left(t_j^2|R_j|^2+|S_j|^2\right),\quad
R_j=\sum_n\frac{v_n}{t_j^2+\omega_n^2},\quad
S_j=\sum_n\frac{\omega_nv_n}{t_j^2+\omega_n^2}.
\]

每项非负。若有限 v 非零，R_j不能全零：
R(t)的有限有理分子若在无限 t_j处为零必恒零，各不同极点留数再强制 v=0。
故 H∞每个有限截面严格正定。积分换序合法：正弦近零为O(x)，rho为O(1/x)，
绝对乘积可积；有限 n,m不存在统一高指标换序的偷换。
不能把 H∞严格正定推成完整 arch W严格正定；H仅是反向块，
完整 arch 的 diagonal subtraction及 multiplier谱底仍须保留。

## 3. 新混合界的 alpha 独立证明

由以上 Gram 特征，Cauchy–Schwarz直接给

\[
|d_\infty^Tv|^2=
\left|c\sum_j b_jR_j\right|^2
\le\left(c\sum_j\frac{b_j}{t_j^2}\right)
\left(c\sum_j b_jt_j^2|R_j|^2\right)
\le\alpha_\infty h_\infty,
\quad\alpha_\infty=\frac2L\sum_j\frac{1-e^{-t_jL}}{t_j^2}.
\]

alpha有限且正确；beta∞=sqrt(2)d∞·v时必须保留
`|beta∞|²≤2alpha∞h∞` 的2，不能漏掉。
对 pole，设 gamma=8sinh²(L/4)/L、t=1/2，则

\[
H_P=\gamma(rr^*+ss^*),\quad
r_n=\frac t{t^2+\omega_n^2},\quad
s_n=\frac{\omega_n}{t^2+\omega_n^2},\quad
d_P(n)=\frac\gamma{t^2+\omega_n^2}.
\]

因此 `|dP·v|²≤alphaP hP`，`alphaP=gamma/t²=32sinh²(L/4)/L`。
背景 B=P+infty 的同向交叉也可用一次 Cauchy保留：

\[
|d_B^Tv|^2\le(\alpha_P+\alpha_\infty)(h_P+h_\infty).
\]

在L=log13，普通数字核对 alpha∞≈2.48712032150857，alphaP≈5.87271282561325。
alphaP随L增长为 `8exp(L/2)/L(1+o(1))`，不是趋零误差。
这些有限系数估计只约束背景 dB、hB；完整 d=dB+dR 与 h=hB+hR仍含
素数及 `2dB·v dR·v` 交叉。没有 hR下界和 dR的有符号控制，
不能替换成 `|d·v|²≤alphaB h`，不能决定完整 D或W符号。
对任意连续 form-domain函数的闭合及增长L统一预算本审查没有证明。

## 4. 真实 p=2 导数不定的严格角度核验

在L=log13、a=log2、w=log2/sqrt2，
`2^3<13<2^4`给 `1/4<log2/log13<1/3`，故
theta=2pi log2/log13严格在(pi/2,2pi/3)。
c1=cos theta属于(−1/2,0)，c2=cos 2theta属于(−1,−1/2)。
正因子2w/L除去后，H'_R的1,2主块为

\[
\begin{pmatrix}c_1&(c_1+2c_2)/3\\(c_1+2c_2)/3&c_2\end{pmatrix},\qquad
\det=-\frac{(c_1-c_2)(c_1-4c_2)}9<0.
\]

两个括号严格为正，所以全N≥2导数都有正、负方向。
数字−0.0511071618294只作转录核对，负号不依赖数字。
它排除指定H的局部Loewner单调；没有证明完整W'_delta不定的全部谱，
没有排除其他联合估计，没有将位移分布称为新Euler积。
signed-source-audit中的奇O' off-diagonal式、diagonal独立分支及a0'=2w/L也正确。

## 5. 重复性、晋级和宏观结算

004已支付奇偶块、极点完整form符号及有限/尾认证；016已有P−V及指定逐块范数no-go。
本次精确H∞ Gram、混合alpha和p2指定导数边界不同于这些对象。
基线关键词检索未发现这些相同式，但并未逐篇阅读526篇原件，
不能声明绝对内部无重复，更不能声明文献首创。
固定/移动区别、D二维判据及保留交叉是既有约束，不能重记为新方法。

真实新增独立内容是辅助背景核的Gram及混合耦合界、指定实际原子导数的严格反例，
以及第6节同一完整实际H的指定负向量；
未付是完整素数有符号求和、背景/素数混合、低簇稳定与连续补空间/增长尺度。
实际宏观瓶颈没有改变。
停止规则：若新恒等式不能控制完整素数/混合项，冻结继续扩N或增加小数的技巧。
重新准入：能在同一实际核上控制hR、dR及交叉并付连续范围/费用的新算术输入。
唯一下一动作：主代理复核本审查与保存来源账本（包括第6节证书）后，
冻结“完整H正性”这条捷径；按C001止损结束数值扩展并保存宏观下一机制，
不能因辅助引理或指定负向量成立取消止损。

## 6. 新增纯有理 H 负向量证书的逆审

本节是父代理追加要求：审 `scripts/weil_h_signed_witness.py` 与
`rational-witness.json`。报告中的脚本字节SHA256与实际文件一致；
本审查没有重复执行会覆写该报告的main，而是逐行审证明步骤，
以精确Fraction复核保存的上端求和账本，并用不同组织方式独立积分核对。

**解析对象正确。** 固定v=(1,−1)、L=log13，完整实际正指标H满足

\[
h(v)=H_{11}+H_{22}-2H_{12}=h_P+h_\infty+
\sum_{k\le13}\frac{\Lambda(k)}{6\pi\sqrt k}
\left[2\sin(\omega_1\log k)-\sin(2\omega_1\log k)\right].
\]

素数幂清单2,3,4,5,7,8,9,11,13完整；13项严格为零，
脚本保留其外包近零区间只会使上界略松，不改变对象。
pole写K=8/L(exp(L/2)+exp(−L/2)−2)=4gamma，
f_n=(1+4omega_n²)^−1，给
`hP=K[(f1−f2)²+(2omega1 f1−2omega2 f2)²]`，因子正确。

**区间运算正确。** down用Fraction整数除法向负无穷取整，up=−down(−x)，
包括负数端点也外包；加减、四端乘除外包正确。
除法先要求分母端点乘积>0，排除零。
非负整数幂对奇幂单调；偶幂跨零时下端置0，否则两端极值外包，均合法。
所有输入来自整数/Fraction/已有区间，没有把普通浮点用于证书运算。

**初等常数与函数余项正确。** log用z=(k−1)/(k+1)的正atanh级数，
M项后余项≤2z^(2M+1)/[(2M+1)(1−z²)]。
atan(1/k)交错级数用首个遗漏项绝对值作双向余项，
Machin pi=16atan(1/5)−4atan(1/239)正确。
sqrt整数的isqrt(k·GRID²)端点对开平方外包。
sin保留奇项至199次；按200次Taylor展式，200次偶项为零，
故余项≤max|x|^201/201!合法，而不需要限制角度在小区间。
exp先缩到[0,1/2]，保留0..99次正项，尾项几何界
`xhi^100/100!/(1−xhi/101)`正确，再用正数平方恢复尺度。
各阶乘以精确正整数作端点除法，避免预先把极小阶乘倒数外包到固定格导致巨大误差。

**Arch尾正确。** t_j间距为2。r_n=t/(t²+omega_n²)、s_n=omega_n/(t²+omega_n²)，
对j≥J有

\[
|r_1-r_2|\le(\omega_2^2-\omega_1^2)t^{-3},\qquad
|s_1-s_2|\le(\omega_1+\omega_2)t^{-2}.
\]

利用1−exp(−tL)≤1和
`sum_(j≥J)t_j^(−p)≤t_J^(−p)+t_J^(1−p)/[2(p−1)]`，
脚本的6次及4次幂尾外包正确。
j≥10的指数因子以1替换，只提供上界，并不提供实际部分和的下界；
最终 `arch_upper=[0,arch.hi+remainder.hi]`显式恢复合法下界0。
因此报告中arch_nonnegative_upper是整体arch的合法区间，
中间arch变量不可另行声称实际部分和的双向包围。

精确有理账本核验了prime_total上端≥每项上端之和，
witness上端≥pole/arch/prime_total上端之和，且该上端严格负：

\[
v^THv\le
-\frac{24474240198438492695402052180959462842377333383873179133634808155030450483}
{57896044618658097711785492504343953926634992332820282019728792003956564819968}<0.
\]

与Gram级数不同的100位数值转录：直接组合原正弦积分

\[
h_\infty=\int_0^L\rho(x)
\frac{2\sin(\omega_1x)-\sin(2\omega_1x)}{6\pi}\,dx
\]

给hP≈0.0581152254481209611，h∞≈0.0417667579336725995，
hR≈−0.1003055094500892403，完整h≈−0.000423526068295680。
证书上端≈−0.000422727327223166，比该数值高约7.98741e−7，
符合正尾预算；数值本身不承担严格符号认证。
这些附加检查保存进 `reverse-audit.json` 的 rational_witness_review。

**新增指定边界，保持宏观限度。** 对所有N≥2，嵌入该向量给实际L=log13的完整H不是半正定。
因此仅从反演、自伴、各背景Gram，推出完整H≥0的捷径已严格失效；
任何无条件全向量 `|d·v|²≤alpha v^THv`（alpha>0）也不可能成立于这个H。
这没有证明W不定，H不是完整Weil二次型，H的负方向可以与W正性相容。
它不排除保留O和a0的完整联合估计，也没有给真实最低奇向量的D符号。
孤立H反例及这条小方法类边界不达到长期Goal要求；宏观正性瓶颈仍未改变。
