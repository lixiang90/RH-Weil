# 固定9/8：完整Weil型到有限目标的解析运输fresh

2026-10-29。独立限定结论：**未发现本次新L的解析运输阻断；下述原norm费用已与实际新source门对齐。仍以新有限目标P0及其完整整数sign为条件，本文不证明9/8完整Q正性。** 不执行完整producer、trial、compiler或Gram，不改STATE/cadence/Git，不新增轮次。本文件是root待消费的数学审查，不能以文件已经写出代替root消费。

## 1. 实际读取、当前证据与范围

已按README/STATE、check后show、Goal、C058、D20261029S、宏观前沿及实际工作树恢复。同G20261027、冻结0c4f、cadence0/history58/latest594/formal19；主Goal的原primitive/principal/mixed与成长core/Ξ完成门不变。

原数学对照是固定b6cd2183c1e79c6c27a34267812a7b2d73ed1b59的`publication/manuscript.tex`：完整规范93–146、Theorem B的分解/尾/误差246–363、一般Certification Theorem538–682、Appendix B.1–B.3 1055–1232、Appendix C1363–1418、D.1–D.2的moment/kernel1432–1558、D.4–D.5 1642–1792。另读项目537及旧C009对象审查的closed-domain/core和primitive→operator记录、555§1–2、新解析迁移稿、当前scalar脚本/receipt与新inverse及其fresh。不是重验Theorem A、全部论文依赖、世界优先权或外部人工复现。

在当前六副本中定向手核07的`prime_source/verify_centers/expanded_matrix/verify_matrix_rows`、08的`prime_sources/assemble`，以及11/12的完整raw-column对象/参数/独立quotient/半径逻辑。新core代码的upper-triangle reader纠正与代码审计由其专门fresh处理，本文不把未运行core或未审代码当已付sign。

实际重新读取并hash三份source packets及receipts，逐项对照公开`source-stage-verification.json`中的receipt；三者相等且access无violation。没有重跑这三条science路线。

| stage | 实际覆盖/控制 | packet SHA256 | receipt SHA256 |
|---|---|---|---|
| moments | 1024、完整oracle/width、4拒绝控制 | `2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9` | `2a602f637455b95c256be2579f280af09bd26d069de58d48d5979f4e1eb3460b` |
| matrices | 15 shifts、225 pairs、151200 intervals、每矩阵448行、9拒绝控制 | `a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2` | `5d3542181b4f8ddc386a4d86290a574221b751a8857994d0d8e742c164e68984` |
| tails | 896 coordinates、448 parity zeros、raw半径2^-524、4拒绝控制 | `d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e` | `d3a30a58eea7beb08371a3ebe97b684957ef95ca6a164a3283ee6c3118ebf953` |

公开source verification当前SHA为`dbb31208d0568feac7c9adff27722d5b55d08381002d23e0a4e35f150b1472c1`。当前cosh receipt为`9856d2acc3e4b23fbf4ef8e144b5a8f2df1a7b0ed21220bc51d35f7b9c0a37d1`；纠正后true-moment 22叶receipt为`af09d25bcb68928beaf5ca361f8998168e03822dd0d45a9c458de6deaea286cb`。旧21叶的single-Binet读法不是当前前件。

## 2. 完整对象、域和exact分解

I=(-9/8,9/8)，H=L²(I,du;C)，F(t)=∫f(u)e^(-itu)du，Plancherel因子1/(2π)。实际symbol是

    AΓ(t)=Reψ(1/4+it/2)−logπ=2θ′(t)。

所有strict n<exp(2L)的pp恰2,3,4,5,7,8,9；权Λ(n)/√n、位移logn，4/8用log2、9用log3。各true shift<9/4且log10>9/4的有向检查已经在新source oracle中实际通过，足以排全部n≥10。没有丢properpowers或以logn冒Λ(n)。

令Cp为七对partial shifts的正权和，M=7/2 I−Cp。定义真实compact K的kernel

    k(u−v)=2cosh((u−v)/2)
           +(2π)^−1∫_|t|≤256(AΓ(t)−7/2)e^(it(u−v))dt。

