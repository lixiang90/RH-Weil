# C070：有限列、相干kernel及固定路径的联合上界

2026-11-01；/root/bc72_primary_reader。实际C070 proof分工；只用已付560/589/591及当前contract/spec，固定X_j=e^j、N_j=j²。本文非ROOT消费或计轮；不改STATE/cadence/Goal/Git，不含新来源、数值或代码。第一槽linear，physical r不与native f=e^{-u/2}r交换。

**结论范围。** 合法有限列和三重kernel如下，Hermite非局部cross terms完整保留。还证明一个实际联合估计：沿本路径，fixed source窗的du-unit ball上C_j/j一致趋0（更一般，对||rhat||∞≤1一致）。这是有明确fixed-eta余项的联合receiver比较，不用fixed-X先穷尽N。但它不判定三源比值：anchor lower、相干交叉的相对量仍未闭合，本文不宣称通过或反例。

## 1. 接收端与规范

H=L²(R+,dx)，Jv(y)=e^{y/2}v(e^y)，U_av(x)=e^{-a/2}v(e^{-a}x)。未归一Fourier将log空间送至L²(R,dmu)，dmu(t)=dt/(2pi)，于是A_r=M_{f_r}，f_r(t)=rhat(t)。

标准real Hermite h_n在L²(dt)归一。接收端e_n(x)=x^{-1/2}h_n(log x)的Mellin像是sqrt(2pi)(-i)^nh_n(t)；列相位不改变E_N。因此下文合法选用同一E_N的ON列

    phi_n(t)=sqrt(2pi) h_n(t),  0≤n<N,
    K_N(v,w)=2pi H_N(v,w),
    H_N(v,w)=Σ_{n<N}h_n(v)h_n(w).

Pi=Pi_{e^j}始终是全部Euler-Gram inverse/returns的原投影。它在Mellin侧的actual continuous projection kernel记k_j(t,v)，相对dmu，k_j(t,t)=2pi rho_{e^j}(t)。这是589/591的actual kernel，不是bare Euler weight或trial子投影。每行属于L²(dmu)，行norm²为k_j(t,t)。

## 2. 合法有限列公式及Fubini范围

对r∈L¹(du)，f_r bounded continuous。令

    L_{j,n}(r;t)=∫ k_j(t,v)[f_r(v)-f_r(t)]phi_n(v)dmu(v).       (A)

每个t的积分由row L²及bounded f_r、phi_n∈L²合法；它就是D_j(r)phi_n，其中D_j=[Pi,A_r]。故

    C_j(r,s)=1/2 Σ_{eps=id,check} Σ_{n<N}
                  ∫L_{j,n}(eps r;t) overline(L_{j,n}(eps s;t))dmu(t). (B)

这与Tr(E_N D_epss* D_epsr E_N)的first-linear convention一致；没有把右E_N移过Pi或multipliers。

等价的显式相干公式为

    C_j(r,s)=1/2 Σ_eps ∭ k_j(t,v) overline(k_j(t,w)) K_N(v,w)
      ×[f_epsr(v)-f_epsr(t)]
      ×overline([f_epss(w)-f_epss(t)]) dmu(t)dmu(v)dmu(w).       (C)

对每先fixed j,N，本式可作absolute Fubini。560的finite-F密度关系给k_j(t,t)≤C_j log(2+|t|)（常数可依完整F_j）；phi_n Schwartz。投影核的Cauchy–Schwarz给

    ∫|k_j(t,v)k_j(t,w)|dmu(t)
       ≤sqrt(k_j(v,v)k_j(w,w)).

因此各n项的absolute三重积分至多

    4||f_r||∞||f_s||∞
       [∫|phi_n(v)|sqrt(k_j(v,v))dmu(v)]² <∞.

在这个Fubini理由里不把C_j当uniform j常数；后面的联合估计不用它。

Christoffel–Darboux按标准Hermite递推给

    H_N(v,w)=sqrt(N/2)
       [h_N(v)h_{N-1}(w)-h_{N-1}(v)h_N(w)]/(v-w),          (D)

对角取连续极限。K_N(v,w)不是非负pointwise权，v≠w项不消失。因此(C)不能改成只有|k_j(t,v)|²的591 positive jump kernel，也不能用K_N(v,v)替去w积分。

