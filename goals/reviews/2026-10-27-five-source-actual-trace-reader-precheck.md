# 五源 actual t_F reader：可计算证书与执行边界

2026-10-27，G20261027／原0c4f基线。执行STATE保存的L=3/2、完整F及五个pole-zero物理源的建设性预检。原C046已结算停止，535／560的迹域、投影和有限Gram存在性不重计；本稿不是C047／584，不把尚未计算的T/E表或Hfin符号当结果。

本轮实际取得一份固定实位算子的精确有理证书，并闭合从同一物理源到有限压缩的误差流程。**数学输入预检可通过；完整数值reader实现及五源表仍待执行。** 下列是标准算子／求积设施的具体落实，统一记建设性0数学轮，cadence1／历史47／cycle16保持。独立fresh及root最终消费状态见收据与STATE。

## 1. 冻结对象和坐标

五源为r_j=(D²−1/4)[χ_L exp(iπju/L)]，L=3/2、j=−2,…,2，χ_L(u)=exp(−1/(1−(u/L)²))于|u|<L，外部为零。它们是Cc∞(R)、support=[−L,L]、端点flat，消费560的zero-extension Dlog(I)域，不误称严格Cc∞(I)。双pole矩精确零；原完整目标仍保pole项。

F={2,3,5,7,11,13,17,19}，N_F=9699690，覆盖p<e³。完整Q使用Γ(s)=Reψ(1/4+is/2)−logπ，以及q=2,3,4,5,7,8,9,11,13,16,17,19的全部Λ(q)/√q，不以logq替代proper-power权。

原表N_ij、Q_ij、T_ij、E_ij均linear-first，源Σc_jr_j的型值为c^T M bar(c)。column实现须将**四表一起transpose**，连source coordinate map和crossblock同步。五族rhat_j=−(s²+1/4)χhat(s−πj/L)在实轴为实，因此其完整矩阵另有real-symmetric对称性；不能将此用于一般复源删项。

物理H=L²(R_+,dx)，U_t f(x)=e^(−t/2)f(e^(−t)x)，cosine F核2cos(2πxy)。unitary log mapVf(y)=e^(y/2)f(e^y)，故A_r=∫r(t)U_tdt无额外指数，P为cutoff1实位Sonin正交投影。

## 2. 已实际运行的C0证书

原532／533有P=H−HFLR0LFH，L=1_(0,1)、H=I−L、C0=LFL、R0=(I−C0²)^−1。全Mellin power不在Hilbert空间，不能直接代入P；主读出避开这一问题。

[精确脚本](../../scripts/tf_reader_arch_gap_certificate.py)已实际运行，结果在[证书](../../reviews/2026-10-27/tf-reader/arch-gap-certificate.json)。固定N=20、160位向外定点区间，C_N核为Σ_(j=0)^N c_j x^(2j)y^(2j)，c_j=2(−1)^j(2π)^(2j)/(2j)!。Gram H_ij=1/(2i+2j+1)，其逆在实际21维逐entry精确有理验证HHinv=I。

Machin arctan交错余项给π的有理包围；两矩阵a Hinv±diag(c_j)以整数向外interval LDL给全部positive pivots，a=999999/10^6。由congruence得||C_N||<a；real Taylor kernel remainderδ_N=2(2π_hi)^(2N+2)/(2N+2)!同时是HS／全operator上界。因此认证

\[
 1-\|C_0\|^2>10^{-6},\qquad \|R_0\|<10^6.
\]

这不是一个浮点eigenvalue或有限矩阵residual冒充无穷维误差。首次执行只在输出过长有理数字串时触及Python序列化限制；改为向外压缩公开witness，数学LDL输入／结论未减弱。最终运行及独立fresh in-memory复算匹配。该证书仅付款投影输入，不是T/E数值实验。

## 3. source-HS夹心保留真实正迹

定义B=∏_(p∈F)(I−p^−1/2 U_logp)，G=(PB*BP)|M，Π=BP G^−1PB*，是BM的真实正交投影。m=∏(1−p^−1/2)、M_+=∏(1+p^−1/2)，d=m²≤G≤M_+²，不能将B当酉。

BM在x<1消失，F BM=B*FM在y<b=1/N_F消失；五源A_r把前一支撑送到x≥a=e^(−L)。所以

\[
 D_r=1_{[a,\infty)}A_rF1_{[b,\infty)},\quad
 A_r\Pi=D_rF\Pi,\quad
 T_{ij}=\operatorname{Tr}(D_i R_\Pi D_j^*),\quad R_\Pi=F\Pi F.
 \tag{1}
\]

D_r核为K_r(xy)，K_r(z)=2∫w_r(v)cos(2πzv)dv、w_r(v)=r(−logv)v^−1/2，v∈[e^−L,e^L]且端点flat。令C_(r,n)=2||w_r^(n)||1/(2π)^n，则|K_r(z)|≤min(C_(r,0),C_(r,n)z^−n)；源全导数给这些常数的明确majorant，不是unknown norm。

变元z=xy给实际

\[
 \|D_r\|_{HS}^2=\int_{ab}^{\infty}|K_r(z)|^2\log(z/(ab))dz<\infty.
 \tag{2}
\]

