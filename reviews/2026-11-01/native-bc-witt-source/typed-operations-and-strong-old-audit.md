# Native BC–Witt: typed operations and strongest-old audit

2026-11-01；独占source审查，SAME G20261027/runtime1793085111，0c4f冻结基线。
先读reading-scope-freeze.json及当前STATE/check/show/决策；不修改公共状态。
独立复核PDF29页、3328150bytes、SHA256
72a0bb1785f593cb447435812278379db471ce4b17944ed02fb85a2011465d60。

**结论：native整系数endomorphism invariant与F/V运算设施真实，并非365或
ordinary relative-K门已消费的同一对象；但没有不同的physical源入口。
对当前经典core记SOURCE0，停止该限定来源门。** 不把源设施说成新Weil
正性，也不从本门推出KEnd／Hermitian／higher或其它relative路线不可能。

实际阅读：§3 physicalPDF7 bottom–14、15 top至§4前，printed453–461，
含3.1–3.4与Th3.11/3.12；§2只使用Hecke对象／代数定义所需段落。
目视共享PNG5、7 bottom、8–14、15 top核全部消费公式；提取时出现的相邻
§2 survey、intro尾及15下半§4开头仅曝光，不作独立结果消费。没有继续
§4、引用或其他版本。保原PDF字节，未用OCR猜改公式。

## 1. 先纠正typed名称：Sbar，不是整数环的代数闭包

PDF字体的overline(mathbb S)被pdftotext误读成Zx；图像确认这里是

    Sbar=S[M]，M=(Q/Z)_+={basepoint 0}∪{e(a):a∈Q/Z}，
    e(a)e(b)=e(a+b)，Sbar[X]=X∧M.

S为本节Γ^op→Sets_*的绝对基底；S[F](X)=F∧X，F为有限pointed set。
这里不是普通Zbar／代数整数环，也没有在本范围证明一个Quillen
K-spectrum或任意projective-module范畴等价。整系数Z出现在最终
endomorphism-invariant ring Z[Q/Z]，与basepoint0、e(0)的乘法单位分开。

Th3.1引用[20,Th2.3]：W0(S)识别为Z[Q/Z]在Aut(Q/Z)=Zhat^×作用下的
不变部分。此为CITED前件，不跟读外部证明。Th3.11将Sbar上的W0识别为
完整group ring；不能把“不变子环”与“完整group ring”混写。

## 2. 实际End对象／零部分／相似性

对象为E=Sbar[F]（有限free pointed-module型）及其自然endomorphism。
Lemma3.2以在1_+上的值识别S-module natural maps；Prop3.4据M等变性给

    Mat_n^R(Sbar) ≅ End_Sbar(Sbar[n_+])，
    rho(mu mu')=rho(mu)∘rho(mu').

Mat^R每列**至多**一个非basepoint项；零列允许。其系数仅为M，不是任意
复矩阵。这一composition是endomorphism的composition，不能直接当作
下述W0的乘法。

为表达相似性，源另引Mat^L（每行至多一项）及无限制行列的Mat_n
bimodule。乘法有定义靠一侧的单项限制；没有赋予任意M矩阵一个普通
加法环。Def3.6所谓alpha invertible，是其在**全部field extensions**
的矩阵像可逆；不是说alpha已有Mat^R的native inverse。

Def3.8的invariant chi取值于commutative ring，要求：
- chi(E,T)=chi(T(E),T)，丢掉非稳定像上的零／nilpotent部分；
- wedge对应加法，over-Sbar的smash对应乘法；
- 按源定义的fieldwise-invertible intertwiner保持similarity。

因此W0是**这些明确relations下的universal endomorphism-invariant
ring**，不是未经说明的ordinary K0(Sbar)、K1或relative K0(A,I)；
本节没有给任意exact sequence的higher-K／Quillen比较。
Th3.11按论文通常的ring/invariant约定消费，不外推任意nonunital
class-valued函数的普遍表示定理。

## 3. tau与Th3.11：直接证明实际支付了什么

Prop3.9先用injective M→k（algebraically closed、characteristic0）作标量
扩张，取非零eigenvalues的divisor，再拉回到M^×：

    tau: Mat_*^R(Sbar) → Z[Q/Z].

