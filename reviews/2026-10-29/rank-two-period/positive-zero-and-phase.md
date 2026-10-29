# 秩二截断 period：正零轴、简单性与全参数相位计数

2026-10-29；`/root/rank2_positive_phase`独占原推导。对当前实际公式的本腿结论闭合：所有先固定有限a≥0的G_a为real even、order恰1的整函数，中心可去值严格正，全部零点为非零imaginary且简单；有准确相位计数及对全部a≥0的共同线性计数上费。以下不使用RH，不消费未读的Lagarias–Suzuki后章证明，不自行授C063/600、计轮或结算整个Weil目标。

## 1. 恢复、来源与既有依赖

实际恢复README/STATE，运行`research_state.py check`后`show`，读完整G20261027、停止C062、AH、599结算、宏观前沿当前段及当前两份source/math准入。恢复时唯一cadence1/history63/latest599/formal20；parent核同runtime1793085111 active，子稿未自行live核父Goal或远端、不建新实例。实际工作树有当前来源/选择稿，不把旧C062预算复用为本腿授权。

实际PDF为math/0412039v4，23页245630bytes；本腿仅读取PDF3全文、PDF4至式(21)及随后整体积分说明，目视核PDF4整页。PDF3所述rank2几何、作者Thm1/2及简单性后置定位是statement/背景，不当作者proof已审；PDF4末非恒定Fourier/Bessel段在图片中曝光，但不消费。没有打开PDF5–23、作者§2以后、Thm5、附录或引用。公式(18)/(20)给下列I；所用常数项积分是已付Eisenstein机制和初等幂积分，不将其算新数学。

**最强旧依赖先扣。** `notes/132-shifted-passivity-abel-resonance.md` §§1–2已经无条件给xi'(1+z)/xi(1+z)的外层positive-real/Pick结构。其§3定义和ThmXW开头曾被工具同时返回，只作曝光，不消费Abel/resonance。本稿自含重导所需strip/Hadamard步骤，是为了G_a边界值、常数、零重数和实际相位的准确消费，不把shifted passivity/Hermite–Biehler原理重新登记为新成果。

准许使用且无RH前件的经典xi事实为：

    xi(s)=s(s−1) Lambda(s)/2，
    Lambda(s)=pi^(−s/2) Gamma(s/2) zeta(s)，
    xi(1−s)=xi(s)，xi(conj s)=conj xi(s)，
    xi(0)=xi(1)=1/2。

xi为order1整函数；其零点rho=beta+i gamma含全重数，0<beta<1，按conjugation与functional equation对称；无条件Riemann–von Mangoldt给N_xi(|gamma|≤R)=O(R log(R+2))，正高度零点数趋无穷。这里用的是既知strict critical strip及计数，不证明或优化新的无零区域/比例。xi在实区间(0,1)正：eta(s)>0由交错正项级数，zeta(s)=eta(s)/(1−2^(1−s))<0，而s(s−1)<0；特别xi(1/2)>0。因此下列中心化乘积没有0根。

## 2. 精确完成、变量与可去点

T=e^(2a)≥1，z=2s−1。来源的有pole完成Lambda与entire xi不可混淆：

    I(T,s)=−Lambda(2s) T^(s−1)/(s−1)
                       +Lambda(2−2s) T^(−s)/s。

对0<Re s<1，此式由恒定Fourier项积分直接得到；其余s按meromorphic continuation。由于

    xi(2s)=s(2s−1)Lambda(2s)，
    xi(2−2s)=(s−1)(2s−1)Lambda(2−2s)=xi(z)，

精确有

    s(s−1) I(T,s)=−T^(−1/2) G_a(z)，                 (1)
    G_a(z)=[exp(az)xi(1+z)−exp(−az)xi(z)]/z。

这不是另选零点后的定义。令E_a(z)=exp(az)xi(1+z)，则xi(z)=xi(1−z)使

    G_a(z)=[E_a(z)−E_a(−z)]/z。                    (2)

