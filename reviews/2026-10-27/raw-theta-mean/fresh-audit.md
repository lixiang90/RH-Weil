# Raw theta mean／joint：独立fresh逆审

始于2026-10-27；2026-10-28完成本次逆审。/root/rm_fresh独占稿，恢复Goal／STATE／D20261027Q及唯一rawmean准入。**最终有限PASS：两份实际终稿已完整核读并绑定，mean强域／actual Pan渐近及joint闭包／连续mixed范围闭合；没有新的classic独立正号或whole结果。** 不改STATE/cadence/Git，不预C048/585，不调核/模型/ray/weight/阻尼或提出下一source。

## 1. 已付输入与exact Mellin加有界余项

保同一明确R_g/K_g、fixed L及c_L>0。前轮实际Poisson/全空间尾和T=∫rW的global L²du→each H^m/C∞费用已付。记α=3/4、

\[
 m(t)=e^{\alpha t}\operatorname{vol}_\mu(M)^{-1}
                    \int_MK_g(ie^t,z)d\mu(z).
\]

实际双尾给

\[
 m(t)=-e^{\alpha t}+O(e^{\alpha t}e^{-a e^t})\quad(t\to+\infty),
\]
\[
 m(t)=c_L^{-1}e^{-\alpha t}
     +O(e^{-\alpha t}e^{-a'e^{-t}})\quad(t\to-\infty).
\]

所以定义

\[
 \nu(t)=m(t)+e^{\alpha t}-c_L^{-1}e^{-\alpha t}
\]

得到一个**全线exact**分解，而非仅局部渐近。其正端leading为−c_L^−1e^−αt，负端leading为+e^αt，余项双指数衰减。因此ν及每个固定阶导数均O(e^−α|t|)，特别ν∈L¹∩L²；一般不能称ν∈S_exp，因它保留了另一端加入的指数项。

对全部r∈F=S_exp,C，

\[
 \ell_0(r)=\int r(t)m(t)dt
 =-L_+(r)+c_L^{-1}L_-(r)+B_\nu(r),
\]
\[
 L_\pm(r)=\int r(t)e^{\pm\alpha t}dt,
 \qquad B_\nu(r)=\int r(t)\nu(t)dt,
 \qquad |B_\nu(r)|\le\|\nu\|_2\|r\|_{du}.
\]

这必须先与旧Mellin读出及553的bounded leg比较；不能忽略该exact分解，再把rawmean命名为全新强源障碍或独立正号。

## 2. 强域、实际Pan系数与原norm不连续

由于|m(t)|≤C e^α|t|，任意N>α有

\[
 |\ell_0(r)|\le\frac{2C}{N-\alpha}p_{N,0}(r).
\]

结合T的原du/Ck费用，R_raw r=Tr+ell0(r)1在全S_exp上是合法smooth强源积分。该强upper不是du/Hlog界，不是necessary lower，也不是全算术theta／height运输。

沿405/553，H=e^(t/2)h>0且在S_exp中，physical p=(D²−1/4)H非零，其全部p_b(t)=p(t−b)属于实际Pan复化空间P。没有裁剪关系。带权分部积分直接给

\[
 A_\pm:=L_\pm(p)
 =\left(\alpha^2-\tfrac14\right)
       \int H(t)e^{\pm\alpha t}dt
 =\frac5{16}\int H(t)e^{\pm\alpha t}dt>0.
\]

ν∈L¹，p∈C0∩L∞，故对每个固定t有p(t−b)→0，且|ν(t)p(t−b)|≤||p||∞|ν(t)|。支配收敛给Bν(p_b)→0于b→±∞。于是准确的两端合并表达为

\[
 \ell_0(p_b)=-A_+e^{\alpha b}
       +c_L^{-1}A_-e^{-\alpha b}+o(1),
       \qquad b\to\pm\infty.
\]

正端leading为负，负端为正；分母最终非零。全部平移的du、Dlog及Hlog范数各自保持不变，而|ell0(p_b)|→∞，所以不存在这些原全线范数的global bounded extension。这个必要费使用真正noncompact关系，不拿compact关系空集过门。

α=±3/4不是classic physical双pole±1/2。p的±1/2矩由D²−1/4恰为0，当前±3/4矩却严格为正；不能改weight使其凑齐或称rawmean已恢复完整pole/Γ。

## 3. 常数方向与无限joint闭包

令S r=(ell0(r),Tr)，E_m=closure_(H^m)T(F)。对b→+∞取实际Pan

\[
 h_b=p_b/\ell_0(p_b).
\]

则ell0(h_b)=1，且对每个固定m，

\[
 \|Th_b\|_{H^m}\le
 C_m\|p\|_{du}/|\ell_0(p_b)|\to0.
\]

同一个b序列对每个m分别成立，故S h_b→(1,0)也在C×C∞ Fréchet拓扑成立，不需跨m统一C_m。强源半范数可能增长并不妨碍所声明的目标拓扑极限；未称h_b在原S_exp强拓扑趋0。

置J_m=closure_(C×H^m)S(P)。它是closed linear空间，含(1,0)，遂含C×{0}。对任意r∈F，553取q_n为有限复Pan组合，使q_n→r于L²。S q_n∈J_m，且(ell0(q_n),0)∈J_m；二者相减给(0,Tq_n)∈J_m。T有实际C_m界，闭性给(0,Tr)∈J_m。因此

\[
 \boxed{\overline{S(P)}^{\mathbf C\times H^m}
  =\overline{S(F)}^{\mathbf C\times H^m}
  =\mathbf C\times E_m.}
\]

反向包含仅用S(P)⊂C×T(F)。将同一论证放在C×C∞，E_∞=closure_(C∞)T(F)，得到同一product闭包。没有使用image闭性，更没有得到exact S(P)=S(F)或S(P)=C×T(F)。

若要始终用actual Pan逼近而不在J内做代数，可对给定r和目标scalar a，先取q_n→r于L²，再选b_n使前n个H^m的||Th_(b_n)||≤1/[n(1+|a−ell0(q_n)|)]。实际Pan q_n+(a−ell0(q_n))h_(b_n)便有scalar恰a、T腿趋Tr。此有限半范数对角选择只证明目标拓扑闭包，不免费支付源适应强费。

## 4. Mixed、常数metric旧根及净值

固定sesquilinear β若在该joint目标拓扑对第一腿连续，且β(S p,S r)=0对全部p∈P,r∈F成立，则actual Pan逼近S s直接给β(S s,S r)=0对全部s,r。即使β仅定义在源像上，使用源像subspace拓扑中的这些逼近已经足够；不应无条件声称它向整个闭包延拓。无需literal S p=0、ker S=P或exact同像。任何同一完整Weil Gram声称因此与537正非根冲突；未据此构造该经典身份。

R_raw r=Tr+ell0(r)1与joint表达的转换由mean/P0给连续逆，因为T(F)全局均值0。相应raw smooth函数的闭包为C1⊕E_m／E_∞。自然metric配对本来只看ddc，所以h(a1,aφ)=0且raw metric拉回等于T的旧拉回；恢复常数不产生新自然height正号。一般continuous joint coupling的退化则由上一joint闭包另付，不只凭这一metric常数旧根。

连续后处理到closed-point目标、只依同joint数据且杀全部Pan，同样在源像常值。无连续性/非闭base/额外实际数据或改变源域不被此闭包一概覆盖；fixed-window、cofinal、signed误差和未逐层Pan的正D′仍须各自责任，不能由名称免费准入。

本次actualmean强费、actualPan leading及joint闭包是明确raw尾／exact两个Mellin矩加L²余项、405/553和平移连续性的标准直接合成。建议0数学轮；不因mean无du费就报escape，也不把raw joint补全称为新classic whole／primitive/RR／growth/core/coupling/Ξ结果。原literal及整体theta/7.4身份冻结保持，最强旧whole leading4/5仍负惯性UPPER。

## 5. 实际终稿对齐和版本绑定

已完整核读mean稿的exact ν分解、两种强upper、raw Bochner域／交换、actualH中心化／正系数／ξ(5/4)常数、L²弱平移o(1)和固定窗scalar费；没有将其固定窗精确norm误用于双polezero子域或Hlog sharp常数。joint稿的actual Pan图闭包C×L²，比本审稿第3节的目标闭包证明还直接，已逐项核同一修正序列、各Hm/C∞投影、β仅在sourceimage定义的连续性、closed-point后处理及metric常数根范围。末尾§8所绑mean实际版本也已核。未发现需要修订的实质错误；不是仅对照相同结论标签。

最终绑定为UTF-8、LF规范化SHA256：

* mean-strong-fees-and-actual-pan.md：f2c0a7ddb7db17bce68f0d2ca59fbff6bd7bdda0c6d282d525bfbdb16f21ac0f（8707 bytes）。
* joint-pan-closure-and-mixed-scope.md：671dabc98959b8fa7288d4e273db77f1633bb419ae8bc0a714f8ccaf0023ce40（9737 bytes；旧8929-byte draft不作最终绑定）。

只有以上版本获本有限PASS。后续mean系数／余项域／norm／Pan源／目标拓扑或pairing语义改变须重闭相应依赖。当前链是标准／最强旧直接合成0数学轮，原literal及整体theta/7.4冻结保持；不完成长期Goal。本稿没有外部论文／PDF／网页新读取，不改任何其他文件或运行状态，也未执行下一候选。
