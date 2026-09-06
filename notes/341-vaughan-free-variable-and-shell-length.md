# 341. 既有Vaughan通道的自由整数变量与shell长度

2026-09-07。周期9第1动作。[T候选，独立复核待完成]。
先核对原恒等式与变量长度，不把Vaughan名称当成新相消。

## 1. 准确恒等式及通道

采用既有脚本power_high_physical_vaughan_channel_audit.py的canonical_channels。
Dirichlet卷积记*，1为常数算术函数，epsilon为卷积单位，
mu_lo(r)=mu(r)1_(r<=U)、mu_hi=mu-mu_lo，
Lambda_lo(v)=Lambda(v)1_(v<=V)、Lambda_hi=Lambda-Lambda_lo。
由mu*1=epsilon，准确地
\[
 \Lambda=\Lambda_{\rm lo}+
       \mu_{\rm lo}*1*\Lambda_{\rm hi}+
       \mu_{\rm hi}*1*\Lambda_{\rm hi}.                \tag{1}
\]
这是脚本采用的两个命名通道：
Type I=Lambda_lo+mu_lo*1*Lambda_hi，
Type II=mu_hi*1*Lambda_hi。
等价的Type I=mu_lo*log-mu_lo*1*Lambda_lo+Lambda_lo
来自1*Lambda=log，但本动作不把两种展开的通道单独混用。

取U=V=max(2,round(Y^(1/4)))，沿用335的X、Y、I和M=X^(1/2)。
充分大Y时a in I意味着a>V，故Lambda_lo(a)=0。
于是两个通道共同使用
\[
 a=rvw,\qquad v>V,\quad w\ge1,
 \quad\hbox{权重为 }\mu(r)\Lambda(v),                  \tag{2}
\]
Type I限定r<=U，Type II限定r>U。
w的算术权为1，但依赖a的原物理核、归一化和mask全部保留。
在Lambda(a)=0的整数上，两个通道相消；不能提前删除这些ghost。
对两分子a,c都展开时，物理响应是四个通道I/I、I/II、II/I、II/II的合并。

## 2. 当前窄cell的mask只有指定整数点删除

240–241固定mask在整数a和prime-power b的当前I内，排除
“a是与b同底的prime power”。因端点比13/7<2，同底两素数幂只能相等。
所以对当前整数扩展，该mask精确等价a≠b；另一对精确等价c≠d。
这一步依赖当前窄区间，不能移植到任意新cell。

固定r,v,b,c,d时，a≠b只从w和中删除可能的单点w=b/(rv)。
完整去对角rvwd-bc≠0也仅删除可能的单点w=bc/(rvd)。
这些删除仍在同一通道无关物理响应里执行，不按mu(r)符号改变。
c若尚为原prime power且固定，Lambda(c)不依赖w；
若随后展开c，它依赖另一套变量，仍需保留两者的共同shell关系。

## 3. 真正可自由求和的w长度

固定r,v,b,c,d后，w先受rvw in I限制。
原shell进一步要求
\[
 \left|\log{rvwd\over bc}\right|\le X^{-1/2},
\quad
 {bc\over rvd}e^{-X^{-1/2}}
       \le w\le {bc\over rvd}e^{X^{-1/2}}.             \tag{3}
\]
因为b,c,d都在I（c即使处于ghost扩展也仍在同一I），该实区间长度
\[
 \ell_w={bc\over rvd}\,2\sinh(X^{-1/2})
             \ll {YX^{-1/2}\over rv}
             ={X^{1/4}\over rv}.                      \tag{4}
\]
与rvw in I取交并删除指定点只会缩短，不改变上界。
因此每个固定外层的整数w数至多1+O(X^(1/4)/(rv))。

Type II有rv>UV约Y^(1/2)=X^(3/8)，所以
\[
 \ell_w\ll X^{-1/8}<1
\]
对充分大X统一成立：每个固定r,v,b,c,d的Type II纤维至多一个整数点。
这不是说整个Type II通道只有一个点；外层变量仍大量存在。
Type I若需要长度趋于无穷，则必须rv=o(X^(1/4))；
因v>V约X^(3/16)，特别需要r=o(X^(1/16))。
这是必要范围，不是该范围内已有可用相消。

## 4. 下一实际动作

对固定全部其他变量的Type II completion直接做Poisson，没有长原整数区间可利用；
仅仅把其代数w范围Y/(rv)写成自由长度会漏掉共同shell缩短因子X^-1/2。
仍需检查两条不同的合法可能：

1. Type I真正长纤维的小rv范围是否可计算，连同其外层成本给实际局部估计；
2. Type II保留两个或更多外层变量共同求和时，是否出现可以使用的算术核与范围。

第二点不由逐纤维至多1点否定；格点可沿耦合曲面分布。
本篇仅完成恒等式、mask和长度账本，没有对所有Vaughan或Poisson方法作否定，
也没有得到完整四阶相关的净界。