分子奇整、z=0可去，所以G_a为real even整函数。每个有限a的order≤1。其中心和端点稍后明确证明非零；不得把分子必有的0根计入G_a零谱。源s中的imaginary高度与z中的高度差因子2：s=1/2+i t对应z=2i t。本腿计数与后续physical Fourier频率一律使用z=i gamma的gamma，不暗换natural clock。

## 3. 半平面严格模长比较：正确水平配对

设U(w)=xi(1/2+w)，c=1/2。U real even、order1且U(0)>0。其±eta配对Hadamard乘积为

    U(w)=U(0) product_(one from ±eta)(1−w²/eta²)。    (3)

因sum|eta|^(−2)<infinity，乘积局部正常收敛；evenness消除order1 Hadamard剩余线性指数。全部eta=alpha+i gamma有|alpha|<c。再按conjugation组块：critical alpha=0给一对±i gamma；noncritical给四元组±alpha±i gamma，保全部重数。

需要证明对z=x+i y、x>0，|U(z+c)|>|U(z−c)|。不能对单个alpha>0零点简单宣称右移距离变大；当x<alpha时单项论证会错。应把同一高度的水平对称零点alpha+i gamma和−alpha+i gamma一起消费。记d=y−gamma，其两距离平方积为

    F(t)=[(t−alpha)²+d²][(t+alpha)²+d²]
        =t⁴+2(d²−alpha²)t²+(alpha²+d²)²。

直接计算

    F(x+c)−F(x−c)
      =8xc[x²+c²+d²−alpha²]>0，                    (4)

其中c²>alpha²。对高度−gamma的同一水平配对同理。critical alpha=0的单根距离平方差为4cx>0，对±gamma分别适用。因此(3)每一个正常收敛quadratic/quartic组块的模长比严格>1。

若U(z−c)=0，U(z+c)不为0（其real坐标x+c>c在零带外），结论直接成立。否则各有限乘积的比至少大于任取一个固定非空组块的>1常数，其余组块比≥1；由(3)正常收敛取极限得

    |xi(1+z)|>|xi(z)|=|xi(1−z)|，Re z>0。         (5)

这里未假设alpha=0；所有actual非critical quartet均实际保留。再乘exp(az)，对a≥0有

    |E_a(z)|/|E_a(−z)|
       =exp(2a Re z)|xi(1+z)|/|xi(z)|>1。           (6)

分母为0时仍按(5)的直接意义理解。(2)遂在右半平面无零；G_a even使左半平面也无零。全部零点只能在imaginary轴。边界简单性与0非零还不能从(6)单独推出，另由下节支付。

## 4. Hadamard实常数的消除与严格正相位

使用xi的标准genus1分解

    xi(s)=exp(A+B s) product_rho [(1−s/rho)exp(s/rho)]。

A可取real，B=xi'(0)/xi(0) real。对非零点s，组合log导数局部正常收敛，取real part得

    Re xi'/xi(s)
      =C+sum_rho (sigma−beta)/[(sigma−beta)²+(t−gamma)²]，
    C=B+sum_rho beta/(beta²+gamma²)，s=sigma+i t。    (7)

两条real级数分别绝对收敛：beta有界，远处项O_s(gamma^(−2))，由RvM可和。故可合法做水平对称重排。s=1/2处xi'(1/2)=0，xi(1/2)>0；sum中的beta与1−beta同gamma两项相消，critical beta=1/2项为0，所以C=0。这一步不能把Hadamard的B随手丢掉，也不能只以“所有项positive”代常数审计。

xi(1+i t)在全real t上非零。选其continuous argument phi_0(t)，phi_0(0)=0；conjugation给phi_0 odd。式(7)在sigma=1遂给

    phi_0'(t)=Re xi'/xi(1+i t)
      =sum_rho (1−beta)/[(1−beta)²+(t−gamma)²]>0。    (8)

