# 一次实际正分布构造：二维 ξ 曲率的纵向边际及其准入失败

2026-10-28；G20261027／runtime1793085111／原0c4f。仅自主构造一个实际公式并做最便宜自筛；不重开577参数、Sonin投影、来源搜索或已停合同。本稿是支持稿，不代root消费或计轮。已恢复README／STATE、check→show、Goal／宏观前沿／C048和当前下一动作；工作树中STATE及其他并行输出由root负责。本稿仅本地推导，无外网、PDF、下载或数值。

**结论。** 下式确实独立于未知根位置的选取，给出有限正谱测度及正型分布。其迭代极限却只记录全部零点的纵坐标和重数；完整Weil型还需要横向权。旧562／578的同对象正负模型立即否定“仅凭该规则便获得完整Weil身份”的通用论证；实际ξ的身份未付，故没有形成新的经典signed输入，建议按构造自筛／标准强旧0收讫并止此recipe。不是经典RH反例，也不是一般曲率方法的不可能定理。

## 1. 唯一实际规则及其输入

采用通常归一化
\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{1}
\]
这可完全从旧405的实际整数theta源取得，不输入根的位置：
\[
 \eta(x)=\pi x^2(\pi x^2-3/2)e^{-\pi x^2},\quad
 h(u)=2\sum_{n\ge1}\eta(ne^u),\quad H_\theta(u)=e^{u/2}h(u),
\]
\[
 \xi(s)=2\int_{\mathbb R}H_\theta(u)e^{(s-1/2)u}\,du.
 \tag{2}
\]
405的M_h(s)=s(s−1)Λ(s)/4给出此系数2；若改用无1/2的completion，系数应4，有限ε也须相应重标。Hθ为已付实S_exp源，式(2)在全复平面成立；这里不是猜测一个未知正极化H。解析定义不选择零点，但极限分析会读出这个实际ξ的完整complex除子，不能把这一点说成已经独立识别纯线。

