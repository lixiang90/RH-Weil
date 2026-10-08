# 九点共享核值 epigraph 证书：不同作者完整审查

2026-10-08，high_product_joint；本輪基线37eb770。
结论：在483已披露的旧PC8连续语义与组合计算准入范围内，限定数学 PASS。
新证书支付全部289个真实相邻闭域，给出
\[
 F_9(g)\ge805103/10^8\qquad(g_0,\ldots,g_7\ge4/5).
\]
这不是样本下界；没有将浮点LP、有限表记录或41次runtime真值称为新的纯Lean内核全域证明。
本审不修改原证书、论文、程序、输出或Git。

## 1. 冻结身份、实读与实际运行

canonical LF为UTF-8，CRLF/lone-CR→LF，保留EOF。

| 输入 | 行／LF字节 | SHA-256 |
|---|---|---|
| [持久epigraph核验器](../../scripts/am_nine_point_epigraph_certificate.py) | 236／11009 | af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32 |
| [完整原子与289证书](../../output/am-nine-point-epigraph-certificate.json) | 68844／1112534 | 0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6 |
| [低松弛收集程序](../../scripts/am_nine_point_low_slack_cover.py) | 219／10565 | 0c203ae8d05796f73e5ca5018935067342a65f6a9eac3a800b5d36893cfde629 |
| [完整低集覆盖及拼接](../../output/am-nine-point-low-slack-cover.json) | 6752／131270 | 628fdf422495f15f3b5f5ce7e035f8f439d43c0928883509f39034c87b0c64ff |
| [原连续语义审查](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) | 228／17120 | 6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46 |
| [低覆盖不同作者审查](am-low-slack-cover-review-checkpoint.md) | 98／8955 | ce22c49d30f61ce76db6f80f5ab61ea748f788a262fdd8f832eff613d141398a |
| [合法九点lift及尾域](am-nine-point-lift-research-high-product.md) | 161／8823 | 88bd93c28ca361a5be70a48504a186378abba57031ac0f149b08eaf5a8acf045 |

本轮全文实读236、219、228、98、161行；原子/报告全部结构化解析，读回全部70个闭端点、模式及289个证书下界。
另完整读取原Solution的PS/PTF、TVal及tangent_valZ证明（12212–12342），
以及mleafP_ok、leafStep_ok、walkC_ok/walk_ok、run和最后反射证明的必要完整段。
原raw Solution的SHA为012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f；
此前准入NumericCore raw SHA为f21a0d9f141a7807a6524f426b64a0c0b7b2e81e12581d3ec528f467e9bd1be3。

实际执行C:\Python312\python.exe -B -X utf8 scripts/am_nine_point_epigraph_certificate.py --check，exit 0；
加-O实际exit 1，导入的旧重放程序拒绝关闭assertions。
核验器只消费固定捕获表和分数dual；--replay才重建并执行隔离Lean v4.34.1。
本审未重复heavy Lean；另独立解析这次完整capture-log，41原标签全true、70原子/YA顺序及字段全部等于持久报告，
30桥的axioms输出仅[propext]，无error/sorry/panic。
隔离副本11675／1042597，canonical SHA266494dee7d848c0b44b9b5ebf30a129c328eeaf93b0d2dcea1ace2fe609a190；
完整日志351／183580，SHA9c0644717933c9afac9e75d90124bfbfebe8869a91f656b6b6480f57c4366c7e。

## 2. 旧有效原子允许两条安全端锚线

设真实span t∈[L,U]，点xp∈[L,U]，值下界V，实际导数d满足lo≤d≤hi。
原TVal给整个[L,U]上w(t)≥V+d(t−xp)，其中w=K²。
tangent_valZ完整证明先在REG凸区证明切线，再以导数顺序或闭分片零阶界覆盖区外；
因而不能将这里的前件简化成“只有点值和点导数已核”。
PTF字段V=lo32(pack)/10¹⁰，lo=(P−2·10⁹)/10⁹，hi=(2·10⁹−M)/10⁹；
enabled点的P,M≥1由原guard提供，字段0不擅自赋予导数语义。

对整个[L,U]分别有
\[
 w(t)\ge V-hi\,xp+(hi-lo)L+lo\,t,\qquad
 w(t)\ge V-lo\,xp+(lo-hi)U+hi\,t.                 \tag{1}
\]
原切线减第一式右端为(d-lo)(t-L)+(hi-d)(xp-L)≥0；
原切线减第二式右端为(hi-d)(U-t)+(d-lo)(U-xp)≥0。
这使两式同时合法，不假设导数恰等某个表端点。
原constant lb/10¹⁰也在完整span上有效；程序保留每一个enabled点的两条式(1)，不只旧加权混合线。
true_L=max(叶span下界,逐gap下界和)，true_U=min(两种上界和)；
lb使用uc=max(true_U,true_L+1)，只是更宽覆盖，零宽真实域也保留。
本审逐1820个原子核这些端点、字段、mode及原paid比较，未将YA整数代数检查单独当作表语义证明。

AM密度正性给所用上盒：|u|≤1/2时cos(√2u)≥3/4，
Σ|c_j|=64604710/10⁹<3/4，归一化质量为1，所以0≤w(t)≤1。
这是真实核性质；z上界1不可仅因LP取值在[0,1]而宣布合法。

