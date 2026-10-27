# 固定c2的有限尾修正项：实际矩求值与认证

2026-10-27；`/root/c2_tail_term`独占稿。按当前[固定pair门](../tf-reader-execution/next-fixed-pair-test.md)只支付第五项

\[
 I=\int_0^2 a(x)\,2^{-1/2}a(x/2)\,dx,
 \qquad a=F\ell_*,\quad \ell_*=1_{(0,1)}(g+p_*).
\]

输入是既存`lowband-vector-input.json`中同一固定h0／F8的确切解析向量：384个integer-frequency g项、27个有理even-monomial p*系数。没有重跑旧68037频率投影scalar，没有运行G／q0／五源表。本文给整个有限积分的误差，root另付v−v*输入运输及其余四项；本有限积分来自已审Plancherel身份，不是丢掉无限物理尾。

## 1. 实际结果

执行命令：

```
python scripts/tf_reader_c2_tail_term.py --output reviews/2026-10-27/tf-reader-c2/tail-term.json
```

最终运行terminal exit0，约0.432秒；260位向外integer intervals，cosine Taylor参数N=32（degree64），33个even moments、1089个逐项确切monomial积分。正式有理区间见[tail-term.json](tail-term.json)的`integral_interval`，短十进制向外略化为

\[
 I\in[3.69786091191449923,\;3.69786091191449936].
\]

正式有理width约1.20620573·10^−16，小于本项1/16384门；该短显示区间略宽，不能代替JSON原有理端点。代码版本和所有源JSON／依赖脚本LF SHA在原记录中绑定，hash仅标版本。

## 2. g的even moments不做高频grid

记NF=9699690，g(y)=Σ_u c_u sin(2πuy)/(NF πy)，所有u为正整数且Σc_u=0。采用既有严格TReader，

\[
 T(u)=2\pi u(\pi/2-\operatorname{Si}(2\pi u)),
 \quad
 \int_0^1g(y)\,dy=-\frac1{2NF\pi^2}\sum_u\frac{c_uT(u)}u.
\]

这里只读取384个T值，不运行旧scalar的68037个二次频率和。小u用real Si Taylor及π argument误差，大u用Laplace积分的有限几何signed余项；实际最大432个Si Taylor项、79个Laplace项，所有舍入向外。

令S_r=Σ_u c_u/(NF u^r)，它是exact rational。对j≥1，integer endpoint的sin=0、cos=1使逐次分部积分精确终止：

\[
 \int_0^1 y^{2j}g(y)\,dy
 =\sum_{l=0}^{j-1}
 \frac{(-1)^{l+1}(2j-1)!}{(2j-1-2l)!\,2^{2l+1}}
 S_{2l+1}\,\pi^{-2l-2}.
\]

因此所需0,…,64阶even moments全部以有限有理frequency sums与向外inverse-π powers求出。p*的贡献独立按exact coefficients求Σ_k p_k/[2(j+k)+1]。未用有限sample或Euclidean coordinate norm冒充函数积分。

## 3. 真实cosine余项及product运输

由g=LF(Bh0)、||Bh0||²=19189712/4849845<4，单位低区间给||g||1<2。故直接有

\[
 L_1:=2+\sum_{k=0}^{26}\frac{|p_k|}{2k+1}
 \ge\|\ell_*\|_1,
 \qquad L_1\approx28.66848779152324.
\]

此界只依同一输入exact norm及exact polynomial，不借巨大R0 norm或未知quadrature。令m_j=∫_0^1y^(2j)ell*(y)dy，

\[
 P_{32}(x)=\sum_{j=0}^{32}q_jx^{2j},
 \qquad q_j=\frac{2(-1)^j(2\pi)^{2j}}{(2j)!}m_j.
\]

实cos Taylor到degree65（odd项为零）给全0≤x≤2统一误差

\[
 |a(x)-P_{32}(x)|\le
 \varepsilon=2L_1\frac{(4\pi_{hi})^{66}}{66!}
 <3.719\cdot10^{-19}.
\]

代码先以exact rational构成此式，再向外取260位有理上界；π取既存证书的上端。由于|a|≤2L1、|P|≤2L1+ε，整个积分的Taylor运输半径为

\[
 \frac2{\sqrt2}(4L_1\varepsilon+\varepsilon^2)
 <6.032\cdot10^{-17}.
\]

其中1/√2由整数平方根给260位有理包围，根误差和系数／矩舍入均在interval计算中保留。

多项式积分准确为

\[
 \frac1{\sqrt2}\int_0^2P_{32}(x)P_{32}(x/2)\,dx
 =\frac1{\sqrt2}\sum_{j,k=0}^{32}
 q_jq_k\frac{2^{2j+1}}{2(j+k)+1}.
\]

1089项以向外integer interval算术相加，再加减上述真实Taylor半径；形式上为有限多项式并不免除其rounding和消去费用。JSON保存完整even moments／q_j区间／积分算术width与余项，认证width由实际有理比较验收，不来自浮点显示。

## 4. 消费边界

本项是exact ell*的finite correction。root合成c2时必须支付另外四项及|c2(v)−c2(v*)|；单项pass不自动成为c2 pass，更不提供Gv、full-G J／residual、q0宽1/16或五源T/E／Hfin。未改变原source／F／cutoff、全部complex源／原du-Dlog／Γ/contact/powers/poles的目标责任，也没有新的classic whole／成长／primitiveRR结论。

本分支未改STATE、cadence、看板、文献库或提交，交root／fresh对齐实际版本后限定消费。数学轮与宏观停止由root统一结算；本次运行和metadata路径修补不另计轮。
