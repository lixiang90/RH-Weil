# 312. 临界线正背景的系数障碍与方向性滤波代价

2026-09-06。VIS-REG第3轮。状态：[T/R] 下述实际临界线子背景上界及受限字典推论；
[C/O] 完整非实正背景的定量控制。前半由已授权独立审查者推导、主线程核读；
后半的方向性转移为本轮继续推导，独立复核待回报。
不作世界优先权声明，不以此单独完成phase2验收。

## 1. 含重数计数给sharp MT窗的Bessel上界

固定 b=1/sqrt2、A=(log T)/2及303的原始高度窗ηA。
按不同的实际临界线高度定义
\[
 B_Ra=\sum_{0<\gamma\le T}\sqrt{m_\gamma}a_\gamma f_\gamma,
 \qquad P_R=B_RB_R^*.
\]
只对实际临界线子集求和，未假设全部零点在临界线。
令
\[
 M_T=\sup_{j\in\mathbb Z}\sum_{\gamma\in[j,j+1),\,0<\gamma\le T}m_\gamma.
\]
无条件全部零点计数给 M_T≤C0 log T，临界线子集继承；低高度并入C0。
可由已归档Bellotti–Wong Theorem1.1的陈述推出此弱化界；本文不复核其全部数值证书。

对v∈L²，置F(t)=∫v(u)ηA(u)e^(itu)du。
Plancherel给 ||F||²=2π||ηAv||²、||F′||≤A||F||。
此处对傅里叶变量求导，不要求sharp窗端点平滑。
在任意单位区间J内，对微积分基本定理的起点积分可得
\[
 |F(x)|^2\le\int_J|F|^2+2\int_J|FF'|,\qquad x\in J.
\]
乘以每个区间的含重数点数并求和，再用Cauchy–Schwarz，得到
\[
 \begin{split}
 \sum_\gamma m_\gamma|F(\gamma)|^2
 &\le M_T(1+2A)\|F\|_2^2\\
 &\le {\pi\over\sinc b}(2+A^{-1})M_T\|v\|_2^2.
 \end{split}
\]
所以A≥1时，取C=3πC0/sinc b便有
\[
 \boxed{\|P_R\|=\|B_R\|^2\le C\log T.} \tag{1}
\]
不要求间距下界或简单性。实型子空间的同一界自然成立。

这是021的分离采样工具及178局部密度机制的直接延伸，证明自含；
不把经典Bessel机制列为新方法。它确实给实际子背景的无RH上界，但尚未控制全部P。

## 2. 目标自身正项不能免除临界线系数成本

条件性地取一个实际非实对 z=x+id、bar z，固定d∈(0,1/2)，T≥x。
记g=ηAe^(−ixu)cosh(du)、h=−iηAe^(−ixu)sinh(du)。
偶性给〈h,g〉=0。即使免费允许任意自身g系数c，若
\[
 \|h-B_Ra-cg\|\le\varepsilon\|h\|,\quad0\le\varepsilon<1,
\]
与h配对并用(1)便得
\[
 \boxed{\|a\|\ge{(1-\varepsilon)\|h\|\over\sqrt{C\log T}}.} \tag{2}
\]
若按未加权列写Σqγfγ，则 ||a||²=Σ|qγ|²/mγ。
没有先投影再错误假设g、h仍正交。

由端点Laplace估计（或显式积分）及固定d>0，
\[
 \|h\|^2\sim {\cos b\over4d\sinc b}{T^d\over\log T},
 \qquad \|a\|\gtrsim_d(1-\varepsilon){T^{d/2}\over\log T}. \tag{3}
\]
证明渐近时令u=A−v，使用cos(bu/A)→cos b和sinh²(du)∼e^(2du)/4；
两端贡献相等，中部指数小，∫0∞e^(−2dv)dv=1/(2d)。
这是所有这类逼近器的必要下界，没有证明该系数阶足够。

更直接地，即使c无惩罚，取H=||h||²，由与h配对可得
\[
 \inf_{a,c}\{\|h-B_Ra-cg\|^2+\lambda\|a\|^2\}
 \ge {\lambda\over C\log T+\lambda}H. \tag{4}
\]
证法：对t=||a||，残差至少(√H−√(C log T)t)+；优化其平方加λt²。
这不排除λ趋零时塌缩；λ≍log T时仅受限字典的正则化目标有固定相对下界。
若计入自身g的真实惩罚，左侧只能增大。

## 3. 完整正背景缺口必须显式保留

对另一非实点w=y+ie，一般有
\[
 \langle h_z,g_w\rangle=
 \int_{-A}^A\eta_A^2\sin((y-x)u)\sinh(du)\cosh(eu)\,du\ne0. \tag{5}
\]
故(2)不能免费用于含全部非实g的字典。令G为所允许非实正列的张成，
q=(I−ΠG)h；完整逼近误差仅给
\[
 \|a\|\ge {\big(\|q\|-\varepsilon\|h\|\big)_+\over\sqrt{C\log T}}. \tag{6}
\]
没有q的独立可见性下界，右侧可能为零。
全部P的范数也不受(1)控制：仅自身正列2m g⊗g的范数就可按T^d/log T增长。

## 4. 回到原算子时只支付测试方向的逆变换

这里提出一个比使用全局||P||更具体的继续方向，但先把有限变分公式列清。
保持**全部实际正负列**，写
\[
 A_T=P_R+2m g\otimes g+P_o-U_TU_T^*,
\]
其中Po包含除目标自身外所有非实正列，UT仍含所有负列，目标列为sqrt(2m)h。
记H=||h||²、L=log T，定义两个真实的方向成本
\[
 \alpha_T={\langle P_oh,h\rangle\over H},\qquad
 \beta_T={\|P_oh\|\over\sqrt H}.
\]
其他负列的贡献非正，故
\[
 -{\langle A_Th,h\rangle\over H}\ge2mH-CL-\alpha_T.
\]
令R=λ(P+λI)^−1、Q=RA_TR、v=R^−1h。由于自身g与h正交，
\[
 {\|v\|\over\sqrt H}\le1+{CL+\beta_T\over\lambda}.
\]
将单位方向v/||v||代入负迹的变分式，严格得到
\[
 \boxed{\operatorname{tr}Q_-
 \ge{(2mH-CL-\alpha_T)_+\over
             (1+(CL+\beta_T)/\lambda)^2}.} \tag{7}
\]
全部正项保留在αT、βT；其他负项只在合法下界中删除。
这里没有把αT、βT写成已证廉价量，也不要求原负谱预先已知。
式(7)本身是经典Rayleigh／合同变换的方向性使用，不能单凭它晋级。

受限情形Po=0时，λ≥CL给
\[
 \operatorname{tr}Q_-\ge\tfrac14(2mH-CL)_+.
\]
这展示了全局||P||代价可能过粗：自身g的范数很大，却不增加该测试方向的逆变换成本。
Po=0只在除目标外无其他非实对的配置中成立，不能作为无条件zeta结论。

## 5. 第3轮结算与第4轮的问题

已获得实际临界线子背景的可核算上界和受限逼近的必要系数成本。
这些没有消除非实正项，对完整正则化负迹还没有新增净预算。
下一轮只检验一个更具体的输入：是否能从实际节点位置／零点计数及明确分离条件，
独立界住(7)的αT、βT，使它比全局||P||转移有可证明的净收益；
先求远高度非实正项的显式尾界，近高度项保留，不能省略或假定下框架。
若该步骤仍只是既有条件框架，按GOAL结算并切换主候选。