## 3. 可付的联合Hermite／actual-Pi估计

以下只用固定eta的已付actual localization，不将eta换成eta_j。

**旧输入。** 591的actual-gevery-tail-and-premise-closure.md §2 (L)，其前件来自589/C052 localization §6：每先fixed eta>0、B>0，记

    a(j)=e^{j/2}/j,
    c_eta=4-4/sqrt(1+4eta²)>0,

则最终有

    sup_{eta≤|t|≤j^B} k_j(t,t)
       ≤exp[-(c_eta/2)a(j)].                               (L)

这里只取B=2。起点J_eta可依eta；不是未经付款的moving-core估计。

**标准Hermite bounds。** Mehler的对角generating identity（可由Hermite generating function逐系数验证）为

    Σ_{n≥0}z^n h_n(t)²
       =[pi(1-z²)]^{-1/2} exp[-(1-z)t²/(1+z)],  0<z<1.

取z=e^{-1/N}，用1-e^{-2/N}≥(1-e^{-2})/N，得到

    H_N(t,t)≤c_H sqrt(N),
    c_H=e/[sqrt(pi(1-e^{-2}))].                           (H1)

取z=1/2又给

    H_N(t,t)≤2^N/sqrt(3pi) exp(-t²/3).                    (H2)

因为N=j²，T=j²，(H2)与Gaussian tail积分给

    Tr(1_{|t|>T}E_N)
      =∫_{|t|>T}H_N(t,t)dt
      ≤sqrt(3/pi) 2^{j²} j^{-2} exp(-j^4/3)=:d_j².         (H3)

这两个bounds作用于receiver，不是source window。

固定eta>0，最终j²>eta；分输入三块I0={|t|<eta}、I1={eta≤|t|≤T}、I2={|t|>T}。置

    a_{j,eta}²=2 c_H j eta,
    b_{j,eta}²=(j²/pi) exp[-(c_eta/2)a(j)].

对任意bounded measurable multiplier f，三块逐项有

    ||Pi 1_I0 M_f E_N||HS
       ≤||f||_{∞,I0} sqrt(Tr(1_I0 E_N))
       ≤||f||_{∞,I0} a_{j,eta};

    ||Pi 1_I1 M_f E_N||HS
       ≤||Pi 1_I1||HS ||M_f E_N||op
       ≤||f||∞ b_{j,eta};

    ||Pi 1_I2 M_f E_N||HS
       ≤||f||∞ sqrt(Tr(1_I2 E_N))
       ≤||f||∞ d_j.

第一、三项用Pi contraction；第二项用(L)及interval长度≤2T。所有Pi 1_I1的HS由positive sandwich trace成立，没有把Pi本身升级trace class。于是得到实际finite-column比较

    ||Pi M_f E_N||HS
      ≤||f||_{∞,I0}a_{j,eta}+||f||∞(b_{j,eta}+d_j),        (E1)

    ||Pi E_N||HS≤a_{j,eta}+b_{j,eta}+d_j.                 (E2)

这按**输入**划分，不声称Pi E_N的输出也在I0，不采用未付的输出localization。

由||M_f Pi E_N||HS≤||f||∞||Pi E_N||HS，

    ||[Pi,M_f]E_N||HS
       ≤2||f||∞(a_{j,eta}+b_{j,eta}+d_j),                 (E3)

因此本候选的reflect-average满足

    C_j(r)≤4||rhat||∞²(a_{j,eta}+b_{j,eta}+d_j)².         (E4)

对每fixed eta，b_j²/j→0、d_j²/j→0，而a_j²/j=2c_H eta。故

    limsup_j sup_{||rhat||∞≤1} C_j(r)/j ≤8c_H eta.

eta可在此后任取小，证明

    sup_{||rhat||∞≤1} C_j(r)/j →0.                       (E5)

其中sup只需遍历本定义合法的physical L¹ sources；(E1)–(E3)本身也对任意bounded f成立。对每先fixed source窗[-L,L]，||rhat||∞≤||r||1≤sqrt(2L)||r||du，于是

    sup_{supp r⊂[-L,L], ||r||du≤1} C_j(r)/j →0.           (E6)

ALL-complex域没有改成real；原zero-extension Dlog由Plancherel同样给充分upper。没有L随j成长或native weighted乘法的uniform Dlog费用。E5/E6是本固定联合路径的严格transfer，不是固定X先穷尽，也不是585/603的巨大occupation lower被反转。

