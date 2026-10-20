# 561. 正 Beurling 测度、自对偶的边界与纯分析恢复整数

2026-10-20，C024。固定 G20261014 文本目标／0c4f≤538；用户新材料准入。
独立终逆审 PASS；root 消费范围与版本见 reviews/2026-10-20/root-consumption-scope.json。
不声明文献首创，不证明 RH。
两项检验属于同一个分析选择条件迭代：宽自对偶条件的反例，以及固定 Fourier 核下的整数识别。

## 1. 先分开三个对象

在对数坐标 u≥0 上，P 是 primitive g-prime 测度，Π 是 prime-power 测度，
M 是含单位 δ0 的 g-integer 测度。记 T_k(u)=ku，要求

\[
 \Pi=\sum_{k\ge1}\frac1k(T_k)_*P,\qquad
 M=\exp_*\Pi:=\delta_0+\sum_{j\ge1}\frac{\Pi^{*j}}{j!},\qquad
 Z(s)=\int_0^\infty e^{-su}\,dM(u)=\exp\int_0^\infty e^{-su}\,d\Pi(u).
 \tag{1}
\]

先在 Re s>1 支付收敛。k 是 Euler 因子的重复度，j 是卷积次数；
这些离散指标不输入任何特殊整数／素数分布。一般 signed distribution 没有此正 Euler 含义；
以下先取正 Borel 测度这个非空子类。物理计数 N(x)=M([0,log x])。

## 2. 宽自对偶＋很强计数正则性仍不充分 [proved]

固定 0<a<1/2，b=1-a，c=ab。定义

\[
 Z_a(s)=\frac{(s-a)(s-b)}{s(s-1)}=1+\frac{c}{s(s-1)}.
 \tag{2}
\]

### 正的 primitive 测度和完整 Euler 关系

令 A_m=1-a^m-b^m。A_0 不使用，A_1=0，且 0<A_m<1 对每个 m≥2 成立。
设 C_m=Σ_{k≥1}k^{-m-1}，只是有限正实数，并定义

\[
 p_a(u)=\frac1u\sum_{m\ge2}\frac{A_m u^m}{m! C_m},\qquad dP_a(u)=p_a(u)\,du.
 \tag{3}
\]

级数局部一致收敛，p_a>0，u→0 时 p_a(u)=O(u)；0<p_a(u)≤(e^u-1-u)/u。
故 P_a 局部有限，e^{-σu} 可积对每个 σ>1 成立。
推前密度与全部重复度的正项 Tonelli 给

\[
 \sum_{k\ge1}\frac1{k^2}p_a(u/k)
 =\frac1u\sum_{m\ge2}\frac{A_m u^m}{m! C_m}\sum_{k\ge1}k^{-m-1}
 =\frac{e^u+1-e^{au}-e^{bu}}u=:q_a(u).
 \tag{4}
\]

因此 Π_a=q_a du 是真实全 prime-power 测度，不是把一个正 Π 免费叫作正 primitive。
分子也可由凸性看出非负；Taylor 正系数另给 primitive 的独立正性。
Frullani 积分在 Re s>1 给

\[
 \int_0^\infty e^{-su}q_a(u)du
 =\log\frac{s-a}{s-1}+\log\frac{s-b}{s}
 =\log Z_a(s),
 \tag{5}
\]

分支由实 s>1 的正值及右半平面解析延拓固定；复 s 的交换用 σ=Re s>1 绝对费。
对每个σ>1，e^{-σu}Π^{*j}=(e^{-σu}Π)^{*j}，总质量级数为exp(∫e^{-σu}dΠ)<∞，
因此正卷积指数存在并且 Laplace 变换等于(2)。由加权有限测度 Laplace 唯一性得

\[
 dM_a(u)=\delta_0+c(e^u-1)du,\qquad
 N_a(x)=1+c(x-1-\log x)=cx+O(\log x).
 \tag{6}
\]

这既付正整数测度，也付准确计数和全部误差；不只是形式 Euler 级数。
primitive 在每个 u>0 上都有正密度，因而不是 lattice 点列。

### 精确函数方程及显式离线零点

Z_a(1-s)=Z_a(s)。清除两个极点后的

