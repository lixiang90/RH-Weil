# 原完整前缀投影与四个上端素数的真实剩余

2026-10-08，第二周期复盘后的第1轮；基线 main
b763892e95a17bbb19f940b1dc4d37b0c2d9536d。保持原数域、真实素数、
原观察对象及同时研究比例和无零区域的完整目标。

本轮在普通ζ的[R_7/8]前件下完成两个实际接口：
完整最大素数前缀的次弧投影，以及至少一个较小高素数的完整混合族。
先按真实四标签分区，再对剩余范围直接重推正包络，得到
\[
 \boxed{\mathcal U_T=\mathfrak K_{489,\mathrm{all}>X^{9/10}}
              +O_\phi(X^{7/10}\log^C X).}
\tag{1}
\]
这里仍是原signed χ-carrier平均的完整unit量；不是逐频率绝对界。
未付核心只含四个素数都大于X^{9/10}的原完整489次弧。
其实际signed省幂仍未证明；完整四阶增长、中心常数、比例和无零边界没有改善。

## 1. 证据与观察对象

本轮两项直接证明分别为
[前缀及固定素数区间投影](../reviews/2026-10-08/hybrid-original-prime-prefix-minor-projection-research-perron.md)、
[完整低标签混合族](../reviews/2026-10-08/hybrid-original-low-label-mixed-union-research-high-product.md)。
不同作者的最终核对见
[联合独审](../reviews/2026-10-08/hybrid-original-prefix-and-low-label-review-checkpoint.md)。

根作者已全文读回两份最终源及独审，独立核算费用与完整分区。
冻结身份按UTF-8 canonical LF，仅统一行尾、不trim：

| 最终输入 | 行数／字节 | SHA256 |
|---|---|---|
| 前缀及矩形投影 | 185／12805 | 2971ae080d520d4a2d1209cfd0b86aaf722302169ee3f516df423f6c1f3aad32 |
| 低标签混合族 | 160／10381 | 55d632dd6565b1c4ed3a1abfd8a7785b3e253c0ddd3e36c52d8cdde48941b0cf |
| 不同作者联合独审 | 91／7550 | eec860065eb2e4a499dcef6af7fd7bed8b4a8536dc89eae4faaf1700bc5683cf |

保持原X=T/(2π)、L、N_L、C²空间profile、same-u、正时间权ν、
时间floor、χ概率平均、真实最大素数q、s<q、p,r<q及p,r≠s等原准确支撑。
原全部高素数区间为(√X,X]；以下“低标签”仍在这个高素数区间内。
本文固定Z=X^{9/10}，不会将它误读为旧p≤√X低素数腿。
旧[489](489-original-high-product-rational-minor-slice.md)的两套频率mask为：
旧分母d≤W=X^{1/10}、半径W/(dS)，以及新增W<d≤B=X^{1/5}、半径1/S。
产品cap固定为K=X^{1193/700}；S仍是原dyadic尺度。

## 2. 完整前缀可以投影到原准确次弧

已冻结的完整q_max≤X^u前缀付款是
\[
 B(u)=3u/2-11/14,\qquad17/20\le u\le1.
\]
它本身没有给前缀内部任何子mask的界。本轮回到原正包络重推：
340源的major逐box费用为W²(Q+S)/√X；
337源的新有理子族费用为B(Q+S)/√X。
限制q≤X^u后，Q+S≪X^u，二者均为X^{u-3/10}log^C X。
内腿系数用固定素数区间与strict q-prefix的binary展开；
原每个整数产品最多两个有序素数factor pairs，正平方能量保持。
外s仍是有限个实际区间，所有common Mellin参数与ν的零支撑保持。
不是将旧signed全域界直接删成子集界。

原完整产品cap通过Poisson后的正整数产品计数、绝对alias尾重推，
固定内素数区间只减少该正计数；点修正直接用完整Parseval正能量。
因而完整实际主带精确减major、cap及新增有理子族，给以下三个不同对象：

| 完整q≤X^u对象 | 费用指数 |
|---|---|
| 未切产品cap的旧minor | max{B(u),u−3/10} |
| 489准确cap外双mask剩余 | max{B(u),493/700} |
| 491删低产品端period后的优化剩余 | max{B(u),993/1400} |