则在原smooth域上exact有Q=〈f,(M+K)f〉+Ttail(f)。其中pole严格是2|∫f cosh(u/2)|²−2|∫f sinh(u/2)|²；kernel中保整个2cosh差，含负odd项。Γ/contact规范来自完整Fourier symbol，未另选origin常数或换成half helper。该身份只用原显式公式/有限带Fubini/Plancherel，不假设未知零点在critical line。

辅助M、K、U及projection/block论证都在全H上，不在无域控制的向量上评价unbounded Q。自然closed域为Dlog,I={f∈H:∫log(2+|t|)|F(t)|²dt<∞}；AΓ加常数与log权等价，prime/pole是bounded selfadjoint扰动。旧537的core证明按任意fixed L原样成立：先fρ(u)=ρ^-1/2f(u/ρ)、ρ↑1，用weighted Fourier dilation强连续缩支撑，再以支持小于(1−ρ)L的mollifier和weighted dominated convergence逼近。因此若本次smooth coercivity最终取得，同一常数延到Dlog,I。也可在Dlog上直接使用上述几何侧exact分解；域外仅解释为extended +∞，不能称Q是全H的bounded form。

## 3. δ与rank-two是全源尾供给

归一化||f||=1后，bounded support给|F^(j)(t)|≤(3/2)L^j<2L^j，对任意complex H源成立。若外带能量E=(2π)^−1∫_|t|>256|F|²<1/2，则band积分>π，某t0∈[-256,256]满足|F(t0)|>1/16。

仍取4096个原间隔区间、h=1/32。每区间的积分均值给节点|F(xj)|≤16√E，间距≥h|j−k|，|t0−xj|≤768。选constant phase取real part，ordinary real Lagrange remainder合法；全部basis权和≤49152^4095/4095!<2^24570。**新余项**为

    2(768L)^4096/4096! < 2(81/128)^4096 <1/32。

所以1/16<16√E·2^24570+1/32，得E>2^-49158。它不是有限basis或real-even测试估计。故压缩sinc Bband满足I−Bband≥δI，δ=2^-49158，S=I−Bband−δI为positive contraction。

外带AΓ−7/2>C=123/1280>1/16只依Ω256和shift7/2，与L无关。取v0=(2L)^−1/2、v1=√(3/(2L))u/L、hj=Svj，parity给〈v0,Sv1〉=0。真实ej的原积分在c=ΩL=288为

    e0=(2/π)∫_c^∞sin²x/x² dx，
    e1=(6/π)∫_c^∞(cosx−sinx/x)²/x² dx。

直接用原积分上下界在288重新代入，得ej>2^-11>δ、81e0<C、27e1<C，且e0<1/29²、e1<(3/50)²。无需把旧c272数字直接迁移。Positive contraction给||hj||²≤ej；对任意complex z0,z1在S半范数中平方完成，得〈f,Sf〉≥Σ|〈hj,f〉|²/(ej−δ)。由Cδ>δ/16，严格可保

    Ttail(f)≥τ||f||²+〈f,Uf〉，τ=2^-49162，
    U=81|h0〉〈h0|+27|h1〉〈h1|≥0。

这里整个tail没有被等同于rank-two；非有限秩剩余供给保留。原negative oddpole仍在K内。

## 4. M与projection的原norm费用

555的cosh Schur只用辅助权，不改变physical du norm。令x=e^u、E=e^L，在u≥0时，负移活跃x>n/E，其行项为Λ(n)(x/n+1)/(x+1)；正移活跃x<E/n，其行项为Λ(n)(x+1/n)/(x+1)。八cell分界是1,E/3,4/E,E/2,5/E,7/E,8/E,9/E,E。每cell行是固定(Ax+B)/(x+1)，所以只需全部16个一侧端点。

本fresh另以direct atanh128正有理log series和exp64正series/显式余项重算这些端点，不调用root脚本的interval helpers，严格确认βcosh<209/64，而max下界>13/4。新结果因此是

    ||Cp||<209/64，mI<M<bI，m=15/64，b=433/64。

旧13/4失败仍保留，不影响这个较弱但正的M下界；m无需超过旧μ29/32。任意complex f都由selfadjoint Schur型界覆盖。