特别地，若C_j(g)>0最终且finite common c_j使c_j C_j(g)→q0>0，则

    c_j j=[c_j C_j(g)]/[C_j(g)/j]→∞.                     (E7)

这是必要校准费，不是任意gain失败；c_j可以趋零但比1/j慢，也可以成长。无限次零分母的分支仍由contract单独处理。

## 4. 三测试的相干障碍具体落在哪里

以下是exact bounded-column identities，不使用未付的unbounded M_t Pi域。

令G=|psihat|²、H(t)=tG(t)，两者bounded，G real even，H real odd。g′的multiplier为iH，故C_j(g′)的对角等于||[Pi,M_H]E_N||HS²；g偶使C_j(g)=||[Pi,M_G]E_N||HS²。Hermite basis可取上文real phi_n，

    t phi_n=sqrt(n/2)phi_{n-1}+sqrt((n+1)/2)phi_{n+1}.

记L_n=[Pi,M_G]phi_n，并定义实际有限列

    B_n=M_G Pi(t phi_n)-M_H Pi phi_n.

由于t phi_n∈L²及M_H bounded，B_n合法，即使尚未知道Pi phi_n∈Dom(M_t)。直接展开给

    [Pi,M_H]phi_n
      =sqrt(n/2)L_{n-1}+sqrt((n+1)/2)L_{n+1}+B_n.          (F)

因而C_j(g′)含邻列n-1/n+1 cross、端点L_N和B_n与该邻列和的cross。L_N只是恒等式中的单个边界列，不代表另选N-path。仅知道Σ||L_n||²=o(j)与Σ||[Pi,H]phi_n||²=o(j)，不能决定这些相干项的相对号或比值；不可把它们丢掉后用occupation的非负jump论证。

平移门也有同样的具体cross。设Z_±=M_{exp(∓iat)}，a=1/2，S_±=[Pi,Z_±]M_G。各列精确为

    [Pi,Z_±M_G]phi_n=Z_±L_n+S_±phi_n.

所以

    C_j(tau_a g)-C_j(g)
      =1/2 Σ_{±,n<N}||S_±phi_n||²
         +Re Σ_{±,n<N}<Z_±L_n,S_±phi_n>.                  (T)

内积此处first-linear，Re无槽歧义。它不是已付591的非负A_R；finite-right receiver保留的第二项目前没有有利号。B、F、T展示了actual source formulas及未付的coherent coupling，不是用PSD重新命名目标。

**精确未闭前件。** 需要在同一Pi_{e^j}、E_{j²}下，对(F)/(T)的有限列cross及非零anchor Σ||L_n||²给相对比较。现有(L)只控制actual对角，E1/E2只给absolute overlap；二者没有提供anchor lower、joint off-diagonal phase或这些cross的相对渐近。特别地，E7的校准可能放大所有尚未控制的o(j)，故不能用E5/E6排Dprime，不能断言C_j(g′)/C_j(g)→0、∞或q1/q0，也不能断言平移比→1。

## 5. 已付／open与最强旧净值

标准/已付：合法Gram、finite-column trace、Hermite generating identity/ladder/CD、560 full HS端点2V、589/591 fixed-eta actual localization。本文实际推导：coherent三重式及E1–E7的fixed-path transfer，明确其uniform source/norm量词；没有新的prime估计、下界、ratio limit或signed净后果。

严格联合upper区别于完整receiver occupation能量，但它仅限制该candidate在1/j能量校准；原题允许unbounded common calibration，故尚不通过或反测C070三源必要门。是否计为新严格部分结果须ROOT按强旧直接推论门裁定，不以本稿或estimate数量计轮。本文交付状态是**ratio unresolved，已定位coherent relative-column lemma**，不以unknown验收成功。

完整q0/q1仍取591 paid actual Weil值，Gamma/contact、all proper powers及双pole没有删；g′odd diagonal与负pole保留。未证明fullmixed/Dprime、全source principal／sections／mixed capacity或growing core/coupling/Xi，也未改whole17/16、9/8 head、same605唯一head+ALL complement正完成、whole4/5负惯性UPPER。只处理固定路径，不续N、gain、receiver、source或合同预算。
