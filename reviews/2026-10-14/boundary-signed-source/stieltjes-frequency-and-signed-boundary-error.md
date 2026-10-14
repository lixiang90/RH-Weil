# 030 signed boundary：实际 Stieltjes 包络、复剖面与频率费用

2026-10-14；执行 AB/STATE 唯一030章节来源门的独立费用审查。
已恢复 AGENTS/README/STATE→check/show→当前 Goal/frontier/C022 completed/AB战略/决策、
next-boundary gate，再读030原§2–5、024和028的准确 core/residual范围、541的频移Γ价。
入口HEAD `0146251644305e87951251a51b11fbe9df714077`，Git status当时无输出；
STATE保存的empty pending不代 live盘点，由root核当前任务handles。
本稿只写指定owned文件；不改公共状态/cadence/Git，不建C023。
同G20261014、0c4f/≤538固定基线；最新已结算555另扣，当前source恢复0轮。

## 1. 原 full Weil 对象、所有 complex profiles及端点角色

原 half-window L>0，I_L=(−L,L)，X=e^(2L)，r在I外零延拓，norm为L²(du;C)。
actual Γ(t)=Reψ_digamma(1/4+it/2)−logπ=2θ′，Fourier hat r(t)=∫r(u)e^(−itu)du。
全部 proper prime powers q<X 的原权 wq=Λ(q)/sqrtq；strictq=X overlap零。

    Q_L(r)=qΓ,I(r)−2Σq<X wq Re C_logn(r)+P(r),
    C_a(r)=∫bar r(u)r(u+a)du,
    P(r)=2Re[A+(r)bar A−(r)],  A±(r)=∫e^(±u/2)r(u)du.

此处没有删odd负pole或把proper powers改成primes。
固定M>0，假设2L>3M；取任意 complex profiles f,g在(0,M)，zeroextend到R。
先可用Cc∞，下述共同量词还覆盖 H¹_0(0,M)或 compactly supported BV 的复化。
定义真实左右端点物理源

    r(−L+x)=f(x),  r(L−y)=g(y), 0<x,y<M,
    r=0 elsewhere;  E=||r||²=||f||²+||g||².

它是原H_L合法源而非Fredholm/quotient标签。H¹_0及BV zeroextensions属于fullDlog；
BV端点jumps须包含在全线variation中。smooth profiles另属于actualΓ operator域。
2L>3M把same-endpoint shifts a≤M与cross-endpoint shifts a≥2L−2M分开；中间shifts correlation恰零。
这是支持几何限制，不声称ALL originalH_L源都具有这一表示。

## 2. 全部 prime 的 exact拆分，保same-endpoint项

令 k(v)=(bar f*g)(v)=∫bar f(x)g(v−x)dx，support⊂[0,2M]，k(0)=k(2M)=0。
对上面H¹/BV源，k连续、W¹,¹；其全线 derivative可从任一factor计算。
cross correlation exact为 k(2L−a)。right same-endpoint有conjugated profile相关，但取Re后相同。
因此原完整prime quadratic恰分解为

    2Σq<X wq Re C_logn(r)=P_self(f,g)+2Re S_X(k),
    P_self=2Σq<e^M wq Re[C_logn(f)+C_logn(g)],
    S_X(k)=Σq<X Λ(q)/sqrtq k(log(X/q)).                  (1)

S_X只有 q∈[Xe^(−2M),X] 可见；两个endpoint的 k值零，strict/full原子约定一致。
P_self包含全部 q<e^M properpowers，不是“boundarylargeprime”之外可以丢掉的误差。
555已结算的原norm all-source Schur bound消费给

    |P_self(f,g)|≤β_(M/2) E,                            (2)

其中β_s是555原half-window s的exact row certificate，β_s~e^s。
粗旧2Σq<e^M wq E也合法，但这里扣除最新555强费用，不用弱子界制造新增。

## 3. actual Chebyshev envelope的精确 Stieltjes fee

设ψ(t)=Σq≤tΛ(q)，R(t)=ψ(t)−t，Y=Xe^(−2M)>1。
实际relative包络与absolute包络分别定义为

    Δ(X,M)=sup_(Y≤t≤X) |R(t)|/t,
    D(X,M)=sup_(Y≤t≤X) |R(t)|.

包络保所有实际primepowers和右连续ψ；sup也含从区间内部逼近的左极限。
它们在fixed有限区间由真实有限ψ表/step endpoints定义，不是ζ零点拟合或假定未知RH误差。
以下先给finite-L exact fee，再消费PNT，不把pointwise fixedu当uniform。

