# C006 最后一轮：全源质量子项与完整返回预算的逆审

2026-10-14。恢复AGENTS、README、STATE/check/show、Goal、C006、D20261014B及533；
起始HEAD核实为44337d2e1492c093dcb263f5ecf57c4676eed3e6。
只写本文件，不改STATE/cadence、不另计研究轮。
已核主代理kernel-subterm.md、direct-budget-audit.md及source-budget-audit.md；
完整source预算与角迹分离的消费状态见末节。

## 1. 实际对象及应证明的量词

冻结源支持U为原两patch，跨度W=log(sqrt6)<log3；V为逐patch两矩零闭子空间。
对每个p≥3，actual primepower型在V严格零；真实差额
`D_p=T_p-T_inf`有source L² compact延拓，这是532已付输入。
533已严格排除 `||p²D_p-A_V||→0`；当前只审尚未排除的绝对可求和上界，
例如 `||D_p||≤C_U p^-2` 或较弱 `sum_p||D_p||<infinity`。
不把fixed-g Sobolev余项当作whole源L²费用。

实际完整密度组织是

    rho_p-rho_inf=-2r cos(as)rho_inf
          +(1-2r cos(as))sum_(j>=1)r^j Mj,
    a=logp, q=p^-1/2, r=q/(1+q²),
    Mj=<k_s,[P(U_a+U_a*)P]^j k_s>.

本逆审先消费第一子项，返回和须另有实际signed控制。

## 2. 大移位核的无源导数界：不同组织复核

实位低cut L=(0,1)，K=LFL、R=(I-K²)^-1，J=R-I=KRK有smooth cosine-even核。
真实physical外部P核为

    P(x,y)=delta(x-y)-(F L R L F)(x,y), x,y≥1.

在rho>1的off-diagonal trace分布上，identity不贡献；实际缩放module因子是sqrt(rho)。
bare FLF的贡献为

    -sqrt(rho) sum_± 1/[pi(rho±1)]
        integral_1^infinity sin(2pi(rho±1)x)/x dx.

SineIntegral余项满足 `|pi/2-Si(t)|≤const/t`，由一次端点分部积分即可。
因此rho≥rho0>1上bare核为O(rho^-3/2)。
此式已经保留actual Gamma与delta全部非振荡项的精确取消；
分别对两个O(rho^-1/2)部分取绝对值会丢掉该新费用。
实际规范仍为2theta'，half规范不能消费这个取消。

对smooth逆修正的双低变量kernel，先在第一变量t积分两次：

    (F L J L F)(rho x,x)
       =4 integral_0^1 integral_0^1 cos(2pi rho x t)J(t,u)cos(2pi x u)dtdu.

首项为const·sin(2pi rho x)f0(x)/(rho x)，
`f0(x)=integral_0^1 J(1,u)cos(2pi x u)du`。
低变量u端点一次积分给f0=O(1/x)，对uJ(1,u)作同样积分给f0'=O(1/x)。
于是f0/x及其导数L¹；x中一次非驻相使首项整体x积分为O(rho^-2)。
sqrt(rho)的trace因子恢复后就是O(rho^-3/2)。

其余两次t积分后的endpoint1及余项带(rho x)^-2，
可直接绝对积分为O(rho^-2)；t=0的J_t(0,u)=0来自cosine-even性。
更深阶版本同样成立，但两次t积分已足够支付本rate。
截断x上端的boundary消失，故这个估计不要求对g作分部积分。
固定低resolvent的Cm核界控制常数，不需要prolate无限求和。

得到真实off-diagonal trace分布的连续核j(t)，满足

    |j(logrho)|≤C_(rho0)rho^-3/2, rho≥rho0>1.

这只是避开identity的外部区；未对未夹source的ambient U_rho P宣告独立TC。
可先有限physical cutoff辨认该核，再在合法source TC的trace分布中消费。
反演对称来自unitary scaling的adjoint及实位密度的实偶性。

## 3. 真正whole源L²子项与尚未消去的返回和

定义 `J_a(g)=integral |ghat(s)|² cos(as)rho_inf(s)ds`。
source压缩的kernel是j(a+t-u)与反向移位的实对称平均。
U×U上|t-u|≤W，因此其绝对值≤C_U exp(-3a/2)。
Schur给

    ||J_a||_(L²(U))≤C_U exp(-3a/2),
    ||-2r J_logp||≤C_U p^-2.

也可用 `||R_g||_1≤||g||_1²≤|U|||g||²` 得同一型界。
固定U时，a接近W的有限prime由避开0的连续核另付有限常数；
对冻结U和所有p≥3，最小rho为3/sqrt6>1，故该避开identity前件实际成立。
两矩零不是此子项的额外估计前件，但最终差额仍在原V消费。

这是比533 fixed-smooth rapid decay更弱的p-rate、更强的source拓扑。
它确实支付一个全源可求和子项，不能据此写完整D_p已有该norm界。

单独返回项的positive trace界不够。对固定p、载频R远大于p时，
532统一carrier/clipping给k_R接近长band载波，C_a在band内部作用近
`2cos(aR)`，故沿相位不为零的载频子序列
`M2(R)`含随band长度K(R)~logR增长的部分。
于是把533的 `|Mj|≤2^(j-2)M2` 直接对全部source单位球积分，
仍会留relative Gamma／高频增长，不能成为uniform O(1/p)的返回费用。
full预算必须先将 `(1-2r cos)` 与整个返回和作actual signed取消，再取norm。

## 4. 联合窗口反例的必要取消核对

在已付误差的finite-chain模型里，每fiber band有n个格点，
B将其嵌入n+1格点，而真实range正交投影rank仍等于n。
对phase周期求平均，carrier投影密度的零Fourier harmonic就是该projection的trace，
因此其与原n格点projection的零harmonic差**精确为0**。
这对任何q以及每个finite fiber成立，不是只在q→0时近似相消。

