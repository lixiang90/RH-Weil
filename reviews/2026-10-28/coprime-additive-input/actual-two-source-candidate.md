# 互素加法双源规则的一次实际构造

2026-10-28；root，G20261027/runtime1793085111/原0c4f。执行formal17后的唯一输入形成动作，尚未准数学合同/计轮。本稿一次冻结以下规则，不在检查后改权、cutoff或补偿；原域/系数经两个独占支持、修后fresh及root核闭，按强旧前置0停止；下述待核问号保留初始生成记录，当前消费见末。不是未知正H、几何primitive或已证明的Weil身份。

## 实际数据与唯一公式

固定有序有限整数数据
\[
 \mathcal T_B=\{a+b=c\le B:\ a,b>0,\ (a,b)=1\}.
\]
两个独立physical源r=e^(u/2)f、s=e^(u/2)g取complex Cc∞或S_exp，du内积第一变量线性。平移为T_a r(u)=r(u-a)。对0<x<1定义
\[
 U_x=T_{\log x}-I,\quad V_x=T_{\log(1-x)}-I,
\]
\[
 J_x(r,s)=\tfrac12[
       \langle U_xr,V_xs\rangle+
       \langle V_xr,U_xs\rangle].
                                                        \tag{1}
\]
此mixed读出Hermitian、对共同physical平移不变；没有假定它正型。

每个三元组一次采用其全部素因子赋值的对数组合
\[
 \gamma(a,b,c)=\sum_p[v_p(a)+v_p(b)-v_p(c)]\log p
              =\log(ab/c).
                                                        \tag{2}
\]
这是一个明确的log-linear收缩，不声称保留完整valuation向量的所有信息。其连续对应为
\[
 G_c(x;r,s)=[\log c+\log x+\log(1-x)]J_x(r,s).
\]
按同一分母进行经验项减均匀项，固定唯一规则
\[
 \boxed{C_B(r,s)=\sum_{2\le c\le B}\frac1{c^2}
 \left[\sum_{\substack{1\le a<c\\(a,c)=1}}
      G_c(a/c;r,s)-\varphi(c)\int_0^1G_c(x;r,s)\,dx
 \right].}                                             \tag{3}
\]
φ(c)是实际primitive分母层的点数；不是拟合目标的权。中心化与c^−2在此首次定义时同时冻结，不先试未中心化版本再改。均匀项是该分母经验分布的Lebesgue对照，**不是**经典WΓ、FP/contact或双pole，不能凭名称视为已接入Γ。

数据同时使用加法、coprimality与三腿赋值，但(2)可能立即丢失想要的joint信息；这正是首门。不把它包装成新的RR、positiveD′生成或几何边证书。

## 原域与先行费用

有限B下，平移在原L²(du)酉，故
\[
 |J_x(r,s)|\le4\|r\|_2\|s\|_2.
\]
对x=a/c的原整数点，有|γ|≤log c；连续对照的绝对积分≤log c+2。因此
\[
 |C_B(r,s)|
 \le8\sum_{2\le c\le B}\frac{\varphi(c)(1+\log c)}{c^2}
                  \|r\|_2\|s\|_2.
                                                        \tag{4}
\]
这是每fixed B、全complex L²源的scalar mixed费用，粗至多O((1+logB)²)；两源用原zero-extension Dlog时再付1/log2。没有给B∞的globaldu统一界。输入S_exp由其L²嵌入合法；此处没有证明原算子输出仍在S_exp，也不把算子值/primitive类与scalar form混同。

若要讨论cofinal B或完整分布，需另付源成长与端点导数/误差；当前不凭有限B上界交换极限。B是整数高度，与physical源窗L、频高T分开。

## 最便宜待核首门

先展开(1)的四个平移差，核contact、±log x、±log(1−x)及±log(x/(1−x))的方向。有限B的非integer ratio项与完整经典Weil目标的±log n原子不同；它们只能检验有限层精确身份，**不能**仅凭某层spurious atom就判D′极限失败，连续对照/无界TV及cofinal取消需独立证据。

其次做原始整除fiber精确合并。记
\[
 E_c(F)=\sum_{(a,c)=1,\ 0<a<c}F(a/c)-\varphi(c)\int_0^1F,
\quad
 R_q(F)=\sum_{1\le k<q}F(k/q)-q\int_0^1F.
\]
预期最便宜账本是
\[
 E_c(F)\stackrel{?}{=}\sum_{d\mid c}\mu(d)R_{c/d}(F).
                                                        \tag{5}
\]
若成立，(3)须在同一product cutoff dq≤B下展开；G_dq含log d+log q，不得漏log derivative或q=1边界。只有在实际原域付绝对收敛后，才可讨论prime资料是否只剩ζ(2)与ζ′(2)两个常数和旧普通grid读出。问号表示本稿尚待独立核查/强旧消费，不是新lemma或准入。

同时定向对照旧036/080–096的divisibility/Farey/Riemann-grid，以及549–550和578的完整fiber/ratio-square责任。若只是这些已有数据的固定mixed后处理或log-linear赋值压缩、没有新独立净方向，按构造前置0止本规则；不继续寻找Γ修补、改指数/权或同数据的另一版本。

## 尚未支付的目标与消费状态

比较目标始终是完整Bζ(r,s)，保原Γ/FP-contact、Λ(p^k)=logp的全部proper powers、两个pole、全complex、原du/Dlog/strong及fixed/cofinal量词。它们没有因(3)而自动出现。本稿不将所需差/净号/q_R消失写成独立输入，也不声称每层必须exact消405；如果后来作精确几何下降解释，仍须全noncompact405及平移、537和coverage。

当前只是一次actual公式形成及待核系数/域门，不是C050/587或新数学结果。独立支持的输出不代root消费；global关键瓶颈、whole4/5负惯性UPPER和Goal完成门未变。原formal17 cadence0/历史50/latest586保持，不再宏观复盘或归零。

最终消费见[根结算](../../../goals/reviews/2026-10-28-coprime-additive-source-gate-stop.md)及[root前件范围](root-consumption-scope.json)。式(5)由两终稿严格闭合，cofinal另保q=1及剔除c=1的+∫ℓJ；不消费极限是否非零。完整reader由global H¹/共同crop与旧553/405/537排除，signed correction另有无界腿的角色仍需独立实物，不自动接背景。当前无C050/587/新数学轮，0/历史50不变。fresh绑定的是4988bytes/d9ad…生成版本，最终只更新状态/链接，实际规则不改。