令P保Legendre degrees0…447。ρ=3/2 ellipse的imaginary semiaxis5/12，e^(itLx)在其上≤exp((5/12)ΩL)。Chebyshev尾的uniform界6Mρ^-448，再乘√(2L)得到

    sup_|t|≤256||(I−P)e^(itu)||²
      ≤72L exp((5/6)ΩL)(2/3)^896
      =81e^240(2/3)^896 <2^-170。

最后一步的准确整数门81·68^240·2^1066<25^240·3^896已独立比较为true，e<68/25由正series尾给出。因此r=2^-85确实可用，不继承旧2^-95。

对a±=exp(±u/2)，degree447 Taylor给residual<3/448!和||a±||<3。新√(2L)=3/2是等号，但L/2<1、exp(L/2)<2仍严格，所以这些strict estimates不破。Pole operator是|a+〉〈a−|+|a−〉〈a+|，四项rank-one差给||Kpole−PKpoleP||<36/448!<p=2^-440。

κ=(2π)^−1∫band|AΓ−7/2|<896不依L；||e^(itu)||=3/2仍给band cross<1344r、band complement norm<896r²。又v0,v1∈ranP，Plancherel/Cauchy–Schwarz给||(I−P)hj||≤r√(256/π)<10r。由hj的已付norm，U cross<45r，U complement正且norm<10800r²。因此对真实V=K+U、J=E*VE、R=V−EJE*，

    R00=0，||R10||<e=1389r+p，
    R11≥−nI，n=896r²+p，
    ||R11||<h=11696r²+p。

n是下界付款，h是norm付款；正U只可从前一项省去，后一项必须包含。当前n<m精确成立。没有把O(r) cross误作O(r²)。

## 5. source实际费用与完整kernel/columns

当前moments是真θq=(256/π)∫_0^1x^(2q)(AΓ(256x)−7/2)dx。02的sym-remainder和01独立oracle都已包括Binet一次；1024项true intervals在1152-grid上的width≤2^55，故midpoint radius≤2^-1098。s=1025/4及Binet256不因L改变。实际R=4·513!/[6^514(1025/4)^514]<2^-1500，integrated fee<2^-1493；它已经包含在true interval，**kernel阶段不再加R**。

真实K的uniform Taylor remainder可取KT=914·576^2048/2048!：band cosine real-Taylor由κ<896支付，pole cosh real-Taylor由其余18充分支付。对整个|u−v|≤9/4，midpoint替换费≤2^-1098 cosh576。独立Fraction比较给

    (9/4)[KT+2^-1098(68/25)^576]<2^-204。

uniform kernel到operator乘窗口长度9/4，完全不含448维数。新closed kernel两路线使用576²、pole中的18²/16²、midpoint分母2^1153及raw L²=81/64；没有再乘第二次L²。当前全部J0 raw intervals/448行的rounding norm≤2^-220，故εH=2^-204+2^-220已与本次实际新数据接上。

对M/M²，当前07确实逐个核true log/root/weight距center≤η=2^-2048，15项中14个nonzero weight，总绝对质量<11。log9的两倍关系没有借来误差半径，checker独立direct log9后实际核新center。所有225三重交集保留，139非空/86空，B=E*M²E，不是A²；外部one-sided trace保留。

最终i,j≤447有|Pi|≤1、|Pi′|≤100128。两source shift各移动≤η，共同overlap内arguments都在[-1,1]，故integral product变动≤4·100128η；端点损失≤2η。若一方overlap为空，这个端点界仍适用。权质量付款后，M²的raw center fee≤121·400514η。十四weight的全ordered-product变化≤308η+196η²，每overlap绝对值<3；故总raw fee

    ≤121·400514η+3(308η+196η²)<2^26η<2^-2021。

该界也足付A较小的one-shift费用。它直接比较最终retained raw entries，不把primitive误差沿expanded895递推放大。中心矩阵的expanded seeds/recurrence误差另由directed oracle支付；07/08确在A/B输出上加2^-2021 raw padding，不能只读label。