## 3. 共享核变量、完整反射及准确目标

左/右七gap frame分别为g₀…g₆及g₁…g₇；两个原28权各有2个零项。
每个九点span只建一个z_ij=w(g_i+⋯+g_{j−1})，共享两帧给同距离的所有约束。
33个继承的非零span及新增(0,8)共34个z，与8gap共42变量。
反射严格为span(i,j)→(7−j,7−i)，其整个原子、点值/导数pack及闭端点一起搬运。
不逆序42端点数组；反射后YA不是新的Farkas证明，核验器没有将它再次用于recover。
同距离、同权及b对称性保证反射原子的TVal仍有效。

把目标乘2SA（SA=10⁸），gap系数恰为
(BS₀,BS₀+BS₁,…,BS₅+BS₆,BS₆)，z系数为两帧对应Ai之和；
新增跨度8系数4SA。因此它准确等于2SA·F₉，不漏1/2，也没有把旧压力重复支付。
全部实际z同时满足constant与每个enabled点两端锚线、0≤z≤1。
两帧的全部28span区间交集形成27个不同长span，另加入八个g≥4/5。
差分闭包以整数5SC=163840计量，θ准确为4SC；没有整数ceil代替θ。
闭包给的各gap上下界是真实连续多面体的有效盒，不要求实际点落在SC整数格上。

## 4. 任意有理非负dual与盒残差都有效

约束写A x≤b、目标c·x；取任意λ≥0，r=c+Aᵀλ。
对每个真实可行点x及其有效盒l≤x≤u，
\[
 c\cdot x\ge-\lambda\cdot b+
 \sum_i r_i\begin{cases}l_i&r_i\ge0,\\u_i&r_i<0.\end{cases}       \tag{2}
\]
式(2)不要求精确驻点、互补松弛或LP最优性。
浮点仅提出λ；实际接受分数严格非负且逐项重算(2)，负残差按上盒支付，不能忽略舍入误差。
稀疏行号无重复且均在真实矩阵中；删零乘子只压缩数据，未删真实约束。
本审另写标准库Fraction实现，不导入作者核验器/旧模块，不调用SciPy或LP。
它独立重建原子、span反射、全部19600个标签配对、稀疏矩阵及逐289个λ/残差。
结果422个共同gap候选、289个共同span及完整可行域；报告恰包含全部289对，没有漏未付来源标签。
独立重建实际exit 0，全部lower逐字分数等于持久报告并≥805103/10⁸。
最小是left112/right42：
\[
 M=\frac{65955289561887369906031994339}{8192000000000000000000000000000},
\quad
 M-\frac{805103}{10^8}
 =\frac{1251801887369906031994339}{8192000000000000000000000000000}>0.
\]
此余量约1.52808·10⁻⁷；本审只准入所选δ=10⁻⁶，不据小数另提高统一奖励。

独立scratch位于忽略目录tmp/pdfs/am-nine-affine-high/，最终全文读回后执行：
independent_epigraph.py，250／11078，SHA3553550519f1ca74043d3fe931d337fbf4107e0090a6d71b1c229fe980fd9324；
independent-epigraph-summary.json，17／641，SHA22955183fc2a805c578313d89083ec4bac421c9a321b36f6a28c02ef023c9306。
其有限计算证实全部数据/dual；连续语义来自第2节及完整捕获连接。

## 5. 从全部低集覆盖到统一九点结论

令c=805003/10⁸、δ=10⁻⁶，T={h≥θ:F₈(h)<c+2δ}。
旧clear-COV分支一个相邻能量≥c，再加θB>2δ；large-gap分支压力≥c，
其余费至少θ(B−max b)=5053/1953125>2δ；small-gap≤1/2与h≥θ不交。
所以T只能进全部32个旧root，在h₆≥h₀半域不进方向叶，空叶也不含真实点。
split/walk保持完整闭覆盖，强minorant=true整域支付c+2δ，故T必在strong=false且oldresult>0记录中。
另一半逐span反射，70原始记录及70反射覆盖T；边界等号归强已付分支，不能遗失。
收集clone仅把最终cN变为cTarget，旧mcheck、guard、tree、cursor与返回值保持不变；
捕获pack来自实际同leaf的pb，不能用手选浮点切线替代此连接。

原八点准入给F₈≥c。若九点任一frame不在T，其两frame平均已经≥c+δ；
否则两frame在覆盖中的某兼容标签对，全部289对由(2)支付完整F₉。
因此得到本审开头的无限连续结论；跨度8只需非负，无须穿零时取错误正下界。
九点跨度预算≤2、总压力B不变，原近对平方>1/40>c+δ；
按已审无损消费桥，九点滑窗端点8c'和32||fε−f||₁m照付，先T→∞再ε→0。
在同一AM输入的解析消费范围内，新分数为66812491/99194897≈.673547662436708。
该比例还应由正式论文完整写出全零点Hermitian/minmax及计数桥；本审未审尚未定稿的新论文。
没有新增RH、普通7/8无零或核表公理，也没有声称新全链已由纯Lean kernel检查。