先固定0≤χ∈Cc∞((-1,2))、χ=1于[0,1]；固定偶的0≤τ∈Cc∞((-2,2))，τ=1于[−1,1]且随|t|不增。令τ_T(t)=τ(t/T)，T≥1。对ε>0定义
\[
 \boxed{\kappa_\epsilon(\sigma,t)
 =\frac{\epsilon^2|\xi'(\sigma+it)|^2}
 {\pi(|\xi(\sigma+it)|^2+\epsilon^2)^2}},
\]
\[
 w_{\epsilon,T}(t)=\tau_T(t)\int\chi(\sigma)
           \kappa_\epsilon(\sigma,t)d\sigma,\qquad
 d\nu_{\epsilon,T}=w_{\epsilon,T}(t)dt,
\]
\[
 W_{\epsilon,T}(u)=\int e^{-itu}d\nu_{\epsilon,T}(t).
 \tag{3}
\]
ν为有限、偶、非负测度。源仍是原physical r=e^{u/2}f，r*=overline{r(−u)}，Fourier为hat r(t)=∫r(u)e^(−itu)du；因此对全部complex compact源
\[
 Q_{\epsilon,T}(r)=W_{\epsilon,T}(r*r^*)
                =\int|\widehat r(t)|^2d\nu_{\epsilon,T}(t)\ge0.
 \tag{4}
\]
这既不是从g_R负部clipping，也不是把目标membership当输入；正号来自实际二维密度。

## 2. 归一化、multiplicity及cutoff边界

令Uε=½log(|ξ|²+ε²)，Δ=∂σ²+∂t²，则直接微分给
\[
 (2\pi)^{-1}\Delta U_\epsilon=\kappa_\epsilon.
 \tag{5}
\]
核1/π与重数不可混：对局部模型f(z)=z^m，半径R圆盘上的曲率总质量是
\[
 \int_{|z|<R}\frac{\epsilon^2m^2|z|^{2m-2}}
 {\pi(|z|^{2m}+\epsilon^2)^2}dA
 =m\frac{R^{2m}}{R^{2m}+\epsilon^2}\longrightarrow m.
 \tag{6}
\]
一般零点写成(z−ρ)^m g(z)、g(ρ)≠0，局部log可积，Uε→log|ξ|于L1_loc；(5)遂给标准Poincaré–Lelong局部质量∑mρδρ。这里只闭合此定义所需局部计算，不建立新的全局定理。

二维到t边际使用**固定χ、固定T下先ε↓0**。对光滑φ(t)，实际紧支测试为χ(σ)τ_T(t)φ(t)。分部积分是
\[
 \int\kappa_\epsilon\chi\tau_T\phi\,d\sigma dt
 =\frac1{2\pi}\int U_\epsilon
       [\chi''\tau_T\phi+\chi(\tau_T\phi)'']d\sigma dt.
 \tag{7}
\]
不能丢χ″、τ′或τ″，不能把二维曲率偷换成一维log的二阶导。它们在原紧支测试中合并保留；不声称各个边界项分别消失。ξ的全部零点在0<Reρ<1，故χ在每个零点上恰为1，水平transition不会漏掉零点质量。于是
\[
 \nu_{\epsilon,T}\ \xrightarrow[\epsilon\downarrow0]{\rm weak}
 \sum_\rho m_\rho\tau_T(\gamma_\rho)\delta_{\gamma_\rho},
 \qquad\gamma_\rho=\Im\rho.
 \tag{8}
\]
不存在本稿已付的joint ε(T)收敛率；ξ在紧矩形上的极小值／相近零点费用也没有被无声支付。

## 3. 原范数、源成长和实际极限范围

记Mε,T=ν(R)。每层有
\[
 Q_{\epsilon,T}(r)\le M_{\epsilon,T}\|r\|_1^2,
 \quad
 Q_{\epsilon,T}(r)\le2\pi\|w_{\epsilon,T}\|_\infty\|r\|_{du}^2,
 \tag{9}
\]
\[
 \|w_{\epsilon,T}\|_\infty
 \le\frac{\|\chi\|_1}{\pi\epsilon^2}
     \sup_{-1\le\sigma\le2,\ |t|\le2T}|\xi'(\sigma+it)|^2.
\]
这些是每先fixed ε,T的真实费用。若supp r⊂[−L,L]，第一界至多2LMε,T||r||du²；对S_exp，p_N,0(r)=sup e^(N|u|)|r(u)|给||r||1≤2p_N,0/N。第二界亦按Plancherel原dt/(2π)运输到zero-extension Dlog，因为
\[
 \|r\|_2^2\le(\log2)^{-1}
 \int\log(2+|t|)|\widehat r(t)|^2\frac{dt}{2\pi}.
\]
不宣称ε↓0、T↑∞时这些global du费用有uniform上界；L、T和ε各自独立，也不把T叫算术cutoff。

在(8)后再令T↑∞。旧零点计数N(T)=O(TlogT)与每先fixed r∈Cc∞的Schwartz Fourier尾给绝对收敛；同理对fixed S_exp源成立。由此得到正型温和分布
\[
 W_{\rm ord}(u)=\sum_\rho m_\rho e^{-i\gamma_\rho u},\qquad
 Q_{\rm ord}(r)=\sum_\rho m_\rho|\widehat r(\gamma_\rho)|^2\ge0.
 \tag{10}
\]
对任意fixed compact测试也由其Schwartz Fourier尾得D′收敛。式(10)是分布求和，不是无条件逐点函数级数；全源逐一成立不等于moving源统一误差。此处没有whole迹／HS／Sonin逆的对象身份。

## 4. 与完整Γ／all-prime-power／双pole的缺口是实质的

实际目标仍逐项保留578的
\[
 W_\zeta=W_\Gamma+2\cosh(u/2)du
 -\sum_{n=p^k\ge2}\Lambda(n)n^{-1/2}
              (\delta_{\log n}+\delta_{-\log n}).
 \tag{11}
\]
WΓ含完整FP及指定contact，Λ(p^k)=logp，0、1两个pole全部保留。式(1)虽然包含实际Γ及pole清除因子，**(3)并没有证明与(11)的分布身份**：completion中的解析因子被包含，不等于curvature边际保留了它们在物理公式中的系数和方向。

精确差异可由原显式公式诊断。令αρ=Reρ−½、L_r(z)=∫r(u)e^(zu)du。完整零点侧为
\[
 Q_\zeta(r)=\sum_\rho m_\rho
 L_r(\alpha_\rho+i\gamma_\rho)
 \overline{L_r(-\alpha_\rho+i\gamma_\rho)}.
 \tag{12}
\]
而(10)只有α=0后的|L_r(iγ)|²总和。二者之差是逐个横向加权配对减去纵轴平方和；写出它没有给出独立误差估计。对实际ξ，本稿不知二者相等与否，不作已知不相等的断言。对全部compact卷积平方证明(10)等于(12)，将给完整Weil正性，正是本次未付的核心箭头，不能叫已知transport或仅有小边界误差。也没有把这项未知差重命名为新Ω、负部或输入。

## 5. 最便宜test已由强旧决定；不启动后继预算

直接使用旧562／578已消费的实际continuous positive-primitive模型，不重新建反例或计算537：
\[
 Z_c(s)=1+\frac c{s(s-1)},\quad E_c(s)=s^2-s+c.
\]
模型保全部Euler repeats、两个pole且native Γ=0。正例c+=5/16的根为½±i/4，纵向测度δ±1/4，恰给native 2cos(u/4)du。负例c−=3/16的根为¼、¾：同一规则只给
\[
 \nu_{\rm ord}=2\delta_0,\quad W_{\rm ord}=2du,
 \qquad W_{\rm native}=2\cosh(u/4)du.
 \tag{13}
\]
旧578的非零非负偶η0、r1=(D²−¼)η0、r−=r1−τ_h r1，h≠0，已付两个pole矩为0；其mean也为0。因此本规则Qord(r−)=0，而旧(13)已给Qnative(r−)<0。丢横向权而取得正号，不能成为原型的正性证明。这只检验transport机制；Γ=0负模型不冒称经典Γ反例。

最短强旧链为：562的同一带重数谱／Weil身份要求＋其正负相变模型，564的预定权／faithful谱规范责任，578的原源负control，已经决定(13)的后果。标准局部曲率计算只是识别本规则落在这条旧链中；没有新的whole-family边界或经典净后果。

576已给宽正锥及membership缺口；577的clipping／q_R等价、578的PNT／Selberg／Toeplitz／平方／全k旧界均不补横向权；585已付actual t、K正成长必要费但不是curvature误差界。旧安全high和542＋555→557 whole4/5负惯性UPPER都不因(3)变化。故本次确有自主提出并核实的正D′生成规则，**仍无可准数学的独立经典input**。尚欠的恰是同(11)全Γ／contact／all pp／双pole、原源和合法极限下的完整signed身份或独立净费用；本稿不把它列成已经存在的合同，也不续ε/T参数、横向moment变体、paper或其他recipe。