新raw Γii=2L/(2i+1)=18/[8(2i+1)]。对输出interval width，half-width radius=width/2^257，因此norm row fee恰Σwidth·4(2i+1)/(18·2^256)，由symmetric absolute-row quadratic inequality在原du norm成立。本次A/B/J0每个448行实际通过；三者max分子均2405760、分母18·2^256，给εA=εB=2^-220和上列J0 rounding fee。source-center与rounding两种费用没有互相替代。

尾列另取argument576的sinc Taylor。其full operator error≤576^2049/(π·2049!)<2^-513，Machin160 remainder<2^-646且pπ>2。由于||Bband||≤1、||Btilde||≤1+TaylorError<2，有||(π/pπ)Btilde−Btilde||<|π−pπ|，故total band error<2^-513+2^-646。当前896坐标的independent factorial quotient包含、半径≤2^-524及448 exact zeros已实际通过；raw multiplier是ΩL²/pπ=324/pπ，δ未省略。

对n≤447,j≤1，新ΓnnΓjj>1/1024，所以完整normalized vector误差<32√448·2^-524<2^-514。再加上述full band/Machin operator误差，得到每条normalized column error<2^-512。以已付||h0||<1/29、||h1||<3/50作rank-one差，严格给σ=9·2^-512。

raw columns对应未归一化p0,p1，必须随后除√Γjj。因此raw U coefficient确为81/Γ00=27/Γ11=36，tail midpoint分母2^641，raw update为36Σtjtj*/2^1282；不是旧648/17，也没有另乘L²。source程序保normalized/ranktwo字段null与analyticErrorFeesPaid=false是其有限程序范围；这里的解析接入依赖本节数学，不需篡改这些原receipts。

## 6. 最后仍有条件的block消费链

M∈[m,b]先于target sign，故G=E*M^-1E>0；B−A²=F*F≥0来自整个M²。一般block theorem用M_c≥m、R00=0及上节e/n/h，得到α=eθ+2e²/(m−n)、β=(e/θ+n)/m²+2h²/[m²(m−n)]，其中θ=2^-48、χ=1。本次可用α0=2^-122>α、β0=2^-22>β。新μ1/8与actual trial norm y须由对应inverse record/实际Z消费，才能给W≥G>0；本文不沿用旧y8或旧integer target。

设D0=B0−A0²，εD=(465/32)2^-220+2^-440。已付εA/B保证D_M≤D0+εDI且D0+εDI≥0。若最后完整证书支付

    P0=H0+Û+W^-1−λ0I−β0D0≥0，
    λ0=εH+σ+α0+β0εD，

则G^-1≥W^-1与J≥H0+Û−(εH+σ)I给

    G^-1+J≥α0I+β0(D0+εDI)≥αI+βD_M。

放大β只在连同εD之后消费，不能对可能不正的裸D0放大。一般全complex block-Schur由此才给M+K+U≥0，进而通过第3节的真实完整tail给Q≥τI。新正congruence/两个compiler全部entry equality/全部Gram residual rows仍须实际完成并由root核；本解析审查不预付它们。

反射与七对shifts、real-even kernel、两条parity tail均相容，两个完整224-sector可覆盖全部448 complex modes，不额外乘2。但仅一个sector、一个方向或Decimal pivot不足。有限P0/其congruent target的失败只否定这一充分比较的认证；原Q还包含未用tail与各保守误差，不能据此判Q负。

最短可消费依赖链是：完整显式公式/原domain→全H的δ与实际Γ exterior→81/27 U及τ→全M正界→projection/pole/full cross-complement→实际source/原Γ/完整kernel与column费用→新W/inverse→条件P0→一般block theorem→Q≥τ。所有已付解析块没有合并成尚未取得的finite sign。即使新fixed窗最后成功，相对537可新增的也仅是17/16→9/8真实全源支持扩大；primitive/principal/mixed、无界成长core/coupling/Ξ和原Goal完成门均未因此支付。

本fresh独立exact重算14个关键有理叶及16个Schur端点，均通过；未生成任何完整数值packet或改变配置，没有pending子任务。根在消费当前文件及实际最终finite结果之前，9/8完整Q正负仍保持unknown。