F_X(t)=t^(−1/2)k(log(X/t))在[Y,X]绝对连续，两个boundary值0。
因此原full原子Stieltjes与continuous主项给

    S_X(k)=∫_[Y,X] F_X(t)dψ(t),
    S_X(k)−sqrtX∫_0^(2M)e^(−v/2)k(v)dv
       =−∫_Y^X R(t)F_X'(t)dt,
    F_X'(t)=−t^(−3/2)[k'(v)+k(v)/2], v=log(X/t).       (3)

两个boundary项因k端值零精确消失；没有忽略strict cutoff原子或引入δ0常数。
换元dt=−t dv得同时有效的两份账本

    |error_X(k)|≤e^L Δ(X,M) V_−(k),
    V_−(k)=∫_0^(2M)e^(−v/2)|k'(v)+k(v)/2|dv;           (4)
    |error_X(k)|≤e^(−L) D(X,M) V_+(k),
    V_+(k)=∫_0^(2M)e^(v/2)|k'(v)+k(v)/2|dv.            (5)

不应把D和Δ混成同一norm。relative(4)免去粗e^M乘数，但仍真实支付profile derivative/oscillation。
continuous主项完全Fubini为

    ∫e^(−v/2)k(v)dv=bar F_− G_−,
    F_±=∫_0^M e^(±x/2)f(x)dx,  G_±=∫_0^M e^(±y/2)g(y)dy. (6)

这只是030同对象 leading channel，未付whole-source sign。

## 4. H¹/BV复剖面的可消费量词，不把导数当原L² norm

定义 weighted profile quantities

    a_f=∫_0^M e^(−x/2)|f(x)|dx,
    b_f=∫_[0,M] e^(−x/2)d|D f|(x),

g同理。H¹_0时b_f=∫e^(−x/2)|f'(x)|dx；BV时包含zeroextension端点jumps。
weighted convolution/measure Tonelli给

    ∫e^(−v/2)|k|≤a_f a_g,
    ∫e^(−v/2)|k'|≤min(b_f a_g,a_f b_g),
    V_−(k)≤(1/2)a_f a_g+min(b_f a_g,a_f b_g).          (7)

这些对ALL complex profiles成立，没有positive/commonprofile假设。
在H¹_0域，a_f≤||f||₂、b_f≤||f'||₂，故

    V_−(k)≤(1/2)||f||||g||+
       min(||f'|| ||g||,||f|| ||g'||).                   (8)

(8)不是all-L² bound；derivative是额外未免费付款的source条件。
若E=1且D0=||f'||²+||g'||²≤K²，则2V_−≤1/2+K。

common physical carrier r_t(u)=e^(itu)r(u)的左右剖面为

    f_t(x)=e^(−itL)e^(itx)f(x),
    g_t(y)=e^(itL)e^(−ity)g(y),
    k_t(v)=e^(it(2L−v))k(v).

这保存exact相位 e^(itlogq)，不是改成two unrelated phase sums。
V_−(k_t)≤(|t|+1/2)a_fa_g+min(b_fa_g,a_fb_g)。
所以同一actual Δ给ALL |t|≤T的原norm scaled误差

    |error_X(k_t)|≤e^L Δ[(T+1/2)a_fa_g+min(b_fa_g,a_fb_g)],
    2|error_X(k_t)|≤e^L Δ[(T+1/2)E+sqrt(D0 E)]          (9)

（后一式H¹_0）。两个 independently modulated profiles也可用相应derivative/BV量；
但共同physicalcarrier必须保上述left/right反向profile相位，不能无声乘错2。

## 5. 双pole的完整leading及次项

原物理源exact有

    A+(r)=e^(−L/2)F_++e^(L/2)G_−,
    A−(r)=e^(L/2)F_−+e^(−L/2)G_+,
    P(r)=2e^L Re[bar F_−G_−]
       +2Re[F_+bar F_−+G_−bar G_+]
       +2e^(−L)Re[F_+bar G_+].                         (10)

共carrier时用f_t,g_t计算这些same moments；leading恰是(6)/(9)的同一signed phase。
不能只保正evenpole而丢negativeoddpole去声称相消。
全部次项R_pole由Cauchy–Schwarz和weightedintervalintegral支付为

    |R_pole|≤2e^(M/2)E+e^(−L+M)E.                      (11)

例如|F_+|≤sqrt(e^M−1)||f||，|F_−|≤sqrt(1−e^(−M))||f||；
local product≤e^(M/2)||f||²，cross 2||f||||g||≤E。
这些费用uniformfrequency（phases不改absolute weighted norms），M增长时不能当O(1)。

