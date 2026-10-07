# whole low parity第四矩的独立全文审查

2026-10-08。审查者 compression_bridge；来源作者 root。
已逐行完整读取研究源293行和最终exact脚本173行。只新增本审查，
没有修改任何研究源、旧文、math、Goal或Git。

| 完整来源 | canonical UTF-8 LF SHA-256 | bytes / lines |
|---|---|---|
| [whole低素数parity研究](hybrid-whole-low-parity-fourth-research-root.md) | 02328b4cfaf902fc0f0d60e37f27989808aaae6bb88e6410c8d120a44487969d | 12980 / 293 |
| [exact全路径脚本](../../scripts/hybrid_whole_low_parity_exact.py) | d990e1a678b86e0f0c4d60cc80285bfa0d4ac5b37085d9e4db6bd90df68f1932 | 6318 / 173 |

canonical为CRLF和lone CR转LF，不trim。结论：**限定 PASS**。
原p≤sqrtX entire low对象、全部内部P、smooth-to-sharp恢复、whole非零原子、
16个e/o四词、varying diagonals与列出的常数均通过。无需high4 bounded；
未发现第6节T-dependent diagonal准入漏洞。
不将脚本运行结果当作非零prime渐近、[R]证明或wholehigh预算。

## 1. 原P与smooth标记的完整费用

每个smooth四词具有恰四个原B_L、固定有限个J_ε。标记乘法并不与P交换。
退出/返回P的closed-word展开提供两次HS crossing：BB、BJ、JJ三类分别
给y²l_L²、y³l_Ll_J、y⁴l_J²。y=O(X^(1/4)/ell)，l_L=O(y sqrtlogell)，
l_J=O_ε(sqrtlogd)，故归一化最大JJ费O_ε(ell^-4)，其余更小。
保留较松logd泄漏容许circle endpoint jump，不能偷用mark periodic性。

物理e/o每步的smooth系数是(1±j(t_j)j(t_(j+1)))/2，均在[0,1]。
与φ或φ²合并后仍是compact C²窗。原near联合Fourier/Hilbert保留准确
n=m剔除、2+2的双方≤X、3+1的product≤2sqrtX；新增有限个Fourier变量
只增加logell固定幂。原far与±ell alias的positive overlap付款不被放大。
因此完整nonzero四词是o(d)，并非把配对主项直接当成entire结论。

## 2. sharp U必须在L的S4中恢复

D2=S−S_ε的compression Schwarz给D2²≤G_ε。Tr(ABAB)≤Tr(A²B²)
对PSD A=D2²、B=L²成立；于是||D2L||4,d⁴≤4τ(G_εL⁴)。
weighted low4已由上一节同样准入，zero起点只落在宽Oε的strip，
故τ(G_εL⁴)=Oε+o_ε1，且有限迹为正。

D1=U−S为S的谱函数，op≤1、HS²=Ologd。原low raw op给
||D1L||4,d⁴≤y⁴||D1||HS²/d=Oell^-4；左乘L为adjoint同界。
准确ULU−S_εLS_ε展开，所有contractions有op≤1，所以L_e、L_o在S4
均传到smooth对象。原整个low4先保证各S4 norm有界，fourfold Hölder
随后保证所有四词迹的传递合法。先fixed ε，再T，最后ε，不使用high4。

## 3. 全零路径及脚本的数学方法

三配对A、A′、O的ordered p,q与four orientations完整保留；同prime的
交集六个sign words只作一次原Oell^-4 correction。没有将p=q当作连续
prime measure的额外原子。初始半区两种取值与每个节点的half状态完整计数。
奇数o的finite迹由U-conjugation准确为零；脚本的early-return同该约束一致。

allowed row长度是max-lower/min-upper的positive part。脚本对所有候选
max lower、min upper作有理half-plane裁剪；unique affine forms去重，
不同cells仅在tie边界重叠，故不重复positive面积。每个凸多边形的fan
三角化保持覆盖；Jacobian乘i!j!/(i+j+2)!准确积分xy times affine length，
包括simplex面积1/2，没有漏乘面积因子。

脚本173行包括weighted-polynomial部分亦FULL READ。独立重运行全部16词，
并另用Fraction多项式积分核对所有row constants。所有输出与source表相符。
all-e手算两半区2(4h⁵/20+8h⁵/120)=1/60；all-o两配对各两方向，
O不可交替越半轴，4∫xymin(x,y)=1/60。mixed eeoo/eooe四种为3/320，
eoeo两种为1/240，全部词之和19/240。不会把这份exact计算替代第1–2节。

## 4. varying V_e,X、V_o,X的准入核对

对u>0，hard odd diagonal准确是
v_o,X(u)=φ(u)²Σ_(e^u<p≤sqrtX)b_p²φ(u−logp)²；u<0反射。
even diagonal另有p≤e^u的负步与p≤e^(ell/2−u)的正步，均保留原φ²。
threshold jumps因此真实存在，但总variation不超过CΣb_p²=O1：
每个prime项的fixed taper variation与indicator jump均有一致界。
不能将这些函数直接称为uniform C²。

Mertens weighted前缀除以ell²在整个fixed compact中一致逼近积分；
translated taper差仅涉及logp宽O1的shell，统一质量O(1/ell)。
outer endpoint strips以固定δ先隔离。v_e极限在0有cusp，但连续，
仍可由fixed bounded C²函数在compact上任意一致逼近；这里不要求其自身C²。

具体可把任一diagonal与其fixed smooth近似g的差作乘法order sandwich：
|v_j,X−g|≤ε_T+ε_g+Cg_strip，E compression保持此order。
对A=H²、L_e²、L_o²等PSD tested second，
|τ A E*(v_j,X−g)E|≤(ε_T+ε_g)τA+Cτ(A G_strip)。
τA已付O1，最后一项由fixed smooth weighted-second为Oδ+o_δ1。
W、V的测试亦同。先T、再smooth精度与δ，足以支付全部varying weights。

尤其τ(H²−W)V_o→0使用H²和W两项各自的PSD sandwich，
不需要未知||Γ||HS bounded，更不会把T-dependent weights免费纳入454。
V_o的U-odd norm由uniform BV circle coefficientsO(1/|n|)、真实P
outside计数min(d,|n|)和U−S给O(sqrtlogd)/sqrt d→0。
这一比较同样不使用high第四矩。

## 5. 常数与结论范围

独立积分v_e=1/8−t/2+t²、v_o=1/8−t²/2、w=t(t+1)/2给
Se=7/960、So=1/120、Seo=13/1920、Ce=9/640、Co=19/1920；
两second均1/12。whole fourth1/60减各same-diagonal second得
even residual3/320、odd residual1/120。mixed square covariance
3/320−13/1920=1/384，合成Δ-even11/480与Δ-odd13/480。
所有constants与原wholelow4、原Δparity独立计算一致。

此审查通过的是entire原low的实际必要常数；没有给整个high残差q上界，
没有证明whole31/22净upper或新的实际比例，也不独立认证外部分析[R]。