\[
 X_a(s)=s(s-1)Z_a(s)=(s-a)(s-b)
 \tag{7}
\]

为实型、有限阶、genus 0、自对偶整函数，却有 a,b 两个离中心线零点。
中心变量 s=1/2+iz 下 X_a=−(z²+r²)，r=1/2-a>0，零点为 z=±ir，非实。
可固定 a=1/4，c=3/16，不使用实际 ζ 的零点数值。

严格范围：Z_a 额外在 s=0 有极点，X_a 只有两个零点；
没有经典 π^{-s/2}Γ(s/2)，没有经典零点密度，也没有离散广义整数。
它排除的是允许一般有限极点缺陷／一般 completion 的宽条件包。
它不反驳经典 Gamma／固定 Gaussian 约束，也不反驳完整 Weil 正性作为充分条件。

### 不把普通测度正性误认为 Weil 正性

令 F_f(z)=∫_R f(t)e^{zt}dt，f∈C_c^∞(R)，f*(t)=overline(f(-t))，h=f*f*。
两极点 0,1 的完整平衡与(4)给

\[
 W_a(h)=\int_\mathbb R 2\cosh(rt)h(t)dt,
 \quad Q_a(f)=W_a(f*f^*)=2\Re\{F_f(r)\overline{F_f(-r)}\}.
 \tag{8}
\]

具体地，极点密度 2cosh(t/2) 减去 prime 密度
|t|e^{-|t|/2}q_a(|t|)=2cosh(t/2)-2cosh(rt)，正好留下(8)。
取 f(t)=tφ(t)，φ 为非零、非负、偶的 C_c^∞ 函数，则 F_f(-r)=−F_f(r)，
且 F_f(r)=2∫_0^∞tφ(t)sinh(rt)dt>0。于是

\[
 Q_a(f)=-2F_f(r)^2<0.\tag{9}
\]

W_a 的密度本身处处为正，仍非卷积正定；它指数增长而非 tempered，
不能由普通正测度或未经核域的 Bochner 口号推出正谱测度。

## 3. 固定 Fourier 自对偶＋单位空隙恢复整数 [proved]

Fourier 约定 \(\widehat f(\xi)=\int f(x)e^{-2\pi ix\xi}dx\)。
设 μ 为 R 上正 tempered 测度，满足

\[
 \widehat\mu=\mu\text{ in }\mathcal S',\qquad
 \mu|_{(-1,1)}=\delta_0.\tag{10}
\]

**结论：μ=Σ_{n∈Z}δ_n。** 不预设离散、整数支撑、乘法闭包或唯一分解。

取实偶 h_j∈C_c^∞(-1/2,1/2) 在 L¹ 和 L² 中逼近区间指标，
令 f_j=|check h_j|²≥0，tilde h(x)=overline(h(-x))。f_j∈S，且
\(\widehat f_j=h_j*\widetilde h_j\) 支持在(-1,1)。
由(10)，

\[
 \int f_jd\mu=\int\widehat f_jd\mu=\widehat f_j(0)=\|h_j\|_2^2\to1,
 \qquad f_j(0)=\left|\int h_j\right|^2\to1.\tag{11}
\]

μ=δ0+ν，ν≥0，故 ∫f_jdν→0。L¹ 收敛使 check h_j 一致趋向
\(\sin(\pi x)/(\pi x)\)。对 ν 用 Fatou 得

\[
 \int\left(\frac{\sin\pi x}{\pi x}\right)^2d\nu(x)=0.\tag{12}
\]

正性使 ν 的支撑是该连续非负函数零集 Z\{0} 的子集；这一步得出整数，
没有在输入中假设整数。于是 μ=Σc_nδ_n，c_0=1。
支撑在 Z 推出 e^{2πix}μ=μ，Fourier 变换推出 μhat 为 1 周期；
自对偶再给 μ 为 1 周期，故 c_n=c_0=1。证毕。

正性和单位空隙承担实际责任。自对偶本身有其他正例，不能宣称一般自对偶皆是整数：
对 d>0，(δ_{dZ}+d^{-1}δ_{Z/d})/(1+d^{-1}) 也是归一化正自对偶测度，
若 d≠1 则在(-1,1)还有非零支撑。Lebesgue 测度与 δ0 的等权和也是正自对偶。