截[a,X]×[b,Y]后遗漏HS²≤C_(r,n)²[(Xb)^(1−2n)+(aY)^(1−2n)]/(2n−1)²。log坐标的kernel e^((ξ+η)/2)K_r(e^(ξ+η))有全局显式Lipschitz界，所以finite logcell rank近似的HS误差δ_r由tail＋mesh＋scalar quadrature组成，随明确精度参数趋零。

若H_r≥||D_r||HS，有限rank近似T^(h)有

\[
 |T_{ij}-T_{ij}^{(h)}|\le\delta_iH_j+(H_i+\delta_i)\delta_j.
 \tag{3}
\]

另有有限compression误差时再乘相应有限D系数的HS/Frobenius norm。A_r本身未被说成HS；只有付款的双真实支撑D_r才允许用operator误差控制trace。这条路线没有source frequency截断，高频内容完整保在compact积分K_r中；Q／Dlog的Fourier求积尾则独立付款。

## 4. 全Hilbert residual闭合全部inverse returns

整个H上置mathcalA=PB*BP+(I−P)，有dI≤mathcalA≤M_+²I。对有限输入cell h_β置v_β=PB*Fh_β，V为这些列，则所需compression为V*mathcalA^−1V。

任意真实Hilbert trial列Z都给

\[
 J(Z)=V^*Z+Z^*V-Z^*\mathcal AZ,\quad R=V-\mathcal AZ,
\]
\[
 V^*\mathcal A^{-1}V-J(Z)=R^*\mathcal A^{-1}R,
 \quad0\le\cdots\le d^{-1}R^*R.
 \tag{4}
\]

真实residual列范数η_β给entry误差≤d^−1η_βη_γ、operator误差≤d^−1Ση_β²，再加J本身的积分／rounding费。比如trial Z选确切有理step，v近似误差ε_v、mathcalAZ近似误差ε_AZ时，residual向量误差≤ε_v+ε_AZ；J中每个inner product也按这两个L²误差和已知trial norms单独加费。仅在finite trial空间求出small residual不能代(4)。

该证书可实际计算所需全H误差：physical step的F像是显式sin差／(πx)，给双端L²尾；cutoff为contraction，dilation为酉、B为有限有界和。R0可用已认证gap下的完整Neumann尾，或cosine polynomial resolvent的global误差；再用完整mathcalA谱尾或(4)验收trial。有限个有误差operator作用在全空间中的误差逐步transport，不是只测有限basis。

projection原稿也给全operator近似P_N、完整G逆谱尾及可选533正则化k_s的真实x^−1尾。optional点reader不能与上述无frequency clipping混用以免漏项；主实施路线固定采用(1)–(4)的HS夹心。

## 5. 原norm／完整Q与交叉块

source原稿给χ全导数界β_n=(64/(3L))^n(n!)²，以及每个r_j的R_n和Fourier尾2LR_n|s|^−n。由官方[DLMF digamma](https://dlmf.nist.gov/5.7.E6)和[trigamma](https://dlmf.nist.gov/5.15.E1)式直接推actualΓ界16+log(2+|s|)、导数界10／36，保contact常数；不以log渐近替定义。

du／shift积分、Dlog／Γ全频尾、nested Fourier／digamma节点、12个powers的位移／权误差和arithmetic均有显式账本。Gram正定由compact ODE及指数多项式独立给出；数值conditioning仍须自己的interval LDL／inverse残差证书。core固定span{r0}，其余四源须在同一原norm下实际正交化后才叫测试补空间；它不是全Dlog补空间。

本轮DLMF原网页公式已重核。直接TeX下载HTTP403，web TeX MIME不支持；本地仅保存准确标注的tool-visible公式提取与版本／SHA，不声称取得原始TeX字节；记录见库。本轮未重读CCM／Burnol原论文，原P和trace依赖沿项目已消费版本。

## 6. root消费与执行限制

实际证据为三稳定原稿、C0证书脚本／JSON及fresh；它们对齐同一fixed F、五个physical源与原norm，保正确map方向、operator／trace角色、所有tail和坐标。量词只是fixed F/L及任意精度的有限计算，不代成长uniform性或full-source signed身份。数值程序的实际mesh／trial／算术精度及返回值仍须产生后再验收，不能由收敛证明预填5×5表。

与强旧相比，532／533投影／k_s、535完整source trace、560全fixed窗桥已付。当前净值是把它们落实成可复现gap及明确HS／残差误差输入，属于标准建设性预检0轮。没有T/E表、没有Hfin判定、没有新whole leading4/5／独立primitiveRR／actualq/core/coupling/Ξ。默认6／允许4–8轮的宏观cadence不变，Goal仍open。

唯一接续执行是实现这条有证书的实际reader，先验一个固定Hilbert输入的真实残差和成本，再完成同一五源表／crossblock；不改L/j/F或借升阶躲有限反例。若成本或enclosure宽度不支持有信息的Hfin检验，保存明确误差／成本即止，不串下一reader公式或paper。只有可靠正Rayleigh可反驳本五源E≤0；pass不外推全源／成长，也不自动准入C047。当前不新建数学合同。