于是actualfull对象的exact费用归约为

    Q_L(r_t)=qΓ,I(r_t)−P_self(f_t,g_t)+R_pole(f_t,g_t)
                  −2Re error_X(k_t).                    (12)

在(12)中全部pp/双pole/Γ都还在。主阶消失只是同一个signed恒等式；remaining可能任意符号。

## 6. actualΓ频率价：同时支付tail和原norm

543/541原件给 |s|≥1的actualΓ(s)=log(|s|/(2π))+ε(s)，|ε(s)|≤7/|s|。
令CΓ有限使 |Γ(s)|≤CΓ+log(2+|s|) for ALL real s（compact head由原Γ连续性支付）。
profiles位移不改变E或D0，因为两端支持不交；base r有||r'||²=D0，hatr的phase可随L而变。
对ALL carrier t、H¹_0 profiles，Jensen/Cauchy–Schwarz支付

    |qΓ,I(r_t)|≤E[CΓ+log(2+|t|+sqrt(D0/E))],             (13)

E=0时source0，单独解释。此式保full Fourier tail，不能只取|ξ−t|小的band。

对BV profiles，令V=Var_R(f)+Var_R(g)，则ALL |t|≤T亦有单独paid上界

    |qΓ,I(r_t)|≤[CΓ+log(2+T)+log3]E+(3log3/(2π))V².    (13b)

因为base |hatr(s)|≤V/|s|，log(2+|t+s|)≤log(2+T)+log(2+|s|)；
|s|≤1的mass项≤log3 E，tail用
∫_1^∞log(2+s)/s² ds=(3/2)log3。BV低carrier也有fulltail费，不借不存在的H¹ derivative。

还可给真正highcarrier价格。取T=|t|≥4，s为base Fourier变量。
在|s|≤T/2，

    |Γ(t+s)−log(T/(2π))|≤2|s|/T+14/T.

其原Plancherel积分≤2sqrt(E D0)/T+14E/T。
在|s|>T/2，令C*=CΓ+log(2π)+log6，完整差≤C*+2log(2+|s|)。
设a=T/2；利用log(2+v)≤log(2+a)+log(v/a)和sup_(x≥1)logx/x²=1/(2e)，得

    |qΓ,I(r_t)−log(T/(2π))E|
      ≤2sqrt(E D0)/T+14E/T
        +(4D0/T²)[C*+2log(2+T/2)+1/e].                 (14)

因此对fixedbaseH¹ profiles，actualΓ价是 E logT−E log(2π)+o(1)，uniformL。
没有把横跨t+s=0的tail忽略；那部分正由D0 tail bound付款。

BV版本也可以付fulltail。令V=Var_R(f)+Var_R(g)，包含端点jumps，则
|hatr(s)|≤V/|s|，uniformL。对1≤|s|≤T/2支付截断firstmoment，
对|s|≥T/2直接积分log/s²；同组织给

    |qΓ,I(r_t)−log(T/(2π))E|
      ≤16E/T+(2V²/(πT))
         [C*+log(T/2)+2log(2+T/2)+2].                 (15)

用∫_a∞log(2+s)/s² ds≤[log(2+a)+1]/a得到tail；近频firstmoment
≤E+(V²/π)log(T/2)。BV并非H¹，不能用不存在的D0替它付款。
公式(13)/(14)/(15)只是Γ实际价格，没有免费推出prime−pole联合支配或Q负性。

## 7. 随L/frequency增长的非空兼容范围，仍是受控profile子类

PNT在ALL sufficiently large realt一致给

    Δ(X,M)≤εψ(Y),  εψ(Y)=sup_(t≥Y)|ψ(t)−t|/t→0，Y→∞.

这里完整multiplicative window的small endpoint Y必须趋∞；只X→∞不够。
H¹原norm E=1的ALL endpointprofiles、D0≤K²、ALL common|t|≤T，由(2)/(9)/(11)/(13)
得到自含 full complex bound

    |Q_L(r_t)|/e^L
      ≤e^(−L)[CΓ+log(2+T+K)+β_(M/2)+2e^(M/2)+e^(−L+M)]
          +Δ(X,M)(T+1/2+K).                            (16)

这是uniformnorm级profile费用，allpp/selfterms/pole次项和Γ价齐全。
BV的同类版本用(7)/(9)中weightedvariation、(13b)替H¹的K与Γ费；
E=1、V≤K时可把(16)的log/Γ项换成CΓ+log(2+T)+log3+(3log3/(2π))K²，
而Δ项仍≤Δ(T+1/2+K)。这另付BV球的量词，不把variation当原norm。
fixedM、fixedK、fixedT重得old030；不能再以这个直接旧推论计功。
允许M(L)增长时保持2L>3M、Y=e^(2L−2M)→∞，并逐项付
Δ(T+K+1)→0、e^(−L)log(2+T+K)→0、e^(M/2−L)→0，才可消费相同 normalizedlittle-o。
若同时让BV bound K=K(L)增长，(13b)另含K²，因此还须 e^(−L)K(L)²→0；
fixedK自动付款。不能把H¹的logK增长条件暗用到BV的quadraticvariation价。
不先fixedu再忽略靠endpoint的smallcutoff或M-growth。