u=9/10时依次为3/5、493/700、993/1400。
最后一项必须另付旧端period；不能把非周期子窗套到489完整周期mask。
这些是完整前缀付款，不能恢复单q、任意tuple子mask或restricted G正能量。

## 3. 至少一个标签≤Z的完整混合族

在原有限实际矩阵上写C_H=C_<+C_>，其中C_<只含√X<p≤Z。
原完整四矩为X^{5/7+ε}，完整截断四矩为X^{79/140+ε}。
先用矩阵Schatten4与χ平均的Minkowski界控制C_>的完整四矩，
再对C_H⁴−C_>⁴中的15个非交换词逐个作Schatten Hölder。
一个词含k≥1个低标签时，其完整χ平均至多
\[
 X^{[k(79/140)+(4-k)5/7]/4+\epsilon}.
\]
最坏k=1，因此
\[
 E=379/560=5/7-3/80<7/10.
\tag{2}
\]
只控制这15词完整和；没有获得任意指定prime四元组集合的界。
实际完整重复族与全上端重复族分别直接由二矩及set-partition迹界付O(1)，
其精确差才恢复本轮mixed四全异量。

physical层在三个内部投影处展开，直接处理七条非全P路径：
闭合路径至少两次跨P/Q，利用原positive crossing能量与op界付款。
不把有限矩阵四词上界免费外推到无限physical trace。
原unit和实际主带的min-label指示，在固定q,s时有准确有限分解：
q≤Z或s≤Z则保留全内矩形；否则
1_{p≤Z或r≤Z}=1_{p≤Z}+1_{r≤Z}−1_{p,r≤Z}。
每个矩形直接重推nn、chirp、graph及alias正包络，费用≤X^{1/2}log^C X。
double-nn的H_n是辅助整数a=qs−h上的Fourier核；
p/r截断仅改变B_n，H_0及原A=qs>4X的EM阈值不变。
所以(2)确已运输到完整实际主带的低标签族。

## 4. 先分区再付款：无需继承旧完整cap费用

先在原完整实际主带逐tuple写L_T=L_small+L_large。
第一项由(2)付清；第二项是q,s>Z且p,r∈(Z,q)的实际矩形。
所有原profile、同一u、s排除和ν频带仍保留。
对L_large直接使用第2节的正包络；不能从旧全主带signed界截取。

每个实际tuple满足qs>Z²=X^{9/5}，所以其旧产品cap完全空。
dyadic QS≥qs/4使原低产品guard QS≤64WX也空，
与新增有理族guard QS>64BX之间均有固定省幂间隙。
原完整n的产品窗、q|n加回、graph、chirp及alias误差直接保持；
两套major/new-rational正包络在全q≤X域的费用仍为X^{7/10}log^C X。
精确减去这两个已付频率域，得到
\[
 L_{\mathrm{large}}=\mathfrak K_{489,\mathrm{all}>Z}
                         +O_\phi(X^{7/10}\log^C X).
\]
因为7/10−E=13/560>0，先固定ε<13/560可吸收mixed项。
再消费425源已经支付的**完整全域**unit↔实际主带桥O(X^{1/2}log^C X)，
即得(1)；没有把这条signed全域桥免费投影成子tuple桥。
这是重新分区后的界，故无需继承493/700的旧全域产品cap费用。

这里选用489完整频率接口。虽然all>Z范围内491的低产品edge cap为空，
高产品范围内其剩余端period仍须保留，不能声称所有端period为空。
本稿没有删去这些高产品端点，亦没有引入491的993/1400误差。

## 5. 全局意义与下一步

未付原完整核心已满足q,s,p,r>X^{9/10}，并有q/s<X^{1/10}；
保持原两套有理complement、全部ν-twists、same-u及完整端period。
误差7/10低于名义5/7，亦低于451全部前件下既有B_*，
但K核心尚未省幂，不能由误差的改善宣布全局四矩或边界改善。
普通[R_7/8]也不能代替451所需Hecke等全部输入。

下一步直接研究这个全上端核心的实际双prime偏差或移位carry signed统计。
保留全部pr−q(s+b)+ell q²，移位因子不自动是prime。
顶端需真实r>2/7的名义节省；严格改善既有B_*需r>0.285801997046972。
继续减少一般CDF、二阶插值与日志辅助优化，中心四阶常数另行检验。
本轮只有实际族归约与误差付款，没有新纪录论文或完整定理认证。
