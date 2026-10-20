# 563 终逆审：分布证书、热CM与全周期算术lift

2026-10-20，独立终逆审。先恢复 README／STATE、check/show、固定 Goal／frontier、
C026／D20261020C 战略，后逐件读563及本目录三个原稿、JSON和精确脚本。
只写本审查，不改公共状态、原证明或Git。审查0轮，不消费为经典RH／whole新输入。

**裁决：PASS，未发现需先修复的数学错误。** 以下结论只在原稿明确的前件和范围内通过；
结构check、脚本成功和hash都不替代证明。C026可由root按完整前件收据结算一次，
不据此完成G20261014宏观Goal。

## 1. 完整热变换的充分方向确已支付

核查对象是实偶W，带原稿(2)的某个固定有限指数阶界，而非任意D'分布。
该界使Gaussian、全部热导数及复空间变量Gaussian卷积均可配对。
Cc∞ cutoff在固定指数加权各导数范数中逼近Gaussian，所以后续正型给出的tempered
延拓和最初指数阶延拓在此配对上一致；未悄悄假设W预先tempered。

反向CM⇒PSD的核心不是只看原点值：Bernstein给ν≥0后，对每个t>0，
w_t=W*k_t是偶整个函数，热方程给
w_t^(2n)(0)=Theta^(n)(t)=(-1)^n∫lambda^n exp(-t lambda)dν。
另一个整个函数v_t(x)=∫cos(x sqrt(lambda))exp(-t lambda)dν的Taylor系数全相同。
复x在紧集时exp(|Im x|sqrt(lambda))由常数乘exp(t lambda/2)控制，
而Theta(t/2)<∞支付所有矩／导数；故这里的整函数唯一性合法。
由w_t=v_t得到每个t的有限正频率测度，继而D'极限闭性支付全部complex compact平方。

特别重核近似单位：对紧支撑h，h*k_t→h于固定指数加权有限导数范数；
支撑邻域内由通常光滑近似单位，远尾由Gaussian吸收exp(a|u|)，无未付长尾。
因此W*k_t→W于D'，不依赖tempered假设。

Fourier约定W(h)=∫hat h dσ、hat h=∫h exp(-iξu)du下，
hat k_t=exp(-tξ²)，没有遗漏2π。平方频率ν=(ξ↦ξ²)_*σ；ν不是primitive测度。
非偶反例cos(u)+2i sin(u)对应(3/2)δ_-1-(1/2)δ_1，热量exp(-t)却非PSD，
与原稿符号相符。故实偶前件不能删除。

热位移Stieltjes版保λ=0的a/x项、禁任意常数b，有限正表示与Laplace唯一性给出
所述一列ε↓0的充分性；没有把正轴正值当正Stieltjes表示。
独立打开原书Theorem1.4及Definition2.1／Theorem2.2，正表示范围一致。
该接口仍是全阶等价，经典独立正表示没有被证明。

## 2. ODE正能量证书的全域、符号和半正商

全D'身份p(∂)W=0确实排除隐藏δ强迫：状态Y乘exp(-uA_p)后导数为零，
故是常向量分布，W解析并由d个初值唯一确定。候选matrix coefficient满足同一ODE及初值，
由此识别的是整个原W，不是删原子后的函数或有限样本拟合。

C*G+GC=0给exp(uC)*G exp(uC)=G；展开g*g*并换名两个积分变量后，
Q=||∫g(u)exp(uC)v du||_G²，复共轭方向正确。
G≥0时kerG对C不变，商上给正内积；没有把该商等同普通trace的全部重数。
连续族C、G=diag(c-1/4,1)、v=sqrt(2)e2的恒等式和两个初值逐乘法通过。
阈值G退化仍给2|∫g|²，一维GNS商不付二重零点trace，这一限制已明写。
反段实奇g=u phi_even给-2(∫g sinh(ru))²<0，确为同一W的实际负测试。

TV余量版使用|(g*g*)(u)|≤||g||₂²，aδ0给a||g||₂²；系数a-||ν||TV方向正确。
固定R版确须在(-2R,2R)付完整分布身份，所有R后才覆盖全部源。
有限秩正核无全L² gap，不允许无余量的小误差传正性，原稿未越此门。

## 3. 函数域comb常数、全部周期pole与trace

