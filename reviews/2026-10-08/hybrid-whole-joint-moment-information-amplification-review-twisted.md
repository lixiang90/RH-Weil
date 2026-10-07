# 整族 moment-information 张量检验的独立全文审查

2026-10-08，审查人 twisted_research。只读全文及各冻结输入，
独立复算全部 finite identities、归一化与两种量词分支。
仅新增本审查，不改被审稿、旧docs、scripts、output、papers、math或Git。

结论：**限定 PASS**。被审稿证明一个准确的 finite trace-information
限制，没有构造原 genuine-prime 算子，没有支付实际四阶上界或新比例。

## 1. 正文绑定与输入

被审完整正文：
[hybrid-whole-joint-moment-information-amplification-research-radial.md](hybrid-whole-joint-moment-information-amplification-research-radial.md)。

canonical UTF-8 LF SHA-256：
`f9e3ffa1aa8c0be583b1c11fc952f8f09bd6deeee9f7bdfa31f3abda1523863e`。
canonical bytes：14884；359行。
规范化仅CRLF→LF及lone CR→LF，不trim或改变EOF。

正文七项输入的本地链接和SHA均逐个重算相符，包含470最终
`729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a`
及两个 split/no-growth 源的最终绑定。没有用旧 small-Q 前件代替实际上界。
被审新增有限论证不需要[R]；把 marked13 作为数据时仍继承其
原conductor-one、fixedgap与bounded-q的准确域。

## 2. Fixed-m finite word 与全部二阶测试

先固定m≥3，再取原T→∞。辅助normalized trace σ=Tr/m满足

\[
 \sigma(A)=\sigma(A^3)=0,\quad \sigma(A^2)=1,
 \quad \sigma(A^4)=\gamma=m/2.
\tag{1}
\]

任意原次序的finite word只有高因子带A；其auxiliary product准确
为A^j，因此正文(5)成立，无需原矩阵交换。总维数dm的normalized
trace必须用τ⊗σ，正文已正确使用这一归一化。

全部零高、两高词保持，含一高或三高词变为准确零。于是任意
lifted F、G的τ(FHGH)、高commutator二矩、W/V全部scalar moments、
固定f(W)及Γ rowweight中心化准确保持。H_e、H_o同样带A，原高
HS parity error保持，非仅得到乘上一个未控制m的误差。

低矩阵与U只带I，整个16个low parity四词原样保持。
Z_j带A、Δ_j带I；故其norm及Γ_j–Δ_j covariance保持，
Δ_j–Z_j与Γ_j–Z_j准确为零。后一式同时使用σ(A)=σ(A³)=0，
不能只凭某个whole orthogonality拆成两分量。正文是直接逐分量计算，
没有这一错误。

原c=τH²L²、k=||[H,L]||²及e均只含零或两个高因子，所以保持；
b、η变为零。原尚未付款的b数值没有被冒充为已知输入。

## 3. 新HS方向、q与whole gap

D=A²−I满足σ(D)=σ(DA)=0、σ(D²)=γ−1。因此

\[
 \widetilde\Gamma=\Gamma\otimes I+H^2\otimes D,
 \qquad \widetilde q=q+(\gamma-1)\tau H^4.
\tag{2}
\]

新增方向与所有F⊗I、低Δ_j⊗I、Z_j⊗A正交；I、A、D三个
auxiliary modes两两正交。正文(11)–(13)、(19)–(20)的norm展开
因此是准确有限恒等式，没有省去增长交费。

whole parity gap的增量是

\[
 \widetilde g-g=(\gamma-1)\tau\bigl(H^2(UH^2U)\bigr)\ge0.
\tag{3}
\]

H²与UH²U均PSD，trace product非负；没有要求它们交换。
m≥3保证γ−1≥0，故最新470的liminf q及liminf g必要下界保持。
q_e、q_o各自和q都可以改变，作者没有声称保持这些未知数值，
也没有恢复已被470排除的Q=1/350。

## 4. 整个第四迹与量词

非交换循环展开给F=a+e+6c−k+4b+4η；张量后为γa+e+6c−k。
利用||HL−LH||₂≤2||HL||₂，k≤4c；e、c≥0，遂

\[
 \widetilde F\ge\gamma a\ge\gamma(\tau H^2)^2.
\tag{4}
\]

flat高二矩趋1/6，故liminf≥γ/36。此处没有把一个未知四阶
预算当已付输入。若原a无界，反三角说明原F也不能统一有界；
若沿某子列a有界，则每个先固定m的模型都有bounded q，
所以bounded-q marked13/split合同的域保留。然而这些模型的
常数可随不同的固定m任意增大。

这是跨所述信息类不存在统一finite上界的结论，不是把固定m
误差用于m(T)，也不是证明原实际F无界。正文明确保持这一量词。
特别是已知某个具体q上界时当然可由有限Cauchy得到依赖该上界的
F界；本检验没有排除这种条件性结论。

正变体A⁺=diag(√m,0,…,0)仍保持second=1、fourth=m；其first/
third moments非零但先固定m，仅把已付odd-H零目标乘固定常数，
极限仍零。反三角(21)足以得到同样的信息限制，不需要假称此
变体把每个odd-H finite word变为准确零。

## 5. 原W、carrier和信息范围的实质边界

正文已充分明示一个关键定义差异：若真的把原每个prime channel
tensor A，其same-prime quadratic diagonal是W⊗A²；本检验选定的
center则是W⊗I。因此即使写出形式E⊗I、P⊗I，仍不是原scalar
coefficient system的实现，不能用它反驳该系统的真实fourth upper。

各已付rowweight测试仅按F⊗I作lift。没有证明新的dm-dimensional
系统拥有原单份interval载波、feature、raw/tail或once-prime系数。
也没有把原scalar admissible rowweight家族扩大成任意新增fiber
测试：若准许I⊗D作为新测试，盲方向自然会可见，但这不是原已付
接口。正文第1、2、6、7节均把这些边界说明清楚。

所以准确成果是：仅再组合当前lifted weighted second、固定rowweight
中心化、low四词和两个parity Gram，不能支付新增H²方向的成本。
要得实际upper仍需原共同路径的genuine-prime四重相关、真实finite-P
compression或额外零侧feature结构。不能从本检验推断所有比例
证书无效，更不能推断RH或实际素数矩阵的反例。

## 6. 审查方法与未验证内容

本审查全文逐式使用auxiliary moments及normalized Schatten/PSD
恒等式独立复算，并核对所有冻结输入绑定；没有依赖作者记述的
32条内存Sympy检查。该记述没有单独输出artifact，本审查不把它
当可复跑证书。有限代数正文已足够，不因此扩大为分析或素数认证。

未发现需要修正文的数学阻断。限定PASS只认证上述finite
information-audit及明确作用域，不认证actual entire fourth boundedness、
未付款joint prime correlation、新比例或新无零区域。