在无限band内部，free scalar `C=2cos(as)`也给准确代数取消：

    (1-2r cos(as))sum_(j>=0)(2r cos(as))^j=1.

故截取M2的q²positive mass或漏掉分子cross会构造假的1/p反例。
任何joint R(p) lower bound还必须支付实际P/完整G与模型之间的误差；
532的O(R^-1/4 sqrt(logR))若比所声称的prime费用大，就不能用于辨认该费用。
本逆审不把“模型里出现某项”或“某个上界不够小”当作actual norm lower bound。

## 5. 两份审查的新核块与Schatten费用

direct稿的两个bare Fourier配对块也通过独立复核。
source rectangle用y=exp(t)x，0≤t≤W、exp(-t)≤x≤1。
同尺度r的difference相位端点为
`A=2pi r(exp(t)-1)`、`B=2pi r(1-exp(-t))`。
在t≤r^-1/2时，A-B=O(r t²)，用Si'的min(1,1/|u|)界给核O(1/r)；
外区两个Si的pi/2主项相消，核O(1/(r²t²))。
两区L¹_t费用之和O(r^-3/2)，plus相位费用O(r^-2)。
不同p幂的ratio与exp(t)有严格gap，因为exp(W)=sqrt6<3≤p；
两个endpoint argument同号，pi/2部分相消，得到O(p^-2max(n,m))。
这些真实block的signed常数、physical kernel振幅2和source-L²费用无遗漏，
但不覆盖低反向scale与完整resolvent低阶cross。

source稿的Schatten插值亦成立。在physical low square中，
每个 `L q^n U_(-na)F L` 的HS范数≤2、op范数≤q^n。
因此r>2时S_r范数≤2^(2/r)q^(n(1-2/r))，完整lacunary sum在S_r中收敛。
delta=K_p-K0满足 `||delta||op=O(q)`、`||delta||S6=O(q^(2/3))`。
低反向项的实际kernel振幅是-2q²，而非op粗q。
固定cutoff1的实位gap与delta op小性支付所有足够late p的共同resolvent界。

精确三阶resolvent余项为

    H3=1/2[(R_(+,0)delta)^3R_(+,p)
                       +(R_(-,0)delta)^3R_(-,p)].

两个尾的加号正确。它保留完整actual逆，Schatten Hölder给
`||H3||op≤Cq³`、`||H3||HS≤Cq²`。
source rectangle使M0=LZH_band F L是HS×HS的真正TC，
`||M0||1≤C_U||g||²`；Mdelta=LZH_band(F_p-F)L则为HS×bounded，
`||Mdelta||HS≤C_Uq||g||²`。
于是独立localized low product确有ordinary trace及全L²费用

    ||H3(M0+Mdelta)||1≤C_Uq³||g||²,
    |2ReTr[H3 M_p]|≤C_U p^-3/2||g||².

它不要求source导数，也不使K_p变成HS。这是新实际TC product费用。

## 6. 角 paired trace 的关键消费限制

不能仅凭已付 `A_g R_p A_g*` TC，断言任意成对finite-angle截断的trace收敛。
strong operator convergence不蕴含trace convergence；
在无限正负角的取消中，未经共同控制的拆分甚至会改变trace极限。
也不能宣告 `h(K_p)M_p`整体TC：h(K_p)通常非HS，M_p只已付HS。
source稿的paired-Tr表述必须注明其具体联合极限／定义。

此外H3是绕K0的非交换展开余项，一般不与K_p交换。
全h(K_p)的逐角标量trace恒等式，不能未经证明逐项套到H3及0..2阶部分。
因此上节普通TC product的费用，本身只认证一个localized product；
将它称为 **实际完整overlap的全部三阶及以上尾** 还须支付额外身份：
从ambient双cutoff block公式、合法有限source-cutoff trace联合极限中，
证明这个ordinary trace与actual E_p的分离一致。
仅定义 `E_p-2ReTr(H3M_p)`为新aggregate在代数上合法，
却不证明它恰等于所声称的0、1、2δ paired核。

本逆审当前没有取得这一joint-limit proof；
因此消费独立TC localized product及其可求和费用，
actual高尾／低aggregate分离只能登记conditional。
不得借这个缺口删除前两return cycles，也不把该局部TC估计冒称完整D_p尾。
主代理已明确提出同一域风险，本文保留这一严格范围。

## 7. 完整预算状态与合同止损意见

已付：actual whole源L²大移位子项O(p^-2)，
真实same/different高scale裸block的可求和费用，
以及精确resolventH3对应的localized TC product O(p^-3/2)。
未付：角trace分离的actual联合极限，完整低阶signed aggregate的uniform费用，
以及整个D_p的可求和source norm。
没有取得actual nonsummable joint counterexample；不能把未知预算说成发散。
三份审查不分别计研究轮。

若最终仍只有这个子项与不可消费的relativeGamma返回界，C006须按第二轮止损。
应停止继续将未知uniform-return预算改名，而保存：
哪些新增actual signed return-kernel输入能够重新准入；
尚未排除的绝对求和上界和正compact增量；
未支付的conditioned base-S/growingS，以及冻结QW−T2低域compact符号。
下一宏观动作宜优先选择真正能约束低域signed overlap的独立输入，
不能以局部p-rate子项或先运输一般S遮盖未付的完整合同。
若后续取得actual联合分离及完整signed低核预算，才可按其确切uniform范围重新准入；
当前两份新稿未提供该整体证明。

本文件不宣告长期Goal完成，不修改STATE/cadence；没有本逆审的后台进程。
