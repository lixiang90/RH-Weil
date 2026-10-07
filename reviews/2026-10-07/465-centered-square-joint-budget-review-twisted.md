# 465 原 centered high-square 联合预算：独立全文审查

2026-10-07。twisted_research。全文限定 PASS。
本报告不修改被审稿、已冻结笔记/论文、math、脚本、输出或 Git。

## 1. 冻结绑定与完整审查范围

被审对象：
[465](../../notes/465-centered-high-square-joint-fourth-budget.md)。
canonical LF SHA-256：
a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464。
UTF-8 原字节 10069、272 行；只把 CRLF/lone CR 改为 LF，不 trim。
本次重新全文阅读五节，没有仅沿用作者推导报告。
初次数学审查为0afe9f35版本；最终scope修订已逐段核验，新增466的
实际阻断并将旧小Q前件明确改为不可达到的反事实，既有有限公式不变。

重核前件：454 的 bounded-multiplication 泄漏、全 log-range 物理
二矩与 alias；461 的 actual entire13；462 的 actual low fourth；
455 的 proper-power Schatten 小量；452 的同响应 padding 稳定性。
另实读197的 quartic LP 与228 §5包含有限边界误差的比例转移。
全部本地 Markdown 目标实存。

## 2. W 的实际域与四个二矩

W 是原同 high 素数 diagonal 的 bounded multiplication 压缩，
不是 H² 的正部或 freely added compensation。
Σ_H b_p²=O(1) 与原 φ derivative bounds 给 w 的统一 sup、
一二阶 L1 derivative，端点值/导数接合。
所以原 finite carrier 的 ell_w²=O(log(2+log X)) 可直接应用。

对 B_RE=EC_R+QB_RE，middle multiplication comparison 的三个项
分别由一侧 w 泄漏、另一侧 prime 泄漏和双 prime 泄漏支付。
正文(6)严格为

m_R ell_w ell_S+m_S ell_w ell_R+||w||∞ell_R ell_S。

HH 费用 O(X log(2+log X)/(log X)²)=o(d)，HL、LL更小。
这个 raw op 账本没有使用 H⁴ bounded，也没有以 physical cyclic trace
免费移除外侧 E。

物理部分在454保留全部 difference Hilbert主项、±log X remainder、
opposite-sign sum-alias实际重叠长度；取 B_H+zB_L，z=1,i，
其 diagonal 是 high+|z|²low，labels互不交。
由复极化得到两个复 cross 本身为 o(d)，不是只得到 real part。

非自伴顺序精确核对：

Tr(WHL)=Tr(LWH)，
conjugate Tr(HWL)=Tr(LWH)=Tr(WHL)。

因此正文先比較物理 B_H M_w B_L，再取共轭，确实恢复所需 WHL；
没有把 HWL 误当成 WHL。HH/LL的物理同label diagonal分别为
〈w²〉与〈w d_low〉。Mertens partial summation 和原共同 profile
给(2)–(4)极限，TrW²=d〈w²〉−ell_w²亦为准确有限恒等式。

## 3. 原 actual Γ 代数与未知增长的量词

Γ=H²−W 是 selfadjoint，q_T=||Γ||HS²/d本身非负。
两个高 weighted 二矩极限使
a_T=Sψ+q_T+o(1)，这个 o(1) 独立于未知 a_T。
作者没有将可能略负的有限 a_T−Sψ 放进根号。

TrH²L²=||HL||HS²≥0，HL不需 selfadjoint。
准确分解
c_T=s_T+TrΓL²/d，
b_T=t_T+TrΓHL/d
配合复 HS Cauchy 给(10)。虽然第二个 pairing及t_T可为复数，
b_T为实数，取绝对值合法。

TrHLHL为实数且绝对值≤TrH²L²，故整个22 union≤6c_T。
finite cyclic expansion 的31、13系数均为4，22系数为4、2，
未丢掉某个 signed word或repeated label。
W≥0、L²≥0给s_T≥0，所以 u_T=s_T+√(q_Te_T)确实非负。

(12)保留 actual e_T、s_T、t_T、η_T，因此无需q_T bounded。
只有另有limsup q_T≤Q<∞，才把低四矩与加权二矩极限统一放进根号，
用连续性/单调性推出(13)。这是正确顺序；
没有让未受控√q_T放大已删的低矩误差。

## 4. Flat 归一化、背景恢复与 one-sided LP

在同一flat profile，d_H=t(t+1)/2，
d_low=1/4−t/2+t²/2正确。精确积分：

∫d_H²=19/480，∫d_H d_low=23/960。

e1=19/240来自462的原 actual low fourth，不等于
仅把低 diagonal平方积分所得的7/240。正文正确区分这些对象。
从而B1(0)=21/80准确。

条件q_T bounded先给whole-prime fourth bounded；随后455的
proper powers归一化S4小量可由triangle/reverse triangle恢复完整Λ。
454在flat的V=Z=J=0及其Cauchy才使背景cubic趋零。
因此(16)没有在未知增长的C³上免费乘O(1/log X)背景误差。
452所要求的同物理响应、零侧padding与d/N→1均仍保留。

本次用Fraction重算(18)–(20)：

Qe1<(17/2400)²，
C1+17/2400=149/4800，
16Q(149/4800)<(9/500)²，
B=2589/8000<1/3，
(1−1/3)²/(1−2/3+B)=32000/47301>27/40。

LP参数(v−B)/(1−v)严格在(0,3/4)，分母正。
197/228的one-sided预算方向正确，无单独三阶矩极限前件；
但整个有限边界/重数/主块转移前件不能只凭这个数值删除。
正文用明确条件语句保留它们。Q=0给320/429也正确。

## 5. 可选更严格有理上界及限定结论

同一Q=1/1600，还可取
√(Qe1)<113/16000，
C1+113/16000=1489/48000，
√(Q·1489/48000)<71/16000，
得到B1(Q)<1293/4000<2589/8000。
作者保守采用2589/8000完全合法，无需修改冻结正文。

限定 PASS。新结果是actual high4、entire31与entire22对同一个
实际平方残差的联合条件预算；不是实际q_T≤1/1600的证明。
其算术缺口仍包含所有signed ratio columns、内部P与共同profile。
本文不把high repeated limit替成whole a_T，不把flat常数混入MT，
不确认新的67.5%比例，也不改变原明列[R]的无零范围。

最终修订的阻断也独立核实：466给actual commutator极限41/10080，
有限PSD不等式最初给liminfq_T≥33479/15482880>1/1600，
466最终§5更强的sharp线性式给liminfq_T≥41/15120>1/400。
因此旧Q充分前件不可达到，不能继续列为实际付款目标。
在这个下界处465的monotone scalar upper已经大于1/3，
所以仅给q一个upper再套该粗预算不能提高flat二矩比例。
这一限制仅针对本envelope，不能推出实际whole fourth或原路线不可改善。
详见[联合独审](465-466-centered-variance-joint-review-twisted.md)，
其最终466绑定为0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe。
