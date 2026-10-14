# C011第二轮：变尺度恒定尾包络的全源标量费用逆审

2026-10-14；仅本文件归本代理所有。不改STATE、cadence、Goal或Git。
本轮先恢复AGENTS、README/STATE、实际research_state.py check/show，再读本版
Goal、MACRO_FRONTIER、唯一C011、D20261014L与539原证明和第一轮逆审。
初始Git HEAD为d092aa73183f05c42d9e2433a4f4dd5371607d80、工作树clean。
本代理get_goal返回null属代理隔离观察，不能据此覆盖root的新Goal运行态。
以下为独立连续逆审，不借普通矩阵、ζ零点、精度扫描或外部PASS标签。

## 1. 原对象、输入责任与全源量词

I_L=(-L,L)、Lebesgue L²、zero-extension、Fourier F(t)=∫f(u)e^(-itu)du；
实际Γ(t)=Reψ(1/4+it/2)-logπ=2θ′，完整pole与全部p^k<e^(2L)在539中保留。
这一审查不删改prime项：

    C_L=Σ_(p^k<e^(2L)) 2logp/√(p^k) (1-log(p^k)/(2L))。

消费539已付的必要门：若一个bounded供应器

    S_L=(β+τ)I-Σ c_n J_logn+D_L

在完整原源类上非负，D_L为任意selfadjoint L²compact，则β+τ≥C_L。
539的carrier/whole-source桥及有限smooth条件已另逆审；本审查不把该门改成
整个Q的负性门。有限Ω的实际Γband/pole与任意额外compact修复均可包含于D_L。

本轮的指定尾供应规则是：对任意L>0、0<Ω<∞及有限实β，有实a≥0、τ≥0，

    a≤inf_(|t|≥Ω)(Γ(t)-β)≤Γ(Ω)-β，
    a(I-B_(L,Ω))≥τI+U，U≥0。

B_(L,Ω)是原support窗的frequency-band orthogonal projection压缩。
第二式须为原完整H_L上的型不等式，或其稠密Cc∞源上的统一不等式；不能把
只在某个有限head/complement上的结论换成它。U可为任意L/Ω依赖、任意秩和
范数的positive compact；下面δ门事实上只需要U≥0，紧性由539供应器门另要求。

## 2. δ严格在(0,1)，有效scalar消元包括等号

令δ=1-||B_(L,Ω)||。B为positive compact contraction。0<||B||，因为任意非零
compact-support源的entire Fourier变换不可能在(-Ω,Ω)全部为0。||B||<1：若
compact B有特征值1，其非零特征源的Fourier支撑同时落于[-Ω,Ω]，但该entire
Fourier在band外开区间消失会迫其恒为0。因此对每个有限positive L/Ω，0<δ<1。

由U≥0可丢其正贡献，取B最大特征源或极值序列给

    τ≤aδ。

将β+τ≥C_L写成β≥C_L-τ，再由a≤Γ(Ω)-β得

    τ≤δa≤δ(Γ(Ω)-C_L+τ)，
    (1-δ)τ≤δ(Γ(Ω)-C_L)，
    τ≤[δ/(1-δ)] [Γ(Ω)-C_L]。                 (V1)

这不是忽略τ后的β≥C_L，也没有把scalar fee移错符号。因δ∈(0,1)、τ≥0，
任何可行参数必须Γ(Ω)≥C_L。若Γ(Ω)=C_L，则V1强制τ=0，再由β≥C_L及
0≤a≤Γ(Ω)-β得β=C_L、a=0，operator不等式强制U=0。
所以任何positive scalar reward必须严格Γ(Ω)>C_L。τ=0的退化准入不自动证明
bounded供应器非负。Ω=0会使δ=1，不能使用V1；该值无频率band且不是本轮规则。

## 3. 独立显式Gaussian估计：误差与原norm不靠谱数值

置c=LΩ、α=Ω/L，完整norm1 Gaussian与原窗截断为

    h(u)=(α/π)^(1/4) exp(-αu²/2)，g=1_I h。

按原Fourier/Plancherel规范，时域截断损失和完整Gaussian的外band损失恰好相同：

    ||h-g||²=E， (2π)^-1∫_(|t|>Ω)|Fh(t)|²dt=E，
    E=erfc(√c)， ||g||²=1-E。

令P_out为频率外band投影。投影三角范数给

    ||P_out g||≤||P_out h||+||P_out(g-h)||≤2√E，
    δ≤<g,(I-B)g>/||g||²≤4E/(1-E)。          (V2)

这显式支付了截断损失、频尾损失及重新归一化；不能把g当完整Gaussian后省去
截断费用。erfc(x)≤exp(-x²)对x≥0：两函数差在x=0为0，其导数为
2exp(-x²)(1/√π-x)，先正后负且无穷远趋0，故差非负。
因此δ≤4exp(-c)/(1-exp(-c))。当c≥log10时，右侧≤4/9<1，单调代入得

    δ/(1-δ)≤4exp(-c)/(1-5exp(-c))≤8exp(-c)。 (V3)