有限functional graph的稳定像是带roots-of-unity权的permutation；故其
非零eigenvalues仍为roots of unity，pullback divisor不依所选embedding。
Almkvist invariant的既有性质被引用以付wedge/direct-sum及smash/tensor
compatibility；不是本审查重证所有Almkvist theory。

Completeness的本地证明有实质内容：去掉transient部分，拆成带权cycle，
取适当root将cycle化为e(s)C(m)，再以有限Fourier intertwiner连到
e(s)Delta(m)。Prop3.10、printed459/PDF13目视为

    V_ij=e(ij/n)，W_ij=e(-ij/n)，
    Delta(n)V=V C(n)，C(n)W=W Delta(n)，
    V^-1=(1/n)W 仅在field extension中.

k含n个不同n-th roots，故char(k)不除n；这个1/n不在原pointed monoid M，
更不证明Sbar内n可逆。正是Def3.6的fieldwise相似性允许使用V；
不能把此证明偷换成“所有对象native自由基变换下已经对角化”。

Th3.11实际给tau诱导的canonical coefficient-ring同构

    W0(Sbar) ≅ Z[Q/Z].

任意源定义的invariant按一维对象[e(a)]的值经group-ring map因式分解。
特别地[e(a)]→e(a)是实际非零整基元；wedge/direct sum与相对smash/tensor
分别给整系数加法与e(a)e(b)=e(a+b)。允许formal differences的是最终
ring，不把有负系数的class自动称为effective endomorphism对象。
没有给无限rank／完成Witt、大Witt空间、source topology或Hilbert norm等价。

这与仅复述“有Witt系数”相比确实支付了一条native universal比较；
但universal有限对象invariant不等于经典physical全部源的primitive商。

## 4. Frobenius／Verschiebung：方向与1/n不能混

§3.4实际显示（5）–（8）：

    F_n(E,T)=(E,T^n)，sigma_n(e(a))=e(na)，
    tau∘F_n=sigma_n∘tau；

    V_n(E,T)在vee_n E上cyclically shift，最后一项用T回第一项，
    tilde-rho_n(e(a))=Σ_(nb=a)e(b)，
    tau∘V_n=tilde-rho_n∘tau.

F_n是ring endomorphism；V_n由wedge构造为additive transfer，未声称
unital ring homomorphism。F_n提高eigenvalue的n次幂，V_n取全部n个
preimages，方向相反。sum有整系数1，没有平均1/n。

如下仅是对源display的精确normalization首检，不是另开数学定理：

    sigma_n tilde-rho_n=n·id，
    tilde-rho_n sigma_n(e(a))=e(a) Σ_(nb=0)e(b).

故若为了与另一种BC convention比较，在Q扩张上定义
rho_n=(1/n)tilde-rho_n，则sigma_n rho_n=id，但rho_n sigma_n是相应
rational idempotent的corner map。**此rho_n不是本文整W0上的V_n。**
尤其tilde-rho_n(1)=Σ_(nb=0)e(b)，n>1时不等1；不能把它当sigma_n的
integral inverse，也不能混用“quasi-inverse”一词省去n。

在实际一维对象[e(0)]上，V2的tau是e(0)+e(1/2)，V3的是
e(0)+e(1/3)+e(2/3)；V2V3经(8)读成全部sixth roots，等V6的tau。
F2F3在[e(a)]上给e(6a)。这是同一个source-provided对象与图的首检，
不只把索引2·3=6当新结果；无科学数值、渐近或新费用推导。

## 5. BC coefficient ring、enriched系统与C*范围

§3开头给integral Hecke model H_Z=Z[Q/Z]⋊N（其定义／presentation指向
[10,§3]），并列sigma_n、tilde-rho_n。§2用于辨认Hecke／operator系统；
没有在此门重新消费KMS、partition function、site RR或analytic survey。

Th3.12的字面结果是：sigma_n↦F_n、tilde-rho_n↦V_n给integral BC-system
与带F/V的W0(Sbar)的canonical identification。**本范围消费分两层：**
- Th3.11的coefficient-ring universal比较及（5）–（8）compatibility有
  可见定义与本地直接证明／检验。