独立核右半平面log derivative：E(s)=q^{g(s-1/2)}P(q^-s)给
E'/E(1/2+w)=gL+LΣ_{n≥1}a_n exp(-nLw)。故原点contact质量为2gL，
W=LΣ_{n∈Z}a_n δ_{nL}；n≠0的q^{|n|}+1保全部周期polar subtraction，
没有误换成实线上的两个rank-one pole项。

直接重展开B_y=Σ_k g(y+kL)U^k，U^{*_H}=U^-1，令n=k-l后，
L∫_0^LTr(B_y B_y^{*_H})dy
=LΣ_n Tr(U^n)∫g(v)bar g(v-nL)dv，恰为Q_W。
H^{1/2}B_y H^-1/2的Hilbert–Schmidt平方给trace非负；外部L和积分区间长度均正确。
compact源保证该展开有限，无周期副本／负n尾的遗漏。

全n trace身份由已知P和Newton／Cayley–Hamilton递推承担，不能只靠N1,N2,N3；
原稿已明确这种依赖。曲线有理性／FE先于RH、Hasse度数正性另供独立几何能量，
已打开Milne pp.1–3核其逻辑顺序。没有由模1纯性自动推指定原Frobenius半单。

## 4. 精确脚本实际重跑

运行python scripts/grh_distribution_certificate.py成功；输出与JSON逐项一致：
N1=9、N2=27、N3=108，trace=-3，discriminant mod5=4，
H=[[1,-3/2],[-3/2,5]]，leading minors=1、11/4，A^T H A=5H。
独立查看F5乘法／不可约模多项式处理及唯一infinity点，未发现计数域或重复点错误。
Fraction核验无浮点，也未读取零点。全次数传播依赖有理性／FE，脚本有限枚举仅交叉核验。

## 5. 经典边界与最强旧对照

从DLMF digamma积分重算t=2a换元，w(a)=2exp(-a/2)/(1-exp(-2a))正确，
W_Gamma穿孔核为-w(|u|)/2∼-1/(2|u|)，原点finite-part及contact项均保留。
另核563新增(13a)：W_Gamma(k_t)=k_t(0)[Γ0+∫w(u)(1-exp(-u²/(4t)))du]，
双pole的Gaussian积分是2exp(t/4)，两侧prime powers给-2k_t(0)ΣΛ(n)n^-1/2
exp(-log²(n)/(4t))。故所有系数、负号及原点差分正确。固定t及有限阶导数的
prime尾有Gaussian对log n的衰减并压过计数增长，积分在0由u²差分及w(u)∼1/u收敛；
这支付可计算性，不支付全部热导数符号。
在log2旁Gamma／pole光滑而实际-Λ(2)/sqrt(2) δ仍非零，故完整经典W不能是
有限常系数齐次ODE的解析解；在0旁又非局部有限Radon测度，排所列有限TV直接类。
这两项不排无限维、无界域、平滑后独立证书、严格D'极限或relative signed修复。

已核041§3含负prime atoms的唯一Laplace逆测度及采样moment障碍；
174§1明确GNS／紧致性只补全已有正性。本稿没有把它们重新结算。
562连续平方和和D'正型锥闭仍作输入；本轮新增是有限输入认证机制与完整周期算术lift，
不是同族再次证明的重复收益。actualζ强旧542+555→557 whole leading4/5、
560成长K/core/coupling和faithful Ξ均未改变；一般数域未被误列为证书已验证。

## 6. 审查版本（LF SHA256）

| 原件 | SHA256 |
|---|---|
| notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md | 094c11cb5909eecc7f4e17468f00b43281b9fc6299042565aa792046807a5f4c |
| arithmetic-counts-and-conservative-realizations.md | cf60c79b33624c57850450df82c7bdf6f1ba10b3409f59e887775224d315d66f |
| heat-stieltjes-and-weil-positivity.md | 376df1529179e61a75d380152150f40d8e6bb56e830c6d802eae81a1ce534e35 |
| independent-analytic-certificates.md | 509132c50a4a3a7ebf19135034a74aa06c55d2b3b47a0e5b17ee6c803d1ae054 |
| elliptic-energy-certificate.json | 827a36f7f125245f06f5bb949624ef3ac6043eb9552355eef26c7d6ff8849406 |
| scripts/grh_distribution_certificate.py | 96270451f8b53ddb97c38e142019a7f7d70bf63fc0b04617a4d1fc6ce2436a37 |

以上hash只绑定所审版本。root仍须保存对象/norm/domain、全量词、paid依赖、零误差、
实际符号、coverage及最强旧净后果的消费记录，不能只以本PASS标记替代根闭合。
