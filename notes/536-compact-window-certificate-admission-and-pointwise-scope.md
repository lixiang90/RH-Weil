# 完整窗原证书准入与逐点阈值范围纠错

2026-10-14；C008第一完整轮；起始HEAD `4377e70`，长期比较基线仍为 `3a72930`。
状态分开：实际对象/闭型域及本轮有理数尾界为proved；原正性/simple数字为cited/open。
这是用户明确追加的C008审查，旧Goal的535方法类边界完成收据保持，不新建runtime Goal。

## 1. 原件、执行及消费门

固定原件是[arXiv2608.24827v2](https://arxiv.org/abs/2608.24827v2)，修订2026-09-02。
[字节收据](../reviews/2026-10-14/c008-certificate/source-receipt.json)记PDF/源包/HTML、作者主页的URL、SHA和核读范围。
PDF为34页，印刷13/33页另渲染核对。源包安全枚举后解包：仅README、main.tex和四PNG。
固定arXiv入口、正文及作者主页论文条目均未定位矩阵、factor、frame、试探向量、误差账本或verifier；
作者主页引用内容文件的该条目 `links=[]`。这限定本次取得范围，不证明附件在全世界不存在。
未运行作者代码、重造原矩阵或联系作者。

正文§17把附件列为证明一部分，而本次未取得它们。因此无法复核原装配到精确积分的误差，
也不能凭正文所列Cholesky residual、inverse iteration或更多精度验收正性。
原偶/奇底、第二偶底及试探Rayleigh数字全部继续cited/open。

两份独立审查：

- [对象、奇偶与闭域](../reviews/2026-10-14/c008-certificate/object-parity-audit.md)。
- [归约、预算与有理数逆审](../reviews/2026-10-14/c008-certificate/reduction-reverse-audit.md)。

## 2. 实际对象与全源量词

设I=[−L,L]，F(t)=∫f(x)e^(itx)dx，Γ(t)=Reψ(1/4+it/2)−logπ=actual 2θ′(t)。
实际prime内容为全部log n<2L的prime powers，系数2Λ(n)/√n；L=4/5时为2、3、4。
对一般complex源完整pole为

\[
 2\operatorname{Re}[F(i/2)\overline{F(-i/2)}]
 =2\left(\left|\int f\cosh(x/2)dx\right|^2
          -\left|\int f\sinh(x/2)dx\right|^2\right).
\]

所以odd极点确为负，不能把even正rank-one搬到所有源。
even multiplier使奇偶cross积分零；实源Fourier共轭对称使实虚cross积分零。
故四个实奇偶sector各自有效下界即可相加得到complex全源下界，量词没有极化缺项。

actualΓ有log增长。自然域是

\[
 \mathcal D_L=\{f\in L^2(I):\int\log(2+|t|)|F(t)|^2dt<\infty\}.
\]

Γ加常数后的positive weighted Fourier form是dense closed；prime与pole是bounded perturbations。
高频L²尾由C/log(2+R)控制，低频restricted Fourier核在有限rectangle是HS。
这给form域到L²的紧嵌入及相应selfadjoint算子的compact resolvent。
因此真正ground实际attained；域外Q=+∞的extended读法可解释“所有L²”的下界。
单纯L² basis completeness不足以给unbounded-form Galerkin收敛，须另付form-core条件。

本仓矩阵的精确源basis为长度ℓ=2L上的
φ_n(x)=ℓ^−1/2 exp(2πin(x+ℓ/2)/ℓ)。中心指数basis与它差D_n=(−1)^n，
这是保范数且保奇偶的unitary相位；直接pole/相关积分给脚本w02与q_nm，Γ规范也一致。
不是以仅hilbertian的半局部同构继承Rayleigh排序。

## 3. 归约、误差与simple排序：成立的逻辑与未付输入

完整符号Ψ_L=Γ−P_L；Binet/shift估计给t≥15/4时
Γ(t)≥log(t/2π)−1/t。尾下界β>0给精确one-sided归约

\[
 Q(f)\ge P(f)+\beta\|f\|^2
 +(2\pi)^{-1}\int_{|t|\le T}(\Psi_L-\beta)|F|^2dt=:R(f).
\]

这是actual全频积分的符号丢弃，与head矩阵正性不同。
若R的head≥a、tail≥d、coupling norm≤b，则全R≥min(a,d)−b。
若另有head的第二minmax≥s₂且tail足够高，则λ₂(R)≥min(s₂,d)−b。
Q≥R把下界向全Q运输；一个精确有限源的Rayleigh上界向真λ₁运输。
所以若even上界严格低于odd全下界与第二even全下界，结合上述compact resolvent，
确可推出真正simple-even ground。原逻辑可成立；本轮未取得支付数字条件的证书。

逆审找到三项可修的正文估计问题：threshold超过T₁的量约1而非O(T₁^−1)；
一个C条目估计漏T/π；未经面板缩放的quad公式数值略大于印刷舍入。
纠正因子后的独立tail/coupling仍远小于1e−100，真实面板缩放也可保守吸收quad差异。
这些不是已证全窗负值或PD失败；完整Bessel/Miller、pole、节点/权重、parsing、
Γ计算、矩阵/Cholesky乘法、Householder frame及试探向量误差仍须原账本逐项核。
在非orthonormal frame上，有限误差还须用frame的Gram下界运输；full rank本身不能支付量化误差。

## 4. 新独立有理数后果：较宽逐点最优性不能消费

全局constant upper bound P_L(t)≤A_L最优：t=0已取等，任意高频亦可逼近。
只用这个常数及上述Γ包络的具体归约必需T>T₁=2πe^A，PNT给其double-exponential尺度。
这不排除有限频段使用实际signed cos后，再接粗尾包络。

[本仓独立脚本](../scripts/c008_pointwise_envelope.py)不输入ζ零点或外部代码，
以Fraction、integer isqrt、Machin atan交错余项、log atanh正项余项及cos Taylor余项，证明

\[
  L=4/5:\qquad \Psi_L(t)\ge1/200\quad (|t|\ge118),
  \qquad 118<T_1.
\]

精确常数向外包围后，在[118,121]用30个宽1/10面板；
中心cos Taylor及|cos′|≤1支付宽度与phase误差。负cos上界乘系数下端，正cos乘上端。
所有面板的Γ粗下界减实际comb均>1/200。
t≥121由单调粗Γ下界减A给>1/200；evenness补负半线。
比较log(118/(2π))<A证明T₁>118，不须近似exp。
所有判定均为精确分数，float只作显示；[结果](../reviews/2026-10-14/c008-certificate/pointwise-envelope-rational.json)
可由脚本重放。独立逆审核向外方向、量词和remainders。

故“任何逐点方法不能降低阈值”的宽泛语句在这个实际对象已有反例；
constant-envelope最优性不变。该结果只改善高频符号尾界，**没有**给低频/whole Q正性，
也不推翻double-exponential渐近方法费用；不会把这个局部纠错升级宏观完成。

## 5. 净后果、瓶颈与止损

若原complex小窗证书将来验收，则C007两patch源U的外端
log2/2+log(3/2)/4<0.8，可运输其actualQW下界；该源域内3、4相关为零。
这不推QW≥T₂或E₂≤0，不矛盾535。
C001的μ=13对应半窗log13/2>0.8，原12组与该定理无覆盖关系。
小窗simple-even也不能运输到其他λ、成长S/U或prolate/Ξ相认。

新独立输入是精确对象/闭域接口及有理数逐点范围反例；正性来源到实际全源的箭头尚未支付。
实际瓶颈未消除，已定位到不可得的原证书及完整误差消费。
C008按一轮止损，状态stopped而非正性验收；不盲目另装配40CPU小时矩阵或加N。
重新准入须可定位原矩阵/代码/账本/frame/试探源及完整向外误差证明，或不同独立signed机制。
唯一下一动作是出现该证据后，先核归约误差与同norm数字证书，再消费全窗结论。
无pending process；暂停比例/无零区域及既有降级路线保持。只消费原cadence一次。