### 固定 Gaussian 版本

设 μ 为**偶**正 tempered 测度，θ_μ(t)=∫e^{-πtx²}dμ(x)，t>0。
若对所有 t>0 有精确恒等式

\[
 \theta_\mu(t)=t^{-1/2}\theta_\mu(1/t),\tag{13}
\]

则 μhat=μ：ν=μhat−μ 为偶 tempered distribution，Gaussian Fourier 公式给
ν(e^{-πtx²})=0。此族在 S 中可任意次微分，故 ν 消灭所有
x^{2m}e^{-x²}（在 t=1/π 取导）。缩放后的偶 Hermite 函数的有限线性张成在偶 S 中稠密，
而它们正是偶多项式乘 Gaussian，故 ν=0。奇部分由偶性为零。
所以(13)＋单位空隙同样恢复完整整数梳。
这里 kernel、全部 t、指数1/2、缺陷归一化都固定，不能依对象任意选择核。

## 4. 识别 ζ 与证明 RH 是两条不同箭头

由§3取正半轴部分 dN=Σ_{n≥1}δ_n，可在 Re s>1 得其 Mellin 变换
Σ_{n≥1}n^{-s}=ζ(s)；这是识别后果，不把整数支撑预先写进输入。
同时 θ_μ(t)=1+2Σ_{n≥1}e^{-πtn²}，产生经典 Gamma 的 Mellin 接口。
但§3的 Fourier 正性在加法 x 空间；§2/Weil 的卷积正定性在乘法对数变量 t 空间。
两者不同，log n 不是等距格点，不能把(11)的正平方免费搬成完整 QW≥0。
Weil 原型／全源／原 norm／Γ／全部 pp／双 pole／成长极限仍须独立支付。

因此，一个符合用户设想的分析纲领已可精确分为：

固定 Fourier／Gaussian 对偶＋正性＋最小空隙 → 整数梳 → 经典 ζ；

以及尚未闭合的：该加性结构 → 独立乘法全 Weil 正性 → 通常 Ξ／RH。
此外，(10)或(13)配单位空隙已经把类压成单个单位整数梳；
因而“此类所有对象都满足RH”仍与经典RH等强，分类本身没有降低正性责任。

## 5. 最强旧对照、归属与净后果

[290](290-positive-euler-duality-model-and-mass-moment-nonidentification.md)已用正整数闭点 Euler、
精确函数方程甚至代数对偶／HL 证明“正Euler＋自对偶不付中心线”。
其 q^n 带 B_n 重数确为一个合法离散 Beurling 多重集；但几何空隙不许 N(x)/x 趋正常数。
§2 新增交集是**正 primitive 连续非 lattice＋N=Ax+O(logx)＋精确自对偶同时**；
不能把旧逻辑否定再登记为新 theorem。§3给本仓可直接复核的纯分析整数识别，
是标准 Fourier／正测度工具的推论，不冒称新的外部定理或首次发现。

081–088 主要是 Nyman–Beurling 逼近，不能因同名充当 generalized primes 的既有基础。
[546](546-arithmetic-comb-full-weil-positivity-and-form-core-noncoverage.md)的特殊正源及补空间不覆盖
成长全 Weil 型；518–526 的谱商／等价酉化不付独立正性，亦不能在此复活。
目前实际 ζ 最强 whole 4/5 与核心／Ξ 缺口均未改变，宏观完成门仍 open。

原始框架参照 Hilberdink–Lapidus [§3](https://arxiv.org/abs/math/0410270)：
一般 Mellin 配对的广义函数方程要核核函数、缺陷、收敛与增长，不能自动升级成经典自对偶。
Fourier 分类背景见 [Baake–Spindeler–Strungaru](https://doi.org/10.1007/s00041-023-10045-z)；
此处具体§3证明自包含，不引用背景分类支付缺失前件。

附件审计、历史代表原件索引、原始文献精确前件分别见 reviews/2026-10-20 三份独立原稿；
消费状态／修订／停线／唯一下一动作见 root 收据与 STATE，不由本稿标题宣告已 root 消费。