各项strictly positive且局部正常收敛；这没有假设零点简单，也没有用RH。定义

    phi_a(t)=a t+phi_0(t)，
    E_a(i t)=|xi(1+i t)| exp(i phi_a(t))，
    phi_a'(t)=a+phi_0'(t)>0。                       (9)

在t=0，(8)给xi'(1)/xi(1)>0，因此

    G_a(0)=2E_a'(0)=2[a xi(1)+xi'(1)]
          =a+2xi'(1)>0。                           (10)

这对所有a≥0成立，并有G_a(0)与1+a同阶的全a上下界，常数只依固定xi。另xi(2)=pi/6、xi(1)=1/2给

    G_a(1)=G_a(−1)=exp(a)pi/6−exp(−a)/2>0，        (11)

因为a≥0且pi>3。(1)中的s(s−1)恰消原两pole而不增加端点零；T≥1时原residue也确不为0。中心z=0可去点与s=0,1是三个不同角色，均已区分。

## 5. 全部零点简单及准确计数

对t≠0，(2)给

    G_a(i t)=2|xi(1+i t)| sin(phi_a(t))/t。          (12)

故零点当且仅当phi_a(t)=n pi，n∈Z\{0}；n=0只对应已经约去的分子中心根。对任一t≠0零点，沿t导数为

    d/dt G_a(i t)
      =2|xi(1+i t)| cos(phi_a(t)) phi_a'(t)/t≠0。    (13)

整函数复导数只差乘i，故每个零点strictly simple。没有用作者后置Thm5来付此项。

下面先证明phi_0(R)→infinity，保证每个n≥1确有唯一正根。令c_rho=1−beta∈(0,1)。对gamma∈[1,R−1]，

    integral_0^R c_rho/[c_rho²+(t−gamma)²] dt
      =arctan((R−gamma)/c_rho)+arctan(gamma/c_rho)
      ≥pi/2。

正高度零点数无界，(8)的非负项积分遂使phi_0(R)→infinity（事实上由RvM还得其量级lower，但本腿只需无界）。所以对每个a≥0存在唯一gamma_(a,n)>0使phi_a(gamma_(a,n))=n pi，n≥1；全部零谱恰为±gamma_(a,n)，无遗漏或额外重数。

记N_a,+ (R)=#{0<gamma_(a,n)≤R}，则对所有R>0，包括R恰为根的endpoint，

    N_a,+ (R)=floor[(aR+phi_0(R))/pi]，
    N_a([−R,R])=2floor[(aR+phi_0(R))/pi]。          (14)

完整实轴interval版本为u<v时

    N_a((u,v])=floor[phi_a(v)/pi]−floor[phi_a(u)/pi]
                                      −1_(u<0≤v)。 (15)

减去的1仅删除分子中心格点，不能把它再加成模型零原子。式(15)也直接支付将来a→infinity局部计数的O(1)舍入责任，但本腿不单凭它宣布全S′极限。

## 6. 全a共同线性计数上费

由(8)非负项可Tonelli积分。R≥1时，先取|gamma|≤2R+2，其每项Poisson积分≤pi，总代价O(R log(R+2))。尾部|gamma|>2R+2上，0≤t≤R给|t−gamma|≥|gamma|/2，所以每项积分≤4R/gamma²。RvM计数经partial summation给

    sum_(|gamma|>2R+2) gamma^(−2)
       =O(log(R+2)/(R+1))。

于是

    0≤phi_0(R)≤C R log(R+2)，R≥1。                (16)

R∈[0,1]由phi_0'在该紧集连续有界给phi_0(R)≤C R；增大同一C后，(16)对全部R>0成立。常数与a无关。连(14)，一次得到

    N_a([−R,R])≤C R[a+log(R+2)]，
                                      a≥0，R>0。   (17)

这里没有需要逐a重新选择的cutoff，也没有只用将随a²增长的inverse-square矩来冒充全a统一费用。它是实际model全谱计数，不是经典xi的N_xi被换了名称。该上费足够另一腿做normalized measure的全尾分析；此稿本身不跳过该责任。