- Th3.12为enriched integral-system的CITED statement；其后没有独立详证，
  文字还指向[20,§2.2]的类比／推广；本门不跟读该引用。

不能由此宣布noncommutative H_Z的bare ring与commutative W0裸环同构，
也没有核任意chosen crossed-product presentation的faithfulness／全部关系。
integral model不是full C*-completion、时间演化、KMS态或任何其上的
Hilbert／norm等价。把1/n加入normalized transfer会换系数／presentation
层，更须独立闭合，不能从本节中免费的W0同构推出。

## 6. 与最强旧比较：不能跨对象0，也不能跨对象正

365的W=C[R_+^×]近似、移动字符chi_lambda/theta_mu与T2T3=T6已真实存在；
固定chi1遗失变换后除子信息的失配也已核。本源的torsion monoid Q/Z、
有限End与整数group ring是另一对象；不能声称365已证明本Theorem3.11，
也不能将其固定标量化no-go直接套到这里。反过来，这个新读native同构
没有提供365所欠的global physical-divisor自然性。

旧Deninger rational-Witt flow给periodic orbit packets的实际设施；不是本
Sbar有限End ring，也未因此拥有共同正Hodge/mixed容量。

573有actual relative charge、指定ideal/−4 obstruction及其闭包；
574–575有非平凡relative线、Cartier、normal/filter和源费用，不能重称
“旧无非零算术类”。574完整Q-marker甚至已经可同时消Pan、保537并有
正纤维metric，却仍无独立容量。本native非零[e(a)]和整数运算不自动比
这项已付控制更接近完整Weil正号。

native unit门的A=Cδ0⊕S_exp、q(U_r)及ordinary K1→relative K0连接像，
因实际unit lift而全源0。这里既不是同一K对象，也没有从U_r到本有限
End范畴的函子，故该0结论**不适用**；本门也未构造一个不liftable的r类。
KK／Todd／endomorphism invariant同样各保自己的范畴和map。

577已有不读未知零点的实际PSD层及完整Gamma协同费用，578已定位signed
缺陷；本§3没有新的正D′ generator／signed-limit比较。整数F/V本身不选
Hermitian号，不支付危险corecross，不能由“整数运算”直达Deligne全阶
global pole或Weil容量。

## 7. 原源／norm／sign／growth前件与净结果

本source-gate domain是有限F、root-of-unity sparse endomorphisms及其
formal invariant ring；目标是Z[Q/Z]及声明的F/V integral系统。它没有

    rho=e^(u/2)f∈S_exp,C → (E_rho,T_rho)／class的actual规则，
    405全部noncompact Pan及平移的principal／boundary消去，
    537非根在同一map下保留、full-source coverage，
    原du／zero-extension Dlog、强半范数、noncompact尾或逆费用，
    integral filtration／section乘法和同源mixed Weil／RR身份，
    Gamma=2theta'、FP/contact、ALL proper powers／双pole完整预算，
    cofinal源窗／频高与通常Xi的合法共同成长比较。

实际roots of unity的finite End eigenvalues不等于ζ零点的谱完整性；
n可取所有正整数也不提供Λ(p^k)=logp、p^-k/2或两pole／Gamma系数。
抽象整数multiplicity与相应source/growth量词不可混同。
本门没有“零physical输出”或“正physical输出”的结论，因为actual map缺失。

因此可保存的新增来源资产是**准确typed native universal coefficient
ring与F/V图**；core净结果SOURCE0。并非因它不是完整RH便判其无价值，
而是本门按预先首检实际确认只有native设施，没有different actual源入口。
没有新principal／sections／mixed/core-cross或成长约束可进入Goal完成门。

旧fixed17/16、9/8 finite448及same605头ALL补空间正完成不变；
542+555→557 whole leading4/5仍为负惯性UPPER，非负谱lower或正性。
关键瓶颈和三个Goal门仍open。来源阅读0数学；不建C070／607，不续§4、
引用、normalized变体、另一K理论、论文或新源构造队列。
