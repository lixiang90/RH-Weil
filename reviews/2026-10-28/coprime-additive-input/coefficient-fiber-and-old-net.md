# 固定互素加法规则：four-shift、完整fiber与强旧净值

2026-10-28；unit_modularity独占支持。恢复Goal／STATE／D20261028R、formal17、check→show及实际工作树；cadence0／历史50／latest586保持。本稿只审root冻结的[唯一规则](actual-two-source-candidate.md)，不改权、cutoff或另造candidate，不建C050／587。无web、PDF、数值、STATE或Git变更；实际源费用／绝对收敛由另一独占腿付，root统一消费前不以支持出稿代结果。

**结论范围。** 有限fiber恒等式严格成立；q=1、φ(c)、strict endpoints及排除c=1均不可漏。绝对收敛后，cofinal规则是两个普通grid读出与ζ(2)、ζ′(2)的固定组合，另有必需补项∫ℓJ。不能由(7)认定恒零，也不能把它简化为只由两个数决定的常数型；本门不需消费C∞是否非零。本稿不从两个常数或有限ratio原子推出经典型不等。若把本规则本身主张为完整Weil逼近，则另一腿的global H¹ bound与旧553／405／537已给更强的limit身份障碍，见§6；这才是准确旧0的链。

## 1. four-shift、±及候选自身的contact

固定内积第一变量线性，\(T_a r(u)=r(u-a)\)。令
\[
 A=\log x,\ B=\log(1-x),\quad
 J_x=\tfrac12[\langle(T_A-I)r,(T_B-I)s\rangle
              +\langle(T_B-I)r,(T_A-I)s\rangle].
\]
由\(\langle T_Ar,T_Bs\rangle=\langle T_{A-B}r,s\rangle\)，精确展开为
\[
 J_x(r,s)=\left\langle\left[I+\tfrac12(
 T_{A-B}+T_{B-A}-T_A-T_{-A}-T_B-T_{-B})\right]r,s\right\rangle.
 \tag{1}
\]
对\(h=r*s^*\)，\(\langle T_a r,s\rangle=h(-a)\)。最终核是偶的，故作为h上的分布恰为
\[
 j_x=\delta_0+\tfrac12[
 \delta_{A-B}+\delta_{B-A}
 -\delta_A-\delta_{-A}-\delta_B-\delta_{-B}],\quad
 J_x=j_x(h).
 \tag{2}
\]
其Fourier symbol是\(1+\cos((A-B)t)-\cos(At)-\cos(Bt)\)，总质量0。J_x为Hermitian mixed型，J_x=J_(1−x)，不因此认定PSD；cos项的正负不能改成全正。

一般x的显式δ0系数为1；x=½时ratio shift为0，还要合并一次contact：
\[
 j_{1/2}=2\delta_0-\delta_{\log2}-\delta_{-\log2}.
\]
primitive点x=½只在c=2、a=b=1出现，连续对照中单点无质量。有限B≥2时，候选自身的δ0原子系数为
\[
 \sum_{2\le c\le B}\frac{E_c(\log c+\ell)}{c^2}
       -\frac{\log2}{4},\qquad
 \ell(x)=\log x+\log(1-x),
 \tag{3}
\]
其中\(E_c(\log c+\ell)=2\sum_{(a,c)=1}\log(a/c)+2\varphi(c)\)。最后项是midpoint ratio并入δ0的额外量。式(3)是候选自己的contact，不是经典Γ的FP/contact，也没有由此取得任何pole项。

三腿赋值收缩确为
\(\gamma=\log a+\log b-\log c\)。高赋值通过\(v_p(n)\log p=\sum_{j\le v_p(n)}\log p\)进入，不能声称保留全部valuation向量；不同prime坐标经过这次log-linear收缩后已经合成三个实数。

## 2. 完整Möbius fiber恒等式，含q=1

对任一F∈L¹(0,1)、且各内部grid值有定义，记
\[
 R_q(F)=\sum_{1\le k<q}F(k/q)-q\int_0^1F(x)dx.
\]
coprimality indicator为\(1_{(a,c)=1}=\sum_{d\mid a,c}\mu(d)\)。在同一c下令c=dq、a=dk，严格内部范围变成1≤k<q，故
\[
 \sum_{(a,c)=1,\ 0<a<c}F(a/c)
 =\sum_{d\mid c}\mu(d)\sum_{1\le k<c/d}F(k/(c/d)).
\]
同时\(\varphi(c)=\sum_{d\mid c}\mu(d)c/d\)，所以
\[
 \boxed{E_c(F)=\sum_{d\mid c}\mu(d)R_{c/d}(F).}
 \tag{4}
\]
F可以随c变；对每个c分别应用即可，没有把G_c换成G_q。

