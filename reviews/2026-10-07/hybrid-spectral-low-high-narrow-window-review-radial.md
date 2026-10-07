# 已付低高谱信息与窄窗策略的独立全文审查

2026-10-07。radial_review。结论：限定 PASS。
全文复核七原子、一般矩松弛、新增MT模型、原高parity、窄窗准入、
S4近似及纯bad模型；
并补核说明性窄平窗极限所用的三阶小量。
只新增本审查，不修改作者报告、已冻结旧稿、math或Git。

## 1. 最终对象与范围

[被审全文](hybrid-spectral-low-high-information-and-narrow-window-research-compression.md)
canonical LF SHA-256：
46aa87f3ab12e7399dd33bc4c6833fbe7362b31781c1ec018d538fd2ffe21f4f；
19084 UTF-8 bytes，426行。CRLF/lone CR统一为LF，不trim。

本次另读取197、454、455、461–463和作者引用的pending parity全文；
原对象与输入hash核对如下：

| 输入 | canonical LF SHA-256 |
| --- | --- |
| 197 | 98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7 |
| 454 | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| 455 | 6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41 |
| 461 | f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b |
| 462 | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| 463 | 6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90 |
| pending high-parity | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |

直接核查[AF v2 §2、Lemma2.1及§4](https://arxiv.org/html/2608.13637v2)
的原窗、feature、Poisson及pairing准入。外部[R]与原分析内核没有重证。
被审报告的第8节旧pending progression/nearcore只读复核也与本次实读相符；
受限正子和不是完整signed范数下界。

## 2. 七原子与一般标量松弛

七原子质量四个\(1/12\)、一个\(19/39\)、两个\(7/78\)和为1；
取\(d\)为156倍数可用diagonal矩阵准确实现。
条件对称展开给
\[
 \mathbb EC^2=1/3,\quad
 \mathbb EL_0^2=\mathbb EH_0^2=1/6,\quad
 \mathbb EH_0L_0=0,
\]
及作者(2)全部四阶数值：
low4、high4均为\(19/240\)，两个entire13/31为0，
\(H_0^2L_0^2\)为\(7/240\)，\(C^4\)为\(1/3\)。
三个\(G=1+C\)谱质量为\(1/6,2/3,1/6\)，位于\(0,1,2\)；
所构造\(P_s,Q_b\)使rank、trace及count预算取等。

整体sign反射配对原子，给一个involution反对易于\(H_0\)；
其bipartite分解确有\(A_0^2=0\)。
这只复现所列抽象parity数据，没有复现实际正素数平移、载波或feature几何。

一般模型置\(x=C/2\)。恒等式
\((x-Z)(x+Z)^3=x^4+2x^3Z-2xZ^3-Z^4\)
与条件对称性直接给entire13为0。
作者的\(w,k_w\)支付全局\(EZ^2=v/4\)、\(EZ^4=v/16\)；
可行差
\[
 k_w-w^2=
 \frac{v(1-4u)(4u-2v+1)}{16(1-v)^2}
\]
在\(0<v\le1/2,\ 0\le u\le1/4\)非负。
因此所列low2、low4及\(EC^4=v\)全部成立；退化端点按零分布解释。
它没有固定非平窗完整Gamma背景及其所有joint混合量。
报告明确排除将flat常数与MT二矩跨profile合并，范围正确。

### 2.1 新增MT背景marginal模型与有理可行性

这是实质数学新增，已经另外全文审查，未按排版更新直接换绑。
对每个\(\alpha\)，三类block的conditional normalized
\(\operatorname{Tr}C\)为\(\alpha\)，
\(\operatorname{Tr}C^2=v\)。积分\(\mathbb E\alpha=0\)给
整个\(G=I+C\)的0/1/2等号谱。
所有概率非负，因为MT的\(|\alpha|<1/5<v\)；
\(A_{\rm bg}=\alpha I\)保留整个scalar marginal并与\(U\)交换，
而\(H_0\)准确反对易于\(U\)。

记\(B=v-K_1\)、\(B_2=vV-K_3\)。直接block展开给
\[
 \mathbb EH_0^2=B(m^2+u)+(1-v)w=V_H,\qquad
 \mathbb EH_0(C-A_{\rm bg})=Bm=V_H .
\]
因此两prime二矩及cross-zero准确。作者\(k\)正是令
\[
 B\mathbb E[h(1-h)^3]+3B_2\mathbb E[h(1-h)]
       -3(1-v)Vw-(1-v)k=0
\]
的解，支付entire13。
把该式代回low4，剩余精确为\(c_0+c_1u\)，作者(3b)无漏项。
尤其type1、type2的\(|\alpha|^5\)项相消，最终Gamma fourth系数
确为\(-3M_4\)。所有conditional prime first moments为0，
更强的bounded \(f(A_{\rm bg})\)线性混合零式也成立。

本次独立以内存Sympy有理多项式积分重算完整462三类路径，
得到作者的两个raw numerator：
\[
 3989807597/66421555200,\qquad
 418537850292443239/6920254601035776000 .
\]
这些同时包含adjacent同号、adjacent异号与rectangle；
并非只用其中一条paired积分代替whole low4。
用相应\(a\)的上下界给整个未知actual \(\mathcal C_L(\psi)\)区间，
所以不是仅用一个上界当作实际low4等式。

独立重算\(P_5,P_6\)给
\(a\in[0.9187253698630652,0.9187253698655744]\)；
同样Taylor夹界给
\(v\in[0.32749929628517,0.32749929632295]\)及
\(V_H\in[0.14991689764922,0.14991689840350]\)，
均落在作者的粗有理表内。唯一root的.287/.288有理符号正确。
\(|\alpha'|\le1\)及Taylor uniform error小于\(10^{-9}\)
支付\(K_1,K_3\)的分段积分修补。
偶次代理积分分别约为.006127190866585及.0000787875112793；
奇绝对值代理为.067530533905505及.000654884177649，
误差均被所列有理区间覆盖。

从作者整个粗区间以Fraction独立计算，得到
\[
 .04323933<u<.04741705,\qquad .07602133<w<.07767352 .
\]
为避免对同一\(m\)的区间重复使用产生无谓损失，可用准确因式
\[
 \mathbb E[h(1-h)^3]
 =m(1-m)^3+3u(1-m)(2m-1)-u^2 .
\]
它直接给
\(.01904972<k<.01957905\)及\(k-w^2>.01301654\)；
因此作者较宽的(3d)严格成立，三原子noise概率合法。
以上显示小数仅描述结果，判定使用有理端点。

新增[证书脚本](../../scripts/hybrid_spectral_mt_joint_exact_certificate.py)
及[已生成JSON](../../output/hybrid-spectral-mt-joint-exact-certificate.json)
的方法也已只读核查。canonical LF bindings为：

| 对象 | SHA-256 | UTF-8 bytes / 行 |
| --- | --- | --- |
| script | 3eb01540243c90f500e5dde853f81775a1c5337c4d9eab2255b66e56147aa943 | 6642 / 179 |
| JSON | e2cb2f65e0067a503035623883b3646e64a5556480b1beb16c08504f22995f41 | 5866 / 131 |

脚本的positive-path Taylor积分及Fraction区间操作与独立计算一致；
float只用于显示。最终脚本的两个raw numerator都实际从
\(P_1,P_2\)三类路径重算，并以已列有理常数作结果断言；
本审查已另外独立计算这两项。
JSON绑定最终46aa87f3报告并记录finite assertions通过；
本次没有执行作者脚本或覆盖输出。
有限证书不认证实际prime Gram、feature realization或外部分析[R]。

此模型仍不匹配454全部joint quadratics：
它的Gamma与prime commute，而原\(J_\psi>0\)。
报告对此作了明确排除，因此新增MT数据不被误称完整算术等号实现。

## 3. 实际高parity与有限误差

原每个high步长\(>L/2\)，故physical
\(A_H=\Pi_-A_H\Pi_+\)，而不是宣称有限\(E^*A_HE\)幂零。
原\(J=M_{\operatorname{sgn}u}\)与\(B_H\)反对易。
Fourier系数\(2/(\pi|n|)\)只在odd非零\(n\)出现；
outside-pair计数\(\min(d,|n|)\)给
\(\|QJE\|_{\rm HS}^2=O(\log d)\)。

保留原\(P\)的(7)余项准确。对\(U=\operatorname{sgn}(E^*JE)\)，
\(\|U-S\|_{\rm HS}^2\le\operatorname{Tr}(I-S^2)\)；
结合原\(y_H\ll\sqrt X/L\)得到(8)及normalized \(O(L^{-2})\)。
Hoffman–Wielandt只支付quadratic谱对称。
升级S4仍给增长的\(O(X/L^4)\)，完全对称稀疏大谱值也不受排除。
所以不能从parity推whole high4有界或三高一低自动小。

## 4. 窄窗准入与完整第四矩

作者明列的是新的固定非负偶窗、\(a>0\)及
\(\sqrt\psi\)的C2零延拓。AF原定理写严格正窗；
本报告没有直接引用它到新窗，而是重核所用准入。
支持在长度不超过\(L\)的区间使Poisson dual lattice非零项消失，
给原归一化全格点平方和\(a_LL^2\)。
线上features非负且有限范数不超过1；非实conjugate pair的
real Hermitian form至多一个正方向。所有rank/inertia预算因此保留。
新的导数及Paley–Wiener界更强，固定窗、height及padding量词顺序正确。

当\(\log n\ge bL\)，physical
\(M_\phi R_{\log n}M_\phi=0\)，含零测端点。
故\(b\le1/2\)时prime全部属于已付low范围。
462完整证明的crossing、near Hilbert、far/alias、唯一零词枚举
只需要固定C2界、非负窗及\(a>0\)，不需要端点严格正。
因此whole prime S4预算可扩展到本窗；这不是只保留paired路径的推断。
455的proper-power S4-small及454全height背景也使用同样窗口前件。
作者(9)的\(\operatorname{Tr}G^4=O(d)\)由三项S4三角不等式合法得到。

## 5. Moment稳定的低秩近似与纯bad账本

原finite carrier中
\(\operatorname{Tr}R_b=bd\)及作者(10)的Fourier和准确；
defect为\(O(\log d)\)。
对谱阈值1/2的两个逐特征值不等式得到
rank \(\Pi_b=bd+O(\log d)\)和
\(\|M_\phi EQ_b\|_{\rm HS}^2=O(\log d)\)。

因\(y_b\ll X^{b/2}/L\)，
\[
 \|C_\Lambda Q_b\|_{S_4}^4
 \ll y_b^4\log d\ll X^{2b}/L^3=o(d)
\]
在\(b\le1/2\)成立。背景packet的S4四次方为\(O(\log d)\)，
余项normalized S4为\(O(1/L)\)。
自伴性给(13)；whole fourth有界已在上一节先付，
故telescoping/Hölder保留四个原始矩。

\(b=1/2\)时额外删去\(O(\log d)\)个压缩eigenvectors的
S4四次方费用不超过\(O(\log d)(1+y_b)^4=O(X/L^3)=o(d)\)。
于是可取rank不超过\(\lfloor d/2\rfloor\)的moment稳定矩阵。
实际\(G\)仍可能full rank，这一点在作者报告中没有混淆。

令simple部分为0，整个近似矩阵归为bad，正惯性不超过其rank；
两项预算只要求\(2b_{\rm bad}\le N+o(N)\)，确实成立。
其trace和前四矩仍与原\(G\)相同至\(o(N)\)。
这严格证明仅依赖这些渐近数据的证书不能排除simple fraction为0。
它不是实际零点features、RH反例或所有AF几何策略的不可能性结论。

## 6. 窄平窗说明性极限的补核

作者先固定admissible smooth profile、令\(T\to\infty\)，
再趋于indicator。这个次序允许各固定profile的导数常数变化；
没有把硬indicator冒充有限T的C2窗口。
两个路径积分随尺度为\(b^5/20,b^5/120\)，
所以完整prime第四矩为\((4D+8O)/b^4=4b/15\)。
AF二矩或454加权二矩给prime二矩\(b/3\)。

三阶小量可在原对象直接补证。对prime-only窄窗，
physical三词的\(|S|<bL\le L/2\)，没有端点alias。
远区有限kernel为\(O(1/X)\)，总正质量不超过\(y_b^3\)，
故normalized费用\(O(X^{3b/2-1}/L^3)=o(1)\)。
近区two-plus/one-minus迫使\(pq\le2X^b\)；
prime与semiprime不可能相等。共同C2窗 Fourier分离后，
log-integer union的Hilbert费用为\(X^{b-1}\)乘固定polylog，仍趋零。
更具体地，用integer divisor-energy粗界，
两列weighted能量各为\(O(X^b\operatorname{polylog}X)\)；
局部间距费用的前因子\(L/d\asymp1/X\)支付该界。

块展开的actual/physical cube差至多
\(3y_b\ell_b^2\)，其中
\(\ell_b\ll X^{b/2}\sqrt{\log(2+L)}/L\)，除以\(d\)趋零。
插入固定C2 bounded背景weight时，额外crossing至多
常数倍\(y_b\ell_b^2+y_b^2\ell_b\ell_h\)，
\(\ell_h=O(\sqrt{\log d})\)已足够，亦为\(o(d)\)。
455和窄prime S4有界保证proper-power cube差为\(o(d)\)。
因此prime三矩及所需even背景weighted cubic确实趋零；
没有使用未知的full high4前件。

在indicator极限背景bulk为\(1/b\)，这些结果给作者(14)：
\[
 (m_1,m_2,m_3,m_4)=
 (1,\ 1/b+b/3,\ 1/b^2+1,\ 1/b^3+2/b+4b/15).
\]
所列质量\(1-b\)在0、质量\(b\)在
\(1/b+\{0,\pm2/\sqrt5\}\)的概率模型直接重现全部四矩。
它属于谱数据说明，不是实际feature实现。

## 7. 验收范围与下一待付项

限定PASS覆盖全部有限模型、真实二范数parity、窄窗full-fourth付款、
moment稳定低秩近似及纯bad账本障碍。
原MT完整joint背景仍未由标量模型实现；\(b>1/2\)的high算术仍开放。
仅凭实际parity与有界二矩不能支付weighted high cubic：
HS配对至少仍出现whole high4或现有op正幂费用。
任何新的严格比例收益都须另付实际signed arithmetic或feature可见性。
本审查不认证新比例、无零边界、RH/RR或底层[R]全链。
