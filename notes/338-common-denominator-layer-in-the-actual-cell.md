# 338. 实际cell的大gcd分母层可以用绝对值估计去除

2026-09-07。周期8第4动作的实际分层估计。[T，内部独立复核通过]。
不是丢弃335发现的长纤维；在原响应中先估计其总贡献。

## 1. 精确分层

固定335的实际prime-power cell、两对distinct-base mask、M=X^(1/2)、
Y=X^(3/4)和规范化响应R_X。这里只讨论合并后的四个Lambda权，
不将下面的估计直接移植到某个Vaughan通道或ghost扩展。

因为I_X端点比至多13/7<2，同底的两个素数幂若都在I_X必相等。
所以对原支持内的b,d，只有两种情况：

- b=d，此时gcd(b,d)=b约为Y，确实有长整数纤维；
- b≠d，此时素数底不同，gcd(b,d)=1。

令R_den为R_X中b=d的部分，R_cop为其余部分。精确地R_X=R_cop+R_den。
在R_den内，去除ad-bc=0等价a≠c，且Delta=log(a/c)。
本篇证明
\[
 \boxed{|R_{\rm den}|\ll X^{-1/4}(\log X)^3=o(1).}       \tag{1}
\]
因此保留这一误差后可以只估计互素分母部分；不是在变换前无代价假设互素。

## 2. 一个确定的分母层绝对值界

写L=log X，K=K_X，bar K=bar K_X(M)。
337第2节的精确有限核估计（也可直接由几何和获得）给
\[
 |K(t)|\ll(1+|t|)^{-1}\quad (|t|\le M),\qquad
 |\bar K|\ll M^{-1}.                                   \tag{2}
\]
全部W在[0,1]，故不用其振荡或平滑性。
若a,c在I_X且a≠c，均值定理及shell限制给
\[
 |X\log(a/c)|\ge {X\over1.30Y}|a-c|,\qquad
 1\le |a-c|\le C {YM\over X}.                           \tag{3}
\]
充分大X时X/Y=X^(1/4)>1。记J=ceil(CYM/X)=O(X^(1/4))。
对固定a，暂将c扩到全部整数上界，使用Lambda(c)<=C L、sqrt(ac)约为Y：
\[
\begin{aligned}
 &\sum_{\substack{c\in I_X,\ c\ne a\\|\log(a/c)|\le M/X}}
 {\Lambda(c)\over\sqrt{ac}}\,
 |K(X\log(a/c))-\bar K|\\
 &\quad\ll {L\over Y}
     \sum_{1\le |j|\le J}
       \left({Y\over X|j|}+{1\over M}\right)
 \ll {L\over X}\{\log(2+J)+1\}
 \ll {L^2\over X}.                                    \tag{4}
\end{aligned}
\]
ceil带来的1/M项也由Y/X控制，因为J约为X^(1/4)趋于无穷。
不要求短区间中有任何素数分布估计。

再用Chebyshev的sum_(a in I) Lambda(a) <<Y，得到
\[
 \sum_{\substack{a,c\in I_X,\ a\ne c\\|\log(a/c)|\le M/X}}
 {\Lambda(a)\Lambda(c)\over\sqrt{ac}}\,
 |K(X\log(a/c))-\bar K|
 \ll {Y L^2\over X}.                                  \tag{5}
\]
在b=d时，两个q权相乘为
Lambda(a)Lambda(c)Lambda(b)^2/(16pi^4 b sqrt(ac))。
又
\[
 \sum_{b\in I_X}{\Lambda(b)^2\over b}\ll L,              \tag{6}
\]
由Lambda(b)<=C L、b约Y及Chebyshev即得。
将(5)(6)相乘，去掉distinct-base mask只增大绝对值上界，证明(1)。
重复素数幂的原Lambda平方已保留，没有用“分母是素数”替换原权。

## 3. 同分子层及真实含义

同理，在a=c时Delta=log(d/b)，把(a,c)与(b,d)角色互换，
仍仅用W<=1，得到该层贡献R_num=O(X^(-1/4)L^3)。
两个层的交集a=c且b=d恰为原来已删除的h=0项，
故它们在R_X中互不重叠。
因此可以进一步写
\[
 R_X=R_{\substack{a\ne c\\ b\ne d}}
               +O(X^{-1/4}L^3),                       \tag{7}
\]
其中剩余实际支持满足gcd(a,c)=gcd(b,d)=1。
这里没有要求跨位置a,d或b,c的素数底也不同。

这条实际误差界与335的“不能未经估计删去大gcd层”相容：
长纤维存在，但该层非零频率至少约X/Y，精确核衰减使其总量小。
它减少后续算术映射的分层工作，未控制互素分母的四素数相关，
未使336的全频率数组成为可分离系数，也没有解决全cell MOM或RH。

336–337固定延拓暂不改写。本篇(7)是一条原物理和的额外合法分解；
若对剩余和重新完成，须明确新的mask并核对零频项，不能把两个版本混为同一F_h。
