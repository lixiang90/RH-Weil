# 固定q0实际实施：原语、投影能量与解析向量输入

2026-10-27；G20261027同运行实例createdAt1793085111，原0c4f冻结基线。按前次[实施交接](../../reviews/2026-10-27/tf-reader/execution-handoff.md)实际执行，未换h0／F8／L。当前结论是：F原语和投影能量已认证，并提取了带真Hilbert误差的显式向量；**q0宽≤1/16未通过，全G非零trial／J／残差及五源T/E仍未执行**。下文是root对实际版本的限定消费；独立审读与版本在[消费收据](../../reviews/2026-10-27/tf-reader-execution/root-consumption-scope.json)。

## 1. 同一对象与有向运输

H=L²(R+,dx)，F为核2cos(2πxy)的自伴酉，L=1_(0,1)、Hcut=I−L，P为cutoff1 Sonin正交投影，M=RanP。这里的cutoff L不等于五源半窗3/2。F8={2,3,5,7,11,13,17,19}，NF=9699690，B=∏(I−p^−1/2 U_logp)，U_t f(x)=e^−t/2 f(e^−t x)。W=B*B，G=PWP|M，d=m²≤G≤u=M+²。

FM=M、FBF=B*及dilation交换给FWF=W，所以P、G逆与F交换。原q0=<h0,FΠFFh0>，h0=1_[1,2]、norm1，准确地等于

\[
 F\Pi_FF=B^*PG^{-1}PB,\qquad q_0=\langle v,G^{-1}v\rangle,\quad v=PBh_0.
\]

旧forcing PB*Fh0与此v由F酉运输，J和整个H上的残差随trial同作F运输保持。不是用有限matrix／替代源来绕开physical尾。

实际finite输入f=Bh0=Σ_(d|NF)μ(d)/d·1_[d,2d]，256项、384 breakpoints、382非零partition cells。endpoint sweep和全pair overlap独立exact核出||f||²=19189712/4849845<4。Pf不是f，后者norm不能代前者。

## 2. 实际运行与独立重放

| 实际输出 | 认证范围 | 未支付的下一责任 |
|---|---|---|
| [Fh0原语](../../reviews/2026-10-27/tf-reader-execution/step-engine-record.md) | 97653 cells、27 dyadic bands，真全H误差<0.021576245<1/32 | 尚未接入G／q0；更严误差的cell数仅为本算法充分计划 |
| [充分成本](../../reviews/2026-10-27/tf-reader-execution/variational-strategy-and-cost.md) | 同f exact norm；Neumann首个充分degree4429773，Chebyshev4451 | 未实际执行这些G迭代；不是必要成本下界 |
| [低区间证书](../../reviews/2026-10-27/tf-reader-execution/lowband-step-certificate.json) | 68037个非零频率，N26、53维Legendre rational trial，整个L²(0,1)残差及R0−RN全operator误差 | 低resolvent残差不是full-G残差 |
| [显式向量输入](../../reviews/2026-10-27/tf-reader-execution/lowband-vector-input.json) | g的384项、p*的27个有理单项系数，v*保完整Fourier尾，||v−v*||<1.061·10^−16 | 没有实际Gv或其pair／norm数值 |

原语的near0／infinite-tail／mesh／coefficient误差全部在physical L²中付款；mesh和coefficient同域采用Young而非平方直接相加。脚本/证书内保存确定性系数流hash，不能把hash当数学证明。三组scalar/原语/成本已独立重放数学字段；时间只是本机运行记录。vector从现存证书提取，不重跑scalar或G。

低区间计算使用g=LFf、C0=LFL、R0=(I−C0²)^−1。integer endpoint和Στ=0消去给真实Fourier tail的Si表达。T(n)=2πn(π/2−Si(2πn))，T(0)=0与连续延拓相容。大频率余项由Laplace积分的有限几何恒等式严格付款，不把渐近级数当收敛级数；小频率用有理π、Si Taylor及argument误差。

