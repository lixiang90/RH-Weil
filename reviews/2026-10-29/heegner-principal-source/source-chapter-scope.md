# BO2010指定Heegner主除子章节：来源范围与未付前件

2026-10-29。仅为指定来源门原件；不改STATE/cadence/Git，不另准C059。本稿实际核原PDF，不以parent消息或旧locator代消费。结论是：原文给合法harmonic Maass输入的真实degree-zero Heegner除子、canonical第三类微分及条件性主除子判据；尚未给项目采样源的harmonic lift、principal消去或原du费用。M37/Delta1的形式cycle可以分real/imag逐项校型，但不能由此宣布通过physical准入。

## 1. 恢复、版本与实际读页

已读goals/README、STATE，check后show，G20261027完整目标/原0c4f基线，C058停止范围、D20261029U、宏观前沿当前段及next-heegner-principal-source-admission.md。首次check遇parent并行写入的pending缺observed_at，已通知parent；parent补齐后本任务实际重新check后show通过。仅此结构恢复，不代数学证明。

固定来源：Jan Bruinier、Ken Ono，*Heegner divisors, L-functions and harmonic weak Maass forms*，Annals172(2010),2135-2181，[官方页](https://annals.math.princeton.edu/2010/172-3/p15)、[固定publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n3-p15-p.pdf)。实际输入literature/local/2026-10-29-bruinier-ono-source/bruinier-ono-annals-2010.pdf，1642204bytes，50PDF页，SHA256 **4e525de101a42344020c8df901e5900fcd68f8d66f1312721b824995609bf4d6**。

独立从该PDF提取定位并用Poppler110dpi渲染目视：PDF24/25=printed2157/2158的(5.1)-(5.4)及相邻输入条件；PDF28/29=printed2161/2162的§5.1假设、(5.10)-(5.12)、Th5.4/5.5及proof/Remark14；PDF30=printed2163只消费Remark14接续的顶部两行；PDF15=printed2148只消费Th3.2 statement及其number-field前提，不查Scholl/Waldschmidt原文。页图独占前缀source-defs/source-chapter/source-scholl/source-remark14-top，均在上述ignored本地目录。

读页曝光说明：整页15/25/28有相邻Prop3.1/§3.1/Th3.3、Lemma5.1及proof、上节末尾等；其中仅Th5.4/5.5证明所明示依赖作cited dependency，未独立支付引用原稿。整页30文本提取意外曝光Remark15、§6opening及Th6.1，未消费其结论或proof，未扩展后章预算；目视30仅核顶部Remark14接续。没有联网/新paper/§7/§8/level或Delta搜索，也没有source/Gram数值重跑。

## 2. 原文标签、degree与输入域（cited）

记论文level为N，本候选令N=M=37；不与旧数值N448混用。固定fundamental discriminant Delta及整数r0，要求Delta congruent r0^2 mod4N。h在原论文L'/L中；合法m为负有理数且

    m in Z + sgn(Delta) Q(h),    d=4Nm sgn(Delta) in Z.

原文说明d是与Delta异号的discriminant且模4N同余于平方。Delta本身须fundamental；d不被要求fundamental。不能将任意负实采样点当合法m。原(5.1)是在L_(dDelta,hr0)/Gamma0(N)上求和，单点权为chi_Delta(lambda)/w(lambda)，w为该lambda的Gamma0(N)稳定子阶，w in {2,4,6}，dDelta<-4时w=2。所有L、Q、genus character沿原定义，不在本门改标度或重新归一化。

原(5.2)为

    y_(Delta,r0)(m,h)=Z_(Delta,r0)(m,h)-deg(Z_(Delta,r0)(m,h))*infinity.

所以y确为degree0。只有Delta!=1时原文才直接写y=Z；固定Delta1不可丢去degree/infinity腿。Delta>0时Z(m,-h)=Z(m,h)，harmonic Maass holomorphic及nonholomorphic系数也取h对称；Delta<0对应反对称。不能直接套Th5.5 proof中的非平凡Galois反不变论证到Delta1，后者须走Remark14的cusp修正。

输入为论文既定H_(1/2,tilde-rho_L)中的harmonic weak Maass form，tilde-rho_L在Delta>0时为rho_L、在Delta<0时为bar-rho_L，f=f^++f^-。本门没有重证§2/§4的域定义或任意给定主部的存在定理；不能把一张有限有理系数表自动识别为该空间成员。原文要求所有c^+(m,h)实，负主部系数按(5.3)/(5.4)合成Z(f)、y(f)；主部系数有理则这些是有理系数除子。§5.1另要求**全部m<=0的c^+(m,h)有理**；Delta1还明确要求**c^+(0,0)=0**以使Phi harmonic。存在满足这些全部条件的f是实际前件，不由finite negative sampling支付。

## 3. canonical Green/第三类微分与主除子判据（cited）

原(5.11)的符号经目视确认是

    eta_(Delta,r0)(z,f) = -1/2 * partial Phi_(Delta,r0)(z,f).

此前metadata locator若记作+1/2不能消费。它不是纸面无关紧要的号：本稿和后续source/Green运输均绑定原负号。由(5.12)其residue divisor为Z(f)+C(f)，C支持在cusps，cusp重数由Weyl vector rho_(f,ell)给出。原文这里将第三类微分的residue条件放宽至real，不能把一般complex residue直接当相同canonical实除子对象。

Th5.4称此eta是Z(f)+C(f)的canonical第三类微分。其q展开为2pi i dz乘以

    rho_(f,ell) - sgn(Delta)*sqrt(Delta) * sum_(n>=1) sum_(d|n)
      (n/d) * (Delta/d) * c^+(|Delta| n^2/(4N d^2), r0 n/(2N d)) * e(nz).

这是原输入的square-index正系数，不是可从负主部直接任意指定的新系数。Th5.4 proof用Phi harmonic与Prop3.1的canonical性质，再对(5.10)微分和Gauss sum重排；本门核了该局部推理，未重证上游theta正则化/Prop5.2/Th5.3/Prop3.1。

Th5.5字面先假Delta!=1。其三项等价为：y(f)某个非零multiple是X0(N)上rational function的divisor；全部正整数n对应的c^+(|Delta|n^2/(4N),r0 n/(2N))为algebraic；同一无限组系数为rational。这里主除子条件是Jacobian类的torsion条件，绝不是任意有理Heegner divisor必principal。

Th3.2 statement的责任是：曲线及degree0 divisor D定义在number field F上时，若非零multiple D principal，则其canonical第三类微分定义在F上；否则该canonical differential不定义在Qbar上。Th5.5 proof由Th5.4正系数展开、此超越性判据及q-expansion/Mobius inversion得到等价；本门只按原文cited消费Th3.2，没有把Scholl超越性或相关height理论重证为项目资产。

**Delta1的Remark14不可省：**还需S_(1/2,tilde-rho_L)=0，或更一般f对该cusp空间正交，才能保证Weyl vectors有理，从而C(f)有理。该正交是论文的modular输入条件，不能换成physical du正交。在此条件下Z(f)+C(f)与y(f)相差degree0的cusp divisor，原文以Manin-Drinfeld使其在J(Q) tensor R中同类，因此Th5.5也成立。这里既非literal divisor相等，也不是cusp项可免费删除，更不从N37自动推出S=0或所选f正交；本门未做该维数/正交证明。

## 4. 对冻结M37/Delta1采样的实际校型及停止范围

Delta1、r0=1满足1 congruent 1^2 mod148，因而twist参数的同余检查通过。I37须保留原合法标签：h in L'_37/L_37，m<0且m in Z+Q(h)，d=148m；不擅自替换Q(h)的basis归一化。只在此I37上取固定sqrt(X)<=|m|<=X^(3/2)时，有限个m/h及原y标签使采样的real/imag部分分别成为有理系数degree0 divisors。h与-h的权因仅依赖m而相同，符合Delta1的对称性；重复标签沿原求和保留，不另除2。

每部分k/T_X是有理数，原w只取2/4/6，因此**12T_X**可清这些有限和及degree修正的几何除子系数分母。这只校型为integral geometric divisor，未付整模型、垂直位、metric、integral line bundle family或section lattice。Complex D只是两条实有理除子的complexification；主除子判据与canonical实residue应先分别应用，不能直接由complex权认定原定理输入。

尚未支付：每个(r,X)相应合法harmonic Maass form f_(r,X)的存在及其真实全域/实系数/constant0/正交条件；正square系数的全部代数性/有理性；所有405 noncompact Pan及平移的actual principal/Green消去；537实际非根源不被送零与全源coverage；du/Dlog/强尾到Jacobian或Green/height的范数和成长费用。Rounding/有限cycle合法不改变这些逻辑方向。即使另有harmonic lift，定理也只是把principal问题移到另一组未知正系数，不能把判据本身当已证明principal身份。

本门实际取得新的章节来源信息，准确补齐了负号、Delta1的constant/cusp条件及合法标签，未形成classic physical-source principal桥。应按本限定来源门停止，不据此开C059、扩至§6/§7/§8、追引用或改level/Delta。它不证明全部Heegner/relative/有费强源路线失败；strongestwhole4/5负惯性UPPER及primitive/principal/sections/mixed、危险corecross/成长Xi仍由原状态保持。本任务不改计轮；root须对齐另一physical-oldscope原稿及不同fresh后自行消费结算。

本任务只写本文件和ignored页图，没有数值session、子任务或其他pending。