q=1的内部和为空而\(R_1(F)=-\int F\)，不能设成0。最便宜的端点检查是F=1：所有q有R_q(1)=−1，c>1时−Σ_(d|c)μ(d)=0，正好E_c(1)=0；只删q=1就会破坏这个恒等式。用(q−1)而非q作中心虽可另立等价账本，但必须同时改所有R_q及补项，本稿固定原规则不作这种改写。

## 3. 同product cutoff的精确展开与cofinal常数

简记J(x)=J_x(r,s)，\(G_c=(\log c)J+\ell J\)。由(4)，原2≤c≤B严格等于
\[
 C_B=\sum_{\substack{d,q\ge1\\2\le dq\le B}}
 \frac{\mu(d)}{d^2q^2}
 [ (\log d+\log q)R_q(J)+R_q(\ell J)].
 \tag{5}
\]
这是同一product cutoff，不能换成d,q各自≤B的矩形而不付尾；也不能漏log d。

为安全消费cofinal，要求并由norm腿核实
\[
 \tag{A}
 \sum_{q\ge1}\frac{(1+\log q)|R_q(J)|+|R_q(\ell J)|}{q^2}<\infty.
\]
加上\(\sum_d|\mu(d)|(1+\log d)/d^2<\infty\)，它给完整double绝对收敛，才允许下列分离。定义普通、**未加coprime筛**的grid读出
\[
 \mathcal A_0=\sum_{q\ge1}q^{-2}R_q(J),\quad
 \mathcal A_1=\sum_{q\ge1}q^{-2}
                [(\log q)R_q(J)+R_q(\ell J)].
\]
Re z>1上的绝对Dirichlet反演及导数给
\[
 \sum_d\frac{\mu(d)}{d^2}=\frac1{\zeta(2)},\qquad
 \sum_d\frac{\mu(d)\log d}{d^2}=\frac{\zeta'(2)}{\zeta(2)^2}.
 \tag{6}
\]
第二式是正号ζ′／ζ²，不能漏掉对d^(−z)求导的负号而写反；ζ′(2)本身为负。

还要处理原c≥2。若把(5)补成dq≥1，(d,q)=(1,1)项为\(R_1(\ell J)=-\int\ell J\)，所以原式必须再**加回**∫ℓJ。因此
\[
 \boxed{C_\infty(r,s)=\frac{\mathcal A_1(r,s)}{\zeta(2)}
 +\frac{\zeta'(2)}{\zeta(2)^2}\mathcal A_0(r,s)
 +\int_0^1\ell(x)J_x(r,s)dx.}
 \tag{7}
\]
这项补正附在本记录，不修改原冻结candidate字节。q=1不能丢，原c=1也不能被无声加入。

(7)说明互素筛及log d在cofinal中只留下两个收敛半平面的已知Euler常数；其余仍是全部ordinary grid的非平凡两源读出，不是两个数决定的常数型。没有保留一个独立的全prime赋值tensor、primitive cycle或经典临界signed预算。ζ(2)当然含全部primes；“只剩两个常数”指本次筛／赋值收缩的角色，不能误说ordinary grid没有整数算术内容。

## 4. 收敛域与原费用的依赖边界

norm腿交付的足够前件是原physical r,s∈H¹(R,du)，J在[0,1]端点为0，且对\(R=\|r\|_{H^1},S=\|s\|_{H^1}\)
\[
 \operatorname{TV}J\le4RS,\qquad
 \operatorname{TV}(\ell J)\le12RS.
\]
端点为0的绝对连续F给\(|R_q(F)|\le\operatorname{TV}F\)，**包括q=1**；这支付(A)及(7)的合法换序。相同费用给C_B在global H¹×H¹上绝对／norm收敛与uniform界，精确常数和尾由该腿原稿负责。本稿在该前件下消费，不用有限B粗du界代替它。

H¹是原u上的导数费，不是globaldu或zero-extension Dlog统一费；频高调制的H¹费用仍增长。Cc∞和S_exp包含于该域，故全部先fixed此类complex源都合法。B、physical窗L和频高相互独立；本稿不扩到moving源／成长窗统一Weil比较。也不以强源费标签免除某个必要读出自身在H¹连续的旧责任。

## 5. B=3／5的ratio系数，只作有限账本检查

令h0=log(3/2)>0。有限c的连续对照中，x↦logx、log(1−x)、log[x/(1−x)]的pushforward在非零点没有原子，所以±h0的有限原子系数只来自离散三元组。

* B=3：c=3的(a,b)=(1,2),(2,1)，γ=−log(3/2)；各j_x在±h0上的负系数为−½。两个ordered点合并给
  \([C_3]_{\delta_{h0}}=[C_3]_{\delta_{-h0}}=\log(3/2)/9\)。
* B=5：c=4无该位移；c=5的(a,b)=(2,3),(3,2)，γ=log(6/5)，各ratio正项为+½。因此
  \([C_5]_{\delta_{\pm h0}}=\log(3/2)/9+\log(6/5)/25\)。

这些是exact log数，不用浮点或ζ零点。它们验证负single-scale项和正cross-ratio项都必须保留。**不能由此宣布D′极限带该原子或已不等于Wζ。** 各层TV没有从norm腿H¹费用自动得到统一Radon控制；后续dense atoms／连续对照的极限仍可能改变分布型。即使逐层可列某个原子，也不能省掉共同局部测试／极限责任。本稿不为此续whole UV或sharp分析。

## 6. 最强旧净后果：limit层身份责任，不是逐层Pan

普通Farey／Riemann grid和Möbius incidence重排本来在080–096；080的整除inverse、085的exact既约fiber合并、096的原坐标Gram等设施并非新缺口。当前A0、A1使用这次具体J test function，不宣称逐式等于旧085的Gram；旧h/r是sawtooth Fourier频率，此x=a/c是log平移核的实参数，两者不混。549／550已强调保全cofactor cross与actual合成方向；(5)不能被当成新row抵消。036区分乘积／max／ratio平方，578已核|Dirichlet polynomial|²会添加ratio频率、contact与二次系数而不自动付线性P／Γ／双pole。(2)、(5)、(7)是本规则确实落到这些责任内的逐式依据，不是按Farey名字预判。

还有更强的已付识别门。**假设**本规则在全部compact complex卷积平方上趋Qζ。由norm腿H¹ norm收敛，极限是C∞；Hermitian polarization给compact mixed身份。对任意r,s∈S_exp，以同一χ(u/R)分别crop；源在H¹及S_exp收敛，C∞由H¹连续，完整Bζ由Γ multiplier／所有pp／双pole的S_exp连续性延续，故身份扩到真正noncompact S_exp。

旧405全Weil radical于是给C∞(p,s)=0，对每个physical \(p\in C(P_{\rm an})\)、其全部平移及固定s∈S_exp成立；这里C是旧物理中心化f↦e^(u/2)f，未把bare关系换成physical向量。旧553§2明确付出这些complex平移span在**每个fixed有限Sobolev、特别H¹**稠密；这不是从L²密度偷换。由C∞的global H¹连续性，固定s的读出在整个H¹上为0。取旧537的非零compact probe r0为r=s便与Qζ(r0)>0矛盾。

所以若声称(3)本身给完整Weil逼近，这个**limit层、全源**身份由强旧＋已付原费用直接排除；不需要要求每个有限B exact消Pan，也不需要用有限ratio原子反证。这是标准强旧净后果，不能以新formula首次打印再算一个完整核心数学轮。

若仅把C∞当作未来某个unbounded／含完整pole读出的一个signed correction，上段不能无条件套到那个未知总型；但本次并未给这种同源identity或独立净方向。均匀对照也没有成为经典Γ／FP-contact。故当前得到的是一个合法ordinary-grid fixed postmap及其原域费用，**无可准入的新独立signed／mixed核心input**；不宣称所有互素加法耦合失败，不推Qζ负或RH反例，不改whole4/5UPPER、585必要费、actualcore／cross或Ξ。

止这一个固定规则，不改c^−2、γ、中心化、权或cutoff，不另接Γ补偿／paper。root统一核两腿前件与分类后消费；本稿不自行结算合同、数学轮或完成长期Goal。

## 7. 实际费用输入绑定

本稿实际读并绑定[source-norm-and-farey-factorization.md](source-norm-and-farey-factorization.md)，10494 bytes，LF SHA-256 `2639c943906396e5ca05972b6dd7d258b060e5bca4b4cd934bcd6af8387dab7b`。其§2–4支付本稿(A)、原H¹端点／BV费用、全double绝对收敛及C_B→C∞的H¹型norm收敛（尾O(log²B/B)）；§6与本稿§6的旧553／共同crop角色相容。本稿直接读了冻结candidate、旧553§1–2及必要尾段，并读080／085／095／096的必要对象段，复用已核036／549–550／578原范围；不是重新审阅整个080–096来源链。root对齐两稿后才作整体消费，哈希不代数学前件。

审中scope补正：原10817 bytes／LF `3f70efb0d4dd5deb1222be4e412548a5baa2f0211e7f45447917cc7c2945bfd4`开头“它不是零”的宽读未被root消费，现冻结并以本版替换。有限ratio系数没有支付C∞非零见证；本门不新增该测试。§6的limit身份553链不依赖C∞是否非零，其余公式与证明范围保持。