C_N为N26全cosine Taylor，shifted Legendre Gram=diag(1/(2l+1))，mpmath仅选择明确有理trial，260位向外integer intervals验收真低H残差平方约5.660·10^−205。全R0−RN norm误差约5.476·10^−17；quadratic运输费约2.167·10^−16已包含forcing替换，因为C_j R_j C_j=R_j−I。不能再把有限逆算术列作未付，也不能把它误当full G已付。

## 3. 已认证数值与未通过的原门

正式边界由JSON有理数定义。以下短端点向外略化：

\[
 \|v\|^2\in[0.15053580249546810,\ 0.15053580249546854].
\]

这个结果进入同一q0的d/u粗谱界后，仅得q0约在[0.0008094495577533444,1]；宽约0.99919，未达1/16。零trial也不通过。未生成非零full-G trial、J区间、whole-H residual验收或T/E／cross表，Hfin没有符号可报告。失败的是本次实际验收，未证明任意实现或该数学路线不可能。

## 4. 从scalar实际提取向量

令x=C_Ng，旧exact rational trial t，e=x−(I−C_N²)t。RN g=g+C_N RN C_Ng，所以

\[
 \|R_0g-(g+C_Nt)\|
 \le\eta_R\|g\|+\kappa_N M_N\|e\|.
\]

script重构C_Nt的27个even-monomial区间，再选择确切有理midpoint p*；全(0,1)误差δpoly≤系数半宽之和。旧t各区间本次实际全singleton，残差包围覆盖所选代表。取ell*=1_(0,1)(g+p*)及

\[
 v_*=f-Hcut F\ell_*,\qquad
 \delta_v=\eta_R\sqrt{\|g\|^2_{hi}}+M_N\sqrt{\|e\|^2_{hi}}+\delta_{poly}
 <1.061\cdot10^{-16}.
\]

κN≤1作保守界，MN<10^6由原gap及δN实际核；F/Hcut均contractive，故该界是整个physical H中的||v−v*||，不是系数norm。v*以exact compact analytic函数的F像定义，保无限尾；它是可操作input，仍不能凭定义声称未来的action求值／quadrature／成本已实现。

## 5. 强旧比较、停止与唯一下一准入

535／560固定窗trace／Gram及上轮reader一般公式已知；本次是其标准建设性实现和固定数值组件，没有新的classic全源／成长signed估计、独立primitive／mixedRR、whole惯性净后果。542+555→557 whole leading4/5仍仅负惯性UPPER。全部Γ/contact、properpowers、双pole和allcomplex／原du-Dlog责任保原五源目标，不能因本h0组件未读它们而删除。当前核心瓶颈未变。

不继续无压缩word展开、重复scalar或改F/L/h0。actual q0预检本次止于上述未通过状态；其充分成本不是方法边界。建设性执行0数学轮，不建C047/584；唯一cadence1／历史47／cycle16保持，不能因代码、运行和审计数计轮，也未藏一项新的全量词定理。

新vector确实比scalar多一个输入。因此只准[一次固定c2配对测试](../../reviews/2026-10-27/tf-reader-execution/next-fixed-pair-test.md)，验证此analytic表示能否实际读一个bounded mixed项及其有限区间误差，目标宽≤1/1024。该门改变的是表示的可执行性判断；不代whole G或q0验收。若求值误差／成本仍无信息，保存缺项后停止这个表示的自动扩展；不自动续素数／Krylov阶数／paper。通过也须重新比较whole-G所欠a/b与主Goal，不能自动晋级数学合同。它优于继续已知scalar或未知几何paper的原因是：当前已经有exact vector及误差，可用一个固定测试真实否决／支持组织选择；独立算术源或成长core新身份出现则优先改策。

Goal同实例active，完成门open；本执行结算不complete或blocked。研究看板、实际DLMF阅读范围、本地文献缓存及GitHub同步另按STATE和远端回执核实。