g在边界有jump，不是假冒Cc∞。此处I-B与U bounded、原Cc∞稠密，故上述
scalar型门可从原源类连续延拓到g；反向也可先smooth strict-support逼近g使
有界型与norm收敛。需要Dlog时，截断Gaussian分段光滑且Fourier O(1/t)，亦属
原logarithmic form域。本文没有用g计算whole-Q值或把该域责任遗漏。

## 4. 同实际Γ，允许所有Ω的统一reward上界

Γ严格随t>0增长可由绝对局部一致可微的digamma级数直接付：

    Γ′(t)=(t/2)Σ_(n≥0) (n+1/4)/[(n+1/4)²+t²/4]²>0。

539 exact输入给L≥3/2时C_L>4>Γ(256)。V1可行参数故必Ω>256。
538/第一轮逆审已独立支付同规范Binet upper，亦可原样核：

    Γ(t)≤log(t/(2π))+1/(15t)+25/(8t²)，t≥256。

因为π>3、log(2π)>1且1/(15·256)+25/(8·256²)<1，故t≥256有Γ(t)<logt。
结合Γ(Ω)≥C_L得Ω≥exp(C_L)。令

    A=L exp(C_L)，x=LΩ。

L≥3/2给A>(3/2)e^4>log10，故V3自动可用。V1于是对每一个可行Ω成立：

    τ≤8exp(-x)(Γ(Ω)-C_L)
      ≤8exp(-x)log(x/A)， x≥A。

再用log(x/A)≤(x-A)/A及sup_(y≥0) y exp(-y)=e^-1，得到不需要扫描Ω的统一界

    0≤τ≤8 exp(-A-1)/A， A=L exp(C_L)，L≥3/2。 (V4)

539自含Euler论证已有C_L→∞，因此该统一上界趋0，快于exp(-L exp(C_L))的
常数倍。未补填C_L的PNT渐近；没有宣称最优指数常数。Γ实际更强的log(t/(2π))
只会改善常数，不是V4所需前件。

V4对任意growth β(L)、Ω(L)、a(L)、每个fixed-L任意compact Γband/pole修复，
以及任意positive compact U_L均成立。rank/norm可以随L无界，不用uniform compact
性：539逐L取carrier，V2逐L测试Gaussian，各自只要求本L完整源门。

## 5. source适应与joint signed的诚实边界

若同一全源规则允许U按测试源重新选择但始终U_f≥0，丢掉其正贡献仍给
a<f,(I-B)f>≥τ||f||²，故统一τ的V2门不变。有限rank frame如何生成、选取或
随L增加亦不帮助这个全源uniform scalar门。

但不能把这句话升级为排除所有source适应。以下逃逸均未排：

- β/a随每个f选择，不形成539的单一bounded供应器；需另付joint算术量词。
- 先删finite-codimension的band-concentrated子空间，只在补空间取scalar floor，
  再分别证明head。在补空间应使用restricted δ，不是本δ。确实可删B的有限个
  大特征模式使restricted ||B||≤1/2；于是该补空间δ≥1/2，原Gaussian可能不满足
  这些源条件。完整head及cross必须另付，本文未证明这样的whole-Q机制失败。
- 保留完整非constant Γtail与prime/pole作同源signed估计，而不要求先把整个尾降
  成a(I-B)后再给uniform τ。真正unbounded Γ供给不会在539高频carrier上消失。
- 允许indefinite/noncompact修复、改变源domain或采用不同算术/几何独立正性。

特别是539的prime必要门虽在有限smooth条件后仍真，V2的Gaussian小gap门不自动
在任意此种条件后的源空间仍真。两个已付款的量词不能无声拼成更强声明。

## 6. 宏观判定与下一消费责任

新增净后果是：即使允许growth β/Ω及任意positive compact rank/source frame，
指定全源constant-envelope供应机制也只能抽到V4级别的统一positive scalar reward。
任何要求uniform τ≥τ0>0，或要求τ(L)渐近明显大于V4的计划，在这类前件下失败。
这比只固定Ω256失败更完整，给严格全Ω成本，而不是有限诊断。

但是V4没有证明所有这类证法无法成功：它允许τ极小且正，允许新的exact误差
与complement预算匹配；没有支付实际成长程序所需误差的不可消除lower，亦未排
head/complement适应及nonconstant Γ/prime joint signed来源。
所以不能由τ极小推whole-Q负、RH失败、无界窗正性不可能或本版Goal完成。

当前Goal第三分支特别要求核变尺度/源适应/joint signed后的核心范围。V4只付
其中uniform scalar抽取的方法费用，没有关掉完整joint signed/分块逃逸，也未
给独立新正性。建议结算为严格成本诊断、C011第二轮止损依据，Goal保持active；
主攻转保留完整Γtail的同源joint估计，而不是再增N/扫描Ω追小δ。

本文件所有数学检查终态，无科学执行进程。root需核其自身Gaussian原证明及
本V1–V4的前件一致后消费；保存/计轮/合同停止与新下一动作均由root决定。