## 7. 阶、规范乘积及可直接消费的二阶矩

实x→+infinity时，Stirling及zeta(1+x)→1给

    xi(1+x)= (x²/sqrt(2)) [x/(2pi e)]^(x/2)
                                                   ·(1+O(1/x))，
    xi(x)/xi(1+x)=O(x^(−1/2))。

因为exp(−2ax)≤1，G的准确差商给更强的全a相对形式

    G_a(x)= [x/sqrt(2)] [x/(2pi e)]^(x/2) exp(ax)
                                                   ·(1+O(x^(−1/2)))， (18)

其中相对O常数对全部a≥0一致；x充分大时两边正。(18)对每先固定有限a给order≥1，结合§2的upper得order恰1。没有声称全a族在complex紧集不归一化有界；exp(az)当然会增长。

由even order1与(10)，规范H_a(z)=G_a(z)/G_a(0)的全零乘积为

    H_a(z)=product_(n≥1)(1+z²/gamma_(a,n)²)。        (19)

(17)使sum gamma^(−2)有限；evenness/正常数清除Hadamard剩余线性指数，没有Gaussian freedom。由原E的Taylor式也有准确恒等式

    sum_(all model gamma) gamma^(−2)
       =H_a''(0)=E_a'''(0)/(3E_a'(0))。              (20)

其有限a正确，但a→infinity leading约a²/3；(20)不能免费给全a统一Schwartz尾。式(17)与另一腿归一化分析才是适当运输，HS或概率坐标在这里也没有被当原physical du/Dlog范数。

## 8. 本腿消费范围与未付项

已付：实际I→G全部系数/负号/可去点及clock；无RH的右半平面严格不等式、Hadamard实常数、boundary phase、G0/端点非零、所有零点imaginary/simple、全谱相位枚举、共同计数上费、order1/全乘积及精确二阶矩。这些是当前实际family证明中的经典依赖与自含特殊情形，不主张首创、不会各算一轮。

未由此稿单独支付：温和分布全尾及a紧化S′/D′极限、405 Pan与完整Wζ目标比较、共同compact精确双pole-zero源、正混合/normalization/source适应/signed费用及strongest-old净果。自然clock之外任意频率b，特别b与a同时退化，未因(14)自动覆盖。没有新primitive/principal/整section/mixed或危险core/cross/成长Xi输入，也未改善whole leading4/5负惯性UPPER。Goal完成门仍open，计数/状态/发布均由root按完整链审结处理。

## 9. 实际输入指纹与终态

| 实物 | 实读范围 | bytes | raw SHA256 |
| --- | --- | ---: | --- |
| goals/GOAL.20261027.md | 全文/完整完成门 | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
| post-599-input-choice/next-rank-two-period-math-admission.md | 全文 | 4122 | 35456a67bfa8143c0828242326cf9f36f2ee83fadd039f603b7c43cc5d2ff8fc |
| post-599-input-choice/lagarias-suzuki-source-admission.md | 全文 | 2185 | 3bd17096bfa34117d9bfb5cf25c6f42d91c1c1e33bb86c2a828b46b895a7b828 |
| literature/local/2026-10-29-lagarias-suzuki/math-0412039v4.pdf | PDF3文字、PDF4至(21)与整体积分说明文字；PDF4整页目视，末Bessel段曝光不消费；未读其余页/作者proof | 245630 | 5028c2f63b14f24415c5077b6a6dd188237aca96498ec7fa8531aaf0a912a075 |
| notes/132-shifted-passivity-abel-resonance.md | §§1–2；§3定义/ThmXW开头工具曝光不消费 | 10313 | 764f4526d61534b7daea63e24771bc954a5f6f63f0612dd189a47058439d738e |

上表post-599路径相对reviews/2026-10-29/。只写本独占稿，UTF-8/LF；无web、新PDF/后章、数值、Git、STATE/cadence/库/Goal修改，无后台待续进程。出稿不代不同fresh/root消费或数学结算。指纹仅认版本，不代独立证明。