有一个明确、非空、source-dependentfrequencycap可复算（非独立新PNT）：
fixedM>0（或M≥M0>0且2L>3M）大L时[Y,X]含一个fullintegerunitinterval。
在该开unitinterval内ψ constant，R=ψ−t的variation为1；故

    Δ(X,M)≥1/(2X)>0.

所以T_L=Δ(X,M)^(−1/2)→∞，而logT_L≤L+(log2)/2。
fixedK有ΔT_L=sqrtΔ→0，Γ价O(L)，故(16)仍给ALL |t|≤T_L normalized相消。
包络finiteψ可核；不需要未知zero位置或ordinary矩阵对角化。
此cap只使(16)可消费，不控制未归一化error趋0或sign。

更大cap的issuedabsolutevariation证书要单独看ΔT；不应从上界不足反actualsignederror必大。
特别对nonzero positivebasek，V_−(k_t)≥|t|∫e^(−v/2)|k|−V_−(k)，
所以native账本本身随carrier线性，Γ实际只logt。这与旧541的abs费责任相同，
不构成新fullsigned方法边界，也不排receiver-aware/source-adapted/finitecodim修复。

## 8. 为什么尚不支付ALL source/core：原coverage和residual责任

即使(16)在所有符合profile条件的源上成立，它仍只作用于

    H_boundary=L²((−L,−L+M))⊕L²((L−M,L))

中的更强derivative/BV-ball或carriercap。
central complement L²((−L+M,L−M))非零，2L>3M时其长度≥2L/3且随L增长。
每个fixedcompact smooth physicalsource，L大时完整落在这个complement；
它的原Q值与norm因autocorrelation及dual-pole product平移/扩窗不变。
因而端点channel不自动缩小所有fixedWeil源的真正正性责任，不能把两端“near-radical”称whole危险core。

H¹/BV条件也不是原Dlog全部源；unboundedfrequency方向需同时核actualΓ价。
pureprime norm~e^L的scalarΓ坏频率区有|t|约到exp(e^L)的规模；
本nativePNT derivativecap没有支付那里全部mixedprofiles。
这指出已出证书的coverage缺口，不证明fullsigned费用在该区失败。

024原Feshbach需要finitecore在Dom(B)、补空间strictγ>0、完整(I−P)Be_i的residualGram。
030固定profile的quadratic/bilinearleading相消与(16)不提供这些operator残差或其共同norm。
028原negative-trace消费还需要评价密度d_Q(t)、各坏井全部tail费用及core/residual裕量；
本profileclass既没有一个经核的finitecodimcore，也没有与central/mixed域的共同comparison。
不能把fixedfinitebasis逐项030极限或finitefrequency通过自动升成这些前件。

## 9. strongest-old、停止和前件闭合记录

独立输入仍是经典unconditionalPNT、030原Stieltjesfixedprofilechannel、543/541actualΓ价；
555最新allsource prime费用已用来付same-endpoint，不再重复计其改常数净值。
本稿把profile/frequency/M-growth费用准确恢复，并给native包络可核的非空兼容class；
未得到新ALLsource/core净后果，不付PSD/o(1)defect/Γ-relative小费/Ξ。
古典速率或zero-free常数没有优化，比例/零区暂停、降级路线均保持。

来源门在只有这些旧工具恢复、finitecap或unknowncoverage时0停止；
不以更改M/T/包络标签建立C023。独立signedprimitive定理或实际finitecodim/fulljoint费和strong-old net
另行原件准入，允许Γ付款与source-adapted/joint修复。fixedprofile对照不升级Goal3。

root消费记录：原physicalL²du/Γzeroextension Dlog；ALLcomplex指定endpointH¹/BV profiles；
先fixedM还是M-growth、L/T/K顺序逐项付；actualψ/rightcontinuous/strictallpp/双pole/2π；
Δ包络与derivative/fullΓtail误差paid；source-direction明确而非labelGram；
central/高freq全域/core/residual/mixed仍open；strong-old net为范围/来源恢复0，宏观Goal不完成。
公共STATE/cadence及唯一下一动作由root按其他独立counter/coverage审查合并后保存。
