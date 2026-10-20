# 局部二次能量选定Gaussian：能排核gauge，不能替代Weil正性

2026-10-20，C028 root原推导。标准harmonic oscillator基态知识不是新定理；
此处新增固定消费测试是564的正self-Fourier gB能否通过一个独立、物理侧的核选择。
本稿所有范数均为L²(R,dx)，与经典Weil的log域Dlog明确不同。

## 1. 输入是局部背景，而不是未知零点

固定加法R及Fourier约定Ff(ξ)=∫f(x)e^{-2πixξ}dx。
在V=H¹(R)∩{g:xg∈L²}取闭二次能量

    E(g)=||g′||²+4π²||xg||².

它是位置与动量的对称二次能量；Fourier交换两项。它不由bare g-integer的
计数measure或Mellin反射自动给出，而是额外指定的local Euclidean结构。
其使用不显式利用整数/素数，也不使用任何ζ零点位置。

在Cc∞分部积分，2Re∫g′ overline(xg)=-||g||²，故

    E(g)-2π||g||²=||g′+2πxg||² >=0.                 (1)

Cc∞在V的图范数中稠密：先平滑cutoff，x乘子尾由xg∈L²控制，cutoff导数
由g∈L²控制，再mollify有界支撑对象。所以(1)在全部complex V成立，无边界项。
等号当且仅当g′+2πxg=0于D′。局部积分因子得g=C exp(-πx²)。
它在V内，故下界2π恰为最小值，等号一维。正核以g(0)=1或∫g=1归一均给

    g0(x)=exp(-πx²),    G0(s)=1/2 π^{-s/2}Γ(s/2), Re s>0. (2)

该选择并非先假设completed函数没有零。只须在物理x侧核验一个一阶微分身份。
更抽象地，先给二次metric及Fourier pairing，选择其最小energy真空；尺度须固定。
任意宽度的Gaussian族不能凭“最小不确定性”四字唯一选出g0，必须保上述固定能量。
通常ladder-operator基态知识核作者课程[Peeters §15.4–15.6](https://www.maths.dur.ac.uk/users/kasper.peeters/mathphys/harmonic_oscillator.html)；(1)和域闭包由本稿直接证明。

## 2. 对564的已知正核作精确负对照

固定A=2^{1/4}，

    gB=(1+A²/2)g0 + A g0(2x) + (A/2)g0(x/2),
    B(s)=(1+A 2^{-s})(1+A 2^{s-1})=B(1-s).

564已付gB>0、Schwartz、F gB=gB、GB=B G0、完整theta/poles及E_B=Bξ。
若将gB除以B(0)，mass/pointvalue/pole residues与g0相同，旧反例仍有含零gauge。
这里不重证或重计这些旧资产，只核新selector：

    (∂+2πx)gB = 2π A x[-3 exp(-4πx²)+(3/8)exp(-πx²/4)]. (3)

括号不恒零（例如x=0的括号为-21/8），故(1)右边严格正。
用∫x²e^{-πd x²}dx=(2πd^{3/2})^{-1}还能精确算出

    E(gB)-2π||gB||²
      = π[9/4 - 36√2/(17√17)] >0.                 (4)

最后严格不等式等价于17√17>16√2，平方是4913>512。
归一gB/B(0)将(4)除以B(0)²，不会消去缺陷。
因此它通过positive/Fourier/defect normalization，却不能通过同一固定局部energy基态条件。
这给一个非循环排B的具体条件，代价是增加local quadratic metric/ground-state选择。

更一般地，若某允许核g∈V满足该等号且归一为1，则g=g0，Mellin变换就是G0；
若G=B G0，由Re s>0中Gamma零自由立即得B=1于该半平面，延拓后全域恒等。
无需先检查B的根、更无需检查ξ的根。此selector同时排除零自由但改变核的非平凡gauge。

## 3. 选择与覆盖的界限

该输入只选择一个archimedean test kernel，不选择arithmetic distribution；
它既不构造Hilberdink–Lapidus的positive dual，也不给完成化Weil剩余量的正定性。
把(1)这个局部平方的非负直接写成经典Weil的平方和，没有同对象identity支持。
561 fixedGaussian＋正tempered物理measure＋unitgap的识别定理可再识别整数，
但那只是归约回经典ζ；经典全部Gamma/prime powers/poles的正性仍是原问题。

连续Zc=1+c/[s(s-1)]两段拥有同样的pole中心与已规定Gamma=0，
c>=1/4有正能量证书，c<1/4没有（563）。它们不是满足固定Gaussian FE的反例：
G0(s)Zc(s)与G0(1-s)Zc(1-s)的比是非恒定Gamma比，故该反射失败。
不能据此声称“canonical经典Gamma＋其FE仍有已知positive Beurling离线例”。

数域的local R/C模型可以给Gaussian产品和相应Gamma；这额外使用local fields、
维数、norm与self-dual measure。任意bare norm分布没有自动携带这些结构。
函数域无archimedean Gamma；其自然输入是几何次数、点数有理性、Frobenius与分次，
不应把一维Gaussian条件当作最一般RH必要条件。

## 4. 本次真正增加什么

新增的是“同一positive gauge”的可执行排除测试与其代价记录；不宣称新oscillator理论。
标准Gamma类的唯一性另由source稿恢复，不以假定completed E零自由作为前件。
选核这一箭头可独立闭合，向Weil正性／纯性的箭头尚未闭合；二者分开是本轮决策信息。
actualζ强旧542+555→557 whole4/5、560成长K、core/Ξ均无改善。
